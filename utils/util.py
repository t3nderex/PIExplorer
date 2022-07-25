from argparse import FileType
import magic
import os


def search_dir(dir_path):
    files = os.listdir(dir_path)
    return files


