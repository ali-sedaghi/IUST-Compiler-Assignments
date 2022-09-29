from antlr4 import *
from gen.JavaParserLabeled import JavaParserLabeled
from gen.JavaParserLabeledListener import JavaParserLabeledListener
from utils import Project, get_parse_tree, search_parent


def get_prefixes(ctx):
    access_branches = ctx.parentCtx.parentCtx.children
    type_branches = ctx.children
    prefixes = []

    for branch in access_branches:
        if type(branch).__name__ == "ModifierContext":
            prefixes.append(branch.getText())

    for branch in type_branches:
        if type(branch).__name__ == "TypeTypeOrVoidContext":
            prefixes.append(branch.getText())

    return prefixes


class DemoListener(JavaParserLabeledListener):
    def __init__(self):
        self.class_methods = dict()

    def enterMethodDeclaration(self, ctx: JavaParserLabeled.MethodDeclarationContext):
        prefixes = get_prefixes(ctx)
        if ("public" in prefixes) and ("void" in prefixes):
            parent_class_ctx = search_parent(ctx, ["ClassDeclarationContext"])
            parent_class_name = parent_class_ctx.IDENTIFIER().getText()
            methods = self.class_methods.get(parent_class_name, [])
            method_name = ctx.IDENTIFIER().getText()
            methods.append(method_name)
            self.class_methods[parent_class_name] = methods


def main(project_dir):
    p = Project(project_dir)
    p.get_java_files()

    for file_name, file_path in p.files:
        tree = get_parse_tree(file_path)
        demo = DemoListener()
        walker = ParseTreeWalker()
        walker.walk(demo, tree)
        print(f"public void methods in file {file_name}: {demo.class_methods}")


if __name__ == "__main__":
    main("../java_project_1/")
