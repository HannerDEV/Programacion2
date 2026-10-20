import random
import time
from typing import TypedDict, Dict, Literal


VehicleType = Literal['Car', 'Motorcycle']

class costumer(TypedDict):
    vehicle_type: VehicleType
    rate: int
    time: int

Parking = Dict[str, costumer]

parking: Parking = {}

RATES = {"1": ("Car", 100), "2": ("Motorcycle", 50)}

statics: Dict[str, int] = {"Car": 0, "Motorcycle": 0,"TOTAL_COP": 0}


def check_in():
    while True:
        print("Select their vehicle")
        op = input("1. Car   2. Motorcycle:\n")
        if op in RATES:
            break
        print("Invalid option")
        
    code = f"{random.randint(0,99999):05d}"
    type_vehicle = RATES[op][0]
    fee = RATES[op][1]
    time0 = time.time()

    print(f"Their code is: {code}")

    parking[code] = {
        "vehicle_type": type_vehicle,
        "rate": fee,
        "time": time0
    }

    statics[type_vehicle] += 1
    print("Vehicle registered sucessfully")
    print("You can continue..")

def check_out():
    while True:
        enter_code = input("Enter their code: ").strip()
        if enter_code not in parking:
            print("Invalid code")
        else:
            break

    vehicle = parking.pop(enter_code)

    rate = vehicle["rate"]
    total_minutes = max(1, (time.time() - vehicle["time"])//60)

    total_fee = rate*total_minutes

    print(f"TOTAL FEE: {total_fee}")
    paid = 0

    while paid < total_fee:
        paid += float(input(f"faltan {total_fee - paid}. Ingrese un billete: "))

    print(f"Sucessful pay. Sobrante: {paid - total_fee}")
    statics["TOTAL_COP"] += total_fee

def abstract_day():
    print(f"\n{'='*8}ABSTRACT OF THE DAY{'='*8}")
    print(f"Entered cars: {statics['Cars']}    Entered motorcycles: {statics['Motorcycles']}")
    print(f"Total Money collected: {statics['TOTAL_COP']}")
    print(f"Vehicles still parked: {len(parking)}")


def main(): 
    options = {"1": check_in, "2": check_out, "3": abstract_day }
    while True:
        print(f"{'='*8}WELCOME TO PARKING SYSTEM{'='*8}")
        print("Select the corresponding option: ")
        op = input("1. Check-in   2. Check-out  3. Abstract of the day    4. Exit\n").strip()

        if op == "4": break

        if op in options: options[op]()
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()