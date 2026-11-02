from typing import Callable

electric_variables: dict = {"voltage": 0, "resistance": 0,"current": 0, "power": 0, "time": 0,"energy": 0}

def current_formula(v: float, r: float):
    return v/r

def power_formula(v: float, i: float):
    return v*i

def energy_formula(p: float, t: float):
    return p*t

def generic_operation(calc_function: Callable[[float, float], float], key1:str, key2:str, key_result:str, units: str):
    while True:
        try:
            variable1 = electric_variables[key1] if electric_variables[key1] != 0 else float(input(f"Enter the {key1}: "))
            variable2 = electric_variables[key2] if electric_variables[key2] != 0 else float(input(f"Enter the {key2}: "))

            if variable1 <= 0 or variable2 <= 0: 
                raise ValueError(f"The {key1} and {key2} values must be greater than zero")

            break
            
        except ValueError as err:
            print(f"An error ocurred:{err}")

    result = calc_function(variable1, variable2)
    print(f"The {key_result} is: {result} {units}")
    
    electric_variables[key1] = variable1
    electric_variables[key2] = variable2
    electric_variables[key_result] = result

def calculate_current():
    return generic_operation(current_formula, "voltage", "resistance", "current", "Ampers" )

def calculate_power():
    return generic_operation(power_formula, "voltage", "current", "power", "Watts")

def calculate_energy():
    return generic_operation(energy_formula, "power", "time", "energy", "KwH")

def determine_sector(enviroment_type: str):
    if enviroment_type == "industrial":
        def rate_industry(num: float):
            if num < 500: return "low"
            if num <= 1500: return "medium"
            else: return "high"
        return rate_industry
    
    else:
        def rate_housing(num: float):
                if num < 50: return "low"
                if num <= 150: return "medium"
                else: return "high"
        return rate_housing

def rate_consumption():
    energy = electric_variables.get("energy", 0)

    if energy == 0:
        print("Please calculate the energy first")
        return

    sector = "0"
    while sector != "1" and sector != "2":
        sector = input("Seleccione el sector (1. Industrial, 2. Vivienda): ")
    rating_function = determine_sector("industrial" if sector == "1" else "housing")

    category = rating_function(energy)

    print(f"The rate of consumption is: {category}") 

def restart_variables():
    for key in electric_variables:
        electric_variables[key] = 0.0
    print("All variables has been restarted")

def main() -> None:
    print(f"{"="*8}WELCOME TO THE ELECTRICAL MAINTENANCE SYSTEM{"="*8}")
    while True:
        options = {"1": calculate_current, "2": calculate_power, "3": calculate_energy, "4": rate_consumption, "5": restart_variables}
        
        print("""
        1. Calculate current
        2. Calculate power
        3. Calculate energy
        4. Rate consumption
        5. Restart variables
        6. Exit\n
        """)
        option = input("Enter the correspond option: ")

        if option == "6":
            print("Exiting...")
            break
        if option in options:
            options[option]()
        else:
            print("Not valid option")



if __name__ == "__main__":
    main()