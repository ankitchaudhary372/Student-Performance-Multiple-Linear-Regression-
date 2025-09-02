import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# Load the trained model
model = joblib.load("performance_model.pkl")

# ----------------- Streamlit Dashboard -----------------
st.set_page_config(page_title="Student Performance Predictor", layout="wide")

# Title and description
st.title("🎓 Student Performance Prediction Dashboard")
st.markdown("""
Predict a student's **Performance Index** based on study habits, previous scores, 
and the number of sample question papers practiced.
""")

# Sidebar for inputs
st.sidebar.header("Student Input Parameters")

hours_studied = st.sidebar.slider("Hours Studied", 0, 12, 5)
previous_scores = st.sidebar.slider("Previous Scores", 0, 100, 50)
sample_papers = st.sidebar.slider("Sample Question Papers Practiced", 0, 10, 3)

# Create DataFrame from input
input_data = pd.DataFrame([[hours_studied, previous_scores, sample_papers]],
                          columns=['Hours Studied', 'Previous Scores', 'Sample Question Papers Practiced'])

# Predict button
if st.button("Predict Performance"):
    prediction = model.predict(input_data)
    st.success(f"✅ Predicted Performance Index: **{prediction[0]:.2f}**")

    # ----------------- Feature Importance Chart -----------------
    features = ['Hours Studied', 'Previous Scores', 'Sample Papers']
    coefficients = model.coef_

    fig, ax = plt.subplots(figsize=(7,4))
    bars = ax.bar(features, coefficients, color='skyblue')
    ax.set_title("Feature Importance (Coefficient Values)", fontsize=14)
    ax.set_ylabel("Coefficient Value")
    ax.set_ylim(min(coefficients)-1, max(coefficients)+1)

    # Add value labels on bars
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2.0, yval + 0.1, f'{yval:.2f}', ha='center', va='bottom')

    st.pyplot(fig)

    # ----------------- Model Accuracy with Range -----------------
    # Load training data (without sleep hours)
    data = {
        "Hours Studied": [7, 4, 8, 5, 7, 3, 7],
        "Previous Scores": [99, 82, 51, 52, 75, 78, 73],
        "Sample Question Papers Practiced": [1, 2, 2, 2, 5, 6, 6],
        "Performance Index": [91, 65, 45, 36, 66, 61, 63]
    }
    df = pd.DataFrame(data)
    X = df[['Hours Studied', 'Previous Scores', 'Sample Question Papers Practiced']]
    y = df['Performance Index']

    y_pred_full = model.predict(X)
    r2 = r2_score(y, y_pred_full)

    # Define ranges
    if r2 >= 0.8:
        range_label = "Good ✅"
        color = "green"
    elif r2 >= 0.5:
        range_label = "Average ⚠️"
        color = "orange"
    else:
        range_label = "Bad ❌"
        color = "red"

    st.markdown(f"📊 Model Accuracy (R² Score): **{r2:.2f}** - <span style='color:{color};'>{range_label}</span>", unsafe_allow_html=True)

# Optional: Show input summary
st.markdown("---")
st.subheader("Input Summary")
st.table(input_data)
