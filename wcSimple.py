"""
word-count.py

author: Dee Corcoran

date: 08/13/2017

A program that takes in multiple txt files
and returns the top 10 highest-occurring words
found in said files and the number of times
that each occurred.
"""


import re           #regex
import operator     #sort a dictionary
import os           #check validity of file



def addFile(text, dict):
    """Tokenizes a blob of text into individual words, which
    are delimited by any characters other than letters or
    numbers."""
    
    text = text.lower()         #undo any capitalization
    wordArray = re.split("[^a-z0-9']+", text)   
    for word in wordArray:
        if word == '':
            break
        if word not in dict:
            dict[word] = 1      #add new word
        else:
            dict[word] += 1     #increase count of an existing word
    return dict



def wc(args):
    """Prompts user for multiple txt file names until they
    enter the word stop, at which point the program calls
    report() and ends."""
    
    dict = {}
    for fileName in args:
        if fileName[-4::] != ".txt":        #add '.txt' extension if it was forgotten
            fileName += ".txt"
        if not os.path.exists(fileName):    #check that file name exists
            print("Cannot find file \'" + fileName + "\'")
        else:                               #read file
            myFile = open(fileName, 'r')
            text = myFile.read().replace('\n', ' ')
            dict = addFile(text, dict)
    sortedDict = sorted(dict.items(),key=operator.itemgetter(1),reverse=True)
    upper = min(10, len(sortedDict))
    return sortedDict[0:upper]
