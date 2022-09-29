# Generated from C:/Users/alise/Documents/University/Semesters/Term 8/Compiler/Exams/Midterm/Project/grammars\Q1.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,9,2,0,7,0,1,0,1,0,1,0,1,0,3,0,7,8,0,1,0,0,0,1,0,0,0,8,0,6,
        1,0,0,0,2,3,5,1,0,0,3,7,5,3,0,0,4,5,5,2,0,0,5,7,5,4,0,0,6,2,1,0,
        0,0,6,4,1,0,0,0,7,1,1,0,0,0,1,6
    ]

class Q1Parser ( Parser ):

    grammarFileName = "Q1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'F1:'", "'F2:'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "Number1", 
                      "Number2", "Max11", "Max12", "Max13", "Max21", "Max22", 
                      "Max23" ]

    RULE_compilationUnit = 0

    ruleNames =  [ "compilationUnit" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    Number1=3
    Number2=4
    Max11=5
    Max12=6
    Max13=7
    Max21=8
    Max22=9
    Max23=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CompilationUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Number1(self):
            return self.getToken(Q1Parser.Number1, 0)

        def Number2(self):
            return self.getToken(Q1Parser.Number2, 0)

        def getRuleIndex(self):
            return Q1Parser.RULE_compilationUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompilationUnit" ):
                listener.enterCompilationUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompilationUnit" ):
                listener.exitCompilationUnit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompilationUnit" ):
                return visitor.visitCompilationUnit(self)
            else:
                return visitor.visitChildren(self)




    def compilationUnit(self):

        localctx = Q1Parser.CompilationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_compilationUnit)
        try:
            self.state = 6
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Q1Parser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2
                self.match(Q1Parser.T__0)
                self.state = 3
                self.match(Q1Parser.Number1)
                pass
            elif token in [Q1Parser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 4
                self.match(Q1Parser.T__1)
                self.state = 5
                self.match(Q1Parser.Number2)
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





