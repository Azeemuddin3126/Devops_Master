#---------------------------------

# Parent class: CelestialBody
class CelestialBody:
    def __init__(self, size, mass, composition, name):
        self.size = size
        self.mass = mass
        self.composition = composition
        self.name = name

# Child class: Satellite
class Satellite(CelestialBody):
    def __init__(self, size, mass, composition, name, host_planet):
        super().__init__(size, mass, composition, name)  # Calling CelestialBody's __init__ method
        self.host_planet = host_planet  # Specific to Satellite

# Child class: Planet
class Planet(CelestialBody):
    def __init__(self, size, mass, composition, name, host_star):
        super().__init__(size, mass, composition, name)  # Calling CelestialBody's __init__ method
        self.host_star = host_star  # Specific to Planet

# Example usage
satellite = Satellite("small", 500, "rocky", "Moon", "Earth")
planet = Planet("large", 5000, "gaseous", "Jupiter", "Sun")

print(satellite.size,satellite.mass,satellite.composition,satellite.name,satellite.host_planet)
print(planet.size,planet.mass)

# Print attributes of the objects
