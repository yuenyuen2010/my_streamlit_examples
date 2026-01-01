# Contents of ~/my_app/pages/08_⚡_caching_and_performance.py
import time
from typing import Tuple

import numpy as np
import pandas as pd
import streamlit as st

st.markdown("# Page 8 ⚡ Caching & Performance")
st.sidebar.markdown("# Page 8 ⚡ Caching & Performance")

st.markdown("Use caching to speed up expensive operations. Below we cache data generation and a heavy computation.")
st.markdown("""
---
""")

@st.cache
def load_data(num_rows: int, num_categories: int, seed: int) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    time.sleep(1.0)  # simulate I/O latency
    categories = [f"Cat {i+1}" for i in range(num_categories)]
    cat = rng.choice(categories, size=num_rows)
    values = rng.normal(loc=50, scale=15, size=num_rows)
    dates = pd.Timestamp.today().normalize() - pd.to_timedelta(rng.integers(0, 365, size=num_rows), unit="D")
    return pd.DataFrame({"category": cat, "value": values, "date": dates})

@st.cache
def expensive_compute(df: pd.DataFrame, power: int) -> float:
    # Simulate a heavy numeric computation
    time.sleep(1.5)
    arr = df["value"].to_numpy()
    return float(np.power(arr, power).sum())

with st.expander("Parameters", expanded=True):
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        num_rows = st.slider("Rows", min_value=1_000, max_value=200_000, value=50_000, step=1_000)
    with c2:
        num_categories = st.slider("Categories", min_value=1, max_value=10, value=4)
    with c3:
        power = st.slider("Power", min_value=1, max_value=6, value=3)
    with c4:
        seed = st.number_input("Seed", min_value=0, value=123, step=1)

# Load data (cached)
start = time.perf_counter()
with st.spinner("Loading data..."):
    df = load_data(num_rows=int(num_rows), num_categories=int(num_categories), seed=int(seed))
load_ms = (time.perf_counter() - start) * 1000

st.metric("Load time (ms)", f"{load_ms:.0f}")
st.write("Data shape:", df.shape)
st.dataframe(df.head(20))

st.markdown("""
---
""")

# Show a progress bar while running the heavy computation
st.markdown("### Heavy computation (cached)")
progress = st.progress(0)
for i in range(20):
    time.sleep(0.02)
    progress.progress(i + 1)

start = time.perf_counter()
with st.spinner("Computing..."):
    result = expensive_compute(df, power=int(power))
compute_ms = (time.perf_counter() - start) * 1000

c_a, c_b = st.columns(2)
with c_a:
    st.metric("Compute time (ms)", f"{compute_ms:.0f}")
with c_b:
    st.metric("Result (∑ value^power)", f"{result:,.2f}")

st.caption("Tip: Run the same parameters twice to see the speed-up from caching. Changing any parameter invalidates the cache.")