# Contents of ~/my_app/pages/03_🎉_page3.py
import pandas
import pandas as pd
import streamlit as st

st.markdown("# Page 6 🆘")
st.sidebar.markdown("# Page 6 🆘")
st.markdown("Reference: https://docs.streamlit.io/library/api-reference/utilities")


"""
# Input widgets
With widgets, Streamlit allows you to bake interactivity directly into your apps with buttons, sliders, text inputs, and more.
"""
st.markdown("") # empty line
st.markdown("""---""")


"""
# Echo
Use in a `with` block to draw some code on the app, then execute it.
"""
st.markdown("") # empty line

with st.echo():
    st.write('This code will be printed')

st.markdown("""---""")


"""
# Experimental show
Write arguments and argument names to your app for debugging purposes.
"""
st.markdown("") # empty line

dataframe = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})
st.experimental_show(dataframe)

st.markdown("""---""")


"""
# Experimental set query params
Set the query parameters that are shown in the browser's URL bar.
"""
st.markdown("") # empty line

st.experimental_set_query_params(
    show_map=True,
    selected=["asia", "america"],
)

st.markdown("""---""")

# """
# # Experimental Get Query Params
# Return the query parameters that is currently showing in the browser's URL bar.
# """
# st.markdown("") # empty line
#
# st.experimental_get_query_params()
#
# st.markdown("""---""")

"""
# Help
Displays the doc string for this object.
"""
st.markdown("") # empty line

st.help(pandas.DataFrame)

st.markdown("""---""")

"""
# Session State
"Reference: https://docs.streamlit.io/library/api-reference/session-state"
Session state is very useful. Print the session state object.
"""
st.write(st.session_state)