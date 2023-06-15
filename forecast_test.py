import requests
import json

url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

querystring = {"q":"London","days":"3"}

headers = {
	"X-RapidAPI-Key": "REDACTED",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

json_object = json.loads(response.json())
json_formatted_str = json.dumps(json_object, indent=2)

#print(response.json())
print(json_formatted_str)