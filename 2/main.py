import math

# Reading each modules mass as a list
moduleList = [int(line.rstrip('\n')) for line in open('../puzzle_input.txt')]
# Defining a list that will store each modules fuel
totalFuelList = []


class Module:
    def __init__(self, mass: int) -> None:
        """
        Module object
        :param mass:  Mass of the initial object
        """
        self.mass = mass
        self.fuelList = []

    def get_fuel(self, mass: int):
        def round_down(n: float) -> int:
            return int(math.floor(n * 10) / 10)
        fuel = round_down(mass / 3) - 2
        # Fuel can not be negative so return 0
        if fuel <= 0:
            return 0
        # Recursive, each fuel as its own mass so we compute the mass of each fuel and append
        self.fuelList.append(fuel)
        self.get_fuel(mass=fuel)

    def get_total_fuel(self):
        """
        Returns the mass of all the fuel needed per module
        """
        self.get_fuel(self.mass)
        return sum(self.fuelList)


for moduleMass in moduleList:
    totalFuelList.append(Module(moduleMass).get_total_fuel())

print(sum(totalFuelList))
