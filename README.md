# File dialogs for windows

```
pip install windows_filedialogs
```

Implements easy windows file dialog functions. Requires the [pywin32](https://pypi.org/project/pywin32/) module.

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
