from msilib.schema import File
from sre_constants import SUCCESS
from tkinter import TRUE
from unittest import skip
from xml.etree.ElementTree import XML
import csv_parser
import xml_parser
import os

INPUT_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__)) + "\\" + "inputFiles"


try:
    files = os.listdir(INPUT_FOLDER_PATH)
except:
    print("[ERROR:INPUT FOLDER DOES NOT EXIST] Input File: '", INPUT_FOLDER_PATH, "'")
    exit()

for file in files:
    file_path = INPUT_FOLDER_PATH + "\\" + file
    SUCCESS = TRUE
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
        SUCCESS = False

    print("....File Parsed and Outputed") if SUCCESS else next