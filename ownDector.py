import time
import re
import langdetect
from glob import glob
import io
import multiprocessing
from natsort import natsorted, ns


mainList = glob('D:/DataClusteringSample0107/20191101/00/*.html')
mainList = natsorted(mainList, alg=ns.IGNORECASE)
fileFolder = io.open(mainList[0], 'r', encoding='utf-8')
getHtml = fileFolder.read()


dictionaryRus = io.open('D:\disk D\DataClusteringCompetition\\russianDictionary.txt', 'r', encoding='cp1251')
getRusDictionary = dictionaryRus.read()
getRusDictionary = re.sub(r'\n', ' ', getRusDictionary)
getRusDictionaryList = getRusDictionary.split()

dictionaryEng = io.open('D:\disk D\DataClusteringCompetition\\englishDictionary.txt', 'r', encoding='utf-8')
getEngDictionary = dictionaryEng.read()
getRusDictionary = re.sub(r'\n', ' ', getRusDictionary)
getEngDictionaryList = getEngDictionary.split()


def sumStrings(x,y,z,i):
    sum = str(x + y + z + i)
    return sum


def detectLang(shortenedListStr, extractedListRus, extractedListEng,shortenedList):
    for i in range(len(getRusDictionaryList)):
        wordsMatch = re.findall(getRusDictionaryList[i], shortenedListStr)
        if getRusDictionaryList[i] in shortenedListStr:
            if 4 > len(getRusDictionaryList[i]) > 1:
                extractedListRus.append(getRusDictionaryList[i])
            elif len(getRusDictionaryList[i]) == 1:
                continue
            else:
                for l in range(len(wordsMatch)):
                    extractedListRus.append(getRusDictionaryList[i])

    for i in range(len(getEngDictionaryList)):
        wordsMatch = re.findall(getEngDictionaryList[i], shortenedListStr)
        if getEngDictionaryList[i] in shortenedListStr:
            if 4 > len(getEngDictionaryList[i]) > 1:
                extractedListEng.append(getEngDictionaryList[i])
            elif len(getEngDictionaryList[i]) == 1:
                continue
            else:
                for l in range(len(wordsMatch)):
                    extractedListEng.append(getEngDictionaryList[i])

    if len(extractedListEng) / len(shortenedList) > 0.3 and not len(extractedListRus) / len(shortenedList) > 0.25:
        return 'en'
    elif len(extractedListRus) / len(shortenedList) > 0.3 and not len(extractedListEng) / len(shortenedList) > 0.25:
        return 'ru'
    elif len(extractedListRus) / len(shortenedList) > 0.3 and len(extractedListEng) / len(shortenedList) > 0.25:
         if len(extractedListRus) / len(shortenedList) > len(extractedListEng) / len(shortenedList):
             return 'ru'
         else:
             return 'en'
    else:
        return 'other'


def mainFunction(i):
    fileFolder = io.open(mainList[i], 'r', encoding='utf-8')
    getHtml = fileFolder.read()
    print(fileFolder.name)

    deleteLink = re.sub(r'href="(.*)"', '', getHtml)
    checkP = re.findall('<p>(.*)</p>', deleteLink)
    checkH = re.findall('<h\d>(.*)</h\d>', deleteLink)
    checkTittle = re.findall('property="og:title" content="(.*)"', deleteLink)
    checkDescription = re.findall('property="og:description" content="(.*)"', deleteLink)

    pageList = sumStrings(checkP, checkH, checkTittle, checkDescription)
    pageList = re.sub(r'&lt;(.*)&gt;', '', pageList)
    pageList = pageList.split()

    shortenedList = []
    extractedListRus = []
    extractedListEng = []

    for x in range(len(pageList)):
        if x % 2 == 1:
            shortenedList.append(pageList[x])

    shortenedListStr = str(shortenedList)
    langflag = detectLang(shortenedListStr, extractedListRus, extractedListEng, shortenedList)
    print(langflag)


def checklist0():
    for i in range(len(mainList)):
        if i % 4 == 0:
            try:
                try:
                   mainFunction(i)
                except IndexError:
                    break

            except langdetect.lang_detect_exception.LangDetectException:
                continue

def checklist1():
    for i in range(len(mainList)):
        if i % 4 == 1:
            try:
                try:
                    mainFunction(i)
                except IndexError:
                    break
            except langdetect.lang_detect_exception.LangDetectException:
                continue

def checklist2():
    for i in range(len(mainList)):
        if i % 4 == 2:
            try:
                try:
                    mainFunction(i)
                except IndexError:
                    break

            except langdetect.lang_detect_exception.LangDetectException:
                continue

def checklist3():
    for i in range(len(mainList)):
        if i % 4 == 3:
            try:
                try:
                    mainFunction(i)
                except IndexError:
                    break
            except langdetect.lang_detect_exception.LangDetectException:
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

