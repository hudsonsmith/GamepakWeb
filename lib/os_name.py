from os import name as true_os_name


def get_os_name() -> str:
    """
    A function to get the operating system name.

    Args:
        None

    Returns:
        os_name: str
    """

    if true_os_name == "posix":
        try:
            # Get the file contents.
            content: str = open("/etc/issue").read()

            # Clean the content to get a clear name.
            bad_chars: list = ["\\n", "\l"]

            for char in bad_chars:
                content = content.replace(char, "")

            return content

        except:
            return "MacOS"

    else:
        return "Windows"
