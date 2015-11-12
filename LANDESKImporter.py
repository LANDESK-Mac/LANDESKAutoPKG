#!/usr/bin/python

"""See docstring for LANDESKImporter class"""

from autopkglib import Processor, ProcessorError
import xml.etree.ElementTree as ET


__all__ = ["LANDESKImporter"]

class LANDESKImporter(Processor):
    """Uploads a package to a LANDESK package server and creates an import
    .xml file to import into the package list on the core. A destination
    URL can also be specified for this .xml file.

    """

    description = __doc__
    input_variables = {
        "package_name": {
            "required": True,
            "description": "The name of the package."
        },
        "package_description": {
            "required": False,
            "description": "The package description"
        },
        "primary_file": {
            "required": True,
            "description": "Location of the file"
        },
        "output_file": {
            "required": True,
            "description": "Where to store the .ldms file"

        }
    }

    output_variables = {
    }

    __doc__ = description

    def main(self):
        name = self.env.get("package_name")
        primary_file = self.env.get("primary_file")
        description = self.env.get("package_description")
        root = ET.Element("ExportableContainer")
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root_name_node = ET.SubElement(root, "Name")
        root_name_node.text = name
        items_node = ET.SubElement(root, "Items")
        items_container = ET.SubElement(items_node, "Exportable")
        items_container.set("xsi:type", "EPackage")
        ET.SubElement(items_container, "Type").text = "1"
        ET.SubElement(items_container, "Name").text = name
        ET.SubElement(items_container, "Description").text = description
        ET.SubElement(items_container, "PrimaryFile").text = string.replace(primary_file, "\%", "%")
        f = open(self.env.get("output_file"), 'w')

        et = ET.ElementTree(root)
        et.write(f, encoding='utf-8', xml_declaration=True)


if __name__ == '__main__':
    PROCESSOR = LANDESKImporter()
    PROCESSOR.execute_shell()
