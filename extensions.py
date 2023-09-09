def get_extension_of_file(file):
    return str(file).split('.')[1].strip()

def check_extension_of_file(extension):
    extensions_dict = {
  "gif": "image/gif",
  "jpg": "image/jpeg",
  "jpeg": "image/jpeg",
  "png": "image/png",
  "pdf": "application/pdf",
  "txt": "application/txt",
  "zip": "application/zip"
}
    return extensions_dict[extension]

def return_mime_type(file):
    return check_extension_of_file(get_extension_of_file(file))