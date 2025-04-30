class Cargo:
    def __init__(self, volume, weight):
        self.volume = volume
        self.weight = weight
    def __str__(self):
        return f"Cargo: {self.volume} m3, {self.weight} kg"

class Truck:
    def __init__(self, payload,  volume_capacity, cargo_list):
        self.payload = payload
        self.volume_capacity = volume_capacity
        self.cargo_list = []

    def add_cargo(self, cargo):
        total_weight = sum(c.weight for c in self.cargo_list)
        total_volume = sum(c.volume for c in self.cargo_list)

        if total_weight + cargo.weight > self.payload:
            raise ValueError("Over weight limit")
        if total_volume + cargo.volume > self.volume_capacity:
            raise ValueError("Over volume limit")
        self.cargo_list.append(cargo)

    def remove_cargo(self, volume, weight):
        for i in self.cargo_list:
            if i.volume == volume and i.weight == weight:
                return self.cargo_list.remove(i)
        raise ValueError("Cargo not found")

    def calculate_load(self):
        total_weight = sum(i.weight for i in self.cargo_list)
        total_volume = sum(i.volume for i in self.cargo_list)
        return f"Total weight: {total_weight}, Total volume: {total_volume}"

    def display_info(self):
        load_info = self.calculate_load()
        return (
            f"Truck info:\n"
            f"Payload capacity: {self.payload}\n"
            f"Volume capacity: {self.volume_capacity} m3\n"
            f"{load_info}"
        )