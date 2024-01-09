import google.generativeai as genai
import streamlit as st

# Assuming you have already set your Google Cloud project and API key
GOOGLE_API_KEY = 'your api key'  # Replace with your actual API key

# Configure the library with your API key
genai.configure(api_key=GOOGLE_API_KEY)

def main():
    st.title('Content Generator')

    prompt = st.text_input('Enter your prompt:')
    points = st.number_input('value:')
    if st.button('Generate Content'):
        generated_content = generate_content(prompt)
        st.subheader('Generated Content:')
        st.write(generated_content)
     
def generate_content(prompt):
    model = genai.GenerativeModel(model_name='gemini-pro')
    response = model.generate_content(prompt)
    result = response.text
    return result

if __name__ == '__main__':
    main()
