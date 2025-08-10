# Contents of ~/my_app/pages/03_🎉_page3.py
import time
from datetime import date, time as dtime

import numpy as np
import pandas as pd
import streamlit as st

st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")

st.markdown("This page showcases common widgets, forms, session state, tabs, and layout utilities.")
st.markdown("""
---
""")

# Tabs for organization
tab_inputs, tab_forms, tab_state, tab_layout = st.tabs(["Inputs", "Forms", "State", "Layout"])

with tab_inputs:
    st.subheader("Widget inputs")
    st.markdown("")

    col_a, col_b, col_c = st.columns(3)
    with col_a:
        age = st.number_input("Age", min_value=0, max_value=120, value=30, step=1, key="age_input")
        color = st.color_picker("Favorite color", value="#FF4B4B", key="color_picker")
    with col_b:
        birthday = st.date_input("Birthday", value=date(1990, 1, 1), key="birthday_input")
        wake_time = st.time_input("Wake-up time", value=dtime(7, 30), key="wake_time_input")
    with col_c:
        satisfaction = st.slider("Satisfaction", min_value=0, max_value=10, value=7, step=1, key="satisfaction_slider")
        rating = st.select_slider("Rating", options=["Poor", "Fair", "Good", "Great", "Excellent"], value="Good", key="rating_select_slider")

    favorite_fruits = st.multiselect(
        "Favorite fruits",
        ["Apple", "Banana", "Cherry", "Durian", "Grape", "Mango"],
        default=["Apple", "Mango"],
        key="favorite_fruits",
    )

    name = st.text_input("Your name", value="Taylor", key="name_input")
    about = st.text_area("About you", value="I love building data apps with Streamlit.", height=100, key="about_text")

    st.markdown("### Current selections")
    st.json({
        "name": name,
        "age": age,
        "birthday": str(birthday),
        "wake_time": str(wake_time),
        "favorite_color": color,
        "satisfaction": satisfaction,
        "rating": rating,
        "fruits": favorite_fruits,
        "about": about,
    })

with tab_forms:
    st.subheader("Form submission")
    st.markdown("Use forms to group inputs and submit them together.")

    with st.form("profile_form"):
        c1, c2 = st.columns(2)
        with c1:
            form_name = st.text_input("Name", value="Alex")
            form_role = st.selectbox("Role", ["Engineer", "Designer", "Analyst", "Manager"]) 
        with c2:
            form_email = st.text_input("Email", value="alex@example.com")
            form_news = st.checkbox("Subscribe to newsletter", value=True)

        st.markdown("Preferences")
        prefs = st.multiselect("Topics", ["AI", "Data", "Web", "Mobile", "Cloud"], default=["AI", "Data"]) 

        submitted = st.form_submit_button("Submit")

    if submitted:
        st.success("Form submitted!")
        st.json({
            "name": form_name,
            "email": form_email,
            "role": form_role,
            "newsletter": form_news,
            "preferences": prefs,
        })

with tab_state:
    st.subheader("Session state")
    st.markdown("State persists across reruns. Use it to build interactive flows.")

    if "counter" not in st.session_state:
        st.session_state.counter = 0

    c_inc, c_val, c_dec = st.columns([1, 2, 1])
    with c_inc:
        if st.button("➕ Increment"):
            st.session_state.counter += 1
    with c_val:
        st.metric("Counter", st.session_state.counter)
    with c_dec:
        if st.button("➖ Decrement"):
            st.session_state.counter -= 1

    st.text_input("Stateful text", key="stateful_text", value=st.session_state.get("stateful_text", "Hello"))

    st.markdown("### All session state")
    st.write(dict(st.session_state))

with tab_layout:
    st.subheader("Layout, feedback and utilities")

    with st.expander("Show code sample"):
        st.code(
            """
import pandas as pd
import numpy as np

sample = pd.DataFrame(np.random.randn(5, 3), columns=list("ABC"))
summary = sample.describe()
print(summary)
            """,
            language="python",
        )

    st.markdown("Progress and status")
    col_left, col_right = st.columns(2)
    with col_left:
        if st.button("Run task with spinner"):
            with st.spinner("Working hard..."):
                time.sleep(1.0)
            st.success("Done!")
    with col_right:
        if st.button("Celebrate 🎈"):
            st.balloons()

    st.markdown("Display data in columns")
    c1, c2, c3 = st.columns(3)
    c1.dataframe(pd.DataFrame(np.random.randn(5, 2), columns=["X", "Y"]))
    c2.table(pd.DataFrame({"A": [1, 2, 3], "B": ["a", "b", "c"]}))
    c3.line_chart(pd.DataFrame(np.random.randn(10, 1), columns=["trend"]))

    st.markdown("Errors and exceptions")
    if st.button("Show example error"):
        try:
            _ = 1 / 0
        except Exception as exc:
            st.exception(exc)

st.markdown("""
---
""")