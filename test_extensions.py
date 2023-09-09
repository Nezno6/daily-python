from extensions import return_mime_type

def test_return_mime_type():
    assert return_mime_type("file.gif") == "image/gif"
    assert return_mime_type("file.jpg") == "image/jpeg"
    assert return_mime_type("file.jpeg") == "image/jpeg"
    assert return_mime_type("file.png") == "image/png"
    assert return_mime_type("file.pdf") == "application/pdf"
    assert return_mime_type("file.txt") == "application/txt"
    assert return_mime_type("file.zip") == "application/zip"