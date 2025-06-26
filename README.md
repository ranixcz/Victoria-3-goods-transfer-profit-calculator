# Victoria 3 Goods Transfer Profit Calculator

A simple Python-based calculator to predict the most profitable amount of goods to transfer between two markets in Victoria 3.  
Supports versions **1.9+**. Prestige goods are not included (yet).

---

## 📥 How to use

1. Download and install [Python](https://www.python.org/downloads/)
2. Optionally install an IDE like:
   - [PyCharm](https://www.jetbrains.com/pycharm/download/?section=windows)
   - [Visual Studio Code](https://code.visualstudio.com/download)
3. Clone or download this repository
4. Open `vic3_calculator.py` and run it

---

## 🛠️ Features

- Calculates **optimal export amount** based on input supply/demand data
- Supports input like `1.22`, `1,22`, or `1220`
- Simple CLI interface (command-line based)
- Designed for quick use while playing

---

## 📊 Input Example

```plaintext
Select goods: fish
Your market: Export: 1.22
Your market: Import: 942
Target market: Export: 554
Target market: Import: 677

```
## 📊 Output Example

```plaintext
Optimal export: 85.7 units
Maximum profit: 385.57
