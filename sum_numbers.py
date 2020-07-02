import re
file_ref = open('sample_data.txt', 'r')
lines = file_ref.readlines()
lst1 = []
count = 0
sum = 0
for item in lines[:]:
    if re.findall('\S+[0-9]\S+', item):
        y = re.findall('\S+[0-9]\S+', item)
        for i in y:
            lst1.append(i)

for item in lst1:
    count += 1


print(count)
print(sum)
print(lst1)