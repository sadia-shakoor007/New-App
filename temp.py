import streamlit as st

name = st.text_input("Enter your name:")
st.subheader(name)
date = st.date_input('Enter your DOB: ')
st.text(f"Your date of birth is: {date}")

age = st.number_input("Enter your age: ")
st.text(age)


#photo = st.camera_input('click your photo')
#st.image(photo)

st.video('https://youtu.be/g-ZNUL96uMw?si=0MrsNGL8zYJg2QuP')