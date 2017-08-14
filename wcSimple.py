"""
word-count.py

author: Dee Corcoran

date: 08/13/2017

A program that takes as argument an array of multiple
txt files and returns a list of tuples containing
the words most commonly used in the txt files and
their individual counts.
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
        if word == '':          #check if file is empty
            break
        if word not in dict:
            dict[word] = 1      #add new word
        else:
            dict[word] += 1     #increase count of an existing word
    return dict



def wc(args):
    """Processes any text files listed in args and returns
    their word count list."""
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
    #sort the dictionary by word count in descending order
    sortedDict = sorted(dict.items(),key=operator.itemgetter(1),reverse=True)
    upper = min(10, len(sortedDict))        #in case the dictionary has less than 10 entries
    return sortedDict[0:upper]
