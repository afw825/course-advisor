import streamlit as st

st.title("🎓 Simple Course Advisor")

courses = [
    {"name": "Intro to Programming", "dept": "CS", "credits": 3},
    {"name": "Data Structures", "dept": "CS", "credits": 4},
    {"name": "Calculus I", "dept": "Math", "credits": 4},
    {"name": "English Composition", "dept": "English", "credits": 3},
    {"name": "Statistics", "dept": "Math", "credits": 3}
]

selected_dept = st.selectbox("Select Department", options=["All", "CS", "Math", "English"])

keyword = st.text_input("Keyword Search")

if st.button("Show Courses"):
    for course in courses:
        name = course["name"].lower()
        dept = course["dept"]
        if (keyword in name) and (dept == selected_dept or "All"):
            st.write(f"{course["name"]}   ({course["credits"]} credits)")
            if course["credits"] == 4:
                st.write("High workload course")
            else:
                st.write("Regular workload")