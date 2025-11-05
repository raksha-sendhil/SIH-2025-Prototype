# SIH 2025: AI-based Dropout Prediction and Counseling System

## Overview
This repository contains the **basic prototype** of our Smart India Hackathon project.  
The core functionality focuses on **predicting dropout risk** for students based on attendance and test scores.  

**Main Prototype Features:**
- Input: Attendance and test scores (CSV or structured format)
- Output: Risk category for each student (High / Medium / Low)
- Prediction accuracy display
- Color-coded risk display (optional UI)

---

## Tech Stack / Requirements
- **Python 3**
- Libraries:
  - `pandas` → data manipulation
  - `scikit-learn` → machine learning model
  - `streamlit` → optional UI (minimal, to show predictions)


## Branches
- main                → Stable branch for approved code
- data-management     → Data cleaning and preparation
- model-training      → ML model development and training
- prediction          → Generating predictions on new data

##Repo Structure
```bash
SIH-2025_Prototype/

├── data_management/          # Python scripts for cleaning and preparing data
│   └── data_transformation.py
│
├── model_training/           # ML model training scripts
│   └── model_training.py
│
├── prediction/               # Scripts to generate predictions on new data
│   └── prediction.py
│
└── README.md                 # Project information, workflow, instructions
│
└── requirements.txt          # Has the requirements (libraries and tools) to be installed
│
└── main.py                   # The master code file, which calls the other modules and functions in it
            

```
