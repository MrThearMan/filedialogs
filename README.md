# File dialogs for windows

```
pip install windows-filedialogs
```

Implements easy windows file dialog functions. Requires the [pywin32](https://pypi.org/project/pywin32/) module.

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
* ext: list[tuple[str, str]] - List of available extensions as (description, extension) tuples. Default is ("All files", "*").
* multiselect: bool - Allow multiple files to be selected. Default is False.

Returns: Path to a file to open if multiselect=False. List of the paths to files which should be opened if multiselect=True. None if file open dialog canceled.

Raises: IOError - File open dialog failed.

---

#### *save_file_dialog*
* title: str - Dialog title. Default is no title.
* directory: str - Directory to open file dialog in. Default is the current working directory.
* default_name: str - Default file name on dialog open. Default is empty.
* default_ext: str - Default file extension on dialog open. Default is no extension.
* ext: list[tuple[str, str]] - List of available extensions as (description, extension) tuples. Default is ("All files", "*").

Returns: Path file should be save to. None if file save dialog canceled.

Raises: IOError - File save dialog failed.

---

#### *save_file_dialog*
* title: str - Dialog title. Default is no title.
* encoding: str - Encoding for the folder. Default is Latin-1.

Returns: Path to folder. None if no folder selected.

---