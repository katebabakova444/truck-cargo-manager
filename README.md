# Truck Cargo Manager

A simple logistics-style project written in Python using Object-Oriented Programming (OOP).

## Description

This project simulates a truck that can carry cargo under specific weight and volume limits.  
It includes logic to:
- add and remove cargo,
- calculate total load,
- prevent overloads,
- and display detailed truck status.

## Technologies

- Python 3.x

## Features

- `Cargo` class: defines individual cargo units with volume and weight
- `Truck` class: manages a list of cargo, enforces capacity limits, and calculates current load
- Error handling using `ValueError`
- Clear string output for tracking cargo status

## Example

```python
cargo1 = Cargo(volume=2, weight=500)
cargo2 = Cargo(volume=3, weight=700)

truck = Truck(payload=2000, volume_capacity=10, cargo_list=[])
truck.add_cargo(cargo1)
truck.add_cargo(cargo2)

print(truck.display_info())
```

## Output

```
Truck info:
Payload capacity: 2000
Volume capacity: 10 m3
Total weight: 1200, Total volume: 5
```

## Author

Created by Kateryna Babakova as part of her Python OOP learning path.