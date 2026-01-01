# my_streamlit_examples

A collection of small Streamlit examples demonstrating common widgets, layouts, charts, and media features.

## Quickstart

1. Create and activate a virtual environment (optional but recommended)
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the app:

```
streamlit run 01_🎈_main_page.py
```

## What’s inside

- `01_🎈_main_page.py`: Core Streamlit concepts (tables, charts, widgets, layout, metrics, JSON, progress)
- `pages/02_❄️_page2.py`: NYC Uber pickups demo with caching, charts, and map
- `pages/03_🎉_page3.py`: Widgets, forms, session state, tabs, layout utilities
- `pages/04_🔢_page4.py`: Chart gallery (line/area/bar, Matplotlib, Altair, Vega-Lite, Bokeh, Pydeck, Graphviz, map, Plotly)
- `pages/05_🅰️_page5.py`: Comprehensive widgets showcase (buttons, radios, multiselects, file uploader, camera input, media playback)
- `pages/05_📁_media_and_files.py`: Media (image/audio/video), file upload + processing, camera input, downloads
- `pages/06_🆘_page6.py`: Utilities (echo, experimental_show, query params, help, session state)
- `pages/07_📊_interactive_charts.py`: Interactive Altair and Plotly charts with filters and CSV download
- `pages/08_⚡_caching_and_performance.py`: Cached data generation and heavy compute with timing metrics

Note: Having two page files both numbered `05_...` will display both in the sidebar; you can rename one to adjust ordering.

## Assets

Local media files used by examples:
- `sunrise.jpg`
- `sample4.ogg`
- `sample-mp4-file.mp4`

If you remove or rename these files, related examples will show an informational message.
