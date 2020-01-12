import os
import re
from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--root-path', help='Full Input Path')
parser.add_argument('-w', '--new-width', help='New image width')
args = parser.parse_args()

# The new width for images in the ROOT_PATH folder.
NEW_WIDTH = args.new_width or 640
# Path to the folder you want Python to find and resize images
ROOT_PATH = args.root_path or r'/PATH/TO/PICTURES'


def calc_new_height(width, height, new_width):
    return round(new_width * height / width)


def resize(root, file, new_width, new_img_name):
    original_img_path = os.path.join(root, file)
    new_img_path = os.path.join(root, new_img_name)

    try:
        new_width = int(new_width)
    except:
        raise TypeError(
            f'-w, --new-width or NEW_WIDTH must be a number. Sent "{NEW_WIDTH}".')

    pillow_img = Image.open(original_img_path)
    width, height = pillow_img.size

    new_height = calc_new_height(width, height, new_width)

    new_img = pillow_img.resize((new_width, new_height), Image.LANCZOS)

    try:
        new_img.save(
            new_img_path,
            optimize=True,
            quality=50,
            exif=pillow_img.info.get('exif')
        )
    except:
        try:
            new_img.save(
                new_img_path,
                optimize=True,
                quality=50,
            )
        except:
            raise RuntimeError(f'Could not convert "{original_img_path}".')

    print(f'Saved at {new_img_path}')


def is_image(extension):
    extension_lowercase = extension.lower()
    return bool(re.search(r'^\.(jpe?g|png)$', extension_lowercase))


def files_checks(root, file):
    filename, extension = os.path.splitext(file)

    if not is_image(extension):
        return

    flag = '_CONVERTED'

    if flag in file:
        return

    new_img_name = filename + flag + extension

    resize(root=root, file=file, new_width=NEW_WIDTH, new_img_name=new_img_name)


def files_loop(root, files):
    for file in files:
        files_checks(root, file)


def main(root_folder):
    for root, dirs, files in os.walk(root_folder):
        files_loop(root, files)


if __name__ == '__main__':
    main(ROOT_PATH)
