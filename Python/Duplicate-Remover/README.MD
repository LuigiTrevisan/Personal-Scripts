# Duplicate Remover

This script removes duplicate files from a folder by comparing their hashes.

## Setup

This script uses Python 3.8+ default libraries, so no additional setup is required other than installing Python 3.8 or above.

You might want to use pyinstaller to create an executable file for the script.

```sh
$ pip install pyinstaller
```

```sh
$ pyinstaller --noconfirm --clean --onefile --console --icon=icon.ico duplicateremover.py
```

The executable file will be located in the dist folder.

## Running

```sh
$ python duplicateremover.py
```

Or run the executable file located in the dist folder (if you used pyinstaller).

## Screenshots

### Before
![Before](https://i.imgur.com/c8IRKKr.png)

### After
![After](https://i.imgur.com/MLT7Ufu.png)

### Message Box after removing duplicates
![Message](https://i.imgur.com/bsTQIGi.png)