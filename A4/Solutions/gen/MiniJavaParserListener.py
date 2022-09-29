from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniJavaParser import MiniJavaParser
else:
    from MiniJavaParser import MiniJavaParser

# This class defines a complete listener for a parse tree produced by MiniJavaParser.
class MiniJavaParserListener(ParseTreeListener):

    # Enter a parse tree produced by MiniJavaParser#program.
    def enterProgram(self, ctx:MiniJavaParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#program.
    def exitProgram(self, ctx:MiniJavaParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#mainClass.
    def enterMainClass(self, ctx:MiniJavaParser.MainClassContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#mainClass.
    def exitMainClass(self, ctx:MiniJavaParser.MainClassContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#classDeclaration.
    def enterClassDeclaration(self, ctx:MiniJavaParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#classDeclaration.
    def exitClassDeclaration(self, ctx:MiniJavaParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#varDeclaration.
    def enterVarDeclaration(self, ctx:MiniJavaParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#varDeclaration.
    def exitVarDeclaration(self, ctx:MiniJavaParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:MiniJavaParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:MiniJavaParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#type_.
    def enterType_(self, ctx:MiniJavaParser.Type_Context):
        pass

    # Exit a parse tree produced by MiniJavaParser#type_.
    def exitType_(self, ctx:MiniJavaParser.Type_Context):
        pass


    # Enter a parse tree produced by MiniJavaParser#statement.
    def enterStatement(self, ctx:MiniJavaParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#statement.
    def exitStatement(self, ctx:MiniJavaParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expression6.
    def enterExpression6(self, ctx:MiniJavaParser.Expression6Context):
        pass

    # Exit a parse tree produced by MiniJavaParser#expression6.
    def exitExpression6(self, ctx:MiniJavaParser.Expression6Context):
        pass


    # Enter a parse tree produced by MiniJavaParser#expression7.
    def enterExpression7(self, ctx:MiniJavaParser.Expression7Context):
        pass

    # Exit a parse tree produced by MiniJavaParser#expression7.
    def exitExpression7(self, ctx:MiniJavaParser.Expression7Context):
        pass


    # Enter a parse tree produced by MiniJavaParser#expression4.
    def enterExpression4(self, ctx:MiniJavaParser.Expression4Context):
        pass

    # Exit a parse tree produced by MiniJavaParser#expression4.
    def exitExpression4(self, ctx:MiniJavaParser.Expression4Context):
        pass


    # Enter a parse tree produced by MiniJavaParser#expression5.
    def enterExpression5(self, ctx:MiniJavaParser.Expression5Context):
        pass

    # Exit a parse tree produced by MiniJavaParser#expression5.
    def exitExpression5(self, ctx:MiniJavaParser.Expression5Context):
        pass


    # Enter a parse tree produced by MiniJavaParser#expression2.
    def enterExpression2(self, ctx:MiniJavaParser.Expression2Context):
        pass

    # Exit a parse tree produced by MiniJavaParser#expression2.
    def exitExpression2(self, ctx:MiniJavaParser.Expression2Context):
        pass


    # Enter a parse tree produced by MiniJavaParser#expression3.
    def enterExpression3(self, ctx:MiniJavaParser.Expression3Context):
        pass

    # Exit a parse tree produced by MiniJavaParser#expression3.
    def exitExpression3(self, ctx:MiniJavaParser.Expression3Context):
        pass


    # Enter a parse tree produced by MiniJavaParser#expression1.
    def enterExpression1(self, ctx:MiniJavaParser.Expression1Context):
        pass

    # Exit a parse tree produced by MiniJavaParser#expression1.
    def exitExpression1(self, ctx:MiniJavaParser.Expression1Context):
        pass


    # Enter a parse tree produced by MiniJavaParser#expression8.
    def enterExpression8(self, ctx:MiniJavaParser.Expression8Context):
        pass

    # Exit a parse tree produced by MiniJavaParser#expression8.
    def exitExpression8(self, ctx:MiniJavaParser.Expression8Context):
        pass


    # Enter a parse tree produced by MiniJavaParser#expression10.
    def enterExpression10(self, ctx:MiniJavaParser.Expression10Context):
        pass

    # Exit a parse tree produced by MiniJavaParser#expression10.
    def exitExpression10(self, ctx:MiniJavaParser.Expression10Context):
        pass


    # Enter a parse tree produced by MiniJavaParser#expression9.
    def enterExpression9(self, ctx:MiniJavaParser.Expression9Context):
        pass

    # Exit a parse tree produced by MiniJavaParser#expression9.
    def exitExpression9(self, ctx:MiniJavaParser.Expression9Context):
        pass


    # Enter a parse tree produced by MiniJavaParser#expression12.
    def enterExpression12(self, ctx:MiniJavaParser.Expression12Context):
        pass

    # Exit a parse tree produced by MiniJavaParser#expression12.
    def exitExpression12(self, ctx:MiniJavaParser.Expression12Context):
        pass


    # Enter a parse tree produced by MiniJavaParser#expression01.
    def enterExpression01(self, ctx:MiniJavaParser.Expression01Context):
        pass

    # Exit a parse tree produced by MiniJavaParser#expression01.
    def exitExpression01(self, ctx:MiniJavaParser.Expression01Context):
        pass


    # Enter a parse tree produced by MiniJavaParser#expression11.
    def enterExpression11(self, ctx:MiniJavaParser.Expression11Context):
        pass

    # Exit a parse tree produced by MiniJavaParser#expression11.
    def exitExpression11(self, ctx:MiniJavaParser.Expression11Context):
        pass


    # Enter a parse tree produced by MiniJavaParser#expression00.
    def enterExpression00(self, ctx:MiniJavaParser.Expression00Context):
        pass

    # Exit a parse tree produced by MiniJavaParser#expression00.
    def exitExpression00(self, ctx:MiniJavaParser.Expression00Context):
        pass


    # Enter a parse tree produced by MiniJavaParser#expression03.
    def enterExpression03(self, ctx:MiniJavaParser.Expression03Context):
        pass

    # Exit a parse tree produced by MiniJavaParser#expression03.
    def exitExpression03(self, ctx:MiniJavaParser.Expression03Context):
        pass


    # Enter a parse tree produced by MiniJavaParser#expression02.
    def enterExpression02(self, ctx:MiniJavaParser.Expression02Context):
        pass

    # Exit a parse tree produced by MiniJavaParser#expression02.
    def exitExpression02(self, ctx:MiniJavaParser.Expression02Context):
        pass


    # Enter a parse tree produced by MiniJavaParser#expression04.
    def enterExpression04(self, ctx:MiniJavaParser.Expression04Context):
        pass

    # Exit a parse tree produced by MiniJavaParser#expression04.
    def exitExpression04(self, ctx:MiniJavaParser.Expression04Context):
        pass


    # Enter a parse tree produced by MiniJavaParser#identifier.
    def enterIdentifier(self, ctx:MiniJavaParser.IdentifierContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#identifier.
    def exitIdentifier(self, ctx:MiniJavaParser.IdentifierContext):
        pass



del MiniJavaParser