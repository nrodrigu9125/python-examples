# http://www.pythonchallenge.com/pc/def/peak.html
import urllib.request

# class Node:
#     def __init__(self, data):
#         self.item = data
#         self.ref = None

# class LinkedList:
#     def __init__(self):
#         self.start_node = None


class NothingPageData:
    def __init__(self, nothingVal, pageAsString):
        self.nothingVal = nothingVal
        self.pageAsString = pageAsString


def printNothings(nothingData):
    for nothing in nothingData:
        print(f'{nothing.pageAsString}; go to {nothing.nothingVal}')


firstNothing = NothingPageData(12345, 'and the next nothing is 44827')
nothingList = [firstNothing]

for x in range(400):
    queryParam = nothingList[x].nothingVal
    url = f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={queryParam}'
    with urllib.request.urlopen(url) as f:
        resp = f.read(300).decode('utf-8')
        nextNothing = ''.join(filter(str.isdigit, resp))
        nothingList.append(NothingPageData(nextNothing, resp))


printNothings(nothingList)