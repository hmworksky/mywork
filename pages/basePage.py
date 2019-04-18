from airtest.core.api import Template
from public.tools import get_object


class BasePages:

    def __init__(self, file_name, resolution=None):
        self.resolution = resolution if resolution and isinstance(resolution, tuple) else (1080, 1920)
        self.file_name = file_name

    def get_image(self, image_name, record_pos=None):
        """获取图片地址"""
        img_url = get_object(self.file_name, image_name)
        return Template(img_url, record_pos=record_pos, resolution=self.resolution)
