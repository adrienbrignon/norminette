import pathlib
import norminette


class File:
    """A file wrapper class."""

    def __init__(self, path: str = None):
        """The class constructor."""

        self.line = None
        self.line_number = 0
        self.path = pathlib.PurePath(path)

        try:
            self.fp = open(path)
        except IOError:
            self.fp = None

    def __str__(self):
        """The file textual representation."""

        return self.path.as_posix()

    @property
    def name(self) -> str:
        """Get the file name (without extension)."""

        return self.path.stem

    @property
    def extension(self) -> str:
        """The file extension."""

        return self.path.suffix[1:]

    @property
    def fullname(self) -> str:
        """Get the file fullname (with extension)."""

        return '{}.{}'.format(self.name, self.extension)

    def get_line(self) -> norminette.Line:
        """Get the file current line."""

        return self.line

    def get_content(self) -> str:
        """Get the file content (and restore the file pointer to where it was)."""

        pointer = self.fp.tell()

        self.fp.seek(0)

        content = self.fp.read()

        self.fp.seek(pointer)

        return content

    def next_line(self):
        """Get the file current line."""

        if self.fp is None:
            return None

        for line in iter(self):
            return line

    def __iter__(self) -> iter:
        """Iterator through the lines of the file."""

        if self.fp is None:
            return None

        while True:
            text = self.fp.readline()

            if not text:
                break

            self.line_number = self.line_number + 1
            self.line = norminette.Line(self, text, self.line_number)

            yield self.line

    def __del__(self):
        """The class destructor."""

        if self.fp is not None:
            self.fp.close()
