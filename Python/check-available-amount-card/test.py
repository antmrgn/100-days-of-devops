#import urllib.request, json 
#with urllib.request.urlopen("https://meal.gift-cards.ru/api/1/virtual-cards/+7927012345/1234") as url:
#    data = json.loads(url)
#    print(data['data.balance.availableAmount'])



# import urllib library
from urllib.request import urlopen
  
# import json
import json
# store the URL in url as 
# parameter for urlopen
url = "https://meal.gift-cards.ru/api/1/virtual-cards/+7927012345/1234"
  
# store the response of URL
response = urlopen(url)
  
# storing the JSON response 
# from url in data
data_json = json.loads(response.read())
  
# print the json response
print(data_json['data.balance.availableAmount'])