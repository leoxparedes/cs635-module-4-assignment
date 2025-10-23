import pytest
from refactored_bank import database as db
import tempfile

def test_read_write_append(tmp_path):
    # use temp file
    f = tmp_path / "testfile.txt"
    # initially empty
    assert db.read_csv(f) == []
    # append one row
    db.append_csv(f, ["1", "Alice", "100"])
    content = db.read_csv(f)
    assert content == [["1", "Alice", "100"]]
    # append another row
    db.append_csv(f, ["2","Bob","200"])
    content = db.read_csv(f)
    assert content == [["1","Alice","100"], ["2","Bob","200"]]
    # overwrite file
    db.write_csv(f, [["X","Y","Z"]])
    content = db.read_csv(f)
    assert content == [["X","Y","Z"]]
