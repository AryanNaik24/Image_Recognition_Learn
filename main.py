from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time 


def threshold(imageArray):
    balanceArray = []
    newArr = imageArray

    for eachRow in imageArray:
        for eachPixel in eachRow:
            print (eachPixel)
            time.sleep(2)



img=Image.open('imagestest/numbers/0.1.png')
imgArr=np.asarray(img)


img2=Image.open('imagestest/dotndot.png')
imgArr2=np.asarray(img2)


img3=Image.open('imagestest/numbers/y0.5.png')
imgArr3=np.asarray(img3)


img4=Image.open('imagestest/numbers/y0.4.png')
imgArr4=np.asarray(img4)


fig = plt.figure()
ax1 = plt.subplot2grid((8,6),(0,0),rowspan=4,colspan=3)
ax2 = plt.subplot2grid((8,6),(4,0),rowspan=4,colspan=3)
ax3 = plt.subplot2grid((8,6),(0,3),rowspan=4,colspan=3)
ax4 = plt.subplot2grid((8,6),(4,3),rowspan=4,colspan=3)


ax1.imshow(imgArr)
ax2.imshow(imgArr2)
ax3.imshow(imgArr3)
ax4.imshow(imgArr4)

plt.show()

