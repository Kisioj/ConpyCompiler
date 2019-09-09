import struct
import sys

import assembly


def external_print(value):
    print(value)


EXTERNAL_SYMBOLS = [external_print]


OPCODE_2_INSTRUCTION = {
    0x01: assembly.PushInt,
    0x02: assembly.PushVar,
    0x03: assembly.Call,
    0x04: assembly.CallExternal,
    0x05: assembly.JumpForwardIfFalse,
    0x06: assembly.JumpForward,
    0x07: assembly.Add,
    0x08: assembly.Mult,
    0x09: assembly.Return,
    0x10: assembly.Assign,
}


class FuncFrame:
    def __init__(self, ip, params_count):
        self.return_to = ip
        self.locals = [None] * params_count


class Reference:
    def __init__(self, index):
        self.index = index


class VM:
    def __init__(self):
        self.external_function_symbols = []
        self.function_symbols = []
        self.start_instruction_index = -1
        self.instructions = []
        self.file = None
        self.INSTR_2_METHOD = {
            assembly.PushInt: self.op_push_int,
            assembly.PushVar: self.op_push_var,
            assembly.Call: self.op_call,
            assembly.CallExternal: self.op_call_external,
            assembly.JumpForwardIfFalse: self.op_jump_forward_if_false,
            assembly.JumpForward: self.op_jump_forward,
            assembly.Add: self.op_add,
            assembly.Mult: self.op_mult,
            assembly.Return: self.op_return,
            assembly.Assign: self.op_assign,
        }

        self.func_frames_stack = []
        self.data_stack = []
        self.ip = -1

    def pop_int_from_stack(self):
        value = self.data_stack.pop()
        if isinstance(value, Reference):
            func_frame = self.func_frames_stack[-1]
            return func_frame.locals[value.index]
        return value

    def read_int(self):
        return struct.unpack('<i', self.file.read(4))[0]

    def read_bool(self):
        return struct.unpack('?', self.file.read(1))[0]

    def load_file(self, file):
        self.file = file
        self.start_instruction_index = self.read_int()
        symbols_count = self.read_int()
        for _ in range(symbols_count):
            is_external = self.read_bool()
            symbol = {
                # 'id': self.read_int(),
                # 'external': self.read_bool(),
                'params_count': self.read_int(),
                'address': self.read_int(),
            }
            if is_external:
                self.external_function_symbols.append(symbol)
            else:
                self.function_symbols.append(symbol)

        instructions_count = self.read_int()
        for _ in range(instructions_count):
            opcode = self.read_int()
            instruction_class = OPCODE_2_INSTRUCTION[opcode]
            if issubclass(instruction_class, assembly.ValueInstruction):
                value = self.read_int()
                instruction = instruction_class(value)
            else:
                instruction = instruction_class()
            self.instructions.append(instruction)

    def run(self):
        self.ip = self.start_instruction_index
        instructions_count = len(self.instructions)

        while -1 < self.ip < instructions_count:
            instruction = self.instructions[self.ip]
            handler_method = self.INSTR_2_METHOD[type(instruction)]

            if issubclass(type(instruction), assembly.ValueInstruction):
                handler_method(instruction.value)
            else:
                handler_method()

    def op_push_int(self, value):
        self.ip += 1
        self.data_stack.append(value)

    def op_push_var(self, value):
        self.ip += 1
        self.data_stack.append(Reference(value))

    def op_call(self, value):
        func_symbol = self.function_symbols[value]
        params_count = func_symbol['params_count']
        func_address = func_symbol['address']
        self.func_frames_stack.append(FuncFrame(self.ip + 1, params_count))
        self.ip = func_address

    def op_call_external(self, value):
        self.ip += 1
        handler_method = EXTERNAL_SYMBOLS[value]
        args = [
            self.pop_int_from_stack()
            for _ in range(handler_method.__code__.co_argcount)
        ]
        handler_method(*args)

    def op_jump_forward_if_false(self, jump_step):
        if self.pop_int_from_stack():
            self.ip += 1
        else:
            self.ip += jump_step

    def op_jump_forward(self, jump_step):
        self.ip += jump_step

    def op_add(self):
        self.ip += 1
        right = self.pop_int_from_stack()
        left = self.pop_int_from_stack()
        self.data_stack.append(left + right)

    def op_mult(self):
        self.ip += 1
        right = self.pop_int_from_stack()
        left = self.pop_int_from_stack()
        self.data_stack.append(left * right)

    def op_return(self):
        func_frame = self.func_frames_stack.pop()
        self.ip = func_frame.return_to

    def op_assign(self):
        self.ip += 1
        reference = self.data_stack.pop()
        right = self.pop_int_from_stack()
        func_frame = self.func_frames_stack[-1]
        func_frame.locals[reference.index] = right


def main():
    _, input_filename = sys.argv

    vm = VM()
    with open(input_filename, 'rb') as file:
        vm.load_file(file)

    vm.run()


if __name__ == '__main__':
    main()
