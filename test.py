import time
import re
import langdetect
from glob import glob
import io
import multiprocessing
from natsort import natsorted, ns
from html2text import HTML2Text

getTime = time.time()
mainList = glob('D:/DataClusteringSample0107/20191105/13/*.html')
mainList = natsorted(mainList, alg=ns.IGNORECASE)

fileFolder = io.open(mainList[0], 'r', encoding='utf-8')
getHtml = fileFolder.read()

checkP = re.findall('<p>(.*)</p>', getHtml)
checkH = re.findall('<h\d>(.*)</h\d>' , getHtml)
checkTittle = re.findall('property="og:title" content="(.*)"', getHtml)
checkDescription = re.findall('property="og:description" content="(.*)"', getHtml)

def sumStrings(x,y,z,i):
    sum = str(x + y + z + i)
    return sum

# sumStrings(checkP,checkH,checkTittle,checkDescription)

# print(sumStrings(checkH, checkP, checkTittle, checkDescription))


print('----- %s' % (time.time() - getTime))

def checklist0():
    for i in range(len(mainList)):
        if i % 4 == 0:
            try:
                try:
                    fileFolder = io.open(mainList[i], 'r', encoding='utf-8')
                    getHtml = fileFolder.read()
                    print(fileFolder.name)

                    loseN = re.sub(r'\n', ' ', getHtml)
                    result = re.search('<body>(.*)</body>', loseN)
                    nextRes = re.sub(r'<h1>', '', result.group(1))
                    nextRes1 = re.sub(r'<p>', '', nextRes)

                    newList = nextRes1.split()
                    transList = []

                    x = 0
                    for x in range(len(newList)):
                        if x % 7 == 1:
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
                    # print(fileFolder.name)

                    loseN = re.sub(r'\n', ' ', getHtml)
                    result = re.search('<body>(.*)</body>', loseN)
                    nextRes = re.sub(r'<h1>', '', result.group(1))
                    nextRes1 = re.sub(r'<p>', '', nextRes)

                    newList = nextRes1.split()
                    transList = []

                    x = 0
                    for x in range(len(newList)-1):
                        if x % 7 == 1:
                            transList.append(newList[x])

                    res = langdetect.detect(str(newList))
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
                    # print(fileFolder.name)

                    loseN = re.sub(r'\n', ' ', getHtml)
                    result = re.search('<body>(.*)</body>', loseN)
                    nextRes = re.sub(r'<h1>', '', result.group(1))
                    nextRes1 = re.sub(r'<p>', '', nextRes)

                    newList = nextRes1.split()
                    transList = []

                    x = 0
                    for x in range(len(newList)):
                        if x % 7 == 1:
                            transList.append(newList[x])

                    res = langdetect.detect(str(newList))
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
                    # print(fileFolder.name)

                    loseN = re.sub(r'\n', ' ', getHtml)
                    result = re.search('<body>(.*)</body>', loseN)
                    nextRes = re.sub(r'<h1>', '', result.group(1))
                    nextRes1 = re.sub(r'<p>', '', nextRes)

                    newList = nextRes1.split()
                    transList = []

                    x = 0
                    for x in range(len(newList)-1):
                        if x % 7 == 1:
                            transList.append(newList[x])

                    res = langdetect.detect(str(newList))

                except IndexError:
                    break
            except langdetect.lang_detect_exception.LangDetectException:
                # print('other')
                continue


if __name__ == '__main__':

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
