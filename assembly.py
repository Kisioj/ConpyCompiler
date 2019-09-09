import struct


class AssemblyInstruction:
    def pack(self):
        return struct.pack('<i', self.ID)


class ValueInstruction(AssemblyInstruction):
    def __init__(self, value):
        self.value = value

    def pack(self):
        return super().pack() + struct.pack('<i', self.value)


class PushInt(ValueInstruction):
    ID = 0x01


class PushVar(ValueInstruction):
    ID = 0x02


class Call(ValueInstruction):
    ID = 0x03


class CallExternal(ValueInstruction):
    ID = 0x04


class JumpForwardIfFalse(ValueInstruction):
    ID = 0x05


class JumpForward(ValueInstruction):
    ID = 0x06


class Add(AssemblyInstruction):
    ID = 0x07


class Mult(AssemblyInstruction):
    ID = 0x08


class Return(AssemblyInstruction):
    ID = 0x09


class Assign(AssemblyInstruction):
    ID = 0x10


