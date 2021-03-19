"""File dialog functions."""

import os
import pywintypes
from win32gui import GetDesktopWindow, GetOpenFileNameW, GetSaveFileNameW
from win32com.shell import shell, shellcon
from win32con import OFN_EXPLORER, OFN_ALLOWMULTISELECT


__all__ = [
    "open_file_dialog",
    "save_file_dialog",
    "open_folder_fialog"
]


def open_file_dialog(title=None, directory=os.getcwd(), default_name="", default_ext="", ext="All Files\0*.*\0", multiselect=False):
    """Open a file open dialog at a specified directory.

    :param title: Dialog title.
    :type title: str
    :param directory: Directory to open file dialog in.
    :type directory: str
    :param default_name: Default file name.
    :type default_name: str
    :param default_ext: Default file extension. Only letters, no dot.
    :type default_ext: str
    :param ext: Extensions that are allowed. Format: "Format1\0*.ext1\0Format2\0*.ext2\0".
    :type ext: str
    :param multiselect: Allow multiple files to be selected.
    :type multiselect: bool
    :return: Path to a file to open if multiselect=False. List of the paths to files which should be opened if multiselect=True. None if file open dialog canceled.
    :rtype: str or list[str] or None
    :raises IOError: File open dialog failed.
    """

    # https://programtalk.com/python-examples/win32gui.GetOpenFileNameW/

    flags = OFN_EXPLORER
    if multiselect:
        flags = flags | OFN_ALLOWMULTISELECT

    try:
        file_path, _, _ = GetOpenFileNameW(InitialDir=directory, File=default_name, Flags=flags, Title=title, MaxFile=2 ** 16, Filter=ext, DefExt=default_ext)

        paths = file_path.split('\0')

        if len(paths) == 1:
            return paths[0]
        else:
            for i in range(1, len(paths)):
                paths[i] = os.path.join(paths[0], paths[i])
            paths.pop(0)

        return paths

    except pywintypes.error as e:
        if e.winerror == 0:
            return
        else:
            raise IOError


def save_file_dialog(title=None, directory=os.getcwd(), default_name="", default_ext="", ext="All Files\0*.*\0"):
    """Open a file save dialog at a specified directory.

    :param title: Dialog title.
    :type title: str
    :param directory: Directory to open file dialog in.
    :type directory: str
    :param default_name: Default file name.
    :type default_name: str
    :param default_ext: Default file extension. Only letters, no dot.
    :type default_ext: str
    :param ext: Extensions that are allowed. Format: "Format1\0*.ext1\0Format2\0*.ext2\0".
    :type ext: str
    :return: Path file should be save to. None if file save dialog canceled.
    :rtype: str or None
    :raises IOError: File save dialog failed.
    """

    # https://programtalk.com/python-examples/win32gui.GetSaveFileNameW/

    try:
        file_path, _, _ = GetSaveFileNameW(InitialDir=directory, File=default_name, Title=title, MaxFile=2 ** 16, Filter=ext, DefExt=default_ext)

        return file_path

    except pywintypes.error as e:
        if e.winerror == 0:
            return
        else:
            raise IOError


def open_folder_dialog(title="", encoding="ISO8859-1"):
    """Open a folder open dialog.

    :param title: Dialog title.
    :type title: str
    :param encoding: Encoding for the folder. Default is for Finnish letters.
    :type encoding: str
    :return: Path to folder. None if no folder selected.
    :rtype: str
    """

    # http://timgolden.me.uk/python/win32_how_do_i/browse-for-a-folder.html

    desktop_pidl = shell.SHGetFolderLocation(0, shellcon.CSIDL_DESKTOP, 0, 0)
    pidl, display_name, image_list = shell.SHBrowseForFolder(GetDesktopWindow(), desktop_pidl, title, 0, None, None)

    if (pidl, display_name, image_list) != (None, None, None):
        return shell.SHGetPathFromIDList(pidl).decode(encoding)
