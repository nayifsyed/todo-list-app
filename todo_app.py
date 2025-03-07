import streamlit as st

# Initialize session state for tasks if not already created
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Title
st.title("📝 To-Do List App")

# Input field for new task
task = st.text_input("Enter a task:")

# Add Task Button
if st.button("Add Task"):
    if task:
        st.session_state.tasks.append(task)  # Store in session state
        st.success("Task added!")
    else:
        st.warning("Please enter a task.")

# Display tasks
st.subheader("Your Tasks:")
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks, 1):
        st.write(f"{i}. {task}")
else:
    st.write("No tasks added yet.")

# Remove Task
remove_task = st.text_input("Enter the exact task to remove:")
if st.button("Remove Task"):
    if remove_task in st.session_state.tasks:
        st.session_state.tasks.remove(remove_task)
        st.success("Task removed!")
    else:
        st.warning("Task not found.")

