import os
import argparse
from antlr4 import *
from gen.JavaLexer import JavaLexer
from gen.JavaParserLabeled import JavaParserLabeled
from gen.JavaParserLabeledListener import JavaParserLabeledListener


class FindMethods(JavaParserLabeledListener):
    def __init__(self):
        self.methods = []

    def enterMethodDeclaration(self, ctx: JavaParserLabeled.MethodDeclarationContext):
        self.methods.append(str(ctx.IDENTIFIER()))


def extract_methods(project_directory):
    result = []
    for root, _, files in os.walk(project_directory):
        for file in files:
            if file.split('.')[-1] == 'java':
                file_path = os.path.join(root, file)
                stream = FileStream(file_path, encoding="utf8")

                lexer = JavaLexer(stream)
                token_stream = CommonTokenStream(lexer)

                parser = JavaParserLabeled(token_stream)
                tree = parser.compilationUnit()

                listener = FindMethods()
                walker = ParseTreeWalker()

                walker.walk(listener, tree)

                package_details = {
                    "package_name": file_path,
                    "methods": listener.methods
                }
                result.append(package_details)
    return result


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description='Java methods extractor')
    arg_parser.add_argument(
        'dir',
        type=str,
        help='Directory of Java project'
    )
    args = arg_parser.parse_args()
    methods = extract_methods(args.dir)
    print(methods)
