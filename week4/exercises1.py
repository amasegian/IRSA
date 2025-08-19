#Exercise 1
events = [
    "meteor shower", "lunar eclipse", "solar flare", "meteor shower",
    "comet sighting", "meteor shower", "lunar eclipse", "comet sighting"
]

#Exercise 2
observation_methods = {
    "optical": ["M31", "M42", "M45", "NGC224"],
    "radio": ["M1", "M87", "NGC5128"],
    "infrared": ["M31", "NGC1976", "M45"],
    "x-ray": ["M1", "NGC1275"]
}

#Exercise 4
distances_ly = [10.5, 32.7, 4.3, 65.2, 21.1]

#Exercise 5
galaxies = {"Andromeda": 0.78, "Triangulum"0.85, "Whirlpool": 7.0}
conversion_factor = 3.26e6

for galaxy in galaxies:
    ly_distance = galaxy * conversion_factor
    print("The galaxy " + galaxy + " is " + ly_distance + " light years away.")