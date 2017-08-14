"""
word-count.py

author: Dee Corcoran

date: 08/13/2017

A program that takes in multiple txt files
and returns the top 10 highest-occurring words
found in said files and the number of times
that each occurred.
"""


import re
import operator



def addFile(text, dict):
    """Tokenizes a blob of text into individual words, which
    are delimited by any characters other than letters or
    numbers."""
    
    text = text.lower()
    wordArray = re.split("[^a-z0-9']+", text)
    for word in wordArray:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    return dict



def report(dict):
    sortedDict = sorted(d.items(),key=operator.itemgetter(1))
    n = 0
    while n < 10:
        entry = sortedDict[n]
        print(entry[0] + ":", entry[1])
        n += 1



def main():
    dict = {}
    fileName = ""
    print("Please enter file name(s). Type 'stop' to end program")
    while fileName != "stop":
        fileName = input("File name: ")
        myFile = open(fileName, 'r')
        text = myFile.read().replace('\n', ' ')
        dict = addFile(text, dict)
    report(dict)


