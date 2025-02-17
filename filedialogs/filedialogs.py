"""File dialog functions."""

import os
from typing import List, Optional, Tuple, Union

import pywintypes  # type: ignore[import-untyped]
from win32com.shell import shell, shellcon  # type: ignore[import-untyped]
from win32con import OFN_ALLOWMULTISELECT, OFN_EXPLORER  # type: ignore[import-untyped]
from win32gui import GetDesktopWindow, GetOpenFileNameW, GetSaveFileNameW  # type: ignore[import-untyped]

__all__ = [
    "open_file_dialog",
    "open_folder_dialog",
    "save_file_dialog",
]


def open_file_dialog(  # noqa: PLR0913
    title: Optional[str] = None,
    directory: Optional[str] = None,
    default_name: str = "",
    default_ext: str = "",
    ext: Optional[List[Tuple[str, Union[str, Tuple[str, ...]]]]] = None,
    multiselect: bool = False,
) -> Union[str, List[str], None]:
    """
    Open a file open dialog at a specified directory.

    :param title: Dialog title.
    :param directory: Directory to open file dialog in.
    :param default_name: Default file name.
    :param default_ext: Default file extension. Only letters, no dot.
    :param ext: List of available extension(s) description + name tuples,
                e.g. [("JPEG Image", "jpg"), ("PNG Image", "png")].
                or, [("MPEG-4 Variations", ("m4v", "mp4", "m4p")), ("AVI Variations", ("avi", "amv"))]
    :param multiselect: Allow multiple files to be selected.
    :return: Path to a file to open if multiselect=False.
             List of the paths to files, which should be opened if multiselect=True.
             None if file open dialog canceled.
    :raises IOError: File open dialog failed.
    """
    # https://programtalk.com/python-examples/win32gui.GetOpenFileNameW/

    if directory is None:
        directory = os.getcwd()  # noqa: PTH109

    flags = OFN_EXPLORER
    if multiselect:
        flags = flags | OFN_ALLOWMULTISELECT

    if ext is None:
        ext_filter = "All Files\0*.*\0"
    else:
        ext_filter = ""
        for name, extensions in ext:
            if isinstance(extensions, str):
                ext_filter += f"{name}\0*.{extensions}\0"
                continue
            ext_filter += f"{name}\0" + ";".join(f"*.{extension}" for extension in extensions) + "\0"

    try:
        file_path, _, _ = GetOpenFileNameW(
            InitialDir=directory,
            File=default_name,
            Flags=flags,
            Title=title,
            MaxFile=2**16,
            Filter=ext_filter,
            DefExt=default_ext,
        )
    except pywintypes.error as error:
        if error.winerror == 0:
            return None
        raise IOError from error

    paths: list[str] = file_path.split("\0")

    if len(paths) == 1:
        return paths[0]

    for i in range(1, len(paths)):
        paths[i] = os.path.join(paths[0], paths[i])  # noqa: PTH118
    paths.pop(0)
    return paths


def save_file_dialog(
    title: Optional[str] = None,
    directory: Optional[str] = None,
    default_name: str = "",
    default_ext: str = "",
    ext: Optional[List[Tuple[str, Union[str, Tuple[str, ...]]]]] = None,
) -> Optional[str]:
    """
    Open a file save dialog at a specified directory.

    :param title: Dialog title.
    :param directory: Directory to open file dialog in.
    :param default_name: Default file name.
    :param default_ext: Default file extension. Only letters, no dot.
    :param ext: List of available extension(s) description + name tuples,
                e.g. [("JPEG Image", "jpg"), ("PNG Image", "png")].
                or, [("MPEG-4 Variations", ("m4v", "mp4", "m4p")), ("AVI Variations", ("avi", "amv"))]
    :return: Path file should be saved to. None if file save dialog canceled.
    :raises IOError: File save dialog failed.
    """
    # https://programtalk.com/python-examples/win32gui.GetSaveFileNameW/

    if directory is None:
        directory = os.getcwd()  # noqa: PTH109

    if ext is None:
        ext_filter = "All Files\0*.*\0"
    else:
        ext_filter = ""
        for name, extensions in ext:
            if isinstance(extensions, str):
                ext_filter += f"{name}\0*.{extensions}\0"
                continue
            ext_filter += f"{name}\0" + ";".join(f"*.{extension}" for extension in extensions) + "\0"

    try:
        file_path: str
        file_path, _, _ = GetSaveFileNameW(
            InitialDir=directory,
            File=default_name,
            Title=title,
            MaxFile=2**16,
            Filter=ext_filter,
            DefExt=default_ext,
        )
    except pywintypes.error as error:
        if error.winerror == 0:
            return None
        raise IOError from error

    return file_path


def open_folder_dialog(title: str = "", encoding: str = "ISO8859-1") -> Optional[str]:
    """
    Open a folder open dialog.

    :param title: Dialog title.
    :param encoding: Encoding for the folder. Default is Latin-1.
    :return: Path to folder. None if no folder selected.
    """
    # http://timgolden.me.uk/python/win32_how_do_i/browse-for-a-folder.html

    desktop_pidl = shell.SHGetFolderLocation(0, shellcon.CSIDL_DESKTOP, 0, 0)
    pidl, display_name, image_list = shell.SHBrowseForFolder(GetDesktopWindow(), desktop_pidl, title, 0, None, None)

    if (pidl, display_name, image_list) != (None, None, None):
        return shell.SHGetPathFromIDList(pidl).decode(encoding)  # type: ignore[no-any-return]
    return None
