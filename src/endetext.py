import sys
from . import imgprocess


class LSB(object):
    def __init__(self, img: str, text="./test/encode_text.txt"):
        self.img = imgprocess.ImageProcess(img).openImage()
        self.text = text  # 信息所在文件
        self.width = self.img.size[0]
        self.height = self.img.size[1]

    def getKey(self) -> str:
        """获取待隐藏的信息, 返回信息的二进制形式"""
        f = open(self.text, "rb")
        fi = f.read()
        try:
            if 8 * len(fi) > 3 * self.width * self.height:
                raise AreaLess(self.width, self.height, fi)
        except Exception as result:
            print(result)
            f.close()
            sys.exit()
        else:
            return "".join(str(bin(i)).replace("0b", "").rjust(8, "0") for i in fi)

    def lsbEncode(self, out_filename="./test/decode_image.png"):
        """LSB隐写加密方法"""
        print("Start Encode".center(24, "-"))
        key = self.getKey()
        key_length = len(key)

        i = 0
        for h in range(self.height):
            for w in range(self.width):
                pixel = self.img.getpixel((w, h))
                r = pixel[0]
                g = pixel[1]
                b = pixel[2]

                if i == key_length:
                    break

                r = r - r % 2 + int(key[i])
                i += 1
                if i == key_length:
                    self.img.putpixel((w, h), (r, g, b))
                    break

                g = g - g % 2 + int(key[i])
                i += 1
                if i == key_length:
                    self.img.putpixel((w, h), (r, g, b))
                    break

                b = b - b % 2 + int(key[i])
                i += 1
                if i == key_length:
                    self.img.putpixel((w, h), (r, g, b))
                    break

                if i % 3 == 0:
                    self.img.putpixel((w, h), (r, g, b))

        print(f"信息已被隐藏入图片 \"{out_filename}\"")
        print("End Encode".center(24, "-"))

        self.img.save(out_filename)

    def lsbDecode(self, out_filename="./test/decode_text.txt"):
        """LSB隐写解密方法"""
        print("Start Decode".center(24, "-"))

        key_list = []
        for h in range(self.height):
            for w in range(self.width):
                pixel = self.img.getpixel((w, h))
                r = str(pixel[0] % 2)
                g = str(pixel[1] % 2)
                b = str(pixel[2] % 2)
                key_list.append(r)
                key_list.append(g)
                key_list.append(b)

        ret = ""
        tmp = ""
        for key in key_list:
            tmp += key
            if len(tmp) == 8:
                tmp = "0b" + tmp
                ret += chr(int(eval(tmp)))
                tmp = ""

        f = open(out_filename, "w", encoding="UTF-8")
        f.write(ret[0:50])
        print(f"图片中隐藏的信息已被写入 \"{out_filename}\"")
        print("End Decode".center(24, "-"))
        f.close()


class AreaLess(Exception):
    """待隐藏信息过长"""

    def __init__(self, height, width, key):
        self.width = width
        self.height = height
        self.key = key

    def __str__(self):
        return f"The key \"{self.key}\" is too long so it can't be hidden in the image."
