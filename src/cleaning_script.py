import pandas as pd
from pathlib import Path

INPUT = Path("../data/raw/raw_data.txt")
OUTPUT = Path("../data/processed/cleaned_data.csv")

def main():
    if not INPUT.exists():
        raise FileNotFoundError(f"Raw file not found: {INPUT.resolve()}")

    records = []
    with INPUT.open("r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) != 7:
                continue
            _, drink, price, branch, payment, _, date = parts
            price_num = float(price.replace("£", ""))
            records.append({
                "Drink": drink,
                "Price": price_num,
                "Branch": branch,
                "PaymentType": payment,
                "Date": pd.to_datetime(date, dayfirst=True, errors="coerce")
            })

    df = pd.DataFrame(records).dropna()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT, index=False)
    print(f"✅ Saved cleaned file: {OUTPUT}")

if __name__ == "__main__":
    main()
