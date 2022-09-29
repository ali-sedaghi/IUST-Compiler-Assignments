import queue
from AST import AST
from gen.MiniJavaParserListener import MiniJavaParserListener
from gen.MiniJavaParser import MiniJavaParser


class MiniJavaListener(MiniJavaParserListener):
    def __init__(self):
        self.ast = AST()
        self.q = queue.Queue()

    # AST Builder
    # def exitExpression00(self, ctx: MiniJavaParser.Expression00Context):
    #     value = ctx.ADD() | ctx.SUB() | ctx.MUL() | ctx.LT() | ctx.AND()
    #     self.ast.make_node(value, None, None)
    #
    # def exitIdentifier(self, ctx: MiniJavaParser.IdentifierContext):
    #     self.ast.add_child(None, None)
