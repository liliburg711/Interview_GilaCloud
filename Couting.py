from collections import Counter

urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
]

fileDict = {}
for url in urls:
    changeStr = str(url)
    filename = changeStr.split("/")[-1]
    if filename not in fileDict.keys():
        fileDict.setdefault(filename, 1)
    else:
        fileDict[filename] += 1

print(dict(Counter(fileDict).most_common(3)))
