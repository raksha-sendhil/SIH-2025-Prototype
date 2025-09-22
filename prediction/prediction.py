import joblib
import pandas as pd





def dropout_predictor(new_data, st_id):
    loaded_model=joblib.load('dropout_DecisionTree_model.joblib')
    # Align columns with training order
    expected_cols = loaded_model.feature_names_in_
    new_data = new_data[expected_cols]
    predictions = loaded_model.predict(new_data)
    data={'risk_zone':predictions}
    final_df=pd.concat([st_id,pd.DataFrame(data)],axis=1)
    return final_df