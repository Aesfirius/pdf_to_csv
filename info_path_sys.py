import os
import sys


def determine_os_path(_platform=None):
    """
    Return \ or / for detected platform.
    :param _platform: a string used to identify the platform
    """
    if not _platform:
        _platform = sys.platform
    if _platform.startswith('win'):
        result = "\\"
        return result
    else:
        return '/'


def path_to_project():
    suf = determine_os_path()
    path_to_p = os.path.dirname(os.path.abspath(__file__)) + suf
    return path_to_p
