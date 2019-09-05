import norminette


class ColumnsCount(norminette.Rule):
    """Check the number of lines inside of a function."""

    CODE = 'F3'
    SEVERITY = norminette.Severity.MAJOR

    def get_description(self) -> str:
        """Get the rule description."""

        return 'This line exceeds the maximum of {} columns'.format(self.options.get('max', 80))

    def on_line(self, line: norminette.Line) -> bool:
        """Check the given line."""

        return len(str(line).expandtabs(self.options.get('tab_width', 4))) <= self.options.get('max', 80)


class FunctionLinesCount(norminette.Rule):
    """Check the number of lines inside of a function."""

    CODE = 'F4'
    SEVERITY = norminette.Severity.MAJOR

    def get_description(self) -> str:
        """Get the rule description."""

        return 'Function body contains too many lines'

    def on_node(self, node: norminette.ast.Node) -> bool:
        """Check the given file."""

        return True


class FunctionArgumentsCount(norminette.Rule):
    """Check the number of lines inside of a function."""

    CODE = 'F5'
    SEVERITY = norminette.Severity.MAJOR

    def get_description(self) -> str:
        """Get the rule description."""

        return 'Function exceeds the maximum of {} arguments'.format(self.options.get('max', 4))

    def on_node(self, node: norminette.ast.Node) -> bool:
        """Check the given file."""

        arguments = 0

        if isinstance(node, norminette.ast.FuncDef):
            if node.decl.type.args is None:
                return True

            for arg in node.decl.type.args:
                arguments = arguments + 1

        return arguments <= self.options.get('max', 4)


class FunctionWithoutArgumentsVoid(norminette.Rule):
    """Check the number of lines inside of a function."""

    CODE = 'F5'
    SEVERITY = norminette.Severity.MAJOR

    def get_description(self) -> str:
        """Get the rule description."""

        return 'A function taking no parameters should take void as argument'

    def before_node(self, node: norminette.ast.Node) -> bool:
        """Whether or not the node should be checked."""

        return isinstance(node, norminette.ast.FuncDef)

    def on_node(self, node: norminette.ast.Node) -> bool:
        """Check the given file."""

        if node.decl.type.args is None:
            return False

        return True
