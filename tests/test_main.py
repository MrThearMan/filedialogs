import os
from pathlib import Path
from unittest.mock import patch

import pytest
import pywintypes

import filedialogs


def test_open_file_dialog__default():
    params = {}

    def side_effect(**kwargs):
        nonlocal params
        params = kwargs
        return "foo", 0, 0

    with patch("filedialogs.filedialogs.GetOpenFileNameW", side_effect=side_effect):
        file_path = filedialogs.open_file_dialog()

    assert file_path == "foo"
    assert params == {
        "DefExt": "",
        "File": "",
        "Filter": "All Files\x00*.*\x00",
        "Flags": 524288,
        "InitialDir": os.getcwd(),
        "MaxFile": 65536,
        "Title": None,
    }


def test_open_file_dialog__title_dir_name_ext():
    params = {}

    def side_effect(**kwargs):
        nonlocal params
        params = kwargs
        return "foo", 0, 0

    with patch("filedialogs.filedialogs.GetOpenFileNameW", side_effect=side_effect):
        file_path = filedialogs.open_file_dialog("title", "dir", "name", "ext")

    assert file_path == "foo"
    assert params == {
        "DefExt": "ext",
        "File": "name",
        "Filter": "All Files\x00*.*\x00",
        "Flags": 524288,
        "InitialDir": "dir",
        "MaxFile": 65536,
        "Title": "title",
    }


def test_open_file_dialog__extensions():
    params = {}

    def side_effect(**kwargs):
        nonlocal params
        params = kwargs
        return "foo", 0, 0

    with patch("filedialogs.filedialogs.GetOpenFileNameW", side_effect=side_effect):
        file_path = filedialogs.open_file_dialog(ext=[("Python", "py"), ("Image", "jpg")])

    assert file_path == "foo"
    assert params == {
        "DefExt": "",
        "File": "",
        "Filter": "Python\x00*.py\x00Image\x00*.jpg\x00",
        "Flags": 524288,
        "InitialDir": os.getcwd(),
        "MaxFile": 65536,
        "Title": None,
    }


def test_open_file_dialog__extensions__multiple():
    params = {}

    def side_effect(**kwargs):
        nonlocal params
        params = kwargs
        return "foo", 0, 0

    with patch("filedialogs.filedialogs.GetOpenFileNameW", side_effect=side_effect):
        file_path = filedialogs.open_file_dialog(ext=[("Python", ("py", "pyx")), ("Image", ("jpg", "png"))])

    assert file_path == "foo"
    assert params == {
        "DefExt": "",
        "File": "",
        "Filter": "Python\x00*.py;*.pyx\x00Image\x00*.jpg;*.png\x00",
        "Flags": 524288,
        "InitialDir": os.getcwd(),
        "MaxFile": 65536,
        "Title": None,
    }


def test_open_file_dialog__multiselect():
    params = {}

    def side_effect(**kwargs):
        nonlocal params
        params = kwargs
        return "foo\0bar\0fizz\0buzz", 0, 0

    with patch("filedialogs.filedialogs.GetOpenFileNameW", side_effect=side_effect):
        file_path = filedialogs.open_file_dialog(multiselect=True)

    assert file_path == [str(Path("foo", "bar")), str(Path("foo", "fizz")), str(Path("foo", "buzz"))]
    assert params == {
        "DefExt": "",
        "File": "",
        "Filter": "All Files\x00*.*\x00",
        "Flags": 524800,
        "InitialDir": os.getcwd(),
        "MaxFile": 65536,
        "Title": None,
    }


def test_open_file_dialog__close():
    error = pywintypes.error()  # noqa
    error.winerror = 0
    print(error)

    with patch("filedialogs.filedialogs.GetOpenFileNameW", side_effect=error):
        file_path = filedialogs.open_file_dialog()

    assert file_path is None


def test_open_file_dialog__error():
    error = pywintypes.error()  # noqa
    error.winerror = 1
    print(error)

    with patch("filedialogs.filedialogs.GetOpenFileNameW", side_effect=error):
        with pytest.raises(OSError):
            filedialogs.open_file_dialog()


def test_save_file_dialog__default():
    params = {}

    def side_effect(**kwargs):
        nonlocal params
        params = kwargs
        return "foo", 0, 0

    with patch("filedialogs.filedialogs.GetSaveFileNameW", side_effect=side_effect):
        file_path = filedialogs.save_file_dialog()

    assert file_path == "foo"
    assert params == {
        "DefExt": "",
        "File": "",
        "Filter": "All Files\x00*.*\x00",
        "InitialDir": os.getcwd(),
        "MaxFile": 65536,
        "Title": None,
    }


def test_save_file_dialog__title_dir_name_ext():
    params = {}

    def side_effect(**kwargs):
        nonlocal params
        params = kwargs
        return "foo", 0, 0

    with patch("filedialogs.filedialogs.GetSaveFileNameW", side_effect=side_effect):
        file_path = filedialogs.save_file_dialog("title", "dir", "name", "ext")

    assert file_path == "foo"
    assert params == {
        "DefExt": "ext",
        "File": "name",
        "Filter": "All Files\x00*.*\x00",
        "InitialDir": "dir",
        "MaxFile": 65536,
        "Title": "title",
    }


def test_save_file_dialog__extensions():
    params = {}

    def side_effect(**kwargs):
        nonlocal params
        params = kwargs
        return "foo", 0, 0

    with patch("filedialogs.filedialogs.GetSaveFileNameW", side_effect=side_effect):
        file_path = filedialogs.save_file_dialog(ext=[("Python", "py"), ("Image", "jpg")])

    assert file_path == "foo"
    assert params == {
        "DefExt": "",
        "File": "",
        "Filter": "Python\x00*.py\x00Image\x00*.jpg\x00",
        "InitialDir": os.getcwd(),
        "MaxFile": 65536,
        "Title": None,
    }


def test_save_file_dialog__extensions__multiple():
    params = {}

    def side_effect(**kwargs):
        nonlocal params
        params = kwargs
        return "foo", 0, 0

    with patch("filedialogs.filedialogs.GetSaveFileNameW", side_effect=side_effect):
        file_path = filedialogs.save_file_dialog(ext=[("Python", ("py", "pyx")), ("Image", ("jpg", "png"))])

    assert file_path == "foo"
    assert params == {
        "DefExt": "",
        "File": "",
        "Filter": "Python\x00*.py;*.pyx\x00Image\x00*.jpg;*.png\x00",
        "InitialDir": os.getcwd(),
        "MaxFile": 65536,
        "Title": None,
    }


def test_save_file_dialog__close():
    error = pywintypes.error()  # noqa
    error.winerror = 0
    print(error)

    with patch("filedialogs.filedialogs.GetSaveFileNameW", side_effect=error):
        file_path = filedialogs.save_file_dialog()

    assert file_path is None


def test_save_file_dialog__error():
    error = pywintypes.error()  # noqa
    error.winerror = 1
    print(error)

    with patch("filedialogs.filedialogs.GetSaveFileNameW", side_effect=error):
        with pytest.raises(OSError):
            filedialogs.save_file_dialog()


def test_open_folder_dialog__default():
    params = ()

    def side_effect(*args):
        nonlocal params
        params = args
        return 0, 0, 0

    with patch("filedialogs.filedialogs.shell.SHBrowseForFolder", side_effect=side_effect):
        with patch("filedialogs.filedialogs.shell.SHGetPathFromIDList", return_value=b"foo"):
            dir_path = filedialogs.open_folder_dialog()

    assert dir_path == "foo"
    assert params == (65548, [], "", 0, None, None)


def test_open_folder_dialog__title__encoding():
    params = ()

    def side_effect(*args):
        nonlocal params
        params = args
        return 0, 0, 0

    with patch("filedialogs.filedialogs.shell.SHBrowseForFolder", side_effect=side_effect):
        with patch("filedialogs.filedialogs.shell.SHGetPathFromIDList", return_value=b"foo"):
            dir_path = filedialogs.open_folder_dialog("title", "UTF-8")

    assert dir_path == "foo"
    assert params == (65548, [], "title", 0, None, None)
