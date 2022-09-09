from PIL import Image


class ImageProcess(object):
    """打开、保存图片"""

    def __init__(self, filename: str):
        self.filename = filename
        self.support = ["RGB"]

    def openImage(self):
        """打开RGB的图片"""
        img = Image.open(self.filename)
        try:
            if img.mode not in self.support:
                raise ModeError(img.mode)
        except Exception as result:
            print(result)
            return img.convert("RGB")
        else:
            return img


class ModeError(Exception):
    """img.mode异常"""

    def __init__(self, mode):
        self.support = ["RGB"]
        self.mode = mode

    def __str__(self):
        return f"Mode \"{self.mode}\" is not supported and it has been convert to \"RGB\""
