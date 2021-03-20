import csv
from pathlib import Path

base_path = Path(__file__).parent
file_path = (base_path / "../data/third_party_sales_1.csv").resolve()

with open(file_path) as f:
    sales = [line for line in csv.reader(f)]
