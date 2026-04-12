
Vignesh Vicky
11:44 AM (0 minutes ago)
to me

import streamlit as st
import requests

#page config
st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon=" ",
    layout="centered",      
)

st.title("Movie Review Sentiment Analysis")
st.write("Enter a movie review and get instant sentiment prediction")

#input box
review = st.text_area("Enter your movie review here:", height=150)

#predict button
if st.button("Analyze Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review first")
    else:
        with st.spinner("Analyzing..."):
            # Call your Flask backend
            response = requests.post(a
                "https://movie-review-sentiment-analysis-1-6pwi.onrender.com/predict",
                json={"reviews": review}
            )
            result = response.json()

        #Display result
        sentiment = result['prediction']
        #confidence = result['confidence']

        if"pos" in sentiment or "neg" in sentiment:
            st.success(f"Sentiment: {sentiment}")
        else:
            st.error(f"Sentiment: {sentiment}")
