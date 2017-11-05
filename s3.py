import os
#clear temp folder
#convert the image to black and white
os.system("convert augu.jpg -threshold 50% tmp/augu-1.jpg")
#remove the borders:
os.system("convert tmp/augu-1.jpg -threshold 50% -fill black -draw 'color 0,0 floodfill' tmp/augu-2.jpg")
#Decoding specifying only uppercase
os.system("tesseract -c tessedit_char_whitelist=ABCDEFGHIJKLMOPQRSTUVWXYZ tmp/augu-2.jpg -")
