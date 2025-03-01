import os

from functions.generate_page import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):

    for file in os.listdir(dir_path_content):
        if os.path.isfile(os.path.join(dir_path_content, file)):
            generate_page(os.path.join(dir_path_content, file), template_path, dest_dir_path, basepath)
        elif os.path.isdir(os.path.join(dir_path_content, file)):
            generate_pages_recursive(os.path.join(dir_path_content, file), template_path, os.path.join(dest_dir_path, file), basepath)
