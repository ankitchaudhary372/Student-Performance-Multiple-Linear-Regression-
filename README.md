# 📊 Student Performance Prediction App

A **Streamlit-based Machine Learning Web App** that predicts a student's **Performance Index** based on their study habits, previous scores, and the number of sample papers practiced.

This project uses **Linear Regression** for prediction and provides an **interactive dashboard** for users to input data and see their performance predictions instantly.

---

## 🚀 Features
- ✅ Simple and interactive **Streamlit dashboard**
- ✅ Predicts **Performance Index** based on student data
- ✅ Displays **model accuracy** with status badges (**Good / Average / Poor**)
- ✅ Uses **Linear Regression** for prediction
- ✅ Lightweight & easy to deploy

---

## 📂 Dataset Columns
| Feature                               | Description                            |
|-------------------------------------|--------------------------------------|
| **Hours Studied**                   | Total hours studied per day          |
| **Previous Scores**                | Previous exam percentage score      |
| **Sample Question Papers Practiced** | Number of sample papers solved     |
| **Performance Index** *(Target)*   | Predicted overall performance score |

---

## 🧠 Machine Learning Model
We trained a **Linear Regression model** using **scikit-learn** on the dataset.

### Steps Involved:
1. Data Preprocessing using **Pandas**
2. Splitting into **Train** and **Test** sets
3. Training a **Linear Regression** model
4. Calculating **R² score** and categorizing performance as:

| Accuracy Score | Status   |
|---------------|----------|
| **≥ 0.85**    | 🟢 Good |
| **0.70 – 0.85** | 🟡 Average |
| **< 0.70**    | 🔴 Poor |

The trained model is saved as **`performance_model.pkl`**.

---

## 🛠️ Tech Stack
- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **Joblib**
- **Matplotlib**
- **Streamlit**

---

## 📦 Installation

Clone this repository:
```bash
git clone https://github.com/your-username/student-performance-prediction.git
