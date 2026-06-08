import os
import sys

# Ensure imports resolve correctly when run from any working directory
sys.path.insert(0, os.path.dirname(__file__))


from main import *

df = load_data("sales.csv")

print("\n--- Head ---")
print(df.head())

print("\n--- Quality Report ---")
print(data_quality_report(df))

print("\n--- Dataset Summary ---")
print(dataset_summary(df))