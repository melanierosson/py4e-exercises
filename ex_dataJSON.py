import json
import urllib.request

# download raw json object
url = "http://py4e-data.dr-chuck.net/comments_42.json"

# declare variables
sum = 0
count = 0

# ask user for JSON data URL
dataLocate = input('\n Enter URL to retrieve data: ')
# if no entry, use default URL from above
if len(dataLocate) < 1 : dataLocate = url

# grabbing JSON data from URL page
data = urllib.request.urlopen(dataLocate).read().decode()

# parsing JSON object
obj = json.loads(data)

# print URL pulling from
print('⭐', dataLocate)

# print characters in data
print('Retrieved', len(data), 'characters')


print(obj)
print(data)

# for item in obj:
#     print('hmm', item['count'])
# for item in data:
#     print(item['count'])


# print(" Count:", count)

# print(" Sum:", sum, '\n')