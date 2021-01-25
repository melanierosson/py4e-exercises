import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

sum = 0

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

dataLocate = input('\n Enter URL to retrieve data: ' + bcolors.OKCYAN)
if len(dataLocate) < 1 : dataLocate = 'http://py4e-data.dr-chuck.net/comments_42.xml'

pageData = urllib.request.urlopen(dataLocate)
data = pageData.read()

print(bcolors.WARNING, dataLocate, bcolors.ENDC)
print('\n Characters:', bcolors.WARNING, len(data), bcolors.ENDC)

tree = ET.fromstring(data)
counts = tree.findall('.//count')


for count in tree.iter('count'):
    strNum = count.text
    intNum = int(strNum)
    sum += intNum

print(" Count:", bcolors.WARNING, len(counts), bcolors.ENDC)

print(" Sum:", bcolors.WARNING, sum, bcolors.ENDC, '\n')