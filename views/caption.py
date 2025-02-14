# Importing Libraries
import streamlit as st
import time
from PIL import Image
# from transformers import BlipProcessor, BlipForConditionalGeneration
from transformers import AutoTokenizer, PaliGemmaForConditionalGeneration, PaliGemmaProcessor, AutoModelForImageTextToText
import torch
import os

# Config
page_icon = Image.open("images/icon.png")
st.set_page_config(layout="centered", page_title="Floodify - Captioning", page_icon=page_icon)

# Initial State
def initial_state():
    if 'image' not in st.session_state:
        st.session_state['image'] = None
    if 'uploading_way' not in st.session_state:
        st.session_state['uploading_way'] = None
    if 'caption_result' not in st.session_state:
        st.session_state['caption_result'] = None

initial_state()

# New Line
def new_line(n=1):
    st.markdown("<br>" * n, unsafe_allow_html=True)

# Progress Bar
def progress_bar():
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.0002)
        my_bar.progress(percent_complete + 1)

# Logo 
col1, col2, col3 = st.columns([0.25,1,0.25])
col2.image("images/FLOODIFY2.png", width=200)
new_line(2)

# Description
st.markdown("""Welcome to Floodify - Captioning, the platform for generating captions for your flood images!""", unsafe_allow_html=True)
st.divider()

# Dataframe selection
st.markdown("<h2 align='center'> <b> Upload Your Image</b> </h2>", unsafe_allow_html=True)
new_line(1)
st.write("Upload an image to generate a caption. Supported formats: **jpg, jpeg, png**.")
new_line(1)

# Uploading Way
uploading_way = st.session_state.uploading_way
col1, col2, col3 = st.columns(3,gap='large')

# Upload
def upload_click(): st.session_state.uploading_way = "upload"
col1.markdown("<h5 align='center'> Upload File", unsafe_allow_html=True)
col1.button("Upload File", key="upload_file", use_container_width=True, on_click=upload_click)

# Select    
def select_click(): st.session_state.uploading_way = "select"
col2.markdown("<h5 align='center'> Select from Ours", unsafe_allow_html=True)
col2.button("Select from Ours", key="select_from_ours", use_container_width=True, on_click=select_click)

# URL
def url_click(): st.session_state.uploading_way = "url"
col3.markdown("<h5 align='center'> Write URL", unsafe_allow_html=True)
col3.button("Write URL", key="write_url", use_container_width=True, on_click=url_click)

# No Data
if st.session_state.image is None:
    # Upload
    if uploading_way == "upload":
        uploaded_file = st.file_uploader("Upload the Image", type=["jpg", "jpeg", "png"])
        if uploaded_file:
            image = Image.open(uploaded_file)
            st.session_state.image = image
            st.image(image, caption="Uploaded Image", use_container_width=True)

    # Select
    elif uploading_way == "select":
        selected = st.selectbox("Select Image", ["Select", "Image1", "Image2", "Image3"])
        if selected == "Image1":
            st.session_state.image = "data/image_219.jpg"
        elif selected == "Image2":
            st.session_state.image = "data/image_292.jpg"
        elif selected == "Image3":
            st.session_state.image = "data/image_313.jpg"
        if st.session_state.image:
            st.image(st.session_state.image, caption="Selected Image", use_container_width=True)

    # URL
    elif uploading_way == "url":
        url = st.text_input("Enter URL")
        if url:
            st.session_state.image = url
            st.image(url, caption="Image from URL", use_container_width=True)

    new_line()
    st.markdown("<h2 align='center'>  ✨ Generate Caption </h2>", unsafe_allow_html=True)

# Captioning PaliGemma
def generate_caption(image_path):
    try:
        processor = PaliGemmaProcessor.from_pretrained("google/paligemma-3b-mix-224")
        model = PaliGemmaForConditionalGeneration.from_pretrained("google/paligemma-3b-mix-224", torch_dtype=torch.bfloat16)

        image = Image.open(image_path).convert("RGB")
        inputs = processor(image, return_tensors="pt")
        input_text = "<image> caption: "
        inputs = processor(text=input_text, images=image,
                       padding="longest", do_convert_rgb=True, return_tensors="pt")
        out = model.generate(**inputs, max_length=496)
        caption = processor.decode(out[0], skip_special_tokens=True)

        return caption
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Tombol Caption
caption_button = st.button("Generate Caption", use_container_width=True)

# Aksi setelah tombol ditekan
if caption_button:
    if st.session_state.image:
        st.write("Generating caption...")
        progress_bar()

        # Cek tipe data
        if isinstance(st.session_state.image, Image.Image):
            image_path = "temp_image.jpg"
            st.session_state.image.save(image_path)
        else:
            image_path = st.session_state.image
        
        # Captioning dengan PaliGemma
        caption_result = generate_caption(image_path)
        
        # Tampilkan hasil caption
        if caption_result:
            st.session_state.caption_result = caption_result
            st.markdown(f"<h3> Caption Result: </h3><p>{caption_result}</p>", unsafe_allow_html=True)
            st.success("Caption generation complete!")
    else:
        st.warning("Please upload an image first!")
