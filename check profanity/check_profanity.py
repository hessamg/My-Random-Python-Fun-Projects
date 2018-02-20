"""
This part is just to check what ord() does
def test():
    print ord("p")
    print ord("P")
    print ord(">")
    print ord("$")
    print ord("4")
    
test()
"""
import urllib

def read_text():
    quotes = open(r"E:\recovery\udacity\python\chapter 5\movie_quotes.txt")
    #quotes = open("C:\Users\hessa\Desktop\movie_quotes.txt")
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    #print(output)
    if "true" in output:
        print("Profanity Alert!!!")
    elif "false" in output:
        print("This document has no curse word")
    else:
        print("Could not scan the documnet properly")
    connection.close()

read_text()


