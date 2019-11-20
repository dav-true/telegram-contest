import time
import re
import langdetect
from glob import glob
import io

from multiprocessing import Pool

getTime = time.time()
mainList = glob('D:/DataClusteringSample0107/20191101/04/*.html')
print(len(mainList))
i = 0


class CheckList:
    for i in range(len(mainList)):
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

            print(langdetect.detect(str(newList)))

        except langdetect.lang_detect_exception.LangDetectException:
            print('other')
            continue


print('----- %s' % (time.time() - getTime))