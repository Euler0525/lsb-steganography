from src import *


def main():
    while True:
        choice = input("加密信息请按1，解密信息请按2, 退出程序请按3: ")
        if choice == "1":
            encode_image = input(
                "请输入原始图片文件名(default=\"./test/encode_image.png\"):") or "./test/encode_image.png"
            encode_text = input(
                "请输入待隐藏信息的存储位置(default=\"./test/encode_text.txt\"):") or "./test/encode_text.txt"
            encode_obj = endetext.LSB(encode_image, encode_text)
            encode_obj.lsbEncode()
        elif choice == "2":
            decode_image = input(
                "请输入藏有信息的图片的文件名(default=\"./test/decode_image.png\"): ") or "./test/decode_image.png"
            decode_text = input(
                "请输入信息的存储位置(default=\"./test/decode_text.txt\"): ") or "./test/decode_text.txt"
            decode_obj = endetext.LSB(decode_image)
            decode_obj.lsbDecode(decode_text)
        elif choice == "3":
            exit()
        else:
            print("不许调皮！")


if __name__ == "__main__":
    try:
        main()
    except Exception as result:
        print(result)
