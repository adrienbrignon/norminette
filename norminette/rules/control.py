import norminette


class ControlMaxDepth(norminette.Rule):
    """Check the number of lines inside of a function."""

    CODE = 'F4'
    SEVERITY = norminette.Severity.MAJOR

    def get_description(self) -> str:
        """Get the rule description."""

        return 'Function body contains too many lines'

    def before_node(self, node: norminette.ast.Node) -> bool:
        """Whether or not the node should be checked."""

        return isinstance(node, norminette.ast.FuncDecl)

    def on_node(self, node: norminette.ast.Node) -> bool:
        """Check the given file."""

        return True
