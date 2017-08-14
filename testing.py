"""
testing.py

author: Dee Corcoran

date: 08/13/2017

A program that tests the accuracy of word-count.py
and prints a bool indicating if the program has
passed each successive test phase.
"""

import wcSimple
import time



"""
This program uses a file called wcSimple which is a stripped-
down version of word-count in which its input is an array of
txt files and it returns an array of tuples denoting the top
10 most common words and their number of occurrences.
"""


def basic(result):
    """Simply checks to make sure the program can run without
    crashing and will be able to report word counts even if
    it isn't given a minimum of ten unique words."""
    expected = [('a',8)]
    if expected == result:
        print("TEST PASSED")
    else:
        print("TEST FAILED")
        print("file: a.txt")
        print("\nresult:", result)
        print("\nexpected:", expected)



def delimiters(result):
    """Tests a large variety of non-alphanumeric characters to check that
    these characters are stripped when the file gets tokenized."""
    expected = [('are',2),('words',1),('separated',1),('by',1),('different',1),
                ('characters',1),('treated',1),('separately',1),('or',1),('they',1)]
    if expected == result:
        print("TEST PASSED")
    else:
        print("TEST FAILED")
        print("file: delimiters.txt")
        print("\nresult:", result)
        print("\nexpected:", expected,"\n\n")



def numbers(result):
    """Ensures that the program considers numbers to be words."""
    expected = [('9',5),('5',5),('4',4),('3',3),('2',2),('program',1),('should',1),
                ('also',1),('count',1),('numbers',1)]
    if expected == result:
        print("TEST PASSED")
    else:
        print("TEST FAILED")
        print("file: numbers.txt")
        print("\nresult:", result)
        print("\nexpected:", expected, "\n\n")    



def counts(result):
    """A simple file to easily check the word counts from the result."""
    expected = [('a',16),('e',15),('i',14),('j',12),('d',11),('b',9),('c',7),('g',6),
                ('h',3),('16',1)]
    if expected == result:
        print("TEST PASSED")
    else:
        print("TEST FAILED")
        print("file: counts.txt")
        print("\nresult:", result)
        print("\nexpected:", expected, "\n\n")   



def blank(result):
    """Checks how the program deals with a blank file. This test
    initially failed with result [('',1)], so I wrote a condition
    into word-count.py to not alter the dictionary if a file is empty."""
    expected = []
    if expected == result:
        print("TEST PASSED")
    else:
        print("TEST FAILED")
        print("file: empty.txt")
        print("\nresult:", result)
        print("\nexpected:", expected, "\n\n")    


    
    
def addition(result):
    """Checks that word counts don't reset in between files. (e.g. if
    a word has a count of 5, and the file is entered 3 times, it will
    be expected to have a total word count of 15."""
    expected = [('a',48),('e',45),('i',42),('j',36),('d',33),('b',27),('c',21),('g',18),
                ('h',9),('16',3)]
    if expected == result:
        print("TEST PASSED")
    else:
        print("TEST FAILED")
        print("file: counts.txt (x3)")
        print("\nresult:", result)
        print("\nexpected:", expected, "\n\n")



def janeAusten(result):
    """The most common words found in pride and prejudice and their frequencies
    are listed online via datagenetics.com. We are checking the program against
    this existing data.
    However, I found that there are many listings of the word counts
    from pride and prejudice and that no two word tallies are the same. I ultimately
    called this test result 'close enough for me!' and moved on.
    This has been commented out below, but the two results can be compared by running
    this program after uncommenting lines 162 and 163."""
    expected = [('the',4312),('to',4149),('of',3595),('and',3534),('her',2214),('i',2044),('a',1946),
                ('in',1875),('was',1843),('she',1701)]
    if expected == result:
        print("TEST PASSED")
    else:
        print("TEST FAILED")
        print("file: pride_and_prejudice.txt")
        print("\nresult:", result)
        print("\nexpected:", expected, "\n\n")


    
def efficacy(books):
    """Uses several large text files (books from the Gutenberg Project) to determine
    how long the program takes the analyze larger volumes."""
    tic = time.time()
    wcSimple.wc(books)
    toc = time.time()
    print("Processed " + str(len(books)) + " books in " + str(toc-tic) + " seconds.\n")



def main():
    print("Beginning tests...\n")
    basic(wcSimple.wc(["a"]))
    print("...")
    delimiters(wcSimple.wc(["delimiters"]))
    print("...")
    numbers(wcSimple.wc(["numbers"]))
    print("...")
    counts(wcSimple.wc(["counts"]))
    print("...")
    addition(wcSimple.wc(["counts","counts.txt","counts"]))
    #this also tests the program to ensure it can read both plain and .txt file names
    print("...")
    blank(wcSimple.wc(["empty"]))
    print("...")
    #janeAusten(wcSimple.wc(["pride_and_prejudice"]))
    #print("...")
    books = ["pride_and_prejudice", "dracula", "a_tale_of_two_cities",
              "the_adventures_of_sherlock_holmes"]
    #to test word-count with additional text files, simply add their file names to this array
    efficacy(books)
    print("\nTesting complete.\n")



main()
