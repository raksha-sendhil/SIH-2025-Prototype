import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.tree import DecisionTreeClassifier
import joblib
import os

# Get the directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Load dataset
test = pd.read_excel(os.path.join(BASE_DIR, "Academic_Performance.xlsx"))
attendance = pd.read_excel(os.path.join(BASE_DIR, "Attendance_Percentage.xlsx"))
fee_payment = pd.read_excel(os.path.join(BASE_DIR, "FeePayment_Status.xlsx"))

test_attendance=pd.merge(test,attendance,how='inner',on='student_id')
merged=pd.merge(test_attendance,fee_payment,how='inner',on='student_id')


# Names of required columns for model training
attendance_cols = [f'course{i}_attendance_pct' for i in range(1, 7)]
see_total = [f'c{i}_see_total' for i in range(1, 7)]
cie_total = [f'c{i}_cie_total' for i in range(1, 7)]
aggregate = [f'c{i}_aggregate' for i in range(1, 7)]




# Featured names and target model training dataframes
feature_cols =attendance_cols + see_total + cie_total + aggregate + ['percent_paid_y','installments_missed']
X = merged[feature_cols]
y = merged['dropout_risk_label']

# # Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train Decision Tree
dt_model = DecisionTreeClassifier(max_depth=8, random_state=42)
dt_model.fit(X_train, y_train)

# Predict and evaluate on test set
y_pred = dt_model.predict(X_test)
print("Decision Tree Classifier Performance:")
print(classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))

# Calculate probabilities for test set and assign risk zones
probs = dt_model.predict_proba(X_test)

# Get class labels from the model
class_labels = dt_model.classes_

# Convert predicted class probabilities into predicted class names (e.g., 'Low', 'Medium', 'High')
predicted_classes = dt_model.predict(X_test)  # Already done as y_pred

results_df = X_test.copy()
results_df['dropout_prediction'] = predicted_classes

def risk_zone(label):
    if label == 'High':
        return 'High Risk'
    elif label == 'Medium':
        return 'Medium Risk'
    else:
        return 'Low Risk'

# Allotting risk-zones
results_df['risk_zone'] = results_df['dropout_prediction'].apply(risk_zone)

# Re-attaching student IDs
results_df['student_id'] = merged.loc[X_test.index, 'student_id']
display_cols = ['student_id','dropout_prediction', 'risk_zone']
# Printing top 20 results
print(results_df[display_cols].head(20))




joblib.dump(dt_model,'dropout_DecisionTree_model.joblib')
