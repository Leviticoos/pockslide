class SolarSystem:
    def __init__(self, name, sunMass, planets):
        self.name = name
        self.sunMass = sunMass
        self.planets = planets
        
    def mass(self):
        return self.sunMass