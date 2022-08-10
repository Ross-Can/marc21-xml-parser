import parser


xml_parser = parser.Parser(r"C:\Users\WORK\Docughments\Programs\repos\marc21-xml-parser\ile.xml")
xml_parser.parse()

print("Title:", xml_parser.author)