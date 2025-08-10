# Contents of ~/my_app/pages/07_📊_interactive_charts.py
import numpy as np
import pandas as pd
import altair as alt
import plotly.express as px
import streamlit as st

st.markdown("# Page 7 📊 Interactive Charts")
st.sidebar.markdown("# Page 7 📊 Interactive Charts")

st.markdown("Filter data and explore interactive charts built with Altair and Plotly.")
st.markdown("""
---
""")

@st.cache
def generate_sample_timeseries(days: int, categories: int, seed: int) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    start = pd.Timestamp.today().normalize() - pd.Timedelta(days=days)
    date_index = pd.date_range(start=start, periods=days + 1, freq="D")
    category_labels = [f"Cat {i+1}" for i in range(categories)]

    data_frames = []
    for cat_idx, label in enumerate(category_labels):
        base = np.sin(np.linspace(0, 3 * np.pi, len(date_index))) * 10
        noise = rng.normal(0, 3, size=len(date_index))
        drift = np.linspace(0, cat_idx * 2.0, len(date_index))
        values = 50 + base + noise + drift
        df = pd.DataFrame({
            "date": date_index,
            "category": label,
            "value": values,
        })
        data_frames.append(df)

    return pd.concat(data_frames, ignore_index=True)

# Controls
with st.expander("Data & filter controls", expanded=True):
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        days = st.slider("Days", min_value=60, max_value=365, value=180, step=15)
    with c2:
        num_categories = st.slider("Categories", min_value=1, max_value=6, value=4)
    with c3:
        seed = st.number_input("Seed", min_value=0, value=42, step=1)
    with c4:
        smooth = st.slider("Smoothing window", min_value=1, max_value=30, value=7)

    df = generate_sample_timeseries(days=days, categories=num_categories, seed=int(seed))

    min_date, max_date = df["date"].min(), df["date"].max()
    date_range = st.slider(
        "Date range",
        min_value=min_date.to_pydatetime(),
        max_value=max_date.to_pydatetime(),
        value=(min_date.to_pydatetime(), max_date.to_pydatetime()),
    )

    selected_categories = st.multiselect(
        "Categories",
        options=sorted(df["category"].unique().tolist()),
        default=sorted(df["category"].unique().tolist()),
    )

# Filter
mask = (
    df["date"].between(pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1]))
    & df["category"].isin(selected_categories)
)
filtered = df.loc[mask].copy()
filtered.sort_values(["category", "date"], inplace=True)
filtered["value_smooth"] = (
    filtered.groupby("category")["value"].transform(lambda s: s.rolling(window=smooth, min_periods=1).mean())
)

st.markdown("### Filtered data snapshot")
st.dataframe(filtered.tail(20), use_container_width=True)

# Altair chart
st.markdown("#### Altair — smoothed line by category")
alt_chart = (
    alt.Chart(filtered)
    .mark_line()
    .encode(
        x=alt.X("date:T", title="Date"),
        y=alt.Y("value_smooth:Q", title="Value (smoothed)"),
        color=alt.Color("category:N", title="Category"),
        tooltip=["date:T", "category:N", alt.Tooltip("value:Q", format=".2f")],
    )
    .interactive()
)
st.altair_chart(alt_chart, use_container_width=True)

st.markdown("""
---
""")

# Plotly chart
st.markdown("#### Plotly — scatter of raw values")
px_fig = px.scatter(
    filtered,
    x="date",
    y="value",
    color="category",
    opacity=0.7,
    render_mode="webgl",
)
st.plotly_chart(px_fig, use_container_width=True)

st.markdown("""
---
""")

# Download filtered data
csv_bytes = filtered.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download filtered CSV",
    data=csv_bytes,
    file_name="filtered_timeseries.csv",
    mime="text/csv",
)