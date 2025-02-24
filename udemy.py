import streamlit as st
import pandas as pd
import pickle

# Load Model
with open("udemy_rf_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🎓 Udemy Course Enrollment Prediction")
st.write("📌 Enter course details to predict enrollments.")

# User Inputs
price = st.slider("💲 Course Price ($)", 0, 500, 50)
num_reviews = st.slider("⭐ Number of Reviews", 0, 5000, 100)
content_duration = st.slider("⏳ Course Duration (Hours)", 0, 100, 10)
level = st.selectbox("📖 Course Level", ["Beginner", "Intermediate", "Advanced"])
is_paid = st.selectbox("📚 Course Category", ["Programming", "Data Science", "AI & ML"])

# Convert Inputs
level_dict = {"Beginner": 0, "Intermediate": 1, "Advanced": 2}
category_dict = {"Programming": 0, "Data Science": 1, "AI & ML": 2}

input_data = pd.DataFrame({
    "price": [price],
    "num_reviews": [num_reviews],
    "content_duration": [content_duration],
    "level": [level_dict[level]],
    "is_paid": [category_dict[is_paid]]
})

if st.button("🔮 Predict Enrollments"):
    prediction = model.predict(input_data)
    st.metric("📈 Predicted Enrollments", f"{int(prediction[0]):,}")
