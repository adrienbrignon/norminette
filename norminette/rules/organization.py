import re
import norminette

from pycparser import parse_file, c_ast


class ForbiddenFile(norminette.Rule):
    """Check if some forbidden files are versioned."""

    CODE = 'O1'
    SEVERITY = norminette.Severity.MAJOR

    def get_description(self) -> str:
        """Get the rule description."""

        return 'Make sure not to commit this file'

    def on_file(self, file: norminette.File) -> bool:
        """Check the given file."""

        name = self.options.get('name', [])
        extension = self.options.get('extension', [])

        if type(name) is str and re.search(name, file.name) is not None:
            return False
        if type(extension) is str and re.search(extension, file.extension) is not None:
            return False

        if type(name) is list:
            for n in name:
                if re.search(n, file.name):
                    return False

        if type(extension) is list:
            for e in extension:
                if re.search(e, file.extension):
                    return False

        return True


class FunctionsCount(norminette.Rule):
    """Check that a file does not have too many functions."""

    CODE = 'O3'
    SEVERITY = norminette.Severity.MAJOR

    def get_description(self) -> str:
        """Get the rule description."""

        return 'This file contains more than {} functions'.format(self.options.get('max', 5))

    def before_file(self, file: norminette.File) -> bool:
        """Whether or not the given file should be checked."""

        return file.extension in self.options.get('extensions', ['c', 'h']) and file.fp is not None

    def on_file(self, file: norminette.File) -> bool:
        """Check the given file."""

        functions = 0

        try:
            ast = parse_file(str(file), use_cpp=True)
        except Exception as e:
            return True

        for node in ast:
            if isinstance(node, c_ast.FuncDef):
                functions = functions + 1

        return functions <= self.options.get('max', 5)


class FileName(norminette.Rule):
    """Check the file name."""

    CODE = 'O4'
    SEVERITY = norminette.Severity.MAJOR

    def get_description(self) -> str:
        """Get the rule description."""

        return 'This file has a name that does not respect the convention'

    def before_file(self, file: norminette.File) -> bool:
        """Whether or not this file should be checked."""

        return file.extension in self.options.get('extensions', ['c', 'h'])

    def on_file(self, file: norminette.File) -> bool:
        """Check the given file."""

        regex = self.options.get('regex', None)

        if regex is not None:
            return re.fullmatch(regex, file.name) is not None

        return True
