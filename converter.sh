##!/usr/bin/env bash
set -e
if [ $# -eq 0 ]
then
    echo "Please supply the name of the Directory"
    exit 1
fi

DIR="$1" #Directory
for i in "$DIR"*/
do
    echo "Converting Files in $i"
    python ngm2jpg.py "$i"

    WIDTH="$(identify "$i"NGM*.jpg | cut -d " " -f3 | cut -d "x" -f 1 | datamash mode 1)" #Find the most common Width
    HEIGHT="$(identify "$i"NGM*.jpg | cut -d " " -f3 | cut -d "x" -f 2 | datamash mode 1)" #Find the most common Height
    convert "$i""NGM*.jpg" -set filename:base "%[basename]" -resize "$WIDTH"x"$HEIGHT"\! "$i""%[filename:base].jpg" #Convert all files to be of the same size
    convert "$i""NGM*.jpg" -set filename:base "%[basename]"  "$i""%[filename:base].pdf" #Convert into pdf
    fd --type=f --extension=cng --extension=jpg NGM "$i" --exec-batch rm {} #Delete .cng and .jpg to conserve space

done

echo "All Done"

