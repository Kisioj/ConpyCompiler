# Generated from Conpy.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("`\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\7\2\33")
        buf.write("\n\2\f\2\16\2\36\13\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3&\n\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\7\4.\n\4\f\4\16\4\61\13\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5<\n\5\3\6\3\6\3\6")
        buf.write("\5\6A\n\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\7\7O\n\7\f\7\16\7R\13\7\3\b\3\b\5\bV\n\b\3\t\3\t")
        buf.write("\3\n\3\n\3\13\3\13\3\f\3\f\3\f\2\3\f\r\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\2\2\2^\2\34\3\2\2\2\4!\3\2\2\2\6*\3\2\2\2")
        buf.write("\b\64\3\2\2\2\n=\3\2\2\2\fE\3\2\2\2\16U\3\2\2\2\20W\3")
        buf.write("\2\2\2\22Y\3\2\2\2\24[\3\2\2\2\26]\3\2\2\2\30\33\5\4\3")
        buf.write("\2\31\33\5\n\6\2\32\30\3\2\2\2\32\31\3\2\2\2\33\36\3\2")
        buf.write("\2\2\34\32\3\2\2\2\34\35\3\2\2\2\35\37\3\2\2\2\36\34\3")
        buf.write("\2\2\2\37 \7\2\2\3 \3\3\2\2\2!\"\7\n\2\2\"#\5\24\13\2")
        buf.write("#%\7\3\2\2$&\5\20\t\2%$\3\2\2\2%&\3\2\2\2&\'\3\2\2\2\'")
        buf.write("(\7\4\2\2()\5\6\4\2)\5\3\2\2\2*/\7\5\2\2+.\5\b\5\2,.\5")
        buf.write("\n\6\2-+\3\2\2\2-,\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/\60\3")
        buf.write("\2\2\2\60\62\3\2\2\2\61/\3\2\2\2\62\63\7\6\2\2\63\7\3")
        buf.write("\2\2\2\64\65\7\13\2\2\65\66\7\3\2\2\66\67\5\f\7\2\678")
        buf.write("\7\4\2\28;\5\6\4\29:\7\f\2\2:<\5\6\4\2;9\3\2\2\2;<\3\2")
        buf.write("\2\2<\t\3\2\2\2=>\5\26\f\2>@\7\3\2\2?A\5\f\7\2@?\3\2\2")
        buf.write("\2@A\3\2\2\2AB\3\2\2\2BC\7\4\2\2CD\7\7\2\2D\13\3\2\2\2")
        buf.write("EF\b\7\1\2FG\5\16\b\2GP\3\2\2\2HI\f\5\2\2IJ\7\b\2\2JO")
        buf.write("\5\f\7\6KL\f\4\2\2LM\7\t\2\2MO\5\f\7\5NH\3\2\2\2NK\3\2")
        buf.write("\2\2OR\3\2\2\2PN\3\2\2\2PQ\3\2\2\2Q\r\3\2\2\2RP\3\2\2")
        buf.write("\2SV\5\22\n\2TV\7\r\2\2US\3\2\2\2UT\3\2\2\2V\17\3\2\2")
        buf.write("\2WX\7\16\2\2X\21\3\2\2\2YZ\7\16\2\2Z\23\3\2\2\2[\\\7")
        buf.write("\16\2\2\\\25\3\2\2\2]^\7\16\2\2^\27\3\2\2\2\f\32\34%-")
        buf.write("/;@NPU")
        return buf.getvalue()


class ConpyParser ( Parser ):

    grammarFileName = "Conpy.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "'*'", 
                     "'+'", "'func'", "'if'", "'else'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "FUNC", "IF", "ELSE", "INT", "NAME", "WHITESPACE", 
                      "NEWLINE" ]

    RULE_main = 0
    RULE_funcDef = 1
    RULE_block = 2
    RULE_ifStmt = 3
    RULE_funcCall = 4
    RULE_expr = 5
    RULE_value = 6
    RULE_paramDef = 7
    RULE_paramRef = 8
    RULE_funcNameDef = 9
    RULE_funcNameRef = 10

    ruleNames =  [ "main", "funcDef", "block", "ifStmt", "funcCall", "expr", 
                   "value", "paramDef", "paramRef", "funcNameDef", "funcNameRef" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    FUNC=8
    IF=9
    ELSE=10
    INT=11
    NAME=12
    WHITESPACE=13
    NEWLINE=14

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

        def funcNameDef(self):
            return self.getTypedRuleContext(ConpyParser.FuncNameDefContext,0)


        def block(self):
            return self.getTypedRuleContext(ConpyParser.BlockContext,0)


        def paramDef(self):
            return self.getTypedRuleContext(ConpyParser.ParamDefContext,0)


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
            self.funcNameDef()
            self.state = 33
            self.match(ConpyParser.T__0)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ConpyParser.NAME:
                self.state = 34
                self.paramDef()


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
        self.enterRule(localctx, 4, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(ConpyParser.T__2)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ConpyParser.IF or _la==ConpyParser.NAME:
                self.state = 43
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ConpyParser.IF]:
                    self.state = 41
                    self.ifStmt()
                    pass
                elif token in [ConpyParser.NAME]:
                    self.state = 42
                    self.funcCall()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.match(ConpyParser.T__3)
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
        self.enterRule(localctx, 6, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(ConpyParser.IF)
            self.state = 51
            self.match(ConpyParser.T__0)
            self.state = 52
            self.expr(0)
            self.state = 53
            self.match(ConpyParser.T__1)
            self.state = 54
            self.block()
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ConpyParser.ELSE:
                self.state = 55
                self.match(ConpyParser.ELSE)
                self.state = 56
                self.block()


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

        def funcNameRef(self):
            return self.getTypedRuleContext(ConpyParser.FuncNameRefContext,0)


        def expr(self):
            return self.getTypedRuleContext(ConpyParser.ExprContext,0)


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
        self.enterRule(localctx, 8, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.funcNameRef()
            self.state = 60
            self.match(ConpyParser.T__0)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ConpyParser.INT or _la==ConpyParser.NAME:
                self.state = 61
                self.expr(0)


            self.state = 64
            self.match(ConpyParser.T__1)
            self.state = 65
            self.match(ConpyParser.T__4)
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

        def value(self):
            return self.getTypedRuleContext(ConpyParser.ValueContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ConpyParser.ExprContext)
            else:
                return self.getTypedRuleContext(ConpyParser.ExprContext,i)


        def getRuleIndex(self):
            return ConpyParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ConpyParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.value()
            self._ctx.stop = self._input.LT(-1)
            self.state = 78
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 76
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = ConpyParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 70
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 71
                        self.match(ConpyParser.T__5)
                        self.state = 72
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = ConpyParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 73
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 74
                        self.match(ConpyParser.T__6)
                        self.state = 75
                        self.expr(3)
                        pass

             
                self.state = 80
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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


        def INT(self):
            return self.getToken(ConpyParser.INT, 0)

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
        self.enterRule(localctx, 12, self.RULE_value)
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ConpyParser.NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.paramRef()
                pass
            elif token in [ConpyParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.match(ConpyParser.INT)
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

    class ParamDefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(ConpyParser.NAME, 0)

        def getRuleIndex(self):
            return ConpyParser.RULE_paramDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamDef" ):
                listener.enterParamDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamDef" ):
                listener.exitParamDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamDef" ):
                return visitor.visitParamDef(self)
            else:
                return visitor.visitChildren(self)




    def paramDef(self):

        localctx = ConpyParser.ParamDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_paramDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(ConpyParser.NAME)
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
        self.enterRule(localctx, 16, self.RULE_paramRef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(ConpyParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncNameDefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(ConpyParser.NAME, 0)

        def getRuleIndex(self):
            return ConpyParser.RULE_funcNameDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncNameDef" ):
                listener.enterFuncNameDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncNameDef" ):
                listener.exitFuncNameDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncNameDef" ):
                return visitor.visitFuncNameDef(self)
            else:
                return visitor.visitChildren(self)




    def funcNameDef(self):

        localctx = ConpyParser.FuncNameDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funcNameDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(ConpyParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncNameRefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(ConpyParser.NAME, 0)

        def getRuleIndex(self):
            return ConpyParser.RULE_funcNameRef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncNameRef" ):
                listener.enterFuncNameRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncNameRef" ):
                listener.exitFuncNameRef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncNameRef" ):
                return visitor.visitFuncNameRef(self)
            else:
                return visitor.visitChildren(self)




    def funcNameRef(self):

        localctx = ConpyParser.FuncNameRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcNameRef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(ConpyParser.NAME)
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
        self._predicates[5] = self.expr_sempred
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
         




