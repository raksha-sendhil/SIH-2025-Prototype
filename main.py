import streamlit as s
import pandas as pd
import joblib as j
import data_management.data_transformation as dt
import prediction.prediction as pr
import openpyxl

#USER INTERFACE
s.title("Dropout Prediction System")
s.text("This is a simple dropout prediction system using Streamlit.")
s.markdown("### Input Student details:")


s.markdown("### Attendance details:")
attendance = s.file_uploader("Upload Excel files", type=["xlsx", "xls"],key="attendance")
s.markdown("### Academic Performance details:")
academics_file = s.file_uploader("Upload Excel files", type=["xlsx", "xls"],key="academics")
s.markdown("### Fee Payment details:")
fee_file = s.file_uploader("Upload Excel files", type=["xlsx", "xls"],key="fee")

if attendance and academics_file and fee_file:
    test=pd.read_excel(academics_file)
    attendance=pd.read_excel(attendance)
    fee_payment=pd.read_excel(fee_file)


    clean_data, st_id = dt.data_transformation(test, attendance, fee_payment)


    df=pr.dropout_predictor(clean_data, st_id)


    s.markdown("### Prediction Results:")

    def color_rows(row):
        if row['risk_zone'].lower() == 'high':
            return ['background-color: #d36259; color: black'] * len(row)   # light red
        elif row['risk_zone'].lower() == 'medium':
            return ['background-color: #efd68e; color: black'] * len(row)   # light yellow
        elif row['risk_zone'].lower() == 'low':
            return ['background-color: #b1e79a; color: black'] * len(row)   # light green
        else:
            return [''] * len(row)

    s.dataframe(df.style.apply(color_rows, axis=1)) 