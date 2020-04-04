#!/usr/bin/python3
import json
import requests
import dateutil.parser
import datetime

#get country to look up
#country = input(str('What country to look for? (ISO country code (TH, CH etc.)) ')).upper()

def get_covid_data(country_code):
    #methods
    def f_number(n):
            return str(f'{n:,}')

    def get_variables_locations(v):
            return country_data_json['locations'][0][v]

    # data of country to look up
    base_url = 'https://coronavirus-tracker-api.herokuapp.com/v2/locations?country_code='
    countr_data = requests.get(base_url+country_code)
    country_data_json = countr_data.json()
    #print('API called')
    #data global
    latest_url = base_url.replace('locations?country_code=', 'latest', 1)
    latest_data = requests.get(latest_url)
    latest_json = latest_data.json()
    #print('Global API called')
    #global variables
    global_confirmed = latest_json['latest']['confirmed']
    global_deaths = latest_json['latest']['deaths']
    #global_recovered = latest_json['latest']['recovered']
    global_fatality_rate = global_deaths/global_confirmed*100
    r_global_fatality_rate = round(global_fatality_rate, 2)
    global_population = 7800000000
    r_global_population = 7.8
    global_p_of_pop_infected = global_confirmed/global_population*100
    r_global_p_of_pop_infected = round(global_p_of_pop_infected, 4)
    
    global_data = {
        'global_confirmed': latest_json['latest']['confirmed'],
        'global_deaths': latest_json['latest']['deaths'],
        'global_recovered': latest_json['latest']['recovered'],
        'global_fatality_rate': global_deaths/global_confirmed*100,
        'r_global_fatality_rate': round(global_fatality_rate, 2),
        'global_population': 7800000000,
        'r_global_population': 7.8,
        'global_p_of_pop_infected': global_confirmed/global_population*100,
        'r_global_p_of_pop_infected': round(global_p_of_pop_infected, 4)
    }
    #print(global_data)
    #country cariables

    country = get_variables_locations('country')
    population = get_variables_locations('country_population')
    latest = get_variables_locations('latest')
    confirmed = latest['confirmed']
    deaths = latest['deaths']
    recovered = latest['recovered']
    last_updated = get_variables_locations('last_updated')
    fatality_rate = deaths/confirmed*100
    r_fatality_rate = round(fatality_rate, 2)
    date_obj = dateutil.parser.parse(last_updated)
    date_str = date_obj.strftime('%B %d, %Y')
    p_of_pop_infected = confirmed/population*100
    r_p_of_pop_infected = round(p_of_pop_infected, 4)

    country_data = {
        'country': get_variables_locations('country'),
        'population': get_variables_locations('country_population'),
        'latest': get_variables_locations('latest'),
        'confirmed': latest['confirmed'],
        'deaths': latest['deaths'],
        'recovered': latest['recovered'],
        'last_updated': get_variables_locations('last_updated'),
        'fatality_rate': deaths/confirmed*100,
        'r_fatality_rate': round(fatality_rate, 2),
        'date_obj': dateutil.parser.parse(last_updated),
        'date_str': date_obj.strftime('%B %d, %Y'),
        'p_of_pop_infected': confirmed/population*100,
        'r_p_of_pop_infected': round(p_of_pop_infected, 4)
    }
    #print(country_data)
    return_for_tg = {
        'global_data': global_data,
        'country_data': country_data
    }    
    #print(return_for_tg)
    return return_for_tg
