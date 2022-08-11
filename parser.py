from distutils.command.install_egg_info import safe_name
from traceback import print_tb
from turtle import title
from bs4 import BeautifulSoup


class Parser:

    def __init__(self, xml_loc = -1):
        if xml_loc == -1:
            return
        self.init_new_xml(xml_loc)
        
    def init_new_xml(self, new_xml):
        self.FILE_PATH = new_xml
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

    def printBook(self):
        print("Circ ", self.author)
        print("CD    [", self.title, "]")
        print("")

    def parse(self):
        try:
            data = self.f.read()
            Bs_data = BeautifulSoup(data, "xml")
            Bs_data=Bs_data.find_all('datafield', {'tag':'245'})
            i = 0

            for tags in Bs_data:
                self.locateInfo(tags)
                self.cleanInfo()
                self.printBook()
                i=i+1
            self.record_count = i
        
        except:
            self.title = "-1"
            self.sub_title = "-1"
            self.author = "-1"

