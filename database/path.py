import os
from os import path


def get_script_dir():
    abs_path = path.abspath(__file__)  # полный путь к файлу скрипта
    return path.dirname(abs_path)
