
import csv
import re
from pathlib import Path

# Locate the project folders
project_dir = Path(__file__).parent
input_file = project_dir / "data" / "orders_enriched.csv"
output_file = project_dir / "data" / "orders_clean.csv"

def clean_name(value):
    """Trim extra spaces and standardize name capitalization."""
    value = value.strip()
    return value.title() if value else value

with input_file.open("r", newline="", encoding="utf-8-sig") as source:
    reader = csv.DictReader(source)

    if not reader.fieldnames:
        raise ValueError("The input CSV has no header row.")

    rows = list(reader)
    headers = reader.fieldnames

    required = {
        "first_name", "last_name", "amount"
    }
    if not required.issubset(headers):
        raise ValueError(
            f"Expected columns {sorted(required)}. Found: {headers}"
        )

    for row in rows:
        row["first_name"] = clean_name(row["first_name"])
        row["last_name"] = clean_name(row["last_name"])

        # Keep missing amounts blank; do not replace them with zero.
        if row["amount"].strip().lower() == "null":
            row["amount"] = ""

with output_file.open("w", newline="", encoding="utf-8") as destination:
    writer = csv.DictWriter(destination, fieldnames=headers)
    writer.writeheader()
    writer.writerows(rows)

print(f"Cleaned {len(rows)} orders.")
print(f"Saved file: {output_file}")
