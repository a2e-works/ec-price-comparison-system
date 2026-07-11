"""
EC Price Comparison System (Portfolio Demo)

This is a simplified demonstration of the original workflow.
The production version includes API integration, error handling,
and business-specific logic which are not included in this repository.
"""

import pandas as pd


# ----------------------------------
# Sample Price Lookup
# ----------------------------------

def get_amazon_price(jan):
    sample = {
        "490000000001": 3980,
        "490000000002": 2980,
        "490000000003": 4580,
    }
    return sample.get(jan)


def get_rakuten_price(jan):
    sample = {
        "490000000001": 3180,
        "490000000002": 2680,
        "490000000003": 3980,
    }
    return sample.get(jan)


def get_yahoo_price(jan):
    sample = {
        "490000000001": 3280,
        "490000000002": 2590,
        "490000000003": 4050,
    }
    return sample.get(jan)


# ----------------------------------
# Profit Calculation
# ----------------------------------

def calculate_profit_rate(sell_price, buy_price):

    if buy_price == 0:
        return 0

    return round(((sell_price - buy_price) / buy_price) * 100, 1)


# ----------------------------------
# Main Process
# ----------------------------------

print("[Python] Loading sample CSV...")

df = pd.read_csv("../sample/sample_input.csv", dtype=str)

print(f"[Python] {len(df)} products loaded.")
print()

results = []

print("[Python] Retrieving marketplace prices...")

for _, row in df.iterrows():

    jan = row["JAN"]
    print(f"  Processing JAN: {jan}")

    amazon = get_amazon_price(jan)
    rakuten = get_rakuten_price(jan)
    yahoo = get_yahoo_price(jan)

    if amazon is None:
        continue

    cheapest = min(rakuten, yahoo)

    profit = calculate_profit_rate(
        amazon,
        cheapest
    )

    results.append({

        "JAN": jan,
        "Amazon": amazon,
        "Rakuten": rakuten,
        "Yahoo": yahoo,
        "Purchase Price": cheapest,
        "Profit Rate (%)": profit

    })


output = pd.DataFrame(results)

print()
print("[Python] Writing Excel report...")

output.to_excel(
    "../sample/sample_output.xlsx",
    index=False
)

print("[Python] Completed successfully!")
print("[Python] Output: sample/sample_output.xlsx")

