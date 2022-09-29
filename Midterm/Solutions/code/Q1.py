from antlr4 import *
from gen_Q1.Q1Parser import Q1Parser
from gen_Q1.Q1Lexer import Q1Lexer
from gen_Q1.Q1Listener import Q1Listener


class DemoListener(Q1Listener):
    def __init__(self):
        pass

    def enterCompilationUnit(self, ctx: Q1Parser.CompilationUnitContext):
        pass


def get_parse_tree(file_path):
    file = FileStream(file_path, encoding="utf-8")
    lexer = Q1Lexer(file)
    tokens = CommonTokenStream(lexer)
    parser = Q1Parser(tokens)
    return parser.compilationUnit()


def main():
    pass


if __name__ == "__main__":
    main()
