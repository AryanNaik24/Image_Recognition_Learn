from functools import reduce
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def threshold(imageArray):
    newArr = imageArray.astype(np.uint8).copy()

    balanceArray = []

    # Calculate the balance to discriminate between black and white
    for eachRow in imageArray:
        for eachPixel in eachRow:
            avgNumber = reduce(lambda x, y: int(x) + int(y), eachPixel[:3]) / len(eachPixel[:3])
            balanceArray.append(avgNumber)

    balance = sum(balanceArray) / len(balanceArray)

    # Modify array
    for eachRow in newArr:
        for eachPixel in eachRow:
            if reduce(lambda x, y: int(x) + int(y), eachPixel[:3]) / len(eachPixel[:3]) > balance:
                eachPixel[0] = 255  # Red
                eachPixel[1] = 255  # Green
                eachPixel[2] = 255  # Blue
                eachPixel[3] = 255  # Alpha
            else:
                eachPixel[0] = 0 
                eachPixel[1] = 0    
                eachPixel[2] = 0    
                eachPixel[3] = 255  
    return newArr


# Open images and convert to NumPy arrays
img = Image.open("imagestest/numbers/0.1.png").convert("RGBA")
imgArr = np.asarray(img).copy()

img2 = Image.open("imagestest/dotndot.png").convert("RGBA")
imgArr2 = np.asarray(img2).copy()

img3 = Image.open("imagestest/numbers/y0.5.png").convert("RGBA")
imgArr3 = np.asarray(img3).copy()

img4 = Image.open("imagestest/numbers/y0.4.png").convert("RGBA")
imgArr4 = np.asarray(img4).copy()


imgArr = threshold(imgArr)
imgArr2 = threshold(imgArr2)
imgArr3 = threshold(imgArr3)
imgArr4 = threshold(imgArr4)


fig = plt.figure()
ax1 = plt.subplot2grid((8, 6), (0, 0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8, 6), (4, 0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8, 6), (0, 3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8, 6), (4, 3), rowspan=4, colspan=3)

ax1.imshow(imgArr)
ax2.imshow(imgArr2)
ax3.imshow(imgArr3)
ax4.imshow(imgArr4)

plt.show()
