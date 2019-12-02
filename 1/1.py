import math

# Reading each modules mass as a list
moduleList = [int(line.rstrip('\n')) for line in open('puzzle_input.txt')]
# Defining a list that will store each modules fuel
fuelList = []


def get_fuel(mass: int) -> int:
    def round_down(n: float) -> int:
        return int(math.floor(n * 10) / 10)
    return round_down(mass / 3) - 2


for moduleMass in moduleList:
    fuelList.append(get_fuel(moduleMass))

print(sum(fuelList))
