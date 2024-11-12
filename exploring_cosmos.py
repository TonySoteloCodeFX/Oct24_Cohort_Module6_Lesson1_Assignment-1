import requests
import json

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    planet_list = []
    print("-" * 50)
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue']
            orbit_period = planet['sideralOrbit']
            print(f"Planet Name: {name}\nMass: {round(mass, 2)}\nOrbit Period: {round(orbit_period)} days")
            print("-" * 50)
            planet_list.append(planet)
    return planet_list

def find_heaviest_planet(planets):
    heaviest_weight = 0
    heaviest_name = ''
    for planet in planets:
        if planet['mass']['massValue'] > heaviest_weight:
            heaviest_weight = planet['mass']['massValue']
            heaviest_name = planet['englishName']
    return(heaviest_name, round(heaviest_weight, 2))

def find_longest_orbit(planets):
    longest_orbit = 0
    longest_name = ''
    for planet in planets:
        if planet['sideralOrbit'] > longest_orbit:
            longest_orbit = planet['sideralOrbit']
            longest_name = planet['englishName']
    return(longest_name, round(longest_orbit))

planets = fetch_planet_data()
name, mass = find_heaviest_planet(planets)
name2, orbit = find_longest_orbit(planets)

print(f"The heavies planet is {name}, with a mass of {mass} kg.")
print("-" * 50)
print(f"The planet with the longest year is {name2}, with a year of {orbit} days.")
print("-" * 50)

