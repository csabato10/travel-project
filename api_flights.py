import requests
from requests import get, request
from requests.models import Response

url = "https://travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com/v1/prices/cheap"

querystring = {"origin":"HKT","page":"None","currency":"RUB","destination":"-"}

headers = {
    'x-access-token': "341353",
    'x-rapidapi-host': "travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com",
    'x-rapidapi-key': "9795c52b28msh004fe88c964bc24p1899c5jsn2b42c38742e3"
    }

response = get(url, headers=headers, params=querystring)

print(response)