from PIL import Image
import os
#切图
def cut_image(image):
    width,height = image.size
    item_width = int(width / 4)
    item_height = int(height / 4)
    box_list = []
    for i in range(0,4):
        for j in range(0,4):
            box = (j * item_width,i * item_height,(j + 1) * item_width,(i + 1) * item_height)
            box_list.append(box)
    image_list = [image.crop(box)for box in box_list]
    return image_list
#保存
def save_images(image_list):
    index = 1
    for image in image_list:
        image.save('./' + str(index) + '.png','PNG')
        index += 1


file_path = "ycy.jpg"
image = Image.open(file_path)
image_list = cut_image(image)
save_images(image_list)


