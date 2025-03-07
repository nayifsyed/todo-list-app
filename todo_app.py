import streamlit as st

# Initialize task list
tasks = []

# Streamlit UI
st.title("📝 To-Do List App") #print=

# Input box to add tasks
new_task = st.text_input("Enter a new task:") #input

if st.button("➕ Add Task"): #if statement
    if new_task:
        tasks.append(new_task)
        st.success(f"Added: {new_task}")
    else:
        st.warning("⚠️ Please enter a task.")

# Display tasks
st.subheader("📋 Your Tasks:")
if tasks:
    for i, task in enumerate(tasks, 1):
        st.write(f"{i}. {task}")
else:
    st.info("No tasks added yet.")

# Input box to remove tasks
task_to_remove = st.text_input("Enter a task to remove:")

if st.button("🗑️ Remove Task"):
    if task_to_remove in tasks:
        tasks.remove(task_to_remove)
        st.success(f"Removed: {task_to_remove}")
    else:
        st.error("❌ Task not found.")



        