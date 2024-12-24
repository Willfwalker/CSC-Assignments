import requests
from bs4 import BeautifulSoup

def get_weather(city, country):
    city = city.strip().replace(" ", "-").lower()
    country = country.strip().lower()
    url = f"https://www.timeanddate.com/weather/{country}/{city}"

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve data for {city}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    temp_element = soup.find("div", class_="h2")

    if temp_element:
        temperature = temp_element.text.strip()
        print(f"The current temperature in {city} is {temperature}.")
    else:
        print(f"Could not find temperature for {city}")

if __name__ == "__main__":
    city = input("Enter a City: ")
    country = input("Enter a Country: ")
    get_weather(city, country)
