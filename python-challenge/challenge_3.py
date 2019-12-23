# http://www.pythonchallenge.com/pc/def/linkedlist.php
from collections import Counter
import re
concatList = []
path = r'C:\Users\nrodr\source\repos\python\challenge3.txt'
with open(path) as file:
    data = file.read()
    # print(data)
    m = re.findall(r"([a-z])([A-Z]{3})([a-z])([A-Z]{3})([a-z])",
                 data)

    lol = re.findall(r"(\w+) (\w+)", "Isaac Newton, physicist")
    if m:
      
      test = m[0:len(m)]
      # a = set([t[0] for t in test])
      # b = set([t[2] for t in test])
      # print(test)
      #res = Counter(data)
      #print(res)
      
      for a in test:
        firstTuple = set(a[0])
        secondTuple = set(a[2])

        leftTupleString = str(a[0])
        rightTupleString = str(a[2])
        concatList.append(a[2])
        # if leftTupleString[0] == rightTupleString[0]:
        #   concatList.append(a[1])
        #   print(f"{leftTupleString[0]} is equal to {rightTupleString[0]} and {leftTupleString[0]} is equal to {rightTupleString[1]}")
        #   print(f"{leftTupleString} - {rightTupleString} - {a[1]}")

      #   if len(firstTuple) == 1:
      #     concatList.append(a[1])
      #     print("T0 = All chars are the same - ", firstTuple, " - ", a[0])
      #   if len(secondTuple) == 1:
      #     concatList.append(a[1])
      #     print("T2 = All chars are the same - ", secondTuple, " - ", a[2]) 
      # # res = Counter(concatList)
      print(concatList)
      # mot
      # newSet = list(m[0:len(m)])
      # newSet = set(range(m[0:len(m)]))
      # print(newSet)
      # print(set(m[0]) - set(m[1]))
        # for g in m:
        #     print(set(g[0]) - set(g[1]))
            # if len(g) == 1:
            #     concatList.append(g)
    # if lol:
    #     print(lol)

# print(' '.join(concatList))
