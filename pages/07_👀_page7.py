import streamlit as st
import logging

logger = logging.getLogger(__name__)

st.set_page_config(page_title="Page 7", page_icon="👀")

st.markdown("# Page 7 👀")
st.sidebar.markdown("# Page 7 👀")
st.markdown("Reference: https://docs.streamlit.io/library/api-reference/layout")

"""
# Forms
Forms allow you to batch multiple widgets together so that the script only reruns when a submit button is pressed.
"""
st.markdown("")

with st.form("my_form"):
    st.write("Inside the form")
    my_number = st.slider('Pick a number', 1, 10)
    my_color = st.selectbox('Pick a color', ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'])
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.write(f"slider: {my_number}, color: {my_color}")
        logger.info(f"Form submitted with number: {my_number} and color: {my_color}")

st.markdown("""---""")

"""
# Tabs
Tabs let you separate content into different views within the same context.
"""
st.markdown("")

try:
    tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

    with tab1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

    with tab2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

    with tab3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
except AttributeError:
    st.error("st.tabs is not available in your Streamlit version.")

st.markdown("""---""")

"""
# Expander
Expanders allow you to hide content that is not immediately relevant.
"""
st.markdown("")

with st.expander("See explanation"):
    st.write("""
        The chart above shows some numbers I picked for you.
        I rolled 100 dice and summed the results...
    """)
    st.image("https://static.streamlit.io/examples/dice.jpg", width=200)

st.markdown("""---""")

"""
# Container
Containers let you insert elements out of order.
"""
st.markdown("")

container = st.container()
container.write("This is inside the container")
st.write("This is outside the container")

# Now write to the container again
container.write("This is also inside the container, but written after the outside text.")


st.markdown("""---""")

"""
# Status Elements
Streamlit includes several status elements to display messages to the user.
"""
st.markdown("")

col1, col2 = st.columns(2)

with col1:
    if st.button('Show Success'):
        st.success('This is a success message!', icon="✅")

    if st.button('Show Info'):
        st.info('This is an info message', icon="ℹ️")

with col2:
    if st.button('Show Warning'):
        st.warning('This is a warning message', icon="⚠️")

    if st.button('Show Error'):
        st.error('This is an error message', icon="🚨")

if st.button('Show Exception'):
    e = RuntimeError('This is an exception of type RuntimeError')
    st.exception(e)

st.markdown("""---""")

"""
# Fun Elements
Add some animation to your app!
"""
st.markdown("")

col1, col2 = st.columns(2)

with col1:
    if st.button('Balloons 🎈'):
        st.balloons()

with col2:
    if st.button('Snow ❄️'):
        st.snow()

st.markdown("""---""")
