import os
import shutil

def copy_static_to_public(nested_directory = ""):
    base_static_dir = os.path.join(os.getcwd(), "static")
    base_public_dir = os.path.join(os.getcwd(), "public")

    current_nested_static_path = os.path.join(base_static_dir, nested_directory)
    current_nested_public_path = os.path.join(base_public_dir, nested_directory)

    if not os.path.exists(base_public_dir) and nested_directory == "":
        os.mkdir(base_public_dir)

    if len(os.listdir(base_public_dir)) > 0  and nested_directory == "":
        for name in os.listdir(base_public_dir):
            if os.path.isfile(os.path.join(base_public_dir, name)):
                os.remove(os.path.join(base_public_dir, name))
            elif os.path.isdir(os.path.join(base_public_dir, name)):
                shutil.rmtree(os.path.join(base_public_dir, name))

    for name in os.listdir(current_nested_static_path):
        if os.path.isfile(os.path.join(current_nested_static_path, name)):
            shutil.copy(os.path.join(current_nested_static_path, name), os.path.join(current_nested_public_path))
        elif os.path.isdir(os.path.join(current_nested_static_path, name)):
            os.mkdir(os.path.join(current_nested_public_path, name))
            copy_static_to_public(os.path.join(nested_directory, name))


