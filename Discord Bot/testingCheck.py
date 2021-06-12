import cv2
import check

while True:
    a = input()
    if a == "check":
        print(check.startSearch())
        fileName = input("Pick a file name ")
        check.vidOut(fileName)
        break 