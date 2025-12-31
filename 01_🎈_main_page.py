# Contents of ~/my_app/01_🎈_main_page.py
import streamlit as st
import pandas as pd
import numpy as np
import time
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.info("Main page loaded")

st.set_page_config(
    page_title="My Streamlit Example App",
    page_icon="🧊",
    layout="wide",
    # initial_sidebar_state="expanded",
    # menu_items={
    #    'Get Help': 'https://www.extremelycoolapp.com/help',
    #    'Report a bug': "https://www.extremelycoolapp.com/bug",
    #    'About': "# This is a header. This is an *extremely* cool app!"
    # }
)

st.subheader('Debug Area - Print Raw data')
st.write("12345678")
st.markdown("""---""")

st.markdown("# Main page 🎈")
st.markdown("links:")
st.markdown("https://docs.streamlit.io/library/get-started/main-concepts")
st.sidebar.markdown("# Main page 🎈")


"""
# Example 1 - Create a simple table
Here's our first attempt at using data to create a table:
You can also write to your app without calling any Streamlit methods.
Streamlit supports "magic commands," which means you don't have to use st.write() at all.
"""
st.markdown("")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
df

# Or use the following code
# st.write(pd.DataFrame({
#    'first column': [1, 2, 3, 4],
#    'second column': [10, 20, 30, 40]
# }))
st.markdown("""---""")

"""
# Example 2 - render dataframe with styler
For example, let's create a data frame and change its formatting with a Pandas Styler object.
In this example, you'll use Numpy to generate a random sample, and the st.dataframe() method to draw an interactive table.
"""
st.markdown("")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))
st.markdown("""---""")

"""
# Example 3 - render dataframe with st.table
Streamlit also has a method for static table generation: st.table().
"""
st.markdown("")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.table(dataframe)
st.markdown("""---""")

"""
# Example 4 - Draw a line chart
You can easily add a line chart to your app with st.line_chart().
We'll generate a random sample using Numpy and then chart it.
"""
st.markdown("")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)
st.markdown("""---""")


"""
# Example 5 - Plot a map
With st.map() you can display data points on a map.
Let's use Numpy to generate some sample data and plot it on a map of San Francisco.
"""
st.markdown("")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
st.markdown("""---""")


"""
# Example 6 - Widgets - slider
When you've got the data or model into the state that you want to explore,
you can add in widgets like st.slider(), st.button() or st.selectbox().
It's really straightforward — treat widgets as variables:
"""
st.markdown("")
x = st.slider('x')  # 👈 this is a widget
logger.debug(f"Slider x value changed to: {x}")
st.write(x, 'squared is', x * x)
st.markdown("""---""")


"""
# Example 7 - Widgets - text_input
Every widget with a key is automatically added to Session State.
For more information about Session State, its association with widget state, and its limitations,
see Session State API Reference Guide.
"""
st.markdown("")
st.text_input("Your name", key="name")
if st.session_state.name:
    logger.debug(f"Name entered: {st.session_state.name}")

# You can access the value at any point with:
st.session_state.name
st.markdown("""---""")


"""
# Example 8 - Widgets - Chartboxes
One use case for checkboxes is to hide or show a specific chart or section in an app.
st.checkbox() takes a single argument, which is the widget label.
In this sample, the checkbox is used to toggle a conditional statement.
"""
st.markdown("")
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    chart_data
st.markdown("""---""")


"""
# Example 9 - Widgets - Selectbox for options
Use st.selectbox to choose from a series.
You can write in the options you want, or pass through an array or data frame column.
"""
st.markdown("")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

option = st.selectbox(
    'Which number do you like best?',
    df['first column'])

logger.info(f"Selectbox option chosen: {option}")

'You selected: ', option
st.markdown("""---""")


"""
# Example 10 - Layout - Add selectbox and slider to sidebar (Please check sidebar)
For example, if you want to add a selectbox and a slider to a sidebar,
use st.sidebar.slider and st.sidebar.selectbox instead of st.slider and st.selectbox:
"""
st.markdown("")
# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
st.markdown("""---""")


"""
# Example 11 - Layout - Columns
Beyond the sidebar, Streamlit offers several other ways to control the layout of your app.
st.columns lets you place widgets side-by-side, and st.expander lets you conserve space by hiding away large content.
"""
st.markdown("")  # empty line
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
st.markdown("""---""")


"""
# Example 12 - Show progress
Now, let's create a progress bar:
"""
st.markdown("")  # empty line
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(20):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'...and now we\'re done!'
st.markdown("""---""")


"""
# Example 13 - metric
Display a metric in big bold font, with an optional indicator of how the metric changed.
"""
st.markdown("")  # empty line

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.markdown("""---""")


"""
# Example 14 - st.json
Display object or string as a pretty-printed JSON string.
"""
st.markdown("")  # empty line

st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
})

st.markdown("""---""")
