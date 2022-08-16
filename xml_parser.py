from distutils.command.install_egg_info import safe_name
from tarfile import RECORDSIZE
from traceback import print_tb
from turtle import title, write_docstringdict
from bs4 import BeautifulSoup


class XML_Parser:

    def __init__(self, xml_loc = -1, fileName =""):
        if xml_loc == -1:
            return
        self.init_new_xml(xml_loc, fileName)
        
    def init_new_xml(self, new_xml,fileName):
        self.FILE_PATH = new_xml
        self.FILE_NAME = fileName

        newFile =  self.FILE_NAME
        self.newFile = open(newFile, 'w', encoding="utf-8")

        try:
            self.f =  open(self.FILE_PATH, encoding="utf8")
        except:
            print ("[Error] No such file:", self.FILE_PATH)

    def locateInfo(self,tag):
        try:
            self.sf_a = tag.find("subfield", {'code' : 'a'}).getText()
        except:
            self.sf_a = "-1"

        try:
            self.sf_b = tag.find("subfield", {'code' : 'b'}).getText()
        except:
             self.sf_b = "-1"

        try:
            self.sf_c = tag.find("subfield", {'code' : 'c'}).getText()
        except:
            self.sf_c = "-1"
    
    def cleanInfo(self):
        self.title = self.sf_a.replace(":","").strip()
        self.title = self.sf_a.replace("/","").strip()

        self.sub_title = self.sf_b.replace(":","").strip()
        self.sub_title = self.sf_b.replace("/","").strip()

        self.author = self.sf_c.replace(":","").strip()
        self.author = self.sf_c.replace("/","").strip()

    def createEntry(self):
        entry = "Circ " + self.author + "\n"
        entry +="CD    [" + self.title + "]" + "\n"
        entry += "\n"

        print(entry)
        return entry

    def parse(self):
        try:
            data = self.f.read()
            Bs_data = BeautifulSoup(data, "xml")
            Bs_data=Bs_data.find_all('datafield', {'tag':'245'})
            self.record_count = 0

            for tags in Bs_data:
                self.locateInfo(tags)
                self.cleanInfo()
                self.writeEntryToFile()
                self.record_count += 1
      
        except:
            
            self.title = "-1"
            self.sub_title = "-1"
            self.author = "-1"
        
        
        print("Record Count:" , self.record_count)

    def writeEntryToFile(self):
        entry = self.createEntry()
        self.newFile.write(entry)


