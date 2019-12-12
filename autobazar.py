import xml.etree.ElementTree as ET

with open('Autobazar_in.xml', 'r') as xml_file:
  tree = ET.parse(xml_file)

root = tree.getroot()
for i, item in enumerate(root.findall('./advertisement')):
  item.find('id').text = str(i)
  item.find('text').text = ""

tree.write('Autobazar.xml', encoding="UTF-8", xml_declaration=True)
