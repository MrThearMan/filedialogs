# File dialogs for Windows

[![Coverage Status][coverage-badge]][coverage]
[![GitHub Workflow Status][status-badge]][status]
[![PyPI][pypi-badge]][pypi]
[![GitHub][licence-badge]][licence]
[![GitHub Last Commit][repo-badge]][repo]
[![GitHub Issues][issues-badge]][issues]
[![Downloads][downloads-badge]][pypi]
[![Python Version][version-badge]][pypi]

```shell
pip install windows-filedialogs
```

---

**Documentation**: [https://mrthearman.github.io/filedialogs/](https://mrthearman.github.io/filedialogs/)

**Source Code**: [https://github.com/MrThearMan/filedialogs/](https://github.com/MrThearMan/filedialogs/)

**Contributing**: [https://github.com/MrThearMan/filedialogs/blob/main/CONTRIBUTING.md](https://github.com/MrThearMan/filedialogs/blob/main/CONTRIBUTING.md)

---

Implements easy Windows file dialog functions. Requires the [pywin32](https://pypi.org/project/pywin32/) module.

### Basic use:

```python
from filedialogs import save_file_dialog, open_file_dialog, open_folder_dialog

openpath = open_file_dialog()
if openpath:
    with open(openpath, "r") as f:
        ...

savepath = save_file_dialog()
if savepath:
    with open(savepath, "w") as f:
        ...

openfolder = open_folder_dialog()
if openfolder:
    with open(os.path.join(openfolder, ...), "w") as f:
        ...
```

## Documentation:

#### *open_file_dialog*
* title: str - Dialog title. Default is no title.
* directory: str - Directory to open file dialog in. Default is the current working directory.
* default_name: str - Default file name on dialog open. Default is empty.
* default_ext: str - Default file extension on dialog open. Default is no extension.
* ext: list[tuple[str, str | tuple[str, ...]]] - List of available extensions as (description, extension) tuples. Default is ("All files", "*").
* multiselect: bool - Allow multiple files to be selected. Default is False.

Returns: Path to a file to open if multiselect=False. List of the paths to files which should be opened if multiselect=True. None if file open dialog canceled.

Raises: IOError - File open dialog failed.

---

#### *save_file_dialog*
* title: str - Dialog title. Default is no title.
* directory: str - Directory to open file dialog in. Default is the current working directory.
* default_name: str - Default file name on dialog open. Default is empty.
* default_ext: str - Default file extension on dialog open. Default is no extension.
* ext: list[tuple[str, str | tuple[str, ...]]]  - List of available extensions as (description, extension) tuples. Default is ("All files", "*").

Returns: Path file should be save to. None if file save dialog canceled.

Raises: IOError - File save dialog failed.

---

#### *open_folder_dialog*
* title: str - Dialog title. Default is no title.
* encoding: str - Encoding for the folder. Default is Latin-1.

Returns: Path to folder. None if no folder selected.

---

[coverage-badge]: https://coveralls.io/repos/github/MrThearMan/filedialogs/badge.svg?branch=main
[status-badge]: https://img.shields.io/github/actions/workflow/status/MrThearMan/filedialogs/test.yml?branch=main
[pypi-badge]: https://img.shields.io/pypi/v/windows-filedialogs
[licence-badge]: https://img.shields.io/github/license/MrThearMan/filedialogs
[repo-badge]: https://img.shields.io/github/last-commit/MrThearMan/filedialogs
[issues-badge]: https://img.shields.io/github/issues-raw/MrThearMan/filedialogs
[version-badge]: https://img.shields.io/pypi/pyversions/windows-filedialogs
[downloads-badge]: https://img.shields.io/pypi/dm/windows-filedialogs

[coverage]: https://coveralls.io/github/MrThearMan/filedialogs?branch=main
[status]: https://github.com/MrThearMan/filedialogs/actions/workflows/test.yml
[pypi]: https://pypi.org/project/windows-filedialogs
[licence]: https://github.com/MrThearMan/filedialogs/blob/main/LICENSE
[repo]: https://github.com/MrThearMan/filedialogs/commits/main
[issues]: https://github.com/MrThearMan/filedialogs/issues
