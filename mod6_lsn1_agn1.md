<h1>Module 6 Lesson 1: Assignments | Web Fundamentals</h1>
<hr>

<h3>1. Exploring Web Technologies and Python Programming</h3>

<b>Objective:</b> The aim of this assignment is to deepen your understanding and practical skills in web technologies and Python programming. You will explore the functionalities of the World Wide Web, web architectures, and the Python programming language, particularly focusing on setting up environments, API interactions, and data handling.

<b>Problem Statement:</b> You are tasked with creating a Python application that interfaces with a public API, fetches data, and processes it. This application should provide insights into how different web architectures work and demonstrate your ability to set up a Python environment, make API requests, and handle JSON data.

<h5><i>Task 1: Setting Up a Python Virtual Environment and Installing Packages</i></h5>

1. Create a new Python virtual environment in your project directory.
<br>

2. Activate the virtual environment.
<br>

3. Install the `requests` packages.

<b>Expected Outcome:</b> A successfully created and activated virtual environment with the required packages installed.

<h5><i>Task 2: Fetching Data from the Pokémon API</i></h5>

1. Write a Python script to make a GET request to the Pokémon API (`https://pokeapi.co/api/v2/pokemon/pikachu`).
<br>

2. Extract and print the name and abilities of the Pokémon.

<b>Expected Outcome:</b> The script should output the name of the Pokémon (Pikachu) and a list of its abilities.

<h5><i>Task 3: Analyzing and Displaying Data</i></h5>

1. Modify the script to fetch data for three different Pokémon.
<br>

2. Create a function to calculate and return the average weight of these Pokémon.
<br>

3. Print the names, abilities, and average weight of the three Pokémon. **Code Example:**

```
def fetch_pokemon_data(pokemon_name):
    return #json response

def calculate_average_weight(pokemon_list):
    return #average weight

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
```
<b>Expected Outcome:</b> The script should display the names and abilities of the three chosen Pokémon and their average weight. The function should correctly calculate and return the average weight based on the data fetched from the API. 

<hr>

<h3>2. Exploring the Digital Cosmos with Python and the Web</h3>

<b>Problem Statement:</b> Imagine you are a developer tasked with creating a feature for a web application that provides users with insightful information about various space objects. Your application will fetch data from a publicly available space API, process this data, and display it in a user-friendly format.

<h5><i>Task 1: Set up a Python Virtual Environment and Install Required Packages</i></h5>

1. Create a new virtual environment in Python. 
<br>

2. Activate the virtual environment. 
<br>

3. Install the `requests` package for making HTTP requests.

<b>Expected Outcome:</b> A successfully created and activated virtual environment with the `requests` package installed.

<h5><i>Task 2: Fetch Data from a Space API</i></h5>

1. Write a Python script that makes a GET request to a space API (e.g., [The Solar System OpenData](https://api.le-systeme-solaire.net/en/)) to fetch data about planets.
<br>

2. Parse the JSON response and extract information about each planet, such as its name, mass, and orbit period.

<b>Code Example:</b>

```
import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = #get planet English name
            mass = #get planet mass
            orbit_period = #get planet orbit period
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()
```
<b>Expected Outcome:</b>

```
Planet: Uranus, Mass: 8.68127, Orbit Period: 30685.4 days
Planet: Neptune, Mass: 1.02413, Orbit Period: 60189.0 days
Planet: Jupiter, Mass: 1.89819, Orbit Period: 4332.589 days
Planet: Mars, Mass: 6.41712, Orbit Period: 686.98 days
Planet: Mercury, Mass: 3.30114, Orbit Period: 87.969 days
Planet: Saturn, Mass: 5.68336, Orbit Period: 10759.22 days
Planet: Earth, Mass: 5.97237, Orbit Period: 365.256 days
Planet: Venus, Mass: 4.86747, Orbit Period: 224.701 days
```

<h5><i>Task 3: Data Presentation and Analysis</i></h5>

1. Perform a simple analysis, such as finding the planet with the longest orbit period or the heaviest planet. 

```
import requests

def fetch_planet_data():
    # Enhance format the output in a more readable manner
    return #list of planets

def find_heaviest_planet(planets):
    return #heaviest planet

planets = fetch_planet_data()
name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")
```
<b>Expected Outcome:</b> A more structured and formatted output, along with an analysis result, such as identifying the heaviest planet in the solar system.

<b>NOTE:</b> Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected. If you have a function, make sure the function is called and runs. If there are classes/objects, make sure they are instantiated and the methods are called.

The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.