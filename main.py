#!/usr/bin/env python3
import numpy as np
import os,sys
from PIL import Image

def reduceimg(img):
    outfile = os.path.splitext(img)[0] + "_" + ".jpeg"
    try:
        # reduced image dimensions
        size = (8,8)
        img = Image.open(img)
        img = img.resize(size, Image.ANTIALIAS)
        return img
    except IOError:
        raise Exception("Bad File")

# convert to grey scale
def greyscale(img):
    img = img.convert('1')
    return img
# get average greyscale color
def average_colors(img):
    pixelWeight = list(img.getdata())
    listLen = len(pixelWeight)
    totalsum = 0
    counter = 0
    for i in range(listLen):
        totalsum += pixelWeight[i]
        counter += 1
    averageVal = totalsum/counter
    return averageVal

#compares img average to every pixel
#gets img hash value
def compare_bits(img,imgAvg):
    pixelWeight = list(img.getdata())
    listLen = len(pixelWeight)
    assert(listLen==64)
    bitRes = ""
    for i in range(listLen):
        greyscale = rgb2grey(pixelWeight[i])
        if greyscale > imgAvg:
            bitRes += "1"
        else:
            bitRes += "0"
    return bitRes

#greyscale image formula
#convert tuple to greyscaled pixel
def rgb2grey(rgbTuple):
    red = rgbTuple[0]
    green = rgbTuple[1]
    blue = rgbTuple[2]
    greyscale = 0.299*red + 0.587*green + 0.114*blue
    return greyscale

# https://en.wikipedia.org/wiki/Hamming_distance
def hammingDifference(bitNum1, bitNum2):
    result = 0
    for index in range(len(bitNum1)):
        if (bitNum2[index]!=bitNum1[index]):
            result += 1
    return result

# print statements on the images
def isdifferent(dif):
    if dif < 10:
        print("These images, from preliminary results are the same.")
    elif dif < 20:
        print("These images, from preliminary results are the similar.")
    elif dif < 25:
        print("These images, from preliminary results are roughly similar.")
    else:
        print("These images, from preliminary results are different.")

def main():
    #reduces image, greyscales
    #averages and then hashes image
    img1 = sys.argv[1]
    img1 = reduceimg(img1)
    greyImg1 = greyscale(img1)
    imgAvg1 = average_colors(greyImg1)
    bitHash1 = compare_bits(img1,imgAvg1)

    #for image2
    img2 = sys.argv[2]
    img2 = reduceimg(img2)
    greyImg2 = greyscale(img2)
    imgAvg2 = average_colors(greyImg2)
    bitHash2 = compare_bits(img2,imgAvg2)

    #computes difference in hashes
    dif = hammingDifference(bitHash1,bitHash2)

    #print results
    print()
    print("Img1's hash value is",(hex(eval(("0b" + bitHash1)))[2:]))
    print("Img2's hash value is",(hex(eval(("0b" + bitHash2)))[2:]))
    print("The hash difference is",dif)
    isdifferent(dif)
    print()
    return

if __name__ == "__main__":
    main()



