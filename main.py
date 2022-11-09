import requests
from pprint import pprint
from config import open_weather_token




def get_weather(city, open_weather_token):
    try: 
        r = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        # pprint(data)
        
        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]


        print(f"Погода в городе: {city}\n Температура: {cur_weather}"
        f"Влажность: {humidity}\n Давление: {pressure} мм.рт.ст\n Ветер: {wind}"
        f"Хорошего дня!"
        )


    except Exception as ex:
        print(ex)
        print("Проверьте название города")


def main():
    city = input("Введите город")
    get_weather(city, open_weather_token)




    if __name__ ==  '__main__':
        main()