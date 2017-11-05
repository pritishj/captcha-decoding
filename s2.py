import os
#Removing temp files for new case
#os.system("rm tmp/*")
#Converting image to gray
os.system("convert 300026.png -colorspace gray tmp/300026-1.png")
#convert it to black and white
os.system("convert tmp/300026-1.png -threshold 50% tmp/300026-2.png")
#Decoding
os.system("tesseract tmp/300026-2.png -")
