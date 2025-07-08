import xml.etree.ElementTree as ET

xml_data = """
<person>
    <name>Ivan</name>>
    <age>31</age>
    <city>Moscow</city>
</person>
"""

root = ET.fromstring(xml_data)

print(root.find('name').text)