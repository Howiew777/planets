from planetarium1 import planets

mercury = planet("Mercury", "gaseous", 1, 330)
venus = planet("Venus", "toxic", 2, 132)
earth = planet("Earth", "home", 1, 76)
mars = planet("Mars", "martian", 2, 53)
jupiter = planet("Jupiter", "stupider", 12, -19)
saturn = planet("Saturn", "rings", 4, -78)
uranus = planet("Uranus", "dwarf", 3, -219)
neptune = planet("Neptune", "blue", 7, -347)


print("What planet would you like to see?")
p = input()

if(p == "mercury"):
    print(mercury)
if(p == "venus"):
    print(venus)
if(p == "earth"):
    print(earth)
if(p == "mars"):
    print(mars)
if(p == "jupiter"):
    print(jupiter)
if(p == "saturn"):
    print(saturn)
if(p == "uranus"):
    print(uranus)
if(p == "neptune"):
    print(neptune)
