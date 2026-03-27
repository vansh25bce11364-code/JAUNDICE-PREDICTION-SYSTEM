# 🟡 Jaundice Prediction System

A machine learning-based command-line tool that predicts the likelihood of jaundice in a patient based on clinical symptoms and lab indicators using a **Random Forest Classifier**.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Input Parameters](#input-parameters)
- [Output](#output)
- [How It Works](#how-it-works)
- [Limitations](#limitations)
- [Disclaimer](#disclaimer)

---

## Overview

This project demonstrates the use of a supervised machine learning model to assist in early screening of jaundice. The system takes patient-reported symptoms and a basic lab indicator as input, then outputs a prediction along with a risk percentage.

> ⚠️ **This tool is for educational purposes only and must NOT be used as a substitute for professional medical diagnosis.**

---

## Features

- Simple command-line interface
- Trained on symptom-based patient data
- Provides binary prediction (Jaundice / No Jaundice)
- Outputs risk probability percentage
- Lists detected symptoms when jaundice is predicted

---

## Requirements

- Python 3.7+
- `pandas`
- `scikit-learn`
- `numpy`

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/jaundice-prediction.git
cd jaundice-prediction
```

2. **Install dependencies:**

```bash
pip install pandas scikit-learn numpy
```

---

## Usage

Run the script directly from your terminal:

```bash
python jaundice_prediction.py
```

You will be prompted to enter patient details one by one.

---

## Input Parameters

| Parameter | Description | Values |
|---|---|---|
| `bilirubin` | High bilirubin level in blood | 0 = No, 1 = Yes |
| `yellow_eyes` | Yellowing of the eyes (scleral icterus) | 0 = No, 1 = Yes |
| `yellow_skin` | Yellowing of the skin | 0 = No, 1 = Yes |
| `age` | Patient's age | Integer (years) |
| `dark_urine` | Presence of dark-coloured urine | 0 = No, 1 = Yes |
| `fatigue` | Fatigue or general weakness | 0 = No, 1 = Yes |
| `abdominal_pain` | Abdominal pain or discomfort | 0 = No, 1 = Yes |

---

## Output

**If jaundice is detected:**
```
PREDICTION RESULT:
JAUNDICE DETECTED!
Risk: 85%

Common symptoms found:
- Yellow eyes
- Yellow skin
- High bilirubin
- Dark urine

Please consult a doctor immediately!
```

**If no jaundice is detected:**
```
PREDICTION RESULT:
NO JAUNDICE DETECTED
Risk: 10%

Patient appears healthy
Continue regular health checkups
```

---

## How It Works

1. **Training Data** — A small dataset of 15 labeled patient records is built in-memory, each with 7 clinical features and a jaundice label (0 or 1).

2. **Model** — A `RandomForestClassifier` with 10 decision trees is trained on this data. Each tree learns patterns from the features; the final prediction is decided by majority vote.

3. **Prediction** — User-provided inputs are passed to the trained model, which returns:
   - A class label (`0` or `1`)
   - A probability score used as the "risk percentage"

4. **Output** — The result and any matching symptoms are displayed in a readable format.

---

## Limitations

| Limitation | Detail |
|---|---|
| Small dataset | Only 15 training samples — insufficient for real-world reliability |
| Binary features | Bilirubin is treated as 0/1 instead of a continuous mg/dL value |
| No validation | No train/test split or cross-validation is performed |
| Not clinically validated | The model has not been tested against real patient data |

---

## Disclaimer

This project is intended **solely for educational and demonstration purposes**. It does not constitute medical advice. Always consult a qualified healthcare professional for diagnosis and treatment.

---

## License

This project is open-source and available under the [MIT License](LICENSE).
