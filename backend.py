import requests

API_KEY = "c1f7379ff79ac721b055169b7b717120"

def get_data(place, forcast_dates=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data



if __name__ == "__main__":
    print(get_data(place="Tokyo"))
