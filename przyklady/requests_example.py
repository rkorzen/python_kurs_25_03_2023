# pip install requests
import requests

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C/?format=json")

print(response)
rates = response.json()[0]["rates"]


currency = "AUD"
amount = 100

print(rates)
print(type(rates))

data = [x for x in rates if x['code'] == currency]
print(data[0]['ask'] * amount)
