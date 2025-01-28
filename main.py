from PIL import Image
import numpy as np

img=Image.open('imagestest/dot.png')

imgArr=np.asarray(img)

print(imgArr)