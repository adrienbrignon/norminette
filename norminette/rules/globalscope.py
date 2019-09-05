import re
import norminette


class GlobalscopeFileHeader(norminette.Rule):
    """Check that the file contains an Epitech header."""

    CODE = 'G1'
    SEVERITY = norminette.Severity.MAJOR

    def get_description(self) -> str:
        """Get the rule description."""

        return 'File header is missing or invalid'

    def on_file(self, file: norminette.File) -> bool:
        """Check the given file."""

        headers = self.options.get('headers', [])

        for header in headers:

            for name in header.get('names', []):
                if re.fullmatch(name, file.name):
                    return re.match(header.get('regex'), file.get_content()) is not None

            for extension in header.get('extensions', []):
                if re.fullmatch(extension, file.extension):
                    return re.match(header.get('regex'), file.get_content()) is not None

        return True
