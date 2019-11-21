import time
import re
import langdetect
from glob import glob
import io
import multiprocessing
from natsort import natsorted, ns


mainList = glob('D:/DataClusteringSample0107/testFiles/00/*.html')
mainList = natsorted(mainList, alg=ns.IGNORECASE)
fileFolder = io.open(mainList[0], 'r', encoding='utf-8')
getHtml = fileFolder.read()

def sumStrings(x,y,z,i):
    sum = str(x + y + z + i)
    return sum


def checklist0():
    for i in range(len(mainList)):
        if i % 4 == 0:
            try:
                try:
                    fileFolder = io.open(mainList[i], 'r', encoding='utf-8')
                    getHtml = fileFolder.read()
                    print(fileFolder.name)

                    checkP = re.findall('<p>(.*)</p>', getHtml)
                    checkH = re.findall('<h\d>(.*)</h\d>', getHtml)
                    checkTittle = re.findall('property="og:title" content="(.*)"', getHtml)
                    checkDescription = re.findall('property="og:description" content="(.*)"', getHtml)

                    newList = sumStrings(checkP, checkH, checkTittle, checkDescription).split()
                    transList = []

                    for x in range(len(newList)):
                        if x % 3 == 1:
                            transList.append(newList[x])

                    res = langdetect.detect(str(newList))
                    print(res)

                except IndexError:
                    break

            except langdetect.lang_detect_exception.LangDetectException:
                # print('other')
                continue

def checklist1():
    for l in range(len(mainList)):
        if l % 4 == 1:
            try:
                try:
                    fileFolder = io.open(mainList[l], 'r', encoding='utf-8')
                    getHtml = fileFolder.read()
                    print(fileFolder.name)

                    checkP = re.findall('<p>(.*)</p>', getHtml)
                    checkH = re.findall('<h\d>(.*)</h\d>', getHtml)
                    checkTittle = re.findall('property="og:title" content="(.*)"', getHtml)
                    checkDescription = re.findall('property="og:description" content="(.*)"', getHtml)

                    newList = sumStrings(checkP, checkH, checkTittle, checkDescription).split()
                    transList = []

                    for x in range(len(newList)):
                        if x % 3 == 1:
                            transList.append(newList[x])

                    res = langdetect.detect(str(newList))
                    print(res)
                except IndexError:
                    break
            except langdetect.lang_detect_exception.LangDetectException:
                # print('other')
                continue

def checklist2():
    for i in range(len(mainList)):
        if i % 4 == 2:
            try:
                try:
                    fileFolder = io.open(mainList[i], 'r', encoding='utf-8')
                    getHtml = fileFolder.read()
                    print(fileFolder.name)

                    checkP = re.findall('<p>(.*)</p>', getHtml)
                    checkH = re.findall('<h\d>(.*)</h\d>', getHtml)
                    checkTittle = re.findall('property="og:title" content="(.*)"', getHtml)
                    checkDescription = re.findall('property="og:description" content="(.*)"', getHtml)

                    newList = sumStrings(checkP, checkH, checkTittle, checkDescription).split()
                    transList = []

                    for x in range(len(newList)):
                        if x % 3 == 1:
                            transList.append(newList[x])

                    res = langdetect.detect(str(newList))
                    print(res)

                except IndexError:
                    break

            except langdetect.lang_detect_exception.LangDetectException:
                # print('other')
                continue

def checklist3():
    for l in range(len(mainList)):
        if l % 4 == 3:
            try:
                try:
                    fileFolder = io.open(mainList[l], 'r', encoding='utf-8')
                    getHtml = fileFolder.read()
                    print(fileFolder.name)

                    checkP = re.findall('<p>(.*)</p>', getHtml)
                    checkH = re.findall('<h\d>(.*)</h\d>', getHtml)
                    checkTittle = re.findall('property="og:title" content="(.*)"', getHtml)
                    checkDescription = re.findall('property="og:description" content="(.*)"', getHtml)

                    newList = sumStrings(checkP, checkH, checkTittle, checkDescription).split()
                    transList = []

                    for x in range(len(newList)):
                        if x % 3 == 1:
                            transList.append(newList[x])

                    res = langdetect.detect(str(newList))
                    print(res)

                except IndexError:
                    break

            except langdetect.lang_detect_exception.LangDetectException:
                # print('other')
                continue


if __name__ == '__main__':
    getTime = time.time()
    print(len(mainList))
    p1 = multiprocessing.Process(target=checklist0)
    p2 = multiprocessing.Process(target=checklist1)
    p3 = multiprocessing.Process(target=checklist2)
    p4 = multiprocessing.Process(target=checklist3)
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    print('----- %s' % (time.time() - getTime))

