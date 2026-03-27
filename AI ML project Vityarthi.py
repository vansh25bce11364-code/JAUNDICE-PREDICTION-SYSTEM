import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np
print("=============================")
print("    JAUNDICE PREDICTION")
print("=============================")
print()
# Create simple training data
def create_data():
    # Sample patient data: [bilirubin, yellow_eyes, yellow_skin, age, dark_urine, fatigue, abdominal_pain]
    # bilirubin: 0=normal, 1=high
    # yellow_eyes: 0=no, 1=yes
    # yellow_skin: 0=no, 1=yes
    # age: in years
    # dark_urine: 0=no, 1=yes
    # fatigue: 0=no, 1=yes
    # abdominal_pain: 0=no, 1=yes
    data = [
        [0, 0, 0, 25, 0, 0, 0, 0],  # No jaundice
        [1, 1, 1, 30, 1, 1, 1, 1],  # Jaundice
        [0, 0, 0, 40, 0, 0, 0, 0],  # No jaundice
        [1, 0, 0, 35, 0, 0, 0, 0],  # No jaundice
        [1, 1, 0, 28, 1, 1, 0, 1],  # Jaundice
        [0, 0, 0, 50, 0, 0, 0, 0],  # No jaundice
        [1, 1, 1, 45, 1, 1, 1, 1],  # Jaundice
        [0, 0, 0, 32, 0, 0, 0, 0],  # No jaundice
        [1, 0, 1, 29, 1, 0, 1, 1],  # Jaundice
        [0, 0, 0, 38, 0, 0, 0, 0],  # No jaundice
        [1, 1, 1, 33, 1, 1, 1, 1],  # Jaundice
        [0, 0, 0, 42, 0, 1, 0, 0],  # No jaundice
        [1, 0, 0, 27, 0, 0, 0, 0],  # No jaundice
        [0, 0, 0, 55, 0, 0, 0, 0],  # No jaundice
        [1, 1, 1, 36, 1, 1, 1, 1],  # Jaundice
    ]
    return data
# Train the AI model
data = create_data()
# Convert to arrays
X = []  # Features
y = []  # Target (jaundice: 0=no, 1=yes)
for patient in data:
    X.append(patient[:7])  # First 7 are features
    y.append(patient[7])   # Last one is target
# Create and train model
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X, y)
# Get user input
print("Enter patient details:")
print()
bilirubin = int(input("High bilirubin level? (0=no, 1=yes): "))
yellow_eyes = int(input("Yellow eyes? (0=no, 1=yes): "))
yellow_skin = int(input("Yellow skin? (0=no, 1=yes): "))
age = int(input("Age: "))
dark_urine = int(input("Dark urine? (0=no, 1=yes): "))
fatigue = int(input("Fatigue or weakness? (0=no, 1=yes): "))
abdominal_pain = int(input("Abdominal pain? (0=no, 1=yes): "))
# Make prediction
patient_data = [[bilirubin, yellow_eyes, yellow_skin, age, dark_urine, fatigue, abdominal_pain]]
prediction = model.predict(patient_data)[0]
probability = model.predict_proba(patient_data)[0]
print()
print("PREDICTION RESULT:")
if prediction == 1:
    risk = probability[1] * 100
    print(f"JAUNDICE DETECTED!")
    print(f"Risk: {risk:.0f}%")
    print()
    print("Common symptoms found:")
    if yellow_eyes == 1:
        print("- Yellow eyes")
    if yellow_skin == 1:
        print("- Yellow skin")
    if bilirubin == 1:
        print("- High bilirubin")
    if dark_urine == 1:
        print("- Dark urine")
    print()
    print("Please consult a doctor immediately!")
else:
    risk = probability[1] * 100
    print(f"NO JAUNDICE DETECTED")
    print(f"Risk: {risk:.0f}%")
    print()
    print("Patient appears healthy")
    print("Continue regular health checkups")
print()
print("Always consult a real doctor for diagnosis.")
