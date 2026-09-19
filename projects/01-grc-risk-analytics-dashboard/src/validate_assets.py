import pandas as pd
import csv

#load asset inventory
assets=pd.read_csv("data/assets.csv")

# Display first 5 assets
print(assets.head())

#Show number of assets
print("\nNumber of assets:")
print(len(assets))

#Show all column names
print("\nColumns:")
print(assets.columns.tolist())

print("\n--- DATA QUALITY CHECK ---")

#Check duplicate asset IDs
duplicates= assets[assets["asset_id"].duplicated()]
if duplicates.empty:
    print("PASS: No duplicate asset IDs found")
else:
    print("FAIL: Duplicate asset IDs found")
print(duplicates)

#Check missing assets owners
missing_owners = assets[assets["asset_owner"].isna()]
if missing_owners.empty:
    print("PASS: No assets are missing in asset owner.")
else:
    print("FAIL: assets with missing owners")
print(missing_owners)

#Check missing criticality
missing_criticality=assets[assets["business_criticality"].isna()]
if missing_criticality.empty:
    print("PASS:No invalid business criticality")
else:
    print("FAIL: Business crticality missing.")
print(missing_criticality)

valid_classifications = [

    "Public",
    "Internal",
    "Confidential",
    "Restricted"
]
invalid_classification = assets[
    ~assets["data_classification"].isin(valid_classifications)

    ]
print("\nInvalid Data Classification:")
print(invalid_classification)

overdue_dates=assets[assets["next_review_date"].isna()]
if overdue_dates.empty:
   