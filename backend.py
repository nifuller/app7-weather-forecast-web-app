import requests

API_KEY = "c1f7379ff79ac721b055169b7b717120"

def get_data(place, forcast_dates, kind):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forcast_dates
    filtered_data = filtered_data[:nr_values]
    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data



if __name__ == "__main__":
    print(get_data(place="Tokyo",forcast_dates=3, kind="Temperature"))
