# Contents of ~/my_app/pages/05_📁_media_and_files.py
import io
from pathlib import Path

import pandas as pd
from PIL import Image
import streamlit as st

st.markdown("# Page 5 📁 Media & Files")
st.sidebar.markdown("# Page 5 📁 Media & Files")

st.markdown("This page demonstrates images, audio, video, file upload/processing, and downloads.")
st.markdown("""
---
""")

root = Path(".")

# Images
st.subheader("Display an image")
image_path = root / "sunrise.jpg"
if image_path.exists():
    img = Image.open(image_path)
    st.image(img, caption="Sunrise (local file)", use_column_width=True)
else:
    st.info("Image file 'sunrise.jpg' not found in project root.")

st.markdown("""
---
""")

# Audio
st.subheader("Play audio")
audio_path = root / "sample4.ogg"
if audio_path.exists():
    st.audio(audio_path.read_bytes(), format="audio/ogg")
else:
    st.info("Audio file 'sample4.ogg' not found in project root.")

st.markdown("""
---
""")

# Video
st.subheader("Play video")
video_path = root / "sample-mp4-file.mp4"
if video_path.exists():
    st.video(video_path.read_bytes())
else:
    st.info("Video file 'sample-mp4-file.mp4' not found in project root.")

st.markdown("""
---
""")

# File uploader - CSV
st.subheader("Upload a CSV and preview")
uploaded_csv = st.file_uploader("Choose a CSV file", type=["csv"], key="csv_uploader")
if uploaded_csv is not None:
    try:
        df = pd.read_csv(uploaded_csv)
        st.write("Shape:", df.shape)
        st.dataframe(df.head(100))
        st.write("Summary:")
        st.dataframe(df.describe(include="all"))

        # Provide a downloadable processed CSV (example: first 100 rows)
        sample_df = df.head(100)
        csv_buf = io.StringIO()
        sample_df.to_csv(csv_buf, index=False)
        st.download_button(
            label="Download first 100 rows as CSV",
            data=csv_buf.getvalue(),
            file_name="sample_100_rows.csv",
            mime="text/csv",
        )
    except Exception as exc:
        st.error(f"Failed to read CSV: {exc}")

st.markdown("""
---
""")

# File uploader - Images with simple processing
st.subheader("Upload an image and convert to grayscale")
uploaded_img = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"], key="img_uploader")
if uploaded_img is not None:
    try:
        image = Image.open(uploaded_img)
        st.image(image, caption="Original", use_column_width=True)

        gray = image.convert("L")
        st.image(gray, caption="Grayscale", use_column_width=True)

        # Download processed image
        out_buf = io.BytesIO()
        gray.save(out_buf, format="PNG")
        st.download_button(
            label="Download grayscale PNG",
            data=out_buf.getvalue(),
            file_name="grayscale.png",
            mime="image/png",
        )
    except Exception as exc:
        st.error(f"Failed to process image: {exc}")

st.markdown("""
---
""")

# Camera input (optional; works in supported browsers)
st.subheader("Take a photo with your camera")
photo = st.camera_input("Camera input", key="camera")
if photo is not None:
    cam_img = Image.open(photo)
    st.image(cam_img, caption="Captured photo", use_column_width=True)

st.markdown("""
---
""")