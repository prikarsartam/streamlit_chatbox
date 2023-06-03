import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat

st.set_page_config(page_title="Omnilistener")

with st.sidebar:
    st.title('Omnilistener')
    st.markdown('''
    ## About
    This for now is just an interface to work with:
    - [prikarsartam](<https://prikarsartam.github.io/>)
    - [Article Stand](<https://prikarsartam.github.io/article_stand/index.html>)
    - [OpenAssistant/oasst-sft-6-llama-30b-xor](<https://huggingface.co/OpenAssistant/oasst-sft-6-llama-30b-xor>) LLM model
    
    ''')
    add_vertical_space(5)
    st.write('Made by [Pritam S.](<https://prikarsartam.github.io/about/index.html>)')


if 'generated' not in st.session_state:
    st.session_state['generated'] = ["I'm HugChat, How may I help you?"]

if 'past' not in st.session_state:
    st.session_state['past'] = ['Hi!']


input_container = st.container()
colored_header(label='', description='', color_name='blue-30')
response_container = st.container()

def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text

with input_container:
    user_input = get_text()

def get_auth_cookies():
    cookies = {"auth_token": "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"}
    return cookies


# I need gpt3.5 here
def generate_response(prompt):

    auth_cookies = get_auth_cookies()  
    chatbot = hugchat.ChatBot(cookies=auth_cookies)
    response = chatbot.chat(prompt)
    return response

with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state['generated'][i], key=str(i))
