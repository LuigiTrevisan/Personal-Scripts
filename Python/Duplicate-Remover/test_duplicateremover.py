import os
import tempfile
from duplicateremover import remove_duplicates


def test_remove_duplicates():
    with tempfile.TemporaryDirectory() as tmpdirname:
        for i in range(3):
            with open(os.path.join(tmpdirname, f'file{i}.txt'), 'w') as f:
                f.write('test')

        count, _ = remove_duplicates(tmpdirname)

        assert count == 2
