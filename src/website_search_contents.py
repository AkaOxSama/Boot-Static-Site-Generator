import os


def search_contents_recursive(dir_path: str) -> str:
    file_list = []
    file_contents = os.listdir(dir_path)

    for content in file_contents:
        file_path = os.path.join(dir_path, content)
        if os.path.isfile(file_path):
            file_list.append(file_path)
        else:
            file_list.extend(search_contents_recursive(file_path))

    return file_list