import os

FILES_DIRECTORY = os.getenv("FILES_DIRECTORY")

absolute = os.path.abspath(FILES_DIRECTORY)

def retrieve_all_files():
    files_list = []

    for *_, files in os. walk(absolute):
        for file in files:
            files_list.append(file)

    return files_list