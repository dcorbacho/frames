import os
import sys

def getKey(item):
    return int(item)

if len(sys.argv) < 2:
    print('Error: missing path to images folder')
else:
    path = sys.argv[1]
    images = os.listdir(path)
    if len(sys.argv) == 3:
        prefix = sys.argv[2]
        numbers = sorted(list([image[len(prefix):].partition('.')[0] for image in images if image.startswith(prefix)]), key=getKey)
    else:
        numbers = sorted(list(map(lambda image: image.partition('_')[2].partition('.')[0], images)),key=getKey)

    first = numbers[0]
    last = numbers[len(numbers)- 1]

    if len(numbers) > 0:
        print ("First index: " + first)
        print ("Last index: " + last)

        strlen = len(first)

        index = int(first) + 1
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
