import re

hand = open("Actual_data.txt")
x = list()
for line in hand:
     y = re.findall('[0-9]+', line)
     x = x+y

count = 0
sum=0
for z in x:
    sum = sum + int(z)
    count += 1

print(count)
print(sum)
print(x)