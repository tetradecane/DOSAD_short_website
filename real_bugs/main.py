from image_lib import *
from utils import *
from params import *

img_paths = traverse_files_with_ext('.', 'png')
for img_path in img_paths:
    new_img = resize_and_crop(img_path, target_size=origin_size)
    new_path = os.path.splitext(img_path)[0] + '_processed.png'
    new_img.save(new_path)
