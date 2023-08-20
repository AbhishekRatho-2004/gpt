import streamlit as st
from streamlit_chat import message
import streamlit as st
import os
import openai
st.set_page_config(
    page_title='Chatbot'
)

openai.api_key=st.secrets["api_secret"]

def generate_response(prompt):
    completions=openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message=completions.choices[0].text
    return message
st.header('Stock Bot 🤖')

if 'generated' not in st.session_state:
    st.session_state['generated']=[]

if 'past' not in st.session_state:
    st.session_state['past']=[]

def get_text():
    #input_text=st.text_input("You:","Hello,how are you?",key="input")
    input_text=st.chat_input()
    return input_text

user_input=get_text()

if user_input:
    output=generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])):
        message(st.session_state["past"][i],is_user=True,key=str(i)+'_user')
        message(st.session_state["generated"][i],key=str(i))
