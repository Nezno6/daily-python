from text_wrap import wrap_text, fill_text

def test_wrap_text():
    assert wrap_text("ABCDEFGHIJKLIMNOQRSTUVWXYZ",4) == ["ABCD","EFGH","IJKL","IMNO","QRST","UVWX","YZ"]

def test_fill_text():
    assert fill_text("ABCDEFGHIJKLIMNOQRSTUVWXYZ",4) == "ABCD\nEFGH\nIJKL\nIMNO\nQRST\nUVWX\nYZ"
