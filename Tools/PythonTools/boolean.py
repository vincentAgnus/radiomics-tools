#!/usr/bin/env python

import SimpleITK as sitk
import sys


def image_and(input_image1, input_image2):
    return sitk.And(input_image1, input_image2)


def image_or(input_image1, input_image2):
    return sitk.Or(input_image1, input_image2)


def image_xor(input_image1, input_image2):
    return sitk.Xor(input_image1, input_image2)


def image_not(input_image):
    return sitk.Not(input_image)


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print(sys.argv[0] + " [and|or|xor] input1 input2 output \n" +
              sys.argv[0] + " not input output")
    else:
        operator = sys.argv[1]
        inputFilename1 = sys.argv[2]
        inputFilename2 = sys.argv[3]
        outputFilename = sys.argv[4]

        inputImage1 = sitk.ReadImage(inputFilename1, sitk.sitkUInt16)
        if operator != "not":
            inputImage2 = sitk.ReadImage(inputFilename2, sitk.sitkUInt16)
        else:
            outputFilename = inputFilename2

        if operator == "and":
            outputImage = image_and(inputImage1, inputImage2)
        elif operator == "or":
            outputImage = image_or(inputImage1, inputImage2)
        elif operator == "xor":
            outputImage = image_xor(inputImage1, inputImage2)
        elif operator == "not":
            outputImage = image_not(inputImage1)
        else:
            print("Not supporting operator " + sys.argv[1])
            exit(-1)

        sitk.WriteImage(outputImage, outputFilename)

