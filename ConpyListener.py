# Generated from Conpy.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ConpyParser import ConpyParser
else:
    from ConpyParser import ConpyParser

# This class defines a complete listener for a parse tree produced by ConpyParser.
class ConpyListener(ParseTreeListener):

    # Enter a parse tree produced by ConpyParser#main.
    def enterMain(self, ctx:ConpyParser.MainContext):
        pass

    # Exit a parse tree produced by ConpyParser#main.
    def exitMain(self, ctx:ConpyParser.MainContext):
        pass


    # Enter a parse tree produced by ConpyParser#funcDef.
    def enterFuncDef(self, ctx:ConpyParser.FuncDefContext):
        pass

    # Exit a parse tree produced by ConpyParser#funcDef.
    def exitFuncDef(self, ctx:ConpyParser.FuncDefContext):
        pass


    # Enter a parse tree produced by ConpyParser#block.
    def enterBlock(self, ctx:ConpyParser.BlockContext):
        pass

    # Exit a parse tree produced by ConpyParser#block.
    def exitBlock(self, ctx:ConpyParser.BlockContext):
        pass


    # Enter a parse tree produced by ConpyParser#ifStmt.
    def enterIfStmt(self, ctx:ConpyParser.IfStmtContext):
        pass

    # Exit a parse tree produced by ConpyParser#ifStmt.
    def exitIfStmt(self, ctx:ConpyParser.IfStmtContext):
        pass


    # Enter a parse tree produced by ConpyParser#funcCall.
    def enterFuncCall(self, ctx:ConpyParser.FuncCallContext):
        pass

    # Exit a parse tree produced by ConpyParser#funcCall.
    def exitFuncCall(self, ctx:ConpyParser.FuncCallContext):
        pass


    # Enter a parse tree produced by ConpyParser#expr.
    def enterExpr(self, ctx:ConpyParser.ExprContext):
        pass

    # Exit a parse tree produced by ConpyParser#expr.
    def exitExpr(self, ctx:ConpyParser.ExprContext):
        pass


    # Enter a parse tree produced by ConpyParser#value.
    def enterValue(self, ctx:ConpyParser.ValueContext):
        pass

    # Exit a parse tree produced by ConpyParser#value.
    def exitValue(self, ctx:ConpyParser.ValueContext):
        pass


    # Enter a parse tree produced by ConpyParser#paramDef.
    def enterParamDef(self, ctx:ConpyParser.ParamDefContext):
        pass

    # Exit a parse tree produced by ConpyParser#paramDef.
    def exitParamDef(self, ctx:ConpyParser.ParamDefContext):
        pass


    # Enter a parse tree produced by ConpyParser#paramRef.
    def enterParamRef(self, ctx:ConpyParser.ParamRefContext):
        pass

    # Exit a parse tree produced by ConpyParser#paramRef.
    def exitParamRef(self, ctx:ConpyParser.ParamRefContext):
        pass


    # Enter a parse tree produced by ConpyParser#funcNameDef.
    def enterFuncNameDef(self, ctx:ConpyParser.FuncNameDefContext):
        pass

    # Exit a parse tree produced by ConpyParser#funcNameDef.
    def exitFuncNameDef(self, ctx:ConpyParser.FuncNameDefContext):
        pass


    # Enter a parse tree produced by ConpyParser#funcNameRef.
    def enterFuncNameRef(self, ctx:ConpyParser.FuncNameRefContext):
        pass

    # Exit a parse tree produced by ConpyParser#funcNameRef.
    def exitFuncNameRef(self, ctx:ConpyParser.FuncNameRefContext):
        pass


