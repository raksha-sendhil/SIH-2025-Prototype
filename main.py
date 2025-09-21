import streamlit as s
import pandas as pd
import joblib as j


#USER INTERFACE
s.title("Droput Prediction System")
s.text("This is a simple dropout prediction system using Streamlit.")
s.markdown("### Input Student details:")


s.markdown("### Attendance details:")
attendance_file = s.file_uploader("Upload Excel files", type=["xlsx", "xls"],key="attendance")
s.markdown("### Academic Performance details:")
academics_file = s.file_uploader("Upload Excel files", type=["xlsx", "xls"],key="academics")
s.markdown("### Fee Payment details:")
fee_file = s.file_uploader("Upload Excel files", type=["xlsx", "xls"],key="fee")


#function that takes in files and runs model, returns an excel file named prediction


if attendance_file and academics_file and fee_file:
    prediction=function(attendance_file,academics_file,fee_file)
    df=pd.read_excel(prediction)

    s.markdown("### Prediction Results:")

    def color_rows(row):
        if row['risk_zone'].lower() == 'high':
            return ['background-color: #d36259'] * len(row)   # light red
        elif row['risk_zone'].lower() == 'medium':
            return ['background-color: #efd68e'] * len(row)   # light yellow
        elif row['risk_zone'].lower() == 'low':
            return ['background-color: #b1e79a'] * len(row)   # light green
        else:
            return [''] * len(row)

    s.dataframe(df.style.apply(color_rows, axis=1)) 
