# Generated from C:/Users/alise/Documents/University/Semesters/Term 8/Compiler/Exams/Midterm/Project/grammars\Q1.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Q1Parser import Q1Parser
else:
    from Q1Parser import Q1Parser

# This class defines a complete generic visitor for a parse tree produced by Q1Parser.

class Q1Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Q1Parser#compilationUnit.
    def visitCompilationUnit(self, ctx:Q1Parser.CompilationUnitContext):
        return self.visitChildren(ctx)



del Q1Parser