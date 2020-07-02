import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Vishal</name>
    <phone type="int">
        9969496054
    </phone>
    <email hide="yes"/>
</person>
'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

