from http import HTTPStatus
import os
from re import A

from flask import safe_join

FILES_DIRECTORY = os.getenv("FILES_DIRECTORY")

absolute = os.path.abspath(FILES_DIRECTORY)

def create_files():
    try:
        os.mkdir(absolute)
    except FileExistsError:
        pass
    try:
        os.mkdir(f"{absolute}/.gif")
    except FileExistsError:
        pass
    try:
        os.mkdir(f"{absolute}/.jpg")
    except FileExistsError:
        pass
    try:
        os.mkdir(f"{absolute}/.png")
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

    if "." not in extension[0]:
        extension = "." + extension
        
    for *_, files in os. walk(f"{absolute}/{extension}"):
        for file in files:
            files_list.append(file)

    return files_list

def allowed_extensions_filter(extension):
    ALLOWED_EXTENSIONS = os.getenv("ALLOWED_EXTENSIONS")
    extensions_list= ALLOWED_EXTENSIONS.split(", ")

    try:
        dot_index= extension.index(".")
        extension = extension[dot_index:]
    except ValueError:
        pass

    for extension_item in extensions_list:
        if extension == extension_item or extension == extension_item[1:]:
            return False
    
    return True

def upload_file(file):

    extension = file.filename

    dot_index= extension.index(".")
    extension = extension[dot_index:]

    filepath = safe_join(absolute, f"{extension}/{file.filename}")

    file.save(filepath)