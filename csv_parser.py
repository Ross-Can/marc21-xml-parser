from asyncore import write
from cgitb import text
import csv
from dataclasses import replace
import re
from turtle import title
from venv import create

class CSV_Parser:

    jobTitles = ["performer","instrumentalist", "composer", "singer", "lyricist","conductor"]
    OUTPUT_FILE_EXT = ".txt"

    def __init__(self, csv_loc = -1, fileName =""):
        if csv_loc == -1:
            return
        self.init_new_csv(csv_loc, fileName)
        
    def init_new_csv(self, csv_loc,fileName):
        self.FILE_PATH = csv_loc
        self.FILE_NAME = fileName

        newFile =  self.FILE_NAME.replace('.csv', self.OUTPUT_FILE_EXT)
        self.newFile = open(newFile, 'w', encoding="utf-8")

        self.items = []

        try:
            self.f =  open(self.FILE_PATH, encoding="utf8")
        except:
            print ("[Error] No such file:", self.FILE_PATH)
            return


    def match(self,txt,regEx):
        return re.search(regEx,txt)

    def removeDate(self):
        txtLength = len(self.author)
        loc_of_comma = self.author.index(',')

        removeText = self.author[loc_of_comma:txtLength]
        removeText = removeText.lstrip(',')

        loc_of_comma = removeText.index(',')
        removeText = removeText[loc_of_comma:len(removeText)]
        self.author = self.author.replace(removeText, "")

    def removeJobTitle(self):
        for job in self.jobTitles:
            self.author = self.author.replace(", " + job, "").strip()
        self.author = self.author.replace(". Choir", "").strip()

    def cleanAuthor(self):
        self.removeDate()
        
       

    
    def cleanData(self):
        if self.match(self.author, "((.|\s)+,){2}(.|\s|\d)+."):
            self.cleanAuthor()
        if self.author.endswith('.'):
            self.author = self.author.rstrip('.')
            self.removeJobTitle()
     
            
    def addEntry(self):

        entry = {
            "line1" : "1 CD(s) & Booklet",
            "line2" : "Circ  " + self.author,
            "line3" : "CD    [" + self.title + "]",
            "line4" : self.cn
        }

        self.items.append(entry)


    def parse(self):
       reader = csv.DictReader(self.f)
       for row in reader:
        try:
            self.title = row[' Title'].replace('/',"").strip()
        except:
            self.title = ""
        
        try:
            self.author = row[' Creator'].replace('/',"").strip()
        except:
            self.author = ""

        try: 
             self.cn = row[' Call Number']
             self.cn = re.sub('\D','',self.cn).strip()
        except:
              self.cn = ""

        self.cleanData()
        self.addEntry()
       self.writeEntryToFile()
        
        
    def myFunc(self,label):
        if(len(label['line4']) < 1):
            return 0
        return int(label['line4'])


    def writeEntryToFile(self):

        self.newFile.writelines("Item Count: " + str(len(self.items)) + "\n")

        self.items.sort(key=self.myFunc)
        
        for label in self.items:
            self.newFile.write(label["line1"]+"\n")
            self.newFile.write(label["line2"]+"\n")
            self.newFile.write(label["line3"]+"\n")
            self.newFile.write(label["line4"]+"\n\n")
  
            


