import norminette

from colorama import Fore
from norminette import rules
from pycparser import parse_file


class NormNodeVisitor(norminette.ast.NodeVisitor):

    def __init__(self, rule: norminette.Rule):
        """The visitor constructor."""

        self.rule = rule
        self.current_parent = None

    def generic_visit(self, node: norminette.ast.Node):
        """Visit a node."""

        oldparent = self.current_parent
        self.current_parent = node

        if self.rule.before_node(node) and self.rule.on_node(node) is False:
            print(self.rule.get_color() + self.rule.get_code() + Fore.RESET, '|', node.coord, '|', self.rule.get_description())

        for n in node:
            self.visit(n)

        self.current_parent = oldparent


class Norm:
    """The norm class."""

    EPITECH = [

        # Control
        rules.ControlMaxDepth({max: 3}),

        # Layout
        rules.DeclarationsPerLine({'max': 1}),

        # Function
        rules.ColumnsCount({'max': 80}),
        rules.FunctionWithoutArgumentsVoid(),
        rules.FunctionLinesCount({'max': 20}),
        rules.FunctionArgumentsCount({'max': 4}),

        # Organization
        rules.FunctionsCount({'max': 5}),
        rules.FileName({'regex': r'^[a-z0-9_]+$', 'extensions': ['c', 'h']}),
        rules.ForbiddenFile({
            'name': r'^~\$',
            'extension': [r'gc*', 'o', 'a', 'out', 'so', 'exe']
        }),

        # Global scope
        rules.GlobalscopeFileHeader({
            'headers': [
                {'regex': norminette.constants.Epitech.C_HEADER, 'extensions': ['c', 'h']},
                {'regex': norminette.constants.Epitech.MAKEFILE_HEADER, 'names': ['Makefile']},
            ]
        })

    ]

    def __init__(self, rules: list = [], options: dict = {}):
        """The norm constructor."""

        self.rules = rules
        self.options = options

    def check(self, file: norminette.File):
        """Check a file and its lines for norm compliance."""

        for rule in self.rules:

            # Check the file.
            if rule.before_file(file) and rule.on_file(file) is False:
                print(rule.get_color() + rule.get_code() + Fore.RESET, '|', file.path.as_posix(), '|', rule.get_description())

            # Check each node of the AST.
            if file.extension in ['c', 'h']:
                ast = parse_file(str(file), use_cpp=True)
                visitor = NormNodeVisitor(rule)

                visitor.visit(ast)

        # Check each line of the file.
        for line in iter(file):
            for rule in self.rules:

                if rule.before_line(line) and rule.on_line(line) is False:
                    print(rule.get_color() + rule.get_code() + Fore.RESET, '|', line.file.path.as_posix(), '|', rule.get_description())
