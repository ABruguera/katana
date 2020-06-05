import sys
from os.path import splitext
from PIL import Image


for path in sys.argv[1:]:
    im = Image.open(path)
    file_path_arr = im.filename.split('\\')
    file_name_arr = splitext(file_path_arr[len(file_path_arr)-1])
    file_name = file_name_arr[0]
    file_format = file_name_arr[1]
    file_path = im.filename.replace(file_name+file_format, '')
    left_img = im.crop((0, 0, 1920, 1080))
    right_img = im.crop((1920, 0, 3840, 1080))
    left_img.save(file_path + file_name + '-left' + file_format)
    right_img.save(file_path + file_name + '-right' + file_format)
