import xml.etree.ElementTree as ET

input1 = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Vishal</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Khandekar</name>
        </user>
    </users>
</stuff>
'''

stuff = ET.fromstring(input1)
lst = stuff.findall('users/user')
print('user count:', len(lst))

'''
for item in lst:
    print('Name', item.find('name').text)
    print('ID', item.find('id').text)
    print('Attr', item.get('x'))
'''
