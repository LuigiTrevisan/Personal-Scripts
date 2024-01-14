import time
from tkinter.filedialog import askdirectory
from tkinter import Tk, messagebox
import os
import hashlib
from pathlib import Path
from collections import defaultdict


def remove_duplicates(directory):
    list_of_files = os.walk(directory)

    hashes = defaultdict(list)
    count = 0
    start_time = time.time()

    for root, folders, files in list_of_files:
        for file in files:
            file_path = Path(os.path.join(root, file))
            file_hash = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
            hashes[file_hash].append(file_path)

    for hash, files in hashes.items():
        if len(files) > 1:
            for file_path in files[1:]:
                os.remove(file_path)
                count += 1

    end_time = time.time()

    return count, end_time - start_time


def main():
    Tk().withdraw()
    directory = askdirectory(title='Select Folder', initialdir=os.getcwd())
    count, time_taken = remove_duplicates(directory)
    messagebox.showinfo(title='Duplicate Remover',
                        message=f'{count} files were deleted! \n Time taken: {time_taken} seconds')


if __name__ == "__main__":
    main()
