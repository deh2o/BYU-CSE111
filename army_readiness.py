# CSE 111 W07 Final Project
# Author: Agha Idam Walter

# Nigerian Army Logistics and Deployment Readiness Analyzer
# NOTE: The final project will be submitted as a single Python file named "army_readiness.py" 
#       that includes all the necessary functions and logic to read data, perform calculations, 
#       and generate reports.

import csv

# ---------------------------
# DATA FUNCTIONS
# ---------------------------

def read_dictionary(filename, key_index):
    """Read a CSV file into a dictionary."""
    data = {}
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            key = row[key_index]
            data[key] = row
    return data


# ---------------------------
# CALCULATION FUNCTIONS
# ---------------------------

def calculate_food_status(soldiers, food_days):
    """Return True if food supply is adequate."""
    required_days = 7
    return food_days >= required_days


def calculate_fuel_status(fuel_liters, terrain):
    """Return True if fuel is adequate based on terrain."""
    terrain_multiplier = {
        "forest": 1.2,
        "desert": 1.5,
        "urban": 1.0
    }
    required = 3000 * terrain_multiplier.get(terrain.lower(), 1)
    return fuel_liters >= required


def calculate_ammo_status(ammo_units, soldiers):
    """Return True if ammo supply is adequate."""
    required = soldiers * 5
    return ammo_units >= required


def determine_readiness(food_ok, fuel_ok, ammo_ok):
    """Return readiness level string."""
    if food_ok and fuel_ok and ammo_ok:
        return "FULLY READY"
    elif food_ok or fuel_ok or ammo_ok:
        return "PARTIALLY READY"
    else:
        return "NOT READY"


# ---------------------------
# REPORT FUNCTION
# ---------------------------

def generate_unit_report(unit_data, supply_data):
    unit_id, name, soldiers, terrain = unit_data
    _, food_days, fuel_liters, ammo_units = supply_data

    soldiers = int(soldiers)
    food_days = int(food_days)
    fuel_liters = int(fuel_liters)
    ammo_units = int(ammo_units)

    food_ok = calculate_food_status(soldiers, food_days)
    fuel_ok = calculate_fuel_status(fuel_liters, terrain)
    ammo_ok = calculate_ammo_status(ammo_units, soldiers)

    readiness = determine_readiness(food_ok, fuel_ok, ammo_ok)

    print("\n--- Unit Readiness Report ---")
    print(f"Unit: {name}")
    print(f"Soldiers: {soldiers}")
    print(f"Terrain: {terrain}")
    print(f"Food Status: {'OK' if food_ok else 'LOW'}")
    print(f"Fuel Status: {'OK' if fuel_ok else 'LOW'}")
    print(f"Ammo Status: {'OK' if ammo_ok else 'LOW'}")
    print(f"Overall Readiness: {readiness}")


# ---------------------------
# MAIN FUNCTION
# ---------------------------

def main():
    units = read_dictionary("units.csv", 0)
    supplies = read_dictionary("supplies.csv", 0)

    # print("Units loaded:", units.keys())
    # print("Supplies loaded:", supplies.keys())

    for unit_id in units:
        if unit_id in supplies:
            generate_unit_report(units[unit_id], supplies[unit_id])


if __name__ == "__main__":
    main()