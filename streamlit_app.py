import streamlit as st
import requests

# page config
st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="🎥",
    layout="centered",
)

st.title("Movie Review Sentiment Analysis")
st.write("Enter a movie review and get instant sentiment prediction")

# input box
review = st.text_area("Enter your movie review here:", height=150)

# predict button
if st.button("Analyze Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review first")
    else:
        with st.spinner("Analyzing..."):

            try:
                # API call
                response = requests.post(
                    "https://movie-sentiment-analyzing-model-3.onrender.com/predict",
                    json={"review": review}   # ✅ correct key
                )

                # show status
                st.write("Status Code:", response.status_code)

                # convert to json
                result = response.json()
                st.write("API Response:", result)

                # safe access
                sentiment = result.get("prediction")

                if sentiment:
                    if "pos" in sentiment.lower():
                        st.success(f"😊 Sentiment: {sentiment}")
                    elif "neg" in sentiment.lower():
                        st.error(f"😞 Sentiment: {sentiment}")
                    else:
                        st.info(f"Sentiment: {sentiment}")
                else:
                    st.error("❌ 'prediction' key not found in API response")

            except Exception as e:
                st.error(f"⚠️ Error: {e}")
