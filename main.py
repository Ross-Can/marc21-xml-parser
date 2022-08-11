import parser
import os

def format(xml_parser):
    print("Circ ", xml_parser.author)
    print("CD    [", xml_parser.title, "]")
    print("")


XML_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__)) + "\\" + "inputFiles"
print(XML_FOLDER_PATH)

xml_files = os.listdir(XML_FOLDER_PATH)
xml_parser = parser.Parser()

for file in xml_files:
    file_path = XML_FOLDER_PATH + "\\" + file
    xml_parser.init_new_xml(file_path)
    xml_parser.parse()
    format(xml_parser)
    


