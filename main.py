import pickle
import pandas as pd
import streamlit as st

st.title("🧠 Stroke Prediction")

with open("my_model.pkl", "rb") as f:
    model = pickle.load(f)

age = st.number_input("Age", min_value=1, max_value=120, step=1)

hypertension = st.selectbox("Hypertension", ["No", "Yes"])
hypertension = 0 if hypertension == "Yes" else 1

heart_disease = st.selectbox("Heart Disease", ["No", "Yes"])
heart_disease = 0 if heart_disease == "Yes" else 1

avg_glucose_level = st.number_input("Average Glucose Level", min_value=1, max_value=500, step=1)

bmi = st.number_input("Body Mass Index", min_value=1, max_value=60)

work_type = st.selectbox("Work Type", ["Never Worked Before", "Government Job", "Private Job", "Self-Employed"])
govt_job = 1 if work_type == "Government Job" else 0
never_worked = 1 if work_type == "Never Worked Before" else 0
private = 1 if work_type == "Private Job" else 0
self_employed = 1 if work_type == "Self-Employed" else 0

smoking_status = st.selectbox("Smoking History", ["Never Smoked Before", "Formerly Smoked", "Smoke"])
formerly_smoked = 1 if smoking_status == "Formerly Smoked" else 0
never_smoked = 1 if smoking_status == "Never Smoked Before" else 0
smokes = 1 if smoking_status == "Smoke" else 0


if st.button("Make Prediction"):
    input_data = pd.DataFrame([[age, hypertension, heart_disease, avg_glucose_level, bmi,
                                     govt_job, never_worked, private, self_employed,
                                     formerly_smoked, never_smoked, smokes]],
                              columns=["age", "hypertension", "heart_disease", "avg_glucose_level", "bmi",
                                       "work_type_Govt_job", "work_type_Never_worked", "work_type_Private", "work_type_Self-employed",
                                       "smoking_status_formerly smoked", "smoking_status_never smoked", "smoking_status_smokes"])
    proba = model.predict_proba(input_data)[0][1] * 100

    st.metric("Risk of Stroke", f"{proba:.2f}%")

    if proba < 20:
        st.success("Your risk of stroke is considered low. "
                   "Keep maintaining a healthy lifestyle — regular exercise, "
                   "balanced diet, and avoiding smoking will help you stay safe. "
                   "No urgent need to see a doctor, but regular check-ups are always a good idea ✅")
    elif proba < 50:
        st.warning("Your risk of stroke is moderate. "
                   "It is recommended to monitor your health more closely "
                   "and consider consulting a healthcare professional for advice. "
                   "Making improvements in your lifestyle, such as reducing salt intake, exercising more, "
                   "and managing stress, can significantly lower your risk. ⚠️")
    else:
        st.error("Your risk of stroke is high. It is strongly advised to visit a doctor as soon as possible "
                 "for a thorough check-up. Following medical recommendations, controlling blood pressure, "
                 "and improving your lifestyle are critical steps to reduce the risk of serious complications. ❗")

    st.write("Things you can do to lower your risks:")

    with st.expander("Your personalized health tips"):
        counter = 0
        if age > 50:
            st.write("🧓 Since you are over 50, it is important to monitor your health more regularly. "
                     "Even if your current risk is not high, age itself is a significant factor. "
                     "Consider scheduling regular check-ups, maintaining a balanced diet, and staying physically active"
                     " to reduce potential risks in the future.")
            counter += 1

        if heart_disease == 0:
            st.write("💔 Since you have a history of heart disease, "
                     "it is strongly advised to schedule regular check-ups with your doctor. "
                     "Following prescribed medication, maintaining a balanced diet, avoiding smoking, and staying "
                     "physically active (as recommended by your doctor) are important steps to reduce your risk.")
            counter += 1

        if hypertension == 0:
            st.write("🧬 Since you have hypertension, it is recommended to regularly monitor your blood pressure "
                     "and consult a healthcare professional for proper management. "
                     "Maintaining a healthy diet, reducing salt intake, and regular exercise can significantly "
                     "lower your risk of complications")
            counter += 1

        if bmi >= 25:
            st.write("🏃‍➡️ Since your BMI is above 25, it’s important to maintain a healthy lifestyle. "
                     "With balanced habits, it becomes much easier to keep your body in shape "
                     "and lower the risk of health problems.")
            counter += 1

        if smokes == 1 or formerly_smoked == 1:
            st.write("🫁 Whether you smoke now or have already quit, "
                     "every step you take toward caring for your lungs and heart "
                     "brings you closer to a healthier, stronger life.")

        if counter == 0:
            st.write("💪 Everything looks fine! Remember that consistent healthy habits are the best way "
                     "to keep your risks low.")

    st.write("✨ No matter who you are or where you live, your health is the foundation of everything.")
    st.write("🌱 Stay active, stay balanced — and you’ll always have the energy to be healthy, confident, and truly happy")