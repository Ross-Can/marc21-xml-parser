import csv_parser
import os

def format(xml_parser):
    print("Circ ", xml_parser.author)
    print("CD   [", xml_parser.title, "]")
    print("")


INPUT_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__)) + "\\" + "inputFiles"
print(INPUT_FOLDER_PATH)

csv_files = os.listdir(INPUT_FOLDER_PATH)
csv_parser = csv_parser.CSV_Parser()

for file in csv_files:
    file_path = INPUT_FOLDER_PATH + "\\" + file
    csv_parser.init_new_csv(file_path, file)
    csv_parser.parse()
