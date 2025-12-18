import streamlit as st
from func import r_wFromFile
import json

with open("data.json", "r") as json_file:
    data = json.load(json_file)

user = ''

if "show_popup" not in st.session_state:
    st.session_state.show_popup = False

if "username" not in st.session_state:
    st.title("Login")
    user_input = st.text_input("Username", placeholder="Enter your username",).strip()
    user = user_input.lower()
    
    st.session_state['username'] = user
    st.stop()

users = r_wFromFile(file_name="Users.txt", mode="r")

    
    
if user in users:
    st.success(f"Welcome back, {st.session_state['username']}!")
    st.rerun()

elif user not in users:
    with st.container():
        st.session_state.show_popup = True
        st.write("You are not registered. Click below to sign up.")

        st.button("Sign Up", on_click=lambda: st.session_state.update(show_popup=False))
        
        users = r_wFromFile(file_name="Users.txt", mode="r")
        users.append(user + '\n')
        r_wFromFile(file_name="Users.txt", mode="w", todos=users)

        r_wFromFile(file_name="files/" + st.session_state['username'] + ".txt", mode="w", todos=["You signed up\n"])

        st.success("Signed up successfully!")
        
        st.rerun()

todos = r_wFromFile(file_name="files/" + st.session_state['username'] + ".txt", mode="r")

def addwebtodo():
    todo = st.session_state['newtodo']
    todos.append(todo + '\n')
    r_wFromFile(file_name="files/" + st.session_state['username'] + ".txt", mode="w", todos=todos)

st.title(data['app_name'])
st.subheader("Welcome to the Web Page")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        r_wFromFile(file_name="files/" + st.session_state['username'] + ".txt", mode="w", todos=todos)
        del st.session_state[todo]
        st.rerun()
       
st.text_input(label=data['enter_str'], placeholder="Add new todo...", 
              on_change=addwebtodo, key='newtodo')