from army_readiness import (
    calculate_food_status,
    calculate_fuel_status,
    calculate_ammo_status,
    determine_readiness
)

def test_calculate_food_status():
    assert calculate_food_status(400, 10) == True
    assert calculate_food_status(400, 3) == False


def test_calculate_fuel_status():
    assert calculate_fuel_status(5000, "forest") == True
    assert calculate_fuel_status(1000, "desert") == False


def test_calculate_ammo_status():
    assert calculate_ammo_status(3000, 400) == True
    assert calculate_ammo_status(1000, 400) == False


def test_determine_readiness():
    assert determine_readiness(True, True, True) == "FULLY READY"
    assert determine_readiness(True, False, False) == "PARTIALLY READY"
    assert determine_readiness(False, False, False) == "NOT READY"