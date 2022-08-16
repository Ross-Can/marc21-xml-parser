from msilib.schema import File
from unittest import skip
from xml.etree.ElementTree import XML
import csv_parser
import xml_parser
import os

INPUT_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__)) + "\\" + "inputFileds"


try:
    files = os.listdir(INPUT_FOLDER_PATH)
except:
    print("[ERROR:INPUT FOLDER DOES NOT EXIST] Input File: '", INPUT_FOLDER_PATH, "'")
    exit()

for file in files:
    file_path = INPUT_FOLDER_PATH + "\\" + file

    print("\nReading:", file.strip())

    if file.endswith(".csv"):
        print("CSV File Parsing.....")
        parser = csv_parser.CSV_Parser(file_path, file)
        parser.parse()

    elif file.endswith(".xml"):
        print("XML File Parsing.....")
        parser = xml_parser.XML_Parser(file_path, file)
        parser.parse()

    else:
        print("ERROR: File not in xml or csv format")