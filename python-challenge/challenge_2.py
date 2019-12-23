from collections import Counter

with open("C:/Users/nrodr/source/repos/python/challenge2.txt") as file:
    data = file.read().replace('\n','')
    res = Counter(data)
    print(res)

# import urllib.request
# import PIL.Image
# import PIL.ExifTags


# img = PIL.Image.open("C:\\Users\\nrodr\\source\\repos\\python\\ocr.jpg")

# exif = {
#     PIL.ExifTags.TAGS[k]: v
#     for k, v in img._getexif().items()
#     if k in PIL.ExifTags.TAGS
# }

# print(exif)
# fp = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
# mybytes = fp.read()

# mystr = mybytes.decode("utf8")
# fp.close()

# print(mystr)

