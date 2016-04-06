


#!/usr/local/bin/python3.5

from sys import argv
from bs4 import BeautifulSoup #HTML Parser
import pdb
import shutil
import urllib.request
import requests
import os

TOPIC = "Äquivalenzrelationen"



#Functions------------------------- 
def replaceTag(tag, newTag):
    tag.insert_after(newTag)
    tag.unwrap() #Delete old tag

def replaceMathTag(mathTag):
    content = mathTag.get("tex")
    newTag = '$' + content + '$'
    
    replaceTag(mathTag, newTag)

#example fileUrl:
#https://de.wikibooks.org/wiki/Datei:Drehung_um_90_Grad_und_um_450_Grad.svg
def downloadPictureFromWikifile(fileUrl, fileName):
    picRequest = requests.get(fileUrl)
    
    soup = BeautifulSoup(picRequest.text , 'html.parser')
    linkTagToOriginal = soup.find_all("a", string="Originaldatei")[0]
    picUrl = linkTagToOriginal.get("href")
    picUrl = "https:" + picUrl 

    urllib.request.urlretrieve(picUrl, fileName)

#Need inkscape installed!
def convertImgSvgToPdf(imgPath, outName):
    os.system("inkscape -f " + imgPath + "-A" + outName)

def replaceFigure(figureTag):
    #exchange svgs to pdfs!
    figureHref = figureTag.get("href")
    figureHeightFile = figureTag.get("data-file-height") 
    figureHeightFile = figureTag.get("data-file-width") 
    figureHeight = figureTag.get("height") 
    figureHeight = figureTag.get("width") 
    
    fileName =  figureHref[8:]
    filePage = "https://de.wikibooks.org/wiki/Datei:" + fileName
    downloadPictureFromWikifile(filePage, fileName) 
    convertImgSvgToPdf(fileName, "test1")

    #replaceTag(mathTag, newTag)

#Main------------------------------
if __name__ == "__main__":

     pdb.set_trace()
#
    #inputHtmlFileName = argv[1]
    #inputHtmlFile = open(inputHtmlFileName)  
    #inputHtml = inputHtmlFile.read()
#
    #soup = BeautifulSoup(inputHtml , 'html.parser')
    #mathTags = soup.find_all('math')
    #
    #for tag in mathTags:
        #replaceMathTag(tag)
#
    #
    #open(TOPIC + '.tex', 'w').close() #clean file: empty
    #testFile = open(TOPIC + '.tex', 'a')
    #testFile.write(soup.prettify())
#

