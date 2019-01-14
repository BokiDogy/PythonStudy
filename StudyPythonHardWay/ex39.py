states = {
    "Oregon": "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI"
}

cities = {
    "CA": "San Francisco",
    "MI": "Detroit",
    "FL": "Jacksonville"
}

cities["NY"] = "New York"
cities["OR"] = "Portland"

print("-" * 15)
print("NY State has: ", cities["NY"])
print("OR State has: ", cities["OR"])

print("-" * 15)
print("Michigan's abbreviation is: ", states["Michigan"])
print("Florida's abbreviation is: ", states["Florida"])

print("-" * 15)
print("Michigan has: ", cities[states["Michigan"]])
print("Florida has: ", cities[states["Florida"]])

print("-" * 15)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

print("-" * 15)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

print("-" * 15)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print("-" * 15)
state = states.get("Texas")
print(state)

if not state:
    print("Sorry, no Texas.")

city = cities.get("TX", "Does Not Exist")
print(f"The city for the state 'TX' is: {city}")
