import openai
import os
import streamlit as st
import pandas as pd
import numpy as np

def format_string(s, max_line_length=100):
    words = s.split()
    formatted_string = ""
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 <= max_line_length:
            current_line += word + " "
        else:
            formatted_string += current_line.strip() + "\n"
            current_line = word + " "

    # Add the last line if it contains any words
    if current_line:
        formatted_string += current_line.strip()

    return formatted_string

def prompt_open_ai(prompt, gptid) :
    # Make the API call
    use_model = ""
    answer = ""
    if gptid == 35 : 
        use_model = "gpt-3.5-turbo"
    elif gptid == 40 : 
        use_model = "gpt-4-1106-preview"
    else :
        use_model = "gpt-3.5-turbo"
   
    response = openai.chat.completions.create(
        model=use_model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    
    if response.choices:
        message = response.choices[0].message.content  
    else : 
        message = "No message available."

    answer = format_string(message)

    print(answer)
    
    return answer
        
# Securely set your API key
openai.api_key = st.secrets["OPEN_AI_KEY"]

prompt = ""
prompt_response = ""

st.set_page_config(
    page_title="Exploration of possibilities",
    page_icon="🧊",
)

# Expander section
with st.expander("Instructions"):
  st.write("""Enter a prompt to see the answer given by different GPTs""")

gpt_choice = st.radio(
    "Which GPT do you want to use?",
    [":rainbow[GPT3.5]", "***GPT4.0***"],
    captions = ["Most economical", "Best of the best"])

st.subheader('Prompt')
prompt = st.text_input('Write your prompt!')
st.write("This is your prompt", prompt)

if len(prompt) > 0 and gpt_choice == ":rainbow[GPT3.5]" :
    prompt_response = prompt_open_ai(prompt, 35)
elif len(prompt) > 0 and gpt_choice == "***GPT4.0***" :
    prompt_response = prompt_open_ai(prompt, 40)
else :
    prompt_response = "No response yet :"

st.write("This is the response, ", gpt_choice, " says :", prompt_response)
    
# Survey section
st.write('Which GPT do you prefer? 🍨')
prefer_gpt35 = st.checkbox('I prefer GPT3.5')
prefer_gpt40 = st.checkbox('I prefer GPT4.0')
if prefer_gpt35:
    st.write('Retro tastes!!!')
    st.image("https://i.gifer.com/DJR3.gif", width=400)
if prefer_gpt40:
    st.write('Modern lover!!! 😒') 
    st.image("https://i.gifer.com/DJR3.gif", width=400)



