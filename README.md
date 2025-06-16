## 🚚 Truck Cargo Manager

A simple logistics-style project written in Python using Object-Oriented Programming (OOP).

## 🧠 Why I Built This

A compact project to test how OOP can model systems with rules, limits, and edge cases — beyond just storing data.

## 🔧 Features
- Add and remove cargo
- Calculate total load 
- Prevent overloads 
- Display detailed truck status

## 🧱 Tech & Concepts
- Python OOP (multiple classes, encapsulation, instance validation)
- Input simulation for cargo weights and dimensions
- Error handling with ValueError and custom safeguards
- Formatted output to track and display state clearly
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

## 👩‍💻 Author

Created by Kateryna Babakova (https://github.com/katebabakova444)
This project is part of my backend development journey.
View my full portfolio: kateryna-portfolio (https://github.com/katebabakova444/kateryna-portfolio)