# Generated from Conpy.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("l\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\7\2\33")
        buf.write("\n\2\f\2\16\2\36\13\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3&\n\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\7\4.\n\4\f\4\16\4\61\13\4\3\5")
        buf.write("\3\5\3\5\7\5\66\n\5\f\5\16\59\13\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\5\6D\n\6\3\7\3\7\3\7\5\7I\n\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\7\bQ\n\b\f\b\16\bT\13\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\7\t_\n\t\f\t\16\tb\13\t\3\n\3\n")
        buf.write("\5\nf\n\n\3\13\3\13\3\f\3\f\3\f\2\3\20\r\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\2\2\2l\2\34\3\2\2\2\4!\3\2\2\2\6*\3\2\2\2")
        buf.write("\b\62\3\2\2\2\n<\3\2\2\2\fE\3\2\2\2\16M\3\2\2\2\20U\3")
        buf.write("\2\2\2\22e\3\2\2\2\24g\3\2\2\2\26i\3\2\2\2\30\33\5\4\3")
        buf.write("\2\31\33\5\f\7\2\32\30\3\2\2\2\32\31\3\2\2\2\33\36\3\2")
        buf.write("\2\2\34\32\3\2\2\2\34\35\3\2\2\2\35\37\3\2\2\2\36\34\3")
        buf.write("\2\2\2\37 \7\2\2\3 \3\3\2\2\2!\"\7\13\2\2\"#\7\17\2\2")
        buf.write("#%\7\3\2\2$&\5\6\4\2%$\3\2\2\2%&\3\2\2\2&\'\3\2\2\2\'")
        buf.write("(\7\4\2\2()\5\b\5\2)\5\3\2\2\2*/\7\17\2\2+,\7\5\2\2,.")
        buf.write("\7\17\2\2-+\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/\60\3\2\2\2")
        buf.write("\60\7\3\2\2\2\61/\3\2\2\2\62\67\7\6\2\2\63\66\5\n\6\2")
        buf.write("\64\66\5\f\7\2\65\63\3\2\2\2\65\64\3\2\2\2\669\3\2\2\2")
        buf.write("\67\65\3\2\2\2\678\3\2\2\28:\3\2\2\29\67\3\2\2\2:;\7\7")
        buf.write("\2\2;\t\3\2\2\2<=\7\f\2\2=>\7\3\2\2>?\5\20\t\2?@\7\4\2")
        buf.write("\2@C\5\b\5\2AB\7\r\2\2BD\5\b\5\2CA\3\2\2\2CD\3\2\2\2D")
        buf.write("\13\3\2\2\2EF\7\17\2\2FH\7\3\2\2GI\5\16\b\2HG\3\2\2\2")
        buf.write("HI\3\2\2\2IJ\3\2\2\2JK\7\4\2\2KL\7\b\2\2L\r\3\2\2\2MR")
        buf.write("\5\20\t\2NO\7\5\2\2OQ\5\20\t\2PN\3\2\2\2QT\3\2\2\2RP\3")
        buf.write("\2\2\2RS\3\2\2\2S\17\3\2\2\2TR\3\2\2\2UV\b\t\1\2VW\5\22")
        buf.write("\n\2W`\3\2\2\2XY\f\5\2\2YZ\7\t\2\2Z_\5\20\t\6[\\\f\4\2")
        buf.write("\2\\]\7\n\2\2]_\5\20\t\5^X\3\2\2\2^[\3\2\2\2_b\3\2\2\2")
        buf.write("`^\3\2\2\2`a\3\2\2\2a\21\3\2\2\2b`\3\2\2\2cf\5\24\13\2")
        buf.write("df\5\26\f\2ec\3\2\2\2ed\3\2\2\2f\23\3\2\2\2gh\7\17\2\2")
        buf.write("h\25\3\2\2\2ij\7\16\2\2j\27\3\2\2\2\16\32\34%/\65\67C")
        buf.write("HR^`e")
        return buf.getvalue()


class ConpyParser ( Parser ):

    grammarFileName = "Conpy.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "'{'", "'}'", "';'", 
                     "'*'", "'+'", "'func'", "'if'", "'else'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "FUNC", "IF", "ELSE", "INT", "NAME", 
                      "WHITESPACE", "NEWLINE" ]

    RULE_main = 0
    RULE_funcDef = 1
    RULE_params = 2
    RULE_block = 3
    RULE_ifStmt = 4
    RULE_funcCall = 5
    RULE_arguments = 6
    RULE_expr = 7
    RULE_value = 8
    RULE_paramRef = 9
    RULE_intLiteral = 10

    ruleNames =  [ "main", "funcDef", "params", "block", "ifStmt", "funcCall", 
                   "arguments", "expr", "value", "paramRef", "intLiteral" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    FUNC=9
    IF=10
    ELSE=11
    INT=12
    NAME=13
    WHITESPACE=14
    NEWLINE=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class MainContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ConpyParser.EOF, 0)

        def funcDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ConpyParser.FuncDefContext)
            else:
                return self.getTypedRuleContext(ConpyParser.FuncDefContext,i)


        def funcCall(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ConpyParser.FuncCallContext)
            else:
                return self.getTypedRuleContext(ConpyParser.FuncCallContext,i)


        def getRuleIndex(self):
            return ConpyParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain" ):
                return visitor.visitMain(self)
            else:
                return visitor.visitChildren(self)




    def main(self):

        localctx = ConpyParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ConpyParser.FUNC or _la==ConpyParser.NAME:
                self.state = 24
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ConpyParser.FUNC]:
                    self.state = 22
                    self.funcDef()
                    pass
                elif token in [ConpyParser.NAME]:
                    self.state = 23
                    self.funcCall()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self.match(ConpyParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncDefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ConpyParser.FUNC, 0)

        def NAME(self):
            return self.getToken(ConpyParser.NAME, 0)

        def block(self):
            return self.getTypedRuleContext(ConpyParser.BlockContext,0)


        def params(self):
            return self.getTypedRuleContext(ConpyParser.ParamsContext,0)


        def getRuleIndex(self):
            return ConpyParser.RULE_funcDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDef" ):
                listener.enterFuncDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDef" ):
                listener.exitFuncDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDef" ):
                return visitor.visitFuncDef(self)
            else:
                return visitor.visitChildren(self)




    def funcDef(self):

        localctx = ConpyParser.FuncDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_funcDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(ConpyParser.FUNC)
            self.state = 32
            self.match(ConpyParser.NAME)
            self.state = 33
            self.match(ConpyParser.T__0)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ConpyParser.NAME:
                self.state = 34
                self.params()


            self.state = 37
            self.match(ConpyParser.T__1)
            self.state = 38
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParamsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(ConpyParser.NAME)
            else:
                return self.getToken(ConpyParser.NAME, i)

        def getRuleIndex(self):
            return ConpyParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = ConpyParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(ConpyParser.NAME)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ConpyParser.T__2:
                self.state = 41
                self.match(ConpyParser.T__2)
                self.state = 42
                self.match(ConpyParser.NAME)
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ConpyParser.IfStmtContext)
            else:
                return self.getTypedRuleContext(ConpyParser.IfStmtContext,i)


        def funcCall(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ConpyParser.FuncCallContext)
            else:
                return self.getTypedRuleContext(ConpyParser.FuncCallContext,i)


        def getRuleIndex(self):
            return ConpyParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = ConpyParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(ConpyParser.T__3)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ConpyParser.IF or _la==ConpyParser.NAME:
                self.state = 51
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ConpyParser.IF]:
                    self.state = 49
                    self.ifStmt()
                    pass
                elif token in [ConpyParser.NAME]:
                    self.state = 50
                    self.funcCall()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 56
            self.match(ConpyParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ifBlock = None # BlockContext
            self.elseBlock = None # BlockContext

        def IF(self):
            return self.getToken(ConpyParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(ConpyParser.ExprContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ConpyParser.BlockContext)
            else:
                return self.getTypedRuleContext(ConpyParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(ConpyParser.ELSE, 0)

        def getRuleIndex(self):
            return ConpyParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = ConpyParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(ConpyParser.IF)
            self.state = 59
            self.match(ConpyParser.T__0)
            self.state = 60
            self.expr(0)
            self.state = 61
            self.match(ConpyParser.T__1)
            self.state = 62
            localctx.ifBlock = self.block()
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ConpyParser.ELSE:
                self.state = 63
                self.match(ConpyParser.ELSE)
                self.state = 64
                localctx.elseBlock = self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(ConpyParser.NAME, 0)

        def arguments(self):
            return self.getTypedRuleContext(ConpyParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return ConpyParser.RULE_funcCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCall" ):
                listener.enterFuncCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCall" ):
                listener.exitFuncCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCall" ):
                return visitor.visitFuncCall(self)
            else:
                return visitor.visitChildren(self)




    def funcCall(self):

        localctx = ConpyParser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(ConpyParser.NAME)
            self.state = 68
            self.match(ConpyParser.T__0)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ConpyParser.INT or _la==ConpyParser.NAME:
                self.state = 69
                self.arguments()


            self.state = 72
            self.match(ConpyParser.T__1)
            self.state = 73
            self.match(ConpyParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ConpyParser.ExprContext)
            else:
                return self.getTypedRuleContext(ConpyParser.ExprContext,i)


        def getRuleIndex(self):
            return ConpyParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = ConpyParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.expr(0)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ConpyParser.T__2:
                self.state = 76
                self.match(ConpyParser.T__2)
                self.state = 77
                self.expr(0)
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ConpyParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ValueExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConpyParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self):
            return self.getTypedRuleContext(ConpyParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValueExpr" ):
                listener.enterValueExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValueExpr" ):
                listener.exitValueExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValueExpr" ):
                return visitor.visitValueExpr(self)
            else:
                return visitor.visitChildren(self)


    class BinaryExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConpyParser.ExprContext
            super().__init__(parser)
            self.oper = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ConpyParser.ExprContext)
            else:
                return self.getTypedRuleContext(ConpyParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryExpr" ):
                listener.enterBinaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryExpr" ):
                listener.exitBinaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryExpr" ):
                return visitor.visitBinaryExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ConpyParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ConpyParser.ValueExprContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 84
            self.value()
            self._ctx.stop = self._input.LT(-1)
            self.state = 94
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 92
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = ConpyParser.BinaryExprContext(self, ConpyParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 86
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")

                        self.state = 87
                        localctx.oper = self.match(ConpyParser.T__6)
                        self.state = 88
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = ConpyParser.BinaryExprContext(self, ConpyParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 89
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                        self.state = 90
                        localctx.oper = self.match(ConpyParser.T__7)
                        self.state = 91
                        self.expr(3)
                        pass

             
                self.state = 96
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramRef(self):
            return self.getTypedRuleContext(ConpyParser.ParamRefContext,0)


        def intLiteral(self):
            return self.getTypedRuleContext(ConpyParser.IntLiteralContext,0)


        def getRuleIndex(self):
            return ConpyParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = ConpyParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_value)
        try:
            self.state = 99
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ConpyParser.NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.paramRef()
                pass
            elif token in [ConpyParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.intLiteral()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParamRefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(ConpyParser.NAME, 0)

        def getRuleIndex(self):
            return ConpyParser.RULE_paramRef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamRef" ):
                listener.enterParamRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamRef" ):
                listener.exitParamRef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamRef" ):
                return visitor.visitParamRef(self)
            else:
                return visitor.visitChildren(self)




    def paramRef(self):

        localctx = ConpyParser.ParamRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_paramRef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(ConpyParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IntLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ConpyParser.INT, 0)

        def getRuleIndex(self):
            return ConpyParser.RULE_intLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntLiteral" ):
                listener.enterIntLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntLiteral" ):
                listener.exitIntLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntLiteral" ):
                return visitor.visitIntLiteral(self)
            else:
                return visitor.visitChildren(self)




    def intLiteral(self):

        localctx = ConpyParser.IntLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_intLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(ConpyParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




