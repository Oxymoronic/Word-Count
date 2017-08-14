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
        if word not in dict:
            dict[word] = 1      #add new word
        else:
            dict[word] += 1     #increase count of an existing word
    return dict



def report(dict):
    """Prints a list of the top 10 most-occurring words and
    each of their word counts."""

    #sort words by their count, in descending order
    sortedDict = sorted(dict.items(),key=operator.itemgetter(1),reverse=True)
    n = 0
    numWords = min(10, len(sortedDict))     #in case we have a list of less
    print("\n")                             #than 10 words
    while n < numWords:
        entry = sortedDict[n]
        print("\"" + entry[0] + "\":", entry[1])
        n += 1
    print("\n")



def main():
    """Prompts user for multiple txt file names until they
    enter the word stop, at which point the program calls
    report() and ends."""
    
    dict = {}
    fileName = ""
    print("Please enter file name(s). Type 'stop' to end program")
    while True:
        fileName = input("\nFile name: ")
        if fileName.lower() == "stop":      #check if user has typed the stop command
            report(dict)
            break
        if fileName[-4::] != ".txt":        #add '.txt' extension if it was forgotten
            fileName += ".txt"
        if not os.path.exists(fileName):    #check that file name exists
            print("Cannot find file '" + fileName + "'")
        else:                               #read file
            myFile = open(fileName, 'r')
            text = myFile.read().replace('\n', ' ')
            dict = addFile(text, dict)
    return



main()
