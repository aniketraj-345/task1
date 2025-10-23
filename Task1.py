# --- STEP 1: Upload CSV file ---
from google.colab import files
import io
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set a modern visual style
sns.set(style="whitegrid", palette="muted", font_scale=1.2)

# Upload file
uploaded = files.upload()

# Get the uploaded file name
for fn in uploaded.keys():
    file_name = fn

# Read CSV (World Bank format)
data = pd.read_csv(io.BytesIO(uploaded[file_name]), skiprows=4)

print("✅ File uploaded successfully!\n")
print("📊 Preview of data:")
print(data.head())

# --- STEP 2: Choose a year for histogram ---
year = "2020"  # You can change this

# Drop rows with missing data
year_data = data[["Country Name", year]].dropna()

# --- STEP 3: Histogram ---
plt.figure(figsize=(12, 7))
sns.histplot(year_data[year] / 1e6, bins=25, color="#5dade2", edgecolor='black', kde=True)
plt.title(f"World Population Distribution in {year}", fontsize=18, fontweight='bold', pad=15)
plt.xlabel("Population (in Millions)", fontsize=14)
plt.ylabel("Number of Countries", fontsize=14)
plt.xticks(rotation=0)
plt.grid(visible=True, linestyle='--', alpha=0.4)
plt.show()

# --- STEP 4: Line Graph for Selected Countries ---
countries = ["India", "China", "United States", "Brazil", "Nigeria"]
subset = data[data["Country Name"].isin(countries)]
years = [str(y) for y in range(1960, 2025)]

plt.figure(figsize=(14, 8))
for _, row in subset.iterrows():
    plt.plot(years, row[years].astype(float) / 1e6, linewidth=2.5, label=row["Country Name"])

plt.title("Population Growth (1960–2024)", fontsize=18, fontweight='bold', pad=15)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Population (in Millions)", fontsize=14)
plt.legend(title="Countries", fontsize=12)
plt.grid(visible=True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()