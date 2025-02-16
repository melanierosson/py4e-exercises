# taste the rainbow
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# importing re
import re

# opening file
filename = 'regex_sum_1136998.txt'
filetxt = open(filename)

regex = '[0-9]+'
sumInts = 0  
countInts = 0
integers = []

for line in filetxt : 
	line = line.rstrip()
	integers.append(re.findall(regex, line))
    
# removing empty list items in the file line lists (lines that had no integers)
onlyInts = [listItems for listItems in integers if listItems]

newIntList = []
newIntItemStr = ''

# stringifying everything (there are currently list items within the larger list)
for eachItem in onlyInts :
    for insideEach in eachItem :
        newIntItemStr = newIntItemStr + ' ' + insideEach
    newIntList = newIntItemStr
    # splitting separate items into a single list based on spaces
    numList = newIntList.split()

# getting final numbers from final integer list
for numItems in numList :
    # list item count
    countInts += 1
    # list items sum
    sumInts += int(numItems)

print(bcolors.WARNING + '\n💣  The ' + bcolors.HEADER + 'total number' + bcolors.WARNING + ' of integers in ' + bcolors.OKCYAN + filename + bcolors.WARNING + ' is ' + bcolors.OKGREEN + str(countInts) + bcolors.WARNING)
print('💥  The ' + bcolors.HEADER + 'sum '  + bcolors.WARNING + 'of all the integers in ' + bcolors.OKCYAN + filename + bcolors.WARNING + ' is ' + bcolors.OKGREEN + str(sumInts) + bcolors.ENDC + '\n')
