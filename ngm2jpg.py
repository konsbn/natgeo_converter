"""
Converter for NGM files to JPG
This program converts the NGM files found in the
Complete National Geographic Magazine DVD into JPG files

Installation:
$ pip install -r requirements.txt

Usage:
$ python convert <path_to_directory>

"""
import os
from io import BytesIO
from PIL import Image


def convert(src: str, dst: str = None) -> None:
    """
    Converts the .NGM file to .JPG by XORing with 239 and writes it to disk
    """
    if dst is None:
        # Given no path for output simply make a new file with
        # same name and jpg extension in the src directory
        dst = os.path.splitext(src)[0] + ".jpg"
    with open(src, "rb") as f:  # Read the file into bytearray
        ngm = bytearray(f.read())
    new_ngm = bytearray([i ^ 239 for i in ngm])  # Byte wise XOR with 239
    image = Image.open(BytesIO(new_ngm))
    image.save(dst)


if __name__ == "__main__":
    import sys
    import glob

    try:
        cng_list = glob.glob(sys.argv[1] + "*.cng")
        if not cng_list:
            raise FileNotFoundError("No CNG File Exists")
    except IndexError:
        print("Incomplete List Of Arguments, Please supply the Directory")
        sys.exit(1)

    for cng in cng_list:
        try:
            convert(cng)
        except KeyboardInterrupt:
            sys.exit(1)
