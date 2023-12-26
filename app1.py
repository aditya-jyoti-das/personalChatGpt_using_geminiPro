# app.py
import streamlit as st


import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
    text = text.replace('•', '  *')
    indented_text = textwrap.indent(text, '> ', predicate=lambda _: True)
    return Markdown(indented_text)


GOOGLE_API_KEY=''#type your gemini pro api key here
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')
def main():

    
    st.title("Hello Streamlit!")
    st.write("This is a simple Streamlit app.ADITYA.CORP")
    st.sidebar.title("Options")
    page = st.sidebar.radio("Page", ["Text Generation", "Image To Text"])

    
    

    if page=="Text Generation":
            
        user_input = st.text_input("Write Your Queries Here", )
        st.write(f"Here you ans of you queries\n ")
        # st.write(f"{response.text}")
        if st.button("Click me"):
            response = model.generate_content(user_input)   
            st.write(f"{response.text}")
    if page=="Image To Text":
        pass








    # age = st.slider("Select your age", 0, 100, 25)
    # st.write(f"You selected {age} years old.")

    # data = pd.DataFrame({
    #     'Name': ['Alice', 'Bob', 'Charlie'],
    #     'Age': [25, 30, 35]
    # })

    # st.table(data)  



if __name__ == "__main__":
    main()
