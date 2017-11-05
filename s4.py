import os
#clear tmp folder
#os.system("rm tmp/*")
#blur the image to reduce the noise
os.system("convert wdgvze.png -gaussian-blur 0 tmp/wdgvze-1.png")
#convert it to black and white
os.system("convert tmp/wdgvze-1.png -threshold 25% tmp/wdgvze-2.png")
#replace each pixel by the most frequent colors around it with -paint 1
os.system("convert wdgvze.png -gaussian-blur 0 -threshold 25% -paint 1 tmp/wdgvze-3.png")
#Decoding
os.system("tesseract tmp/wdgvze-3.png -")
