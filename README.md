# Inventory Management and Stock Optimization

A small Python project for a Logistics Data Analyst internship task.

## Files
- `sample_inventory.csv` — illustrative sample inventory dataset (not real company data)
- `inventory_analysis.py` — data cleaning, reorder-point calculation, order quantity recommendation, and summary output
- `current_stock_chart.png`, `reorder_assessment_chart.png`, `inventory_value_chart.png` — charts used in the report
- `README.md` — project instructions

## Requirements
Python 3.9+ recommended. Install dependencies:
```bash
pip install pandas matplotlib
```

## Run
Place the CSV and script in the same folder, then run:
```bash
python inventory_analysis.py
```

The script creates `inventory_analysis_output.csv` and `reorder_assessment.png`.

## Logic
- Reorder point = average daily demand × supplier lead time + safety stock
- Recommended order quantity = max(target stock − current stock, 0)
- Products at or below their reorder point are flagged for review/reordering.

## Important note
The dataset is synthetic and for learning/demo purposes only. Replace it with authorised business data before using results for real decisions. The reorder calculation is a simplified planning aid; actual ordering should consider pack sizes, expiry dates, supplier minimums, demand variability, and budget constraints.
