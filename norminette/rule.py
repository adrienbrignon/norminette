from __future__ import annotations
from colorama import Fore
from pycparser import c_ast

import norminette


class Rule:
    """A base norm rule."""

    CODE = 'X0'
    SEVERITY = norminette.Severity.MINOR
    DESCRIPTION = 'No description provided'

    def __init__(self, options: dict = {}):
        """The rule constructor."""

        self.options = options

    def __str__(self):
        """The rule name."""

        return '[{}] {}'.format(self.get_code(), self.get_description())

    def before(self):
        """Called before the rule."""

        return

    def after(self):
        """Called after the rule."""

        return

    def get_color(self) -> str:
        """Get the color used for output."""

        colors = {
            norminette.Severity.MAJOR: Fore.RED,
            norminette.Severity.MINOR: Fore.YELLOW,
            norminette.Severity.INFO: Fore.CYAN
        }

        return colors.get(self.SEVERITY, Fore.RESET)

    def get_code(self) -> str:
        """Get the rule code."""

        return self.CODE

    def get_severity(self) -> Rule:  # noqa: F821
        """Get the rule severity."""

        return self.SEVERITY

    def get_description(self) -> str:
        """Get the rule description."""

        return self.DESCRIPTION

    def set_code(self, code: str) -> Rule:  # noqa: F821
        """Set the rule code."""

        self.code = code

        return self

    def set_severity(self, severity: norminette.Severity) -> Rule:  # noqa: F821
        """Set the rule severity."""

        self.severity = severity

        return self

    def before_file(self, file: norminette.File) -> bool:
        """Whether or not the file should be checked."""

        return True

    def on_file(self, file: norminette.File) -> bool:
        """Check the given file (the implementation is up to you)."""

        return True

    def before_line(self, line: norminette.Line) -> bool:
        """Whether or not the file should be checked."""

        return True

    def on_line(self, line: norminette.Line) -> bool:
        """Check the given line (the implementation is up to you)."""

        return True

    def before_node(self, node: c_ast.Node) -> bool:
        """Whether or not the node should be checked."""

        return True

    def on_node(self, node: c_ast.Node) -> bool:
        """Check the given node (the implementation is up to you)."""

        return True

    def before_ast(self, ast) -> bool:
        """Whether or not the AST should be checked."""

        return True

    def on_ast(self, ast) -> bool:
        """Check the given AST (the implementation is up to you.)."""

        return True
