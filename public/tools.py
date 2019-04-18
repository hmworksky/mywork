import os


def get_object(page, label):
    """获取图片地址，传递哪个页面，图片名字"""
    image_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'file')
    image_path = os.path.join(image_path, page)
    image_file = os.path.join(image_path, "{}.png".format(label))
    return image_file if os.path.isfile(image_file) else ''


if __name__ == '__main__':
    my_image = get_object('start', 'start')
    print(my_image)



