import struct
import sys
import antlr4
from ConpyLexer import ConpyLexer
from ConpyParser import ConpyParser
from ConpyVisitor import ConpyVisitor as ConpyBaseVisitor
import assembly

EXTERNAL_SYMBOLS = {"print": {"params": [None], 'id': 0}}


class SyntaxErrorListener(antlr4.DiagnosticErrorListener):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.errors_count = 0

    def syntaxError(self, *args, **kwargs):
        self.errors_count += 1


class SemanticAnalysisVisitor(ConpyBaseVisitor):
    def __init__(self):
        self.symbols = {}
        self.next_func_id = 0
        self.current_func_symbol = None
        self.errors_count = 0

    def add_symbol(self, symbol):
        symbol['id'] = self.next_func_id
        self.next_func_id += 1
        self.symbols[symbol['name']] = symbol

    def perror(self, token, message):
        print(f"{token.line}:{token.column}: error: {message}", file=sys.stderr)
        self.errors_count += 1

    def visitFuncDef(self, ctx):
        func_name = ctx.funcName.text

        symbol = {
            'name': func_name,
            'params': self.visitParams(ctx.params()) if ctx.params() else [],
            'external': False,
            'address': None,
        }

        if func_name in self.symbols:
            self.perror(ctx.funcName, f"redefined name '{func_name}'")
        else:
            self.add_symbol(symbol)

        self.current_func_symbol = symbol
        self.visitBlock(ctx.block())
        self.current_func_symbol = None

    def visitParams(self, ctx):
        param_names = set()
        for param in ctx.NAME():
            if param.getText() in param_names:
                self.perror(param.symbol, f"redefined name '{param.getText()}'")
            param_names.add(param.getText())

        return [param.symbol.text for param in ctx.NAME()]

    def visitFuncCall(self, ctx):
        super().visitFuncCall(ctx)
        func_name = ctx.start.text
        if func_name in EXTERNAL_SYMBOLS:
            return

        if func_name not in self.symbols:
            self.perror(ctx.start, f"'{func_name}' undeclared")
            return

        symbol = self.symbols[func_name]
        args_count = len(ctx.arguments().expr()) if ctx.arguments() else 0
        params_count = len(symbol['params'])
        if args_count != params_count:
            self.perror(ctx.start, "arguments count not match")

    def visitParamRef(self, ctx):
        param_name = ctx.getText()
        symbol = self.current_func_symbol
        if not symbol or param_name not in symbol["params"]:
            self.perror(ctx.start, f"'{param_name}' undeclared")


class IRGenerationVisitor(ConpyBaseVisitor):
    def __init__(self, symbols):
        super().__init__()
        self.symbols = symbols
        self.current_func_symbol = None
        self.start_instruction_index = -1

    def visitMain(self, ctx):
        func_symbols = list(self.symbols.values())
        func_id = 0

        defs_instructions = []
        calls_instructions = []
        for child in ctx.children:
            if isinstance(child, ConpyParser.FuncDefContext):
                func_symbols[func_id]['address'] = len(defs_instructions)
                func_id += 1
                defs_instructions.extend(self.visitFuncDef(child))

            elif isinstance(child, ConpyParser.FuncCallContext):
                calls_instructions.extend(self.visitFuncCall(child))

        self.start_instruction_index = len(defs_instructions)

        instructions = defs_instructions + calls_instructions
        return instructions

    def visitBlock(self, ctx):
        instructions = []
        for child in ctx.children:
            if isinstance(child, antlr4.TerminalNode):
                continue
            instructions.extend(self.visit(child))
        return instructions

    def visitIfStmt(self, ctx):
        condition_instructions = self.visit(ctx.expr())
        if_block_instructions = self.visit(ctx.ifBlock)
        additional_instructions_to_skip = 0
        if ctx.elseBlock:
            additional_instructions_to_skip += 1

        instructions = [
            *condition_instructions,
            assembly.JumpForwardIfFalse(len(if_block_instructions)+1+additional_instructions_to_skip),
            *if_block_instructions,
        ]

        if ctx.elseBlock:
            else_block_instructions = self.visit(ctx.elseBlock)
            instructions.extend([
                assembly.JumpForward(len(else_block_instructions)+1),
                *else_block_instructions,
            ])

        return instructions

    def visitFuncDef(self, ctx):
        func_name = ctx.funcName.text
        symbol = self.symbols[func_name]
        params_count = len(symbol['params'])
        instructions = []
        for index in reversed(range(params_count)):
            instructions.extend([
                assembly.PushVar(index),
                assembly.Assign(),
            ])

        self.current_func_symbol = symbol
        instructions.extend([
            *self.visitBlock(ctx.block()),
            assembly.Return()
        ])
        self.current_func_symbol = None
        return instructions

    def visitFuncCall(self, ctx):
        func_name = ctx.funcName.text
        if func_name in EXTERNAL_SYMBOLS:
            symbol = EXTERNAL_SYMBOLS[func_name]
            call_instruction = assembly.CallExternal(symbol['id'])
        else:
            symbol = self.symbols[func_name]
            call_instruction = assembly.Call(symbol['id'])
        return [*self.visitArguments(ctx.arguments()), call_instruction]

    def visitArguments(self, ctx):
        instructions = []
        for argument in ctx.expr():
            instructions.extend(self.visit(argument))
        return instructions

    def visitBinaryExpr(self, ctx):
        left_expr, right_expr = ctx.expr()
        oper2instr = {'*': assembly.Mult, '+': assembly.Add}

        return [
            *self.visit(left_expr),
            *self.visit(right_expr),
            oper2instr[ctx.oper.text]()
        ]

    def visitIntLiteral(self, ctx):
        return [assembly.PushInt(int(ctx.getText()))]

    def visitParamRef(self, ctx):
        param_name = ctx.getText()
        param_index = self.current_func_symbol['params'].index(param_name)
        return [assembly.PushVar(param_index)]


def code_generate(symbols, instructions, start_instruction_index):
    bytecode = []

    bytecode.append(struct.pack('<i', start_instruction_index))
    bytecode.append(struct.pack('<i', len(symbols)))
    for symbol in symbols.values():
        bytecode.append(struct.pack('<i', len(symbol['params'])))
        bytecode.append(struct.pack('<i', symbol['address']))

    bytecode.append(struct.pack('<i', len(instructions)))
    for instruction in instructions:
        bytecode.append(instruction.pack())

    return b''.join(bytecode)


def main():
    _, input_filename, output_filename = sys.argv

    input_stream = antlr4.FileStream(input_filename)
    lexer = ConpyLexer(input_stream)
    token_stream = antlr4.CommonTokenStream(lexer)
    parser = ConpyParser(token_stream)

    listener = SyntaxErrorListener()
    parser.addErrorListener(listener)
    parse_tree = parser.main()
    if listener.errors_count:
        msg = f"{listener.errors_count} syntax error generated"
        print(msg, file=sys.stderr)
        return

    sa_visitor = SemanticAnalysisVisitor()
    sa_visitor.visit(parse_tree)
    if sa_visitor.errors_count:
        msg = f"{sa_visitor.errors_count} semantic error generated"
        print(msg, file=sys.stderr)
        return

    ir_gen_visitor = IRGenerationVisitor(sa_visitor.symbols)
    ir = ir_gen_visitor.visit(parse_tree)

    print('\n'.join([
        type(instr).__name__ + ' ' + str(getattr(instr, 'value', ''))
        for instr in ir
    ]))

    code = code_generate(sa_visitor.symbols, ir, ir_gen_visitor.start_instruction_index)
    print(code)

    with open(output_filename, "wb") as file:
        file.write(code)


if __name__ == '__main__':
    main()
