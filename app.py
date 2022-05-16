# import openCV library for image handling
import cv2
import os

# Get Files in current directory
file_list = [f for f in os.listdir('.') if os.path.isfile(f)]

# Enter what you want to rename your images
rename = input("Rename: ")


def resize_images(file_list, rename):
    number = 0
    for i in file_list:

        # Variables for Renaming
        name = i
        number += 1
        suffix = i[-4:]

        try:
            # Read Image
            img = cv2.imread(i)

            # Resize All images to width of 1500 and relative height
            width = int(1500)
            height = int((img.shape[0]) * (1500/img.shape[1]))

            # Resize Image
            scaled = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)


            cv2.imwrite(rename + "_" + str(number) + suffix,
                        scaled, [cv2.IMWRITE_PNG_COMPRESSION, 9])

        except AttributeError:
            continue


if __name__ == "__main__":
    resize_images(file_list, rename)
