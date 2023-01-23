import requests

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"23456"}

headers = {
	"X-RapidAPI-Key": "928ef862e2mshe8c2642e7e0285bp12a93ejsnd754169fe8dd",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
