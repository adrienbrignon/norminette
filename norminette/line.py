from __future__ import annotations
import norminette


class Line:
    """The line from a file."""

    def __init__(self, file: norminette.File, text: str, number: int):
        """The class constructor."""

        self.column = 0
        self.file = file
        self.text = text
        self.number = number

    def __str__(self) -> str:
        """The class textual representation."""

        return self.text

    def get_text(self) -> str:
        """Get text from line."""

        return self.text

    def set_text(self, text: str) -> Line:  # noqa: F821
        """Set line text."""

        self.text = text

        return self

    def get_number(self) -> int:
        """Get the line number."""

        return self.number

    def get_column(self) -> int:
        """Get the column number."""

        return self.column
