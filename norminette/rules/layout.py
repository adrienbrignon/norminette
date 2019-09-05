import norminette


class DeclarationsPerLine(norminette.Rule):
    """Check that the file contains an Epitech header."""

    CODE = 'L5'
    SEVERITY = norminette.Severity.MINOR

    def __init__(self, options: dict = {}):
        """The rule constructor."""

        self.options = options
        self._count = 0
        self._ignore_count = 0
        self._prev_coord = None
        self._latest_coord = None

    def get_description(self) -> str:
        """Get the rule description."""

        return 'Only {} declarations per line'.format(self.options.get('max', 1))

    def before(self):

        self._latest_coord = None

    def before_node(self, node: norminette.ast.Node) -> bool:
        """Whether or not the node should be checked."""

        if isinstance(node, norminette.ast.ParamList):
            self._ignore_count = len(node.params)

            return False

        if self._ignore_count > 0 and (isinstance(node, norminette.ast.Decl) or isinstance(node, norminette.ast.Typename)):
            self._ignore_count = self._ignore_count - 1

            return False

        return isinstance(node, norminette.ast.Decl)

    def on_node(self, node: norminette.ast.Node) -> bool:
        """Check the given node."""

        if self._prev_coord is not None and self._prev_coord.file == node.coord.file and self._prev_coord.line == node.coord.line:
            self._count = self._count + 1

            if self._latest_coord is not None and self._latest_coord.file == node.coord.file and self._latest_coord.line == node.coord.line:
                return True

            if self._count >= self.options.get('max', 1):
                self._latest_coord = node.coord

                return False

        self._prev_coord = node.coord
