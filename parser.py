from distutils.command.install_egg_info import safe_name
from traceback import print_tb
from turtle import title
from bs4 import BeautifulSoup


class Parser:
    def __init__(self, xml_loc):
        self.init_new_xml(xml_loc)
        
    def init_new_xml(self, new_xml):
        self.FILE_PATH = new_xml
        try:
            self.f =  open(self.FILE_PATH, 'r')
        except:
            print ("[Error] No such file:", self.FILE_PATH)

    def locateInfo(self,xml_data):
        info_xml = xml_data.find('datafield', {'tag':'245'})
        self.sf_a = info_xml.find("subfield", {'code' : 'a'}).getText()
        self.sf_b = info_xml.find("subfield", {'code' : 'b'}).getText()
        self.sf_c = info_xml.find("subfield", {'code' : 'c'}).getText()
    
    def cleanInfo(self):
        self.title = self.sf_a.replace(":","").strip()
        self.sub_title = self.sf_b.replace("/","").strip()
        self.author = self.sf_c.replace(":","").strip()

    def parse(self):
        try:
            data = self.f.read()
            Bs_data = BeautifulSoup(data, "xml")
            self.locateInfo(Bs_data)
            self.cleanInfo()
        except:
            self.title = "-1"
            self.sub_title = "-1"
            self.author = "-1"

