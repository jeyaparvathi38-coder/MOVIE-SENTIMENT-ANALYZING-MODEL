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
            try:
                response = requests.post(
                    "https://movie-sentiment-analyzing-model-3.onrender.com/predict",
                    json={"reviews": review}
                )

                result = response.json()
                st.write("API Response:", result)  # debug

                sentiment = result.get("prediction")

                if sentiment:
                    if "pos" in sentiment.lower() or "neg" in sentiment.lower():
                        st.success(f"Sentiment: {sentiment}")
                    else:
                        st.info(f"Sentiment: {sentiment}")
                else:
                    st.error("Prediction key not found in API response!")

            except Exception as e:
                st.error(f"Error: {e}")
