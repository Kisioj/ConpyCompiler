import subprocess
import sys
import antlr4
from ConpyLexer import ConpyLexer
from ConpyParser import ConpyParser
from ConpyVisitor import ConpyVisitor as ConpyBaseVisitor

FuncDefContext = ConpyParser.FuncDefContext
FuncCallContext = ConpyParser.FuncCallContext


class SyntaxErrorListener(antlr4.DiagnosticErrorListener):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.errors_count = 0

    def syntaxError(self, *args, **kwargs):
        self.errors_count += 1


class SemanticAnalysisVisitor(ConpyBaseVisitor):
    def __init__(self):
        self.symbols_table = {"print": None}
        self.func_ctx = None
        self.errors_count = 0

    def perror(self, token, message):
        print(f"{token.line}:{token.column}: error: {message}",
              file=sys.stderr)
        self.errors_count += 1

    def visitFuncDef(self, ctx):
        self.func_ctx = ctx
        super().visitFuncDef(ctx)
        self.func_ctx = None

    def visitFuncNameDef(self, ctx):
        name, token = ctx.getText(), ctx.start
        if name in self.symbols_table:
            self.perror(token, f"redefined name '{name}'")
        else:
            self.symbols_table[name] = ctx.parentCtx

    def visitFuncNameRef(self, ctx):
        name, token = ctx.getText(), ctx.start
        if name not in self.symbols_table:
            self.perror(token, f"'{name}' undeclared")

    def visitParamDef(self, ctx):
        name = ctx.getText()
        func_name = self.func_ctx.funcNameDef().getText()
        self.symbols_table[f"{func_name}.{name}"] = ctx

    def visitParamRef(self, ctx):
        name, token = ctx.getText(), ctx.start
        if not self.func_ctx:
            self.perror(token, f"'{name}' undeclared")
            return
        func_name = self.func_ctx.funcNameDef().getText()
        param_name = f"{func_name}.{name}"
        if param_name not in self.symbols_table:
            self.perror(token, f"'{name}' undeclared")

    def visitFuncCall(self, ctx):
        super().visitFuncCall(ctx)
        name, token = ctx.start.text, ctx.start
        has_arg = bool(ctx.expr())
        if name not in self.symbols_table:
            return
        def_ctx, has_param = self.symbols_table[name], True
        if def_ctx:
            has_param = bool(def_ctx.paramDef().getText())
        if has_param is not has_arg:
            self.perror(token, "arguments count not match")


MAIN_TEMPLATE = """#include <stdio.h>
{} int main(void) {{ {} return 0; }}"""
IF_TEMPLATE = "if ({}) {{ {} }} else {{ {} }}"
FUNC_TEMPLATE = "void {} ({}) {{ {} }}"
CALL_TEMPLATE = "{} ({});"
PRINT_TEMPLATE = 'printf("%d\\n", {});'


class IRGenerationVisitor(ConpyBaseVisitor):
    def visitMain(self, ctx):
        defs, calls = [], []
        for child in ctx.children:
            if isinstance(child, FuncDefContext):
                defs.append(self.visitFuncDef(child))
            elif isinstance(child, FuncCallContext):
                calls.append(self.visitFuncCall(child))
        defs_code = '\n'.join(defs)
        calls_code = '\n'.join(calls)
        return MAIN_TEMPLATE.format(defs_code, calls_code)

    def visitFuncDef(self, ctx):
        name = ctx.funcNameDef().getText()
        param_code = ""
        if ctx.paramDef():
            param_code = f"int {ctx.paramDef().getText()}"
        block_code = self.visitBlock(ctx.block())
        return FUNC_TEMPLATE.format(name, param_code, block_code)

    def visitBlock(self, ctx):
        code = []
        for child in ctx.children:
            if isinstance(child, antlr4.TerminalNode):
                continue
            code.append(self.visit(child))
        return '\n'.join(code)

    def visitIfStmt(self, ctx):
        if_block, *else_block = ctx.block()
        if_code = self.visitBlock(if_block)
        else_code = ""
        if else_block:
            else_code = self.visitBlock(else_block[0])
        return IF_TEMPLATE.format(
            ctx.expr().getText(), if_code, else_code)

    def visitFuncCall(self, ctx):
        name_text = ctx.funcNameRef().getText()
        expr_text = ctx.expr().getText()
        if name_text == "print":
            return PRINT_TEMPLATE.format(expr_text)
        return CALL_TEMPLATE.format(name_text, expr_text)


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

    visitor = SemanticAnalysisVisitor()
    visitor.visit(parse_tree)
    if visitor.errors_count:
        msg = f"{visitor.errors_count} semantic error generated"
        print(msg, file=sys.stderr)
        return

    visitor = IRGenerationVisitor()
    code = visitor.visit(parse_tree)
    filename_c = f"{input_filename}.c"
    with open(filename_c, "w") as file:
        file.write(code)

    process = subprocess.Popen(["gcc", "-x", "c", filename_c, "-o", output_filename])
    process.wait()


if __name__ == '__main__':
    main()
