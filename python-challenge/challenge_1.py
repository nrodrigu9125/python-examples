import re
import string

def add(c, x):
  return chr(ord(c)+x)

firstArray = ["k","l","m"]
secondArray = ["o","p","q"]
thirdArray = ["e","f","g"]
joinedlist = firstArray + secondArray + thirdArray

foundList = []
otherList = []
whatlist = []

targetString = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

targetString.join(ch for ch in string.printable if ch.isalnum() or ch is " ")

for x in targetString:
  if x.isspace() or x in joinedlist:
    foundList.append(x)
    #print("found: " + x)
  else:
    otherList.append(x)
    #print("did not find: " + x)

# targetString = re.sub(r'\W+', '', targetString)

for x in targetString:
  if x.isspace():
    whatlist.append(x)
  elif x is "y":
    whatlist.append("a")
  else:
    whatlist.append(add(x,2))



formattedList = ""
formattedList = formattedList.join(foundList)
print(formattedList)
formattedList = ""
formattedList = formattedList.join(otherList)
print(formattedList)
formattedList = ""
formattedList = formattedList.join(whatlist)
print(formattedList)

