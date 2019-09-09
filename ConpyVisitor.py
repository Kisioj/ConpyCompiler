# Generated from Conpy.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ConpyParser import ConpyParser
else:
    from ConpyParser import ConpyParser

# This class defines a complete generic visitor for a parse tree produced by ConpyParser.

class ConpyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ConpyParser#main.
    def visitMain(self, ctx:ConpyParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConpyParser#funcDef.
    def visitFuncDef(self, ctx:ConpyParser.FuncDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConpyParser#params.
    def visitParams(self, ctx:ConpyParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConpyParser#block.
    def visitBlock(self, ctx:ConpyParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConpyParser#ifStmt.
    def visitIfStmt(self, ctx:ConpyParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConpyParser#funcCall.
    def visitFuncCall(self, ctx:ConpyParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConpyParser#arguments.
    def visitArguments(self, ctx:ConpyParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConpyParser#valueExpr.
    def visitValueExpr(self, ctx:ConpyParser.ValueExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConpyParser#binaryExpr.
    def visitBinaryExpr(self, ctx:ConpyParser.BinaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConpyParser#value.
    def visitValue(self, ctx:ConpyParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConpyParser#paramRef.
    def visitParamRef(self, ctx:ConpyParser.ParamRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConpyParser#intLiteral.
    def visitIntLiteral(self, ctx:ConpyParser.IntLiteralContext):
        return self.visitChildren(ctx)



del ConpyParser