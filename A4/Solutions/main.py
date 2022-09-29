import os
from antlr4 import *
from gen.MiniJavaLexer import MiniJavaLexer
from gen.MiniJavaParser import MiniJavaParser
from MiniJavaListener import MiniJavaListener


def main():
    script_dir = os.path.dirname(__file__)
    rel_path = "java-samples/Calculator.java"
    input_address = os.path.join(script_dir, rel_path)
    print("Reading file ...")
    try:
        input_file = FileStream(input_address)
        lexer = MiniJavaLexer(input_file)
        stream = CommonTokenStream(lexer)
        parser = MiniJavaParser(stream)
        tree = parser.program()
        listener = MiniJavaListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
    except UnicodeDecodeError:
        print("UnicodeDecodeError occurred in reading " + input_address)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
