#!/usr/bin/python
import os
import sys

path = sys.argv[1]
images = os.listdir(path)
numbers = sorted(list(map(lambda image: image.partition('_')[2].partition('.')[0], images)))

first = numbers[0]
last = numbers[len(numbers)- 1]

if len(numbers) > 0:
    print "First index: " + first
    print "Last index: " + last

strlen = len(first)

index = int(first)
missing = []

for n in numbers:
    if int(n) == index + 1:
        missing.append(str(index).zfill(strlen))
    else:
        if int(n) > index:
            missing.append('{min}-{max}'.format(min = str(index).zfill(strlen), max = str(int(n) - 1).zfill(strlen)))
    index = int(n) + 1

print('Missing:')
print(','.join(missing))
