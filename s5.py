import os
#Remove tmp folder content
#os.system("rm tmp/*")
#erode the image
os.system("convert ofdbmf.jpg -negate -morphology erode octagon:2 -negate tmp/ofdbmf-1.jpg")
#convert it to black and white
os.system("convert tmp/ofdbmf-1.jpg -threshold 70% tmp/ofdbmf-2.jpg")
#Decoding
os.system("tesseract -psm 8 tmp/ofdbmf-2.jpg -")
