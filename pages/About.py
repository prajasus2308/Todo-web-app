import streamlit as st
from json import load
from func import checker

st.set_page_config(page_title="How to Use", page_icon="ⓘ")

with open("data.json", "r") as json_file:
    data = load(json_file)

st.title("About This App")
with st.expander("How to use"):
    st.write(data['about'])

with st.expander("Create a account/login"):
    st.write(data['login_signup'])

# -expander to check if username exists or not.-
with st.expander("Check your username"):
    st.write(data['username_exitesnce'])

    user_input = st.text_input(label=data['enter_username'], placeholder="example-username", key='newtodo').strip().lower()
    if st.button("Check"):
        if checker(user_input.strip().lower()):
            st.warning(data['s'])
        else:
            st.success(data['w'])