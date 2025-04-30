from truck import Cargo, Truck
if __name__ == "__main__":
    cargo1 = Cargo(2, 500)
    cargo2 = Cargo(3, 700)
    cargo3 = Cargo(1, 400)
    truck = Truck(2000, 10, [])
    truck.add_cargo(cargo1)
    truck.add_cargo(cargo2)
    truck.add_cargo(cargo3)
    print(truck.display_info())





