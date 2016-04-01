


#!/usr/local/bin/python3.5

from sys import argv
from bs4 import BeautifulSoup #HTML Parser
import pdb

TOPIC = "Äquivalenzrelationen"


#Functions------------------------- 

def replaceMathTag(mathTag):
    content = mathTag.get("tex")
    newTag = '$' + content + '$'
    
    mathTag.insert_after(newTag)
    mathTag.unwrap() #Delete old tag



#Main------------------------------
if __name__ == "__main__":

    #pdb.set_trace()

    inputHtmlFileName = argv[1]
    inputHtmlFile = open(inputHtmlFileName)  
    inputHtml = inputHtmlFile.read()

    soup = BeautifulSoup(inputHtml , 'html.parser')
    mathTags = soup.find_all('math')
    
    for tag in mathTags:
        replaceMathTag(tag)

    
    open(TOPIC + '.tex', 'w').close() #clean file: empty
    testFile = open(TOPIC + '.tex', 'a')
    testFile.write(soup.prettify())

    

