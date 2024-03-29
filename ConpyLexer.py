# Generated from Conpy.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("V\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\6\f<\n\f\r\f\16\f=\3\r\3\r\7")
        buf.write("\rB\n\r\f\r\16\rE\13\r\3\16\6\16H\n\16\r\16\16\16I\3\16")
        buf.write("\3\16\3\17\3\17\5\17P\n\17\3\17\5\17S\n\17\3\17\3\17\2")
        buf.write("\2\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\3\2\6\3\2\62;\5\2C\\aac|\6\2\62;")
        buf.write("C\\aac|\4\2\13\13\"\"\2Z\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5")
        buf.write("!\3\2\2\2\7#\3\2\2\2\t%\3\2\2\2\13\'\3\2\2\2\r)\3\2\2")
        buf.write("\2\17+\3\2\2\2\21-\3\2\2\2\23\62\3\2\2\2\25\65\3\2\2\2")
        buf.write("\27;\3\2\2\2\31?\3\2\2\2\33G\3\2\2\2\35R\3\2\2\2\37 \7")
        buf.write("*\2\2 \4\3\2\2\2!\"\7+\2\2\"\6\3\2\2\2#$\7}\2\2$\b\3\2")
        buf.write("\2\2%&\7\177\2\2&\n\3\2\2\2\'(\7=\2\2(\f\3\2\2\2)*\7,")
        buf.write("\2\2*\16\3\2\2\2+,\7-\2\2,\20\3\2\2\2-.\7h\2\2./\7w\2")
        buf.write("\2/\60\7p\2\2\60\61\7e\2\2\61\22\3\2\2\2\62\63\7k\2\2")
        buf.write("\63\64\7h\2\2\64\24\3\2\2\2\65\66\7g\2\2\66\67\7n\2\2")
        buf.write("\678\7u\2\289\7g\2\29\26\3\2\2\2:<\t\2\2\2;:\3\2\2\2<")
        buf.write("=\3\2\2\2=;\3\2\2\2=>\3\2\2\2>\30\3\2\2\2?C\t\3\2\2@B")
        buf.write("\t\4\2\2A@\3\2\2\2BE\3\2\2\2CA\3\2\2\2CD\3\2\2\2D\32\3")
        buf.write("\2\2\2EC\3\2\2\2FH\t\5\2\2GF\3\2\2\2HI\3\2\2\2IG\3\2\2")
        buf.write("\2IJ\3\2\2\2JK\3\2\2\2KL\b\16\2\2L\34\3\2\2\2MO\7\17\2")
        buf.write("\2NP\7\f\2\2ON\3\2\2\2OP\3\2\2\2PS\3\2\2\2QS\7\f\2\2R")
        buf.write("M\3\2\2\2RQ\3\2\2\2ST\3\2\2\2TU\b\17\2\2U\36\3\2\2\2\b")
        buf.write("\2=CIOR\3\b\2\2")
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
    FUNC = 8
    IF = 9
    ELSE = 10
    INT = 11
    NAME = 12
    WHITESPACE = 13
    NEWLINE = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "';'", "'*'", "'+'", "'func'", "'if'", 
            "'else'" ]

    symbolicNames = [ "<INVALID>",
            "FUNC", "IF", "ELSE", "INT", "NAME", "WHITESPACE", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "FUNC", "IF", "ELSE", "INT", "NAME", "WHITESPACE", "NEWLINE" ]

    grammarFileName = "Conpy.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


