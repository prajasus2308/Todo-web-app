import streamlit as st
from func import r_wFromFile
import json

st.set_page_config(page_title="My Todos")

with open("data.json", "r") as json_file:
    data = json.load(json_file)

if "username" not in st.session_state:
    st.title("Login")
    user_input = st.text_input("Username", placeholder="Enter your username",).strip().lower()
    
    if not user_input:
        st.warning("Please enter a username to proceed.")
        st.stop()

    st.session_state['temp_user'] = user_input

    users = r_wFromFile(file_name="Users.txt", mode="r")
    user = st.session_state.get("temp_user")
        
    if user in users:
        st.session_state['username'] = user.strip().lower()
        st.success(f"Welcome back, {st.session_state['username']}!")
        del st.session_state['temp_user']
        st.rerun()

    elif user not in users:
        st.write('''You are not registered. Click below to sign up.
        Do not use Capital letters in your username.''')

        if st.button("Sign Up"):
            users.append(f'{user}')
            r_wFromFile(file_name="Users.txt", mode="w", todos=users)
            
            st.session_state['username'] = user.strip().lower()
            r_wFromFile(file_name="files/" + st.session_state['username'] + ".txt", mode="w", todos=["You signed up"])

            del st.session_state['temp_user']
            st.success("Signed up successfully!")
            st.rerun()
        st.stop()

user = st.session_state['username']
todos = r_wFromFile(file_name=f"files/{user}.txt", mode="r")

# -Function to add To-Do item from web interface to the .txt file. it is called in the input box in lines 68 and 69.-
def addwebtodo():
    todo = st.session_state['newtodo'].strip()
    if not todo:
        return
    todos.append(f'{todo}')
    r_wFromFile(file_name="files/" + st.session_state['username'] + ".txt", mode="w", todos=todos)
    st.session_state['newtodo'] = ""

st.title(data['app_name'])
st.subheader("Welcome to the Web Page")
st.write("This app is to increase your productivity")

# -Display To-Do items with checkboxes. Creates the objects as well.-
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        r_wFromFile(file_name="files/" + st.session_state['username'] + ".txt", mode="w", todos=todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label=data['enter_todo'], placeholder="Add new todo...", 
              on_change=addwebtodo, key='newtodo')