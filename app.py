import streamlit as st
from transformers import pipeline

# Load a Hugging Face model (change model name as needed)
@st.cache_resource
def load_model():
    model = pipeline('sentiment-analysis')  # Change this to your desired model type
    return model

# Load the model
model = load_model()

# Streamlit UI
st.title("Hugging Face Model with Streamlit")

st.write("""
This app uses a Hugging Face model to perform sentiment analysis (or any other task you configure).
Enter some text below and the app will provide the analysis.
""")

# Text input box for user to enter text
user_input = st.text_area("Enter some text", "")

# Display results
if user_input:
    st.subheader("Model Output")
    result = model(user_input)
    st.write(result)

# Add some more styling (optional)
st.sidebar.title("Settings")
st.sidebar.write("""
You can change the model and task type here (optional).
""")
