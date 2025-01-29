from functools import reduce
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from matplotlib.ticker import MaxNLocator



#Note from Aryan : If you want to create more examples then use a 8x8 pixel squal in paint to test





def createExamples():
    numberArrayExamples = open('numArEx.txt','a')
    numbersWeHave = range(0,10)
    versionsWeHave = range(1,10)


    for eachNum in numbersWeHave:
        for eachVer in versionsWeHave:
            imgFilePath = 'imagestest/numbers/'+str(eachNum)+'.'+str(eachVer)+'.png'
            ei= Image.open(imgFilePath)
            exImgArr = np.asarray(ei).copy()
            eiar1 = str(exImgArr.tolist())

            lineToWrite = str(eachNum)+'::'+eiar1+'\n'
            numberArrayExamples.write(lineToWrite)


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

#funtion to match the number
def findNum(filePath):
    matchedAr = []
    loadExmpl = open('numArEx.txt','r').read()
    loadExmpl = loadExmpl.split('\n')

    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()

    inQuestion = str(iarl)

    for exmpl in loadExmpl:
        if len(exmpl)>3:
            splitEx = exmpl.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]

            eachPixEx = currentAr.split('],')

            eachPixInQ = inQuestion.split('],')

            x=0

            while x<len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))

                x+=1


    x= Counter(matchedAr)
    print (x)

    #attempt to display the number
    graphX=[]
    graphY=[]

    for eachValue in x:
        print (eachValue)
        graphX.append(eachValue)
        print (x[eachValue])
        graphY.append(x[eachValue])

    gig = plt.figure()
    ax1 = plt.subplot2grid((4,4),(0,0),rowspan=1,colspan=4)
    ax2 = plt.subplot2grid((4,4),(1,0),rowspan=3,colspan=4)

    ax1.imshow(iar)

    ax2.bar(graphX,graphY,align='center')

    plt.ylim(400)

    xloc = MaxNLocator(12)
    ax2.xaxis.set_major_locator(xloc)

    plt.show()





findNum('imagestest/test.png')




