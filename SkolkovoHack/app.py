import streamlit as st


page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page=='Predict':
    st.write("""### You have chosen Predict button""")
elif page=='Explore':
    st.write("""### You have chosen Explore button""")

st.write("""### You have chosen Explore button""")