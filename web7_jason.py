import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location ')

total_number = 0
sum = 0
print('Retriving url', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

# print(json.dumps(js, indent=4))

counts = js['comments']
for item in counts:
    total_number += 1
    sum += int(item['count'])

print('total_number: ', total_number)
print('sum: ', sum)
