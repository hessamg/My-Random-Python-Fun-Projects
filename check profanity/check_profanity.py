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
import urllib.request
import os 

def read_text():
    cwd = os.path.dirname(os.path.realpath(__file__))
    file_to_read = cwd + "\\movie_quotes.txt"
    quotes = open(file_to_read, "r")
    #quotes = open("movie_quotes.txt")
    contents_of_file = quotes.read()
    # print(contents_of_file)    
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    url ="http://www.wdylike.appspot.com/?q=" + text_to_check.replace(" ","%")
    # or use with urllib.request.urlopen(url) as connection
    connection = urllib.request.urlopen(url)
   
    print(connection.read(100).decode('utf-8'))
    output = connection.read("100")
    #print(output)
    if output:
        print("Profanity Alert!!!")
    elif not output:
        print("This document has no curse word")
    else:
        print("Could not scan the documnet properly")
    connection.close()

read_text()


