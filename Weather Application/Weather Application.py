# DSC 510
# Week 12
# Final Project
# Author: Muthukumar Kadhirvel
# 11/17/2021


import requests


api_key = '049bca3a5bd15e8ebf833b0eba2fbda6'
api_url = 'https://api.openweathermap.org/data/2.5/weather?'


def get_temp_unit():
    """Get Unit of temperature to be passed to API. 'F' for Fahrenheit or 'C' for Celsius or 'K' for Kelvin"""
    temp_input = input("Please enter 'F' for Fahrenheit or 'C' for Celsius or 'K' for Kelvin: ")
    temp_input = temp_input.upper()
    while True:
        if temp_input == 'K':
            return 'standard'
        elif temp_input == 'F':
            return 'imperial'
        elif temp_input == 'C':
            return 'metric'
        else:
            temp_input = input("Invalid value entered. Please enter 'F' for Fahrenheit or 'C' for Celsius or 'K' for Kelvin ")
            temp_input = temp_input.upper()


def print_output(dictionary, temp_unit):
    """Print output data based on input city or zip code and unit of temperature selected"""
    weather_data = dict(dictionary)
    output_city = weather_data['name']
    current_temp = weather_data['main']['temp']
    min_temp = weather_data['main']['temp_min']
    max_temp = weather_data['main']['temp_max']
    feels_like = weather_data['main']['feels_like']
    humidity = weather_data['main']['humidity']
    pressure = weather_data['main']['pressure']
    cloud_cover = weather_data['weather'][0]['description']
    if temp_unit == 'standard':
        temp_suffix = 'K'
    elif temp_unit == 'imperial':
        temp_suffix = '°F'
    else:
        temp_suffix = '°C'
    print(f'Current Weather Conditions for {output_city}')
    print("-------------------------------", end='')
    print('-' * len(output_city))
    print(f'Current Temperature    : {current_temp}{temp_suffix}')
    print(f'Maximum Temperature    : {max_temp}{temp_suffix}')
    print(f'Minimum Temperature    : {min_temp}{temp_suffix}')
    print(f'Feels Like Temperature : {feels_like}{temp_suffix}')
    print(f'Pressure               : {pressure}hPa')
    print(f'Humidity               : {humidity}%')
    print(f'Cloud Cover            : {cloud_cover.title()}')


def get_user_input():
    """Get user input for C for City or Z for Zip to look up weather data"""
    # Allow the user to enter C for City or Z for Zip
    user_input = input("Please enter C for city or Z for zip to look up weather data: ")
    user_input = user_input.upper()
    bad_input = True
    while bad_input is True:
        if user_input == 'C':
            bad_input = False
            city = input("Please enter the City Name: ")
            state = input("Please enter the State Name: ")
            get_by_city(city, state)
        elif user_input == 'Z':
            bad_input = False
            zip_code = input("Please enter the Zip Code: ")
            get_by_zip(zip_code)
        else:
            bad_input = True
            user_input = input("Invalid value entered. Please enter C for city or Z for zip to look up weather data: ")
            user_input = user_input.upper()


def get_by_city(city, state):
    """Call Open Weather API to get weather details for city"""
    temp_unit = get_temp_unit()
    try:
        response = requests.get(f'{api_url}q={city},{state},USA&appid={api_key}&units={temp_unit}')
        response.raise_for_status()
        print_output(response.json(), temp_unit)
    except requests.exceptions.HTTPError:
        print(f"Issue accessing Weather Details for {city} City.")


def get_by_zip(zip_code):
    """Call Open Weather API to get weather details for zip code"""
    temp_unit = get_temp_unit()
    try:
        response = requests.get(f'{api_url}zip={zip_code}&appid={api_key}&units={temp_unit}')
        response.raise_for_status()
        print_output(response.json(), temp_unit)
    except requests.exceptions.HTTPError:
        print(f"Issue accessing Weather Details for {zip_code} zip code.")


def main():
    """Main Function"""
    print("Welcome to Final Project")
    choice = 'Y'
    while choice != 'N':
        if choice == 'Y':
            get_user_input()
        else:
            print("Invalid value entered. ", end='')
        # Allow the user to enter Y to perform another weather lookup
        choice = input("Press 'Y' to perform another weather lookup or 'N' to exit: ")
        choice = choice.upper()
    print("Thanks for running Final Project")


if __name__ == "__main__":
    main()
