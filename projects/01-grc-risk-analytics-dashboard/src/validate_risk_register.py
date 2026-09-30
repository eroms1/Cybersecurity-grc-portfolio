import pandas as pd

#data validation checks 
risks =pd.read_csv("data/risk_register.csv")

print(risks.head())
print('\nNumber of risks:')
print(len(risks))

print ("\nColumns:")
print(risks.columns.tolist())

print ("n---RISK REGOSTER DATA QUALITY CHECK---")

#Check Duplicates
duplicates= risks[risks["risk_id"].duplicated()]
if duplicates.empty:
    print("PASS:No duplicate risk IDs found")
else:
    print("FAIL:Duplicate risk IDs found.")
    print(duplicates)

#Check missing risk owners
missing_owners = risks[risks["risk_owner"].isna()]

if missing_owners.empty:
    print("PASS: No risks are missing a risk owner.")
else:
    print("FAIL: Risks with missing risk owners found.")
    print(missing_owners)

#check Inherent liklihood and impact values
valid_scores = [1,2,3,4,5]
invalid_inherent_likelihood = risks[~risks["inherent_likelihood"].isin(valid_scores)
                                    ]
if invalid_inherent_likelihood.empty:
    print("PASS: All inherent likelihood values are valid.")
else:
    print("FAIL: Invalid inherent likelihood values found.")
    print(invalid_inherent_likelihood)

invalid_inherent_impact = risks[~risks["inherent_impact"].isin(valid_scores)
                                 ]
if invalid_inherent_impact.empty:
    print("PASS:All inherent impact values found.")
else:
    print("FAIL:Invalid inherent impact values found.")
    print(invalid_inherent_impact)

#check Residual liklihood and impact values
invalid_residual_likelihood = risks[~risks["residual_likelihood"].isin(valid_scores)
                                    ]
if invalid_residual_likelihood.empty:
    print("PASS: All residual likelihood values are valid.")
else:
    print("FAIL: Invalid residual likelihood values found.")
    print(invalid_residual_likelihood)

invalid_residual_impact = risks[~risks["residual_impact"].isin(valid_scores)
                                    ]
if invalid_residual_impact.empty:
    print("PASS: All residual impact values are valid.")
else:
    print("FAIL: Invalid residual impact values found.")
    print(invalid_residual_impact)

#check Risk Response
valid_response = ["Mitigate", "Accept", "Avoid", "Transfre"]

invalid_responses = risks[~risks['risk_response'].isin (valid_response)
                         ]
if invalid_responses.empty:
    print("PASS: All risk response value are valid.")
else:
    print("FAIL: Invalid risk response values found.")
    print(invalid_responses)

#check Risk Status
valid_risk_statuses = ["Open", "Closed", "In progress", "Under review"]
invalid_risk_statuses = risks[~risks["risk_status"].isin(valid_risk_statuses)
                              ]
if invalid_risk_statuses.empty:
    print("PASS:All risk status values are valid.")
else:
    print("FAIL: Invalid risk status values found.")
    print(invalid_risk_statuses)

#check Risk Treatment
valid_treatment_statuses = ["Not Started",
                        "Completed", 
                        "On Hold", 
                        "In Progress"
                        ]
invalid_treatment_statuses = risks[~risks["treatment_status"].isin(valid_treatment_statuses)
                              ]
if invalid_treatment_statuses.empty:
    print("PASS:All treatment status values are valid.")
else:
    print("FAIL: Invalid treatment status values found.")
    print(invalid_treatment_statuses)

#CROSS-CHECK BETWEEN RISK REGISTER & ASSET CSV
#Load asset inventory
assets= pd.read_csv("data/assets.csv")

#Clean asset IDs in both datasets
assets["asset_id"] = assets["asset_id"].astype("string").str.strip()
risks["asset_id"] = risks["asset_id"].astype("string"). str.strip()

#Treat "-" and blank values as no asset assigned
risks['asset_id']= risks["asset_id"].replace({
    "-": pd.NA,
    "": pd.NA
})

#Create a list of valid asset IDs
valid_asset_ids = assets["asset_id"].dropna().tolist()

#Only check risks that actually reference an asset
risk_with_assets = risks[
    risks["asset_id"].notna()
    & (risks["asset_id"] != "_")
]
#Find asset IDs in the risk register that do not exist in assets.csv
invalid_asset_ids = risk_with_assets[
    ~risk_with_assets["asset_id"].isin(valid_asset_ids)
]
if invalid_asset_ids.empty:
    print("PASS: All references asset IDs exist in the asset inventory.")
else:
    print("FAIL: Invalid asset refrences found.")
    print(invalid_asset_ids[["risk_id", "asset_id"]])