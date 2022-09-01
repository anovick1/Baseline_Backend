import requests
import pandas as pd

#### player info w image
player_info = pd.read_csv("./data/raw-csv/Player Career Info.csv")


url = "https://google-image-search1.p.rapidapi.com/v2/"

querystring = {"q":"Stephen Curry","hl":"en"}

headers = {
	"X-RapidAPI-Key": "dee50abc02msh5f35415b6a9ccfcp16104cjsn949c6585fb98",
	"X-RapidAPI-Host": "google-image-search1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)