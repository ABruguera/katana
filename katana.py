import sys
from os.path import splitext
from PIL import Image

# key: height, values: [width]
resolutions = {
    900: [
        1600
    ],
    1080: [
        1920
    ],
    1440: [
        2560
    ]
}

for path in sys.argv[1:]:
    im = Image.open(path)
    file_path_arr = im.filename.split('\\')
    file_name_arr = splitext(file_path_arr[len(file_path_arr)-1])
    file_name = file_name_arr[0]
    file_format = file_name_arr[1]
    file_path = im.filename.replace(file_name+file_format, '')
    img_height = im.size[1]
    img_width = im.size[0]

    quantity = 0
    for w in resolutions[img_height]:
        if img_width % w == 0:
            quantity = int(img_width / w)
            img_width = w
            break
    if quantity > 1:
        current_x = 0
        for i in range(1, quantity+1):
            to_x = img_width * i
            new_img = im.crop((current_x, 0, to_x, img_height))
            new_img.save(file_path + file_name + f'-{i}' + file_format)
            current_x = to_x
