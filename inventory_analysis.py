"""
Inventory Management and Stock Optimization
Run: python inventory_analysis.py
Requirements: pandas, matplotlib
Input: sample_inventory.csv in the same folder
"""
import pandas as pd
import matplotlib.pyplot as plt

INPUT_FILE = "sample_inventory.csv"

def main():
    df = pd.read_csv(INPUT_FILE)

    # Basic validation and cleaning
    required = ["sku", "product", "current_stock", "avg_daily_demand",
                "lead_time_days", "target_stock", "safety_stock", "unit_cost"]
    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    numeric_cols = ["current_stock", "avg_daily_demand", "lead_time_days",
                    "target_stock", "safety_stock", "unit_cost"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=required).copy()
    df = df[(df[numeric_cols] >= 0).all(axis=1)].copy()

    # Reorder point = demand during lead time + safety stock
    df["reorder_point"] = (
        df["avg_daily_demand"] * df["lead_time_days"] + df["safety_stock"]
    )
    df["recommended_order_qty"] = (
        df["target_stock"] - df["current_stock"]
    ).clip(lower=0)
    df["stock_status"] = df.apply(
        lambda row: "Reorder"
        if row["current_stock"] <= row["reorder_point"]
        else "Sufficient",
        axis=1,
    )
    df["inventory_value"] = df["current_stock"] * df["unit_cost"]

    print("\nInventory Analysis Summary")
    print("--------------------------")
    print(f"Products analysed: {len(df)}")
    print(f"Total units in stock: {df['current_stock'].sum():.0f}")
    print(f"Total inventory value: {df['inventory_value'].sum():.2f}")
    print(f"Products at/below reorder point: {(df['stock_status'] == 'Reorder').sum()}")

    columns = ["sku", "product", "current_stock", "reorder_point",
               "recommended_order_qty", "stock_status", "inventory_value"]
    print("\nProduct-level recommendations:")
    print(df[columns].to_string(index=False))

    df.to_csv("inventory_analysis_output.csv", index=False)
    print("\nSaved results to inventory_analysis_output.csv")

    # Visualise stock status
    counts = df["stock_status"].value_counts()
    counts.plot(kind="bar", title="Inventory Reorder Assessment")
    plt.xlabel("Stock status")
    plt.ylabel("Number of products")
    plt.tight_layout()
    plt.savefig("reorder_assessment.png", dpi=160)
    plt.show()

if __name__ == "__main__":
    main()
