import os

from utils import *

img_paths = traverse_files_with_ext('.', 'png')
for img_path in img_paths:
    if img_path.find('_') != -1:
        print(img_path)
        os.remove(img_path)