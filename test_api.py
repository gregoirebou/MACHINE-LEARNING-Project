import requests
import json

# URL of local Docker API
url = 'http://127.0.0.1:5000/predict'

# ----------------------------------------------------
# TEST CASE 1: "High Risk" Patient
# (GenHlth=5 (Poor), HighBP=1, DiffWalk=1, Age=9 (60-64 yrs))
# ----------------------------------------------------
high_risk_patient = {
    "features": [
        1.0,  # HighBP (Yes)
        1.0,  # HighChol (Yes)
        1.0,  # CholCheck (Yes)
        30.0, # BMI (Obese)
        1.0,  # Smoker (Yes)
        0.0,  # Stroke (No)
        1.0,  # HeartDiseaseorAttack (Yes)
        0.0,  # PhysActivity (No)
        0.0,  # Fruits (No)
        0.0,  # Veggies (No)
        1.0,  # HvyAlcoholConsump (Yes)
        1.0,  # AnyHealthcare (Yes)
        0.0,  # NoDocbcCost (No)
        5.0,  # GenHlth (5 = Very Poor)
        15.0, # MentHlth (15 days)
        15.0, # PhysHlth (15 days)
        1.0,  # DiffWalk (Yes)
        0.0,  # Sex (Female)
        9.0,  # Age (Category 9)
        4.0,  # Education (Level 4)
        5.0   # Income (Level 5)
    ]
}

# Send the request
response = requests.post(url, json=high_risk_patient)
print(f"--- High Risk Patient ---")
print(f"Response: {response.json()}")


# ----------------------------------------------------
# TEST CASE 2: "Low Risk" Patient
# (GenHlth=1 (Excellent), HighBP=0, DiffWalk=0, Age=4 (35-39 yrs))
# ----------------------------------------------------
low_risk_patient = {
    "features": [
        0.0,  # HighBP (No)
        0.0,  # HighChol (No)
        1.0,  # CholCheck (Yes)
        22.0, # BMI (Normal)
        0.0,  # Smoker (No)
        0.0,  # Stroke (No)
        0.0,  # HeartDiseaseorAttack (No)
        1.0,  # PhysActivity (Yes)
        1.0,  # Fruits (Yes)
        1.0,  # Veggies (Yes)
        0.0,  # HvyAlcoholConsump (No)
        1.0,  # AnyHealthcare (Yes)
        0.0,  # NoDocbcCost (No)
        1.0,  # GenHlth (1 = Excellent)
        0.0,  # MentHlth (0 days)
        0.0,  # PhysHlth (0 days)
        0.0,  # DiffWalk (No)
        1.0,  # Sex (Male)
        4.0,  # Age (Category 4)
        6.0,  # Education (Level 6)
        8.0   # Income (Level 8)
    ]
}

# Send the request
response = requests.post(url, json=low_risk_patient)
print(f"\n--- Low Risk Patient ---")
print(f"Response: {response.json()}")