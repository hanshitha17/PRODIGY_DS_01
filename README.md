# PRODIGY_DS_01

# 📊 Population Visualization Project

This project visualizes **global population data** using Python.  
It can:
- Show a **histogram** of population distribution across all countries for a given year.
- Show a **bar chart** of population growth for a specific country from 1960 to 2024.

---

## 📂 Project Structure
```

PRODIGY\_DS\_01/
│-- API\_SP.POP.TOTL\_DS2\_en\_csv\_v2\_38144.csv   # Dataset (World Bank)
│-- main.py                                   # Main Python script
│-- requirements.txt                          # Python dependencies
│-- .gitignore                                # Ignored files
└── README.md                                 # Project documentation

````

---

## 📊 Dataset
- **Source:** [World Bank - Population, total](https://data.worldbank.org/indicator/SP.POP.TOTL)  
- Contains total population data for **countries from 1960 to 2024**.

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/PRODIGY_DS_01.git
cd PRODIGY_DS_01
````

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the script from **VS Code terminal** or any command line:

```bash
python main.py
```

You will be prompted to enter:

* A **year** (e.g., `2020`)
* A **country name** (e.g., `India`)

---

## 📈 Output

The script will:

1. Display a **histogram** of population distribution for the selected year.
2. Display a **bar chart** showing population growth for the selected country.
3. Save both charts locally as `.png` files (ignored in GitHub via `.gitignore`).

---

## 🛠 Requirements

* Python 3.x
* pandas
* matplotlib

---

## 📌 Example Workflow

```bash
Enter year (e.g., 2020): 2020
Enter country name (e.g., India): India
```

✔ Histogram of 2020 populations displayed
✔ Bar chart of India's population growth displayed
✔ Both charts saved locally

---
