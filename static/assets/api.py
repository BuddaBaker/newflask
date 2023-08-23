#API
import requests

url = "https://national-football-players.p.rapidapi.com/players"

headers = {
	"X-RapidAPI-Key": "71d411b83cmshb7b1cee17c5afa3p1c914ejsnde8d0527c7ad",
	"X-RapidAPI-Host": "national-football-players.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

players = response.json().get('player')