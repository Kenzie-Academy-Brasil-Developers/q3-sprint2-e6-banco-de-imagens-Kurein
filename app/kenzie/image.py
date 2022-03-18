import os

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
    try:
        os.mkdir(absolute)
    except FileExistsError:    
        for *_, files in os. walk(absolute):
            for file in files:
                files_list.append(file)

    print(absolute)

    return files_list