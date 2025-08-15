import pandas as pd
import matplotlib.pyplot as plt

# === Load dataset ===
file_path = "API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv"
df = pd.read_csv(file_path, skiprows=4)

# === Choose parameters ===
year = input("Enter year (e.g., 2020): ")
country = input("Enter country name (e.g., India): ")

# === Plot 1: Histogram for population distribution in selected year ===
if year not in df.columns:
    print(f"Year {year} not found in dataset.")
else:
    pop_year = df[year].dropna()
    plt.figure(figsize=(8, 5))
    plt.hist(pop_year, bins=20, edgecolor='black')
    plt.title(f'Population Distribution Across Countries in {year}')
    plt.xlabel('Population')
    plt.ylabel('Number of Countries')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(f"population_distribution_{year}.png")  # Save chart as image
    plt.show()

# === Plot 2: Bar chart for population trend of selected country ===
if country not in df["Country Name"].values:
    print(f"Country '{country}' not found in dataset.")
else:
    country_data = df[df["Country Name"] == country].iloc[0, 4:-1]
    years = country_data.index
    population = country_data.values

    plt.figure(figsize=(10, 5))
    plt.bar(years, population, color='skyblue', edgecolor='black')
    plt.title(f'Population of {country} (1960-2024)')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(f"population_trend_{country}.png")  # Save chart as image
    plt.show()
