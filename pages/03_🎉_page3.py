# Contents of ~/my_app/pages/03_🎉_page3.py
import streamlit as st

st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")

st.markdown('Streamlit is **_really_ cool**.')
st.title('This is a title')
st.header('This is a header')
st.subheader('This is a subheader')
st.caption('This is a string that explains something above.')
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')
st.text('This is some text.')
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')