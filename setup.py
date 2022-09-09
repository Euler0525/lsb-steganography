from setuptools import setup


def readmeFile():
    with open("README.rst", encoding="utf-8") as f:
        return f.read()


setup(name="lsb-steg",
      version="1.0.0",
      description="LSB Steganography for text",
      long_description=readmeFile(),
      packages=["lsb"], py_modules=["main"],
      license="MIT",
      author="Euler0525",
      author_email="13804800525@139.com")
