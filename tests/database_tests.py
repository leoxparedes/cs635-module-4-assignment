import pytest
from src import database as db
import tempfile

#Test for writing and appending to temp database file
def test_read_write_append(tmp_path):
    #Start with temp file
    f = tmp_path / "testfile.txt"
    #Initialize the file as empty
    assert db.read_csv(f) == []
    #Append one row
    db.append_csv(f, ["1", "Alice", "100"])
    content = db.read_csv(f)
    assert content == [["1", "Alice", "100"]]
    #Append another row
    db.append_csv(f, ["2","Bob","200"])
    content = db.read_csv(f)
    assert content == [["1","Alice","100"], ["2","Bob","200"]]
    #Overwrite the file
    db.write_csv(f, [["X","Y","Z"]])
    content = db.read_csv(f)
    assert content == [["X","Y","Z"]]
