import os
import argparse
from antlr4 import *
from gen.JavaLexer import JavaLexer
from gen.JavaParserLabeled import JavaParserLabeled
from gen.JavaParserLabeledListener import JavaParserLabeledListener


class FindAttributesCount(JavaParserLabeledListener):
    def __init__(self):
        self.class_attributes_count = 0
        self.class_name = ""
        self.classes_tuple = []

    def enterClassDeclaration(self, ctx: JavaParserLabeled.ClassDeclarationContext):
        self.class_name = str(ctx.IDENTIFIER())

    def enterVariableDeclarator(self, ctx: JavaParserLabeled.VariableDeclaratorContext):
        self.class_attributes_count += 1

    def exitClassDeclaration(self, ctx: JavaParserLabeled.ClassDeclarationContext):
        self.classes_tuple.append((self.class_name, self.class_attributes_count))


def extract_attributes_count(project_directory):
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

                listener = FindAttributesCount()
                walker = ParseTreeWalker()

                walker.walk(listener, tree)

                class_attributes = {
                    "package_name": file_path,
                    "ClassAttributeCount": listener.classes_tuple
                }
                result.append(class_attributes)
    return result


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description='Java class attributes counter')
    arg_parser.add_argument(
        'dir',
        type=str,
        help='Directory of Java project'
    )
    args = arg_parser.parse_args()
    attributes = extract_attributes_count(args.dir)
    print(attributes)
