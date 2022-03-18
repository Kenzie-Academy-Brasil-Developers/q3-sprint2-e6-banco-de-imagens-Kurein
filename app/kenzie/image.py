import os

from flask import safe_join

FILES_DIRECTORY = os.getenv("FILES_DIRECTORY")
ALLOWED_EXTENSIONS = os.getenv("ALLOWED_EXTENSIONS")

absolute = os.path.abspath(FILES_DIRECTORY)

def create_files_dir():
    extensions_list= ALLOWED_EXTENSIONS.split(", ")
    try:
        os.mkdir(absolute)
    except FileExistsError:
        pass
    for extension in extensions_list:
        try:
            os.mkdir(f"{absolute}/{extension}")
        except FileExistsError:
            pass
        

def retrieve_all_files():
    files_list = []

    for *_, files in os. walk(absolute):
        for file in files:
            files_list.append(file)

    return files_list

def retrieve_extension_files(extension):
    files_list = []
        
    for *_, files in os. walk(f"{absolute}/{extension}"):
        for file in files:
            files_list.append(file)

    return files_list

def allowed_extensions_filter(extension):
    extensions_list= ALLOWED_EXTENSIONS.split(", ")

    try:
        ext = extension.split(".")[-1]
    except ValueError:
        pass

    for extension_item in extensions_list:
        if ext == extension_item:
            return False
    
    return True

def already_exists_filter(filename):
    file_list = retrieve_all_files()
    if filename in file_list:
        return True
    
    return False

def upload_file(file):

    extension = file.filename

    extension = file.split(".")[-1]

    filepath = safe_join(absolute, f"{extension}/{file.filename}")

    file.save(filepath)

def download_filepath(filename):

    extension = filename.split(".")[-1]

    filepath = safe_join(absolute, f"{extension}/{filename}")
    return filepath