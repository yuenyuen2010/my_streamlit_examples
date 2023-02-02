# Contents of ~/my_app/pages/03_🎉_page3.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import plotly.figure_factory as ff
from bokeh.plotting import figure
import pydeck as pdk
import graphviz

st.markdown("# Page 4 🔢")
st.sidebar.markdown("# Page 4 🔢")
st.markdown("Reference: https://docs.streamlit.io/library/api-reference/charts")



"""
# Chart Examples
Streamlit supports several different charting libraries, and our goal is to continually add support for more. Right now, the most basic library in our arsenal is Matplotlib. Then there are also interactive charting libraries like Vega Lite (2D charts) and deck.gl (maps and 3D charts). And finally we also provide a few chart types that are "native" to Streamlit, like st.line_chart and st.area_chart.
"""
st.markdown("") # empty line
st.markdown("""---""")


"""
# Simple Line Chart
Display a line chart.
"""
st.markdown("") # empty line

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.markdown("""---""")

"""
# Simple Area Chart
Display an area chart.
"""
st.markdown("") # empty line

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.area_chart(chart_data)

st.markdown("""---""")

"""
# Simple Bar Chart
Display an bar chart.
"""
st.markdown("") # empty line

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)

st.markdown("""---""")


"""
# Pyplot
Display a matplotlib.pyplot figure.
"""
st.markdown("") # empty line

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

st.markdown("""---""")


"""
# Altair Chart
Display a chart using the Altair library.
"""
st.markdown("") # empty line

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(chart_data).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)

st.markdown("""---""")


"""
# Vega-Lite
Display a chart using the Vega-Lite library.
"""
st.markdown("") # empty line

chart_data = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

st.vega_lite_chart(chart_data, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'a', 'type': 'quantitative'},
        'y': {'field': 'b', 'type': 'quantitative'},
        'size': {'field': 'c', 'type': 'quantitative'},
        'color': {'field': 'c', 'type': 'quantitative'},
    },
})

st.markdown("""---""")


# """
# # Plotly Cahrt
# Display an interactive Plotly chart.
# """
# st.markdown("") # empty line
#
# # Add histogram data
# x1 = np.random.randn(200) - 2
# x2 = np.random.randn(200)
# x3 = np.random.randn(200) + 2
#
# # Group data together
# hist_data = [x1, x2, x3]
#
# group_labels = ['Group 1', 'Group 2', 'Group 3']
#
# # Create distplot with custom bin_size
# fig = ff.create_distplot(
#         hist_data, group_labels, bin_size=[.1, .25, .5])
#
# # Plot!
# st.plotly_chart(fig, use_container_width=True)
#
# st.markdown("""---""")


"""
# Bokeh Chart
Display an interactive Bokeh chart.
"""
st.markdown("") # empty line

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(
    title='simple line example',
    x_axis_label='x',
    y_axis_label='y')

p.line(x, y, legend_label='Trend', line_width=2)

st.bokeh_chart(p, use_container_width=True)
st.markdown("""---""")


"""
# Pydeck Chart
Draw a chart using the PyDeck library.
"""
st.markdown("") # empty line

chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))


st.markdown("""---""")


"""
# Graphviz Chart
Display a graph using the dagre-d3 library.
"""
st.markdown("") # empty line

# Create a graphlib graph object
graph = graphviz.Digraph()
graph.edge('run', 'intr')
graph.edge('intr', 'runbl')
graph.edge('runbl', 'run')
graph.edge('run', 'kernel')
graph.edge('kernel', 'zombie')
graph.edge('kernel', 'sleep')
graph.edge('kernel', 'runmem')
graph.edge('sleep', 'swap')
graph.edge('swap', 'runswap')
graph.edge('runswap', 'new')
graph.edge('runswap', 'runmem')
graph.edge('new', 'runmem')
graph.edge('sleep', 'runmem')

st.graphviz_chart(graph)

st.markdown("""---""")


"""
# Map
Display a map with points on it.
"""
st.markdown("") # empty line

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)

st.markdown("""---""")