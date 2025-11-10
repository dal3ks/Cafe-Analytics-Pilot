import pandas as pd

# File paths
input_file = "raw_data.txt"
output_file = "cleaned_data.csv"

# Read the file
# Each line: Name Drink £Price Branch PaymentType CardNumber Date
data = []
with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) != 7:
            continue  # skip malformed lines
        name, drink, price, branch, payment, card, date = parts
        data.append({
            "Drink": drink,
            "Price": float(price.replace("£", "")),
            "Branch": branch,
            "PaymentType": payment,
            "Date": pd.to_datetime(date, dayfirst=True, errors="coerce")
        })

# Create DataFrame
df = pd.DataFrame(data)

# Drop rows with missing or invalid data
df = df.dropna(subset=["Drink", "Price", "Branch", "PaymentType", "Date"])

# Save cleaned data
df.to_csv(output_file, index=False)
print("✅ Cleaned data saved as:", output_file)
print("Total records:", len(df))