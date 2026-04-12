import streamlit as st
import requests

st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="🎥",
    layout="centered"
)

st.title("Movie Review Sentiment Analysis")
st.write("Enter a movie review and get instant sentiment prediction!")

review = st.text_area("Enter your movie review here:", height=150)

if st.button("Analyze Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review first!")
    else:
        with st.spinner("Analyzing..."):
            response = requests.post(
                "http://127.0.0.1:5000/predict",
                json={"reviews": review}
            )

            result = response.json()
            sentiment = result["prediction"]

            if "pos" in sentiment.lower() or "neg" in sentiment.lower():
                st.success(f"Sentiment: {sentiment}")
            else:
                st.error(f"Sentiment: {sentiment}")
