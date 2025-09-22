import pandas as pd
import numpy as np
import joblib



def ensure_columns(df, required_cols):
    for col in required_cols:
        if col not in df.columns:
            df[col] = np.nan
    return df[required_cols]



def data_transformation(test,attendance,fee_payment):
    attendance_cols = [f'course{i}_attendance_pct' for i in range(1, 7)]
    see_total = [f'c{i}_see_total' for i in range(1, 7)]
    cie_total = [f'c{i}_cie_total' for i in range(1, 7)]
    aggregate = [f'c{i}_aggregate' for i in range(1, 7)]
    test_new = ensure_columns(test, see_total + cie_total + aggregate)
    attendance_new = ensure_columns(attendance, attendance_cols)
    fee_payment_new = ensure_columns(fee_payment, ['percent_paid', 'installments_missed'])
    clean_data = pd.concat([test_new, attendance_new, fee_payment_new], axis=1)
    #fill the NaN values with mean
    numeric_cols = clean_data.columns.difference(['percent_paid', 'installments_missed'])
    row_means = clean_data[numeric_cols].mean(axis=1)
    for col in numeric_cols:
        clean_data[col] = clean_data[col].fillna(row_means)
    clean_data.rename( columns={'percent_paid':'percent_paid_y'}, inplace=True)
    st_id=fee_payment['student_id']
    return clean_data, st_id
