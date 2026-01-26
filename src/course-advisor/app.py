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
        # 1. Lowercase both for case-insensitive search
        name = course["name"].lower()
        search_term = keyword.lower()
        dept = course["dept"]
        
        # 2. Logic fix: Check if 'All' is selected OR if the depts match
        if search_term in name and (selected_dept == "All" or dept == selected_dept):
            # 3. Syntax fix: Use single quotes inside the f-string brackets
            st.write(f"{course['name']} ({course['credits']} credits)")
            
            if course["credits"] == 4:
                st.write("High workload course")
            else:
                st.write("Regular workload")