import os
from antlr4 import *
from gen.JavaLexer import JavaLexer
from gen.JavaParserLabeled import JavaParserLabeled


class Project:
    def __init__(self, project_dir, project_name=None):
        self.project_dir = project_dir
        self.project_name = project_name
        self.files = []

    def get_java_files(self):
        for dir_path, _, file_names in os.walk(self.project_dir):
            for file in file_names:
                if '.java' in str(file):
                    path = os.path.join(dir_path, file)
                    path = path.replace("/", "\\")
                    path = os.path.abspath(path)
                    self.files.append((file, path))


def get_parse_tree(file_path):
    file = FileStream(file_path, encoding="utf-8")
    lexer = JavaLexer(file)
    tokens = CommonTokenStream(lexer)
    parser = JavaParserLabeled(tokens)
    return parser.compilationUnit()


def search_parent(ctx, type_names):
    # Traverse bottom up until reaching a class or method
    current = ctx.parentCtx
    while current is not None:
        type_name = type(current).__name__
        if type_name in type_names:
            return current
        current = current.parentCtx
    return None
