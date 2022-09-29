from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniJavaParser import MiniJavaParser
else:
    from MiniJavaParser import MiniJavaParser

# This class defines a complete generic visitor for a parse tree produced by MiniJavaParser.

class MiniJavaParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniJavaParser#program.
    def visitProgram(self, ctx:MiniJavaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#mainClass.
    def visitMainClass(self, ctx:MiniJavaParser.MainClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#classDeclaration.
    def visitClassDeclaration(self, ctx:MiniJavaParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#varDeclaration.
    def visitVarDeclaration(self, ctx:MiniJavaParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:MiniJavaParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#type_.
    def visitType_(self, ctx:MiniJavaParser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#statement.
    def visitStatement(self, ctx:MiniJavaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expression6.
    def visitExpression6(self, ctx:MiniJavaParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expression7.
    def visitExpression7(self, ctx:MiniJavaParser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expression4.
    def visitExpression4(self, ctx:MiniJavaParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expression5.
    def visitExpression5(self, ctx:MiniJavaParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expression2.
    def visitExpression2(self, ctx:MiniJavaParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expression3.
    def visitExpression3(self, ctx:MiniJavaParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expression1.
    def visitExpression1(self, ctx:MiniJavaParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expression8.
    def visitExpression8(self, ctx:MiniJavaParser.Expression8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expression10.
    def visitExpression10(self, ctx:MiniJavaParser.Expression10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expression9.
    def visitExpression9(self, ctx:MiniJavaParser.Expression9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expression12.
    def visitExpression12(self, ctx:MiniJavaParser.Expression12Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expression01.
    def visitExpression01(self, ctx:MiniJavaParser.Expression01Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expression11.
    def visitExpression11(self, ctx:MiniJavaParser.Expression11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expression00.
    def visitExpression00(self, ctx:MiniJavaParser.Expression00Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expression03.
    def visitExpression03(self, ctx:MiniJavaParser.Expression03Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expression02.
    def visitExpression02(self, ctx:MiniJavaParser.Expression02Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expression04.
    def visitExpression04(self, ctx:MiniJavaParser.Expression04Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#identifier.
    def visitIdentifier(self, ctx:MiniJavaParser.IdentifierContext):
        return self.visitChildren(ctx)



del MiniJavaParser