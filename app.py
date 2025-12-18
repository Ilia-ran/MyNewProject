import streamlit as st
st.title("Моето първо Streamlit приложение")
name = st.text_input("Как се казваш?")
age = st.num_input("На колко години си?")
if name and age:
   st.write(f"Здравей, {name}! Ти си на {age} години!")
