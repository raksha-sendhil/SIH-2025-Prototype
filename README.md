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
- Installation (if needed):
```bash
pip install pandas scikit-learn streamlit

## Branches
- main                → Stable branch for approved code
- data-management     → Data cleaning and preparation
- model-training      → ML model development and training
- prediction          → Generating predictions on new data
- ui                  → Basic, easy to learn front-end interface, uses basic python code, no HTML/CSS/JS needed

## Repo Structure

dropout-risk-predictor/
│
├── data/                     # Raw and processed datasets
│   ├── attendance.csv
│   └── scores.csv
│
├── data_management/          # Python scripts for cleaning and preparing data
│   └── clean_merge.py
│
├── model/                    # ML model training scripts
│   └── train_model.py
│
├── prediction/               # Scripts to generate predictions on new data
│   └── predict.py
│
├── ui/                       # Optional Streamlit UI
│   └── app.py
│
└── README.md                 # Project instructions, workflow, and team info

