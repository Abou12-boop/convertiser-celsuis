
# 🌡️ Temperature Converter (Convertisseur de Température)

A simple Python command-line tool to convert Celsius temperatures to **Kelvin** or **Fahrenheit**.

---

## 📋 Description

This program takes a temperature in **Celsius** as input and converts it to either:
- 🔵 **Kelvin (K)**
- 🔴 **Fahrenheit (F)**

It also handles invalid inputs, such as temperatures below absolute zero.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your machine

### Run the program

```bash
python convertiser.py
```

---

## 🖥️ Usage

When you run the program, you will see:

```
welcom to the convertiser
KELVIN(k)
Fahrenheit (F)
Celsius(C)
enter the temperature in celsius: 100
choice 1=kelvin , 2=Fahrenheit: 1
convertion of 100.0°C celsius to kelvin 373.15
```

### Conversion options

| Choice | Conversion |
|--------|------------|
| `1`    | Celsius → Kelvin |
| `2`    | Celsius → Fahrenheit |

---

## 🔢 Formulas Used

| Conversion | Formula |
|------------|---------|
| Celsius → Kelvin | `K = °C + 273.15` |
| Celsius → Fahrenheit | `°F = (°C × 1.8) + 32` |

---

## ⚠️ Error Handling

- If the temperature entered is **below -273.15°C** (absolute zero), the program prints `"impossible"`.
- If the choice is **not 1 or 2**, the program asks to choose a valid option.

---

## 📁 Project Structure

```
📦 temperature-converter
 ┗ 📜 convertiser.py
 ┗ 📜 README.md
```

---

## 🛠️ Possible Improvements

- [ ] Add support for more unit conversions (Rankine, Réaumur...)
- [ ] Build a graphical interface (GUI) with Tkinter
- [ ] Add input validation to handle non-numeric entries
- [ ] Support converting from Kelvin or Fahrenheit as input

---

## 👤 Author

> Made with ❤️ and Python

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
