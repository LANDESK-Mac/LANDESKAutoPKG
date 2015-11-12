import xml.etree.ElementTree as ET
from io import BytesIO

def build_xml(name):
    root = ET.Element("ExportableContainer")
    root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    root_name_node = ET.SubElement(root, "Name")
    root_name_node.text = name
    items_node = ET.SubElement(root, "Items")
    items_container = ET.SubElement(items_node, "Exportable")
    items_container.set("xsi:type", "EPackage")
    ET.SubElement(items_container, "Type").text = "1"
    ET.SubElement(items_container, "Name").text = name
    ET.SubElement(items_container, "PrimaryFile").text = 'http://%corename%.eng.landesk.com/landesk/files/Adium_1.5.10.dmg'
    et = ET.ElementTree(root)
    f = BytesIO()
    et.write(f, encoding='utf-8', xml_declaration=True)
    print(f.getvalue())



if __name__ == "__main__":
    build_xml("Adium 3");
