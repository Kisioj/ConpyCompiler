# Generated from Conpy.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("Z\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\6\r@\n\r\r\r")
        buf.write("\16\rA\3\16\3\16\7\16F\n\16\f\16\16\16I\13\16\3\17\6\17")
        buf.write("L\n\17\r\17\16\17M\3\17\3\17\3\20\3\20\5\20T\n\20\3\20")
        buf.write("\5\20W\n\20\3\20\3\20\2\2\21\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21\3\2")
        buf.write("\6\3\2\62;\5\2C\\aac|\6\2\62;C\\aac|\4\2\13\13\"\"\2^")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\3!\3\2\2\2\5#\3\2\2\2\7")
        buf.write("%\3\2\2\2\t\'\3\2\2\2\13)\3\2\2\2\r+\3\2\2\2\17-\3\2\2")
        buf.write("\2\21/\3\2\2\2\23\61\3\2\2\2\25\66\3\2\2\2\279\3\2\2\2")
        buf.write("\31?\3\2\2\2\33C\3\2\2\2\35K\3\2\2\2\37V\3\2\2\2!\"\7")
        buf.write("*\2\2\"\4\3\2\2\2#$\7+\2\2$\6\3\2\2\2%&\7.\2\2&\b\3\2")
        buf.write("\2\2\'(\7}\2\2(\n\3\2\2\2)*\7\177\2\2*\f\3\2\2\2+,\7=")
        buf.write("\2\2,\16\3\2\2\2-.\7,\2\2.\20\3\2\2\2/\60\7-\2\2\60\22")
        buf.write("\3\2\2\2\61\62\7h\2\2\62\63\7w\2\2\63\64\7p\2\2\64\65")
        buf.write("\7e\2\2\65\24\3\2\2\2\66\67\7k\2\2\678\7h\2\28\26\3\2")
        buf.write("\2\29:\7g\2\2:;\7n\2\2;<\7u\2\2<=\7g\2\2=\30\3\2\2\2>")
        buf.write("@\t\2\2\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2\2AB\3\2\2\2B\32")
        buf.write("\3\2\2\2CG\t\3\2\2DF\t\4\2\2ED\3\2\2\2FI\3\2\2\2GE\3\2")
        buf.write("\2\2GH\3\2\2\2H\34\3\2\2\2IG\3\2\2\2JL\t\5\2\2KJ\3\2\2")
        buf.write("\2LM\3\2\2\2MK\3\2\2\2MN\3\2\2\2NO\3\2\2\2OP\b\17\2\2")
        buf.write("P\36\3\2\2\2QS\7\17\2\2RT\7\f\2\2SR\3\2\2\2ST\3\2\2\2")
        buf.write("TW\3\2\2\2UW\7\f\2\2VQ\3\2\2\2VU\3\2\2\2WX\3\2\2\2XY\b")
        buf.write("\20\2\2Y \3\2\2\2\b\2AGMSV\3\b\2\2")
        return buf.getvalue()


class ConpyLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    FUNC = 9
    IF = 10
    ELSE = 11
    INT = 12
    NAME = 13
    WHITESPACE = 14
    NEWLINE = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "','", "'{'", "'}'", "';'", "'*'", "'+'", "'func'", 
            "'if'", "'else'" ]

    symbolicNames = [ "<INVALID>",
            "FUNC", "IF", "ELSE", "INT", "NAME", "WHITESPACE", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "FUNC", "IF", "ELSE", "INT", "NAME", "WHITESPACE", 
                  "NEWLINE" ]

    grammarFileName = "Conpy.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


