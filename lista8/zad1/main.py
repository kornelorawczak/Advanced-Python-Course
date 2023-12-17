import datetime as dt
import aiohttp
import asyncio
from prywatne import API_KEY1, API_KEY2

async def kelvin_to_celcius(kelvin): return round(kelvin-273.15, 1)

async def get_coordinates(city_name, session):
    limit = 1
    GEO_URL = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={API_KEY1}"  # pobieramy koordynaty geograficzne miasto po jego nazwie
    async with session.get(GEO_URL) as response:
        data = await response.json()
        return data[0]['lat'], data[0]['lon']

async def get_weather_data(lat, lon, session):
    BASE_URL = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY1}"  # pobieramy dane dot. pogody danego miasta po jego koordynatach
    async with session.get(BASE_URL) as response:
        return await response.json()
async def city_weather(city_name):
    async with aiohttp.ClientSession() as session:
        lat, lon = await get_coordinates(city_name, session)
        response2 = await get_weather_data(lat, lon, session)
        print(f"\n    The weather is descripted as '{response2['weather'][0]['description']}' in {city_name}, {response2['sys']['country']}")
        print(f"    Temperature is {await kelvin_to_celcius(response2['main']['temp'])}℃ but it feels like {await kelvin_to_celcius(response2['main']['feels_like'])}℃ ")
        print(f"    Humidity is {response2['main']['humidity']}%")
        print(f"    The speed of wind is at {response2['wind']['speed']}m/s")
        print(f"    Local date and time is {dt.datetime.utcfromtimestamp(response2['dt']+response2['timezone'])}, sun rises at \
{str(dt.datetime.utcfromtimestamp(response2['sys']['sunrise']+response2['timezone']))[11:]} and sets at \
{str(dt.datetime.utcfromtimestamp(response2['sys']['sunset']+response2['timezone']))[11:]}")

async def get_movie_data(name, session):
    url = "https://imdb188.p.rapidapi.com/api/v1/searchIMDB"
    headers = {
	"X-RapidAPI-Key": API_KEY2,
	"X-RapidAPI-Host": "imdb188.p.rapidapi.com"
    }
    querystring = {"query": name}
    async with session.get(url, headers=headers, params=querystring) as response:
        return await response.json()


async def IMDB_info(name):
    async with aiohttp.ClientSession() as session:
        response = await get_movie_data(name, session)
        if response['status']:
            i=0
            while i<10:
                try:
                    print(f"'{response['data'][i]['title']}' is a {response['data'][i]['qid']} released in {response['data'][i]['year']}, starring {response['data'][i]['stars']} amongst others")
                    break
                except:
                    i+=1
                    continue
        else:
            print("There was an error with searching for this particular name")
async def weekly_top_10():
    url = "https://imdb188.p.rapidapi.com/api/v1/getWeekTop10"
    headers = {
        "X-RapidAPI-Key": API_KEY2,
        "X-RapidAPI-Host": "imdb188.p.rapidapi.com"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            for i in range(10):
                r = (await response.json())['data'][i]
                print(f"{i + 1}. '{r['titleText']['text']}' released on {r['releaseDate']['day']}-{r['releaseDate']['month']}-{r['releaseDate']['year']}, \
has {r['ratingsSummary']['aggregateRating']} average user rating with {r['ratingsSummary']['voteCount']} votes")

async def main():
    action = input("Select action using API: \n Type '1' to learn about weather in chosen city \n Type '2' to learn about a chosen movie/TV show \n Type '3' to learn about top 10 Movies/TV shows this week \n")

    if action == '1':
        city_name = input("Type in the name of a city: ")
        try:
            await city_weather(city_name)
        except IndexError:
            print(f"There is no city with that name!")
    elif action == '2':
        name = input("Type in the name of a movie: ")
        try:
            await IMDB_info(name)
        except IndexError:
            print("There is no movie nor TV show with given name in IMDB database!")
    elif action == '3':
        await weekly_top_10()
    else:
        print("You cannot select this action!")



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


