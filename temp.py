import streamlit as st

name = st.text_input("Enter your name:")
st.subheader(name)


age = st.number_input("Enter your age: ")
st.text(age)


#photo = st.camera_input('click your photo')
#st.image(photo)

