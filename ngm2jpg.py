"""
Converter for NGM files to JPG
"""
import os
from io import BytesIO
from PIL import Image


def convert(src: str, dst: str = "./") -> None:
    """
    Converts the .NGM file to .JPG by XORing with 239 and writes it to disk
    """
    if dst == "./":
        # Given no path for output simply make a new file with
        # same name and jpg extension
        dst = dst + os.path.splitext(os.path.basename(src))[0] + ".jpg"
    with open(src, "rb") as f:  # Read the file into bytearray
        ngm = bytearray(f.read())
    new_ngm = bytearray([i ^ 239 for i in ngm])  # Byte wise XOR with 239
    image = Image.open(BytesIO(new_ngm))  # Write decoded file to JPG
    image.save(dst)


if __name__ == "__main__":
    import sys

    try:
        convert(sys.argv[1], sys.argv[2])
    except IndexError:
        convert(sys.argv[1])
