# LSB图像隐写术

## 项目背景

### LSB隐写术

隐写术是一门关于信息隐藏的技巧与科学，所谓信息隐藏指的是不让除预期的接收者之外的任何人知晓信息的传递事件或者信息的内容。LSB 隐写术是一种图像隐写术技术，其中通过将每个像素的**最低有效位**替换为要隐藏的消息位来将消息隐藏在图像中。

### 实现原理

我们将`png`图片看成是一个二维矩阵，矩阵的每个元素表示图片的一个像素点，包含RGB三个值。如果如果修改这些二进制值的最后一位，图片发生的变化是肉眼不能辨别的，这样就达到了隐藏信息的目的， 如下图

<img title="" src="./img/explain.png" alt="explain.png" width="446">

#### 加密

为实现将一串文本隐藏到图片中，我们可以先逐个获得文本串的字符的`ASCII`码，形成二进制序列，再迭代图片像素值，将像素值的最低位逐个替换为序列中的消息位。流程如下图：

<img title="" src="./img/encode.png" alt="encode.png" width="324">

#### 解密

为提取图片中隐藏的信息，我们只需反转该过程，提取每个像素的最低位，每8位分成一组，分别转化成对应的字符，最后连成字符串即可。流程如下图：

<img title="" src="./img/decode.png" alt="decode.png" width="178">

## 项目目标

实现LSB隐写，包括将文本信息隐藏到图片中，提取图片中隐藏的文本信息。

## 环境依赖

本项目采用python3.9.12编写并且需要pillow第三方库以及它的依赖环境。

```shell
pip install -r requirements.txt
```

## 项目结构

```shell
.
├── README.md
├── dist
│   ├── lsb-steg-1.0.0.linux-x86_64.tar.gz
│   ├── lsb-steg-1.0.0.tar.gz
│   ├── lsb-steg-1.0.0.win-amd64.zip
│   ├── lsb_steg-1.0.0-py3-none-any.whl
│   └── lsb_steg-1.0.0-py3.9.egg
├── img
│   ├── decode.png
│   ├── encode.png
│   ├── explain.png
│   ├── imgprocess.png
│   ├── lsb.png
│   ├── process.png
│   └── result.png
├── lsb
│   ├── __init__.py
│   ├── endetext.py
│   └── imgprocess.py
├── main.py
├── setup.py
└── test
    ├── decode_image.png
    ├── decode_text.txt
    ├── encode_image.png
    └── encode_text.txt

4 directories, 22 files
```

```shell
加密程序 位于endetext.py文件 第26行
解密程序 位于endetext.py文件 第69行
```

### 源代码结构

- **imgprogress.py**，结构如下图
  
  - `ImageProcess`: 根据接收的文件名打开图片，返回`<class 'PIL.PngImagePlugin.PngImageFile'>`
  
  - `ModeError`: 本项目只作用于`RGB`即`png-24`的图片
  
  <img title="" src="./img/imgprocess.png" alt="imgprocess.png" width="269">

- **lsb.py**，结构如下图
  
  - LSB: 接收原始图片和隐藏信息所在文本文件的文件名，用于加密；接收藏有信息的图片的文件名，用于解密
    
    - LSB.lsb_encode:实现LSB加密，另存隐藏有信息的图片
    
    - LSB.lsb_decode:实现LSB解密，将获取的信息存入文本文件
  
  - AreaLess: 确保图片大小足够隐藏待隐藏的信息
  
  <img title="" src="./img/lsb.png" alt="lsb.png" width="385">

- **main.py**
  
  - 加密：
    
    - 用户输入原始图片和存储信息的文本文件的文件名
    
    - 生成隐藏信息的图片
  
  - 解密
    
    - 用户输入藏有信息的图片的文件名和存储获得信息的位置
    
    - 将获取的信息存储到用户指定的文本文件中

## 项目功能

用户运行`main.py`，根据提示指定要实现的功能，包括加密和解密。交互界面和运行结果如下图。

- 加密：用户根据提示输入原始图片文件名和隐藏信息的存储位置（若用户无输入，则默认调用`./test`中相应的的测试文件）

- 解密：用户根据提示输入藏有信心的图片的文件名和获取信息的存储位置（若用户无输入，则默认调用`./test`中相应的的测试文件）

<img title="" src="./img/process.png" alt="process.png" width="559">

<img src="./img/result.png" title="" alt="" width="557">

## 安装与使用

### 安装教程

- 源码压缩包`lsb-steg-1.0.0.tar.gz`
  
  1. 解压
  
  2. 进入层级目录
  
  3. 安装：`python setup.py install `；卸载`pip uninstall lsb-steg`

- 二进制压缩包`lsb-steg-1.0.0.linux-x86_64.tar.gz`和`lsb-steg-1.0.0.win-amd64.zip`
  
  1. 解压
  
  2. 复制到`site-packages`目录下

- `.egg`和`whl`
  
  - easy_install lsb_steg-1.0.0-py3.9.egg
  
  - easy_install lsb_steg-1.0.0-py3-none-any.whl

### 使用示例

```python
from lsb import *


def main():
    while True:
        choice = input("加密信息请按1，解密信息请按2, 退出程序请按3: ")
        if choice == "1":
            encode_image = input("请输入原始图片文件名: ")
            encode_text = input("请输入待隐藏信息的存储位置: ")
            encode_obj = endetext.LSB(encode_image, encode_text)
            encode_obj.lsbEncode()
        elif choice == "2":
            decode_image = input("请输入藏有信息的图片的文件名: ") 
            decode_text = input("请输入信息的存储位置: ") 
            decode_obj = endetext.LSB(decode_image)
            decode_obj.lsbDecode(decode_text)
        elif choice == "3":
            exit()
        else:
            print("不许调皮！")


if __name__ == "__main__":
        main()
```