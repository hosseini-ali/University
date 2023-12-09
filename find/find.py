"""
    This Script will just act like 'find' in Unix.
    It will search for files that you put names in sth.log,
        recursively from you base_path.
"""
import os

base_path = "/your/target/path/to/find/files"


with open("./sth.log", "r") as f:
    names = f.read().split("\n")

def get_directories(path: str) -> (bool, list[str]):
    try:
        return True, os.listdir(path)
    except NotADirectoryError:
        return False, path.split("/")[-1]

def compare(file_name: str, path) -> list[str]:
    res = [path for name in names if name in file_name]
    return res

res = []

def find(path: str):
    global res
    is_directory, dirs = get_directories(path)

    if is_directory:
        for dir in dirs:
            find(path + "/" + dir)

    else:
        res += compare(dirs, path)

    return res

for i in find(base_path):
    print(i)
