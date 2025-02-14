# Importing Libraries
import streamlit as st
import time
from PIL import Image
from ultralytics import YOLO
import torch
from transformers import PaliGemmaForConditionalGeneration, PaliGemmaProcessor
import glob
import os

# Config
page_icon = Image.open("images/icon.png")
st.set_page_config(layout="centered", page_title="Floodify - Detect & Caption", page_icon=page_icon)

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
col1, col2, col3 = st.columns([0.25, 1, 0.25])
col2.image("images/FLOODIFY2.png", width=200)
new_line(2)

# Description
st.markdown("""Welcome to Floodify - Detect & Caption, the platform for detecting gender and generating captions for flood images!""", unsafe_allow_html=True)
st.divider()

# Uploading Way
uploading_way = st.session_state.uploading_way
col1, col2, col3 = st.columns(3, gap='large')

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
        selected = st.selectbox("Select Image", ["Select", "Image1", "Image2", "Image3", "Image4"])
        if selected == "Image1":
            st.session_state.image = "data/image_219.jpg"
        elif selected == "Image2":
            st.session_state.image = "data/image_292.jpg"
        elif selected == "Image3":
            st.session_state.image = "data/image_313.jpg"
        elif selected == "Image4":
            st.session_state.image = "data/image_48.png"
        if st.session_state.image:
            st.image(st.session_state.image, caption="Selected Image", use_container_width=True)

    # URL
    elif uploading_way == "url":
        url = st.text_input("Enter URL")
        if url:
            st.session_state.image = url
            st.image(url, caption="Image from URL", use_container_width=True)

    new_line()
    st.markdown("<h2 align='center'>  🤖 Gender Detection & Generate Caption </h2>", unsafe_allow_html=True)

# YOLO Detection
def yolo_detect(image_path):
    try:
        model_path = os.path.join(os.getcwd(), "best.pt")
        yolo_model = YOLO(model_path)
        results = yolo_model.predict(source=image_path, conf=0.25, save=True)
        
        latest_folder = max(glob.glob('runs/detect/predict*/'), key=os.path.getmtime)
        result_image = glob.glob(f'{latest_folder}/*.jpg')[0]
        
        return result_image
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Captioning PaliGemma
def generate_caption(image_path):
    try:
        processor = PaliGemmaProcessor.from_pretrained("google/paligemma-3b-mix-224")
        model = PaliGemmaForConditionalGeneration.from_pretrained("google/paligemma-3b-mix-224", torch_dtype=torch.bfloat16)
        # model.to(torch.device("cuda" if torch.cuda.is_available() else "cpu"))

        image = Image.open(image_path).convert("RGB")
        input_text = "<image> Caption:"
        inputs = processor(text=input_text, images=image,
                           padding="longest", do_convert_rgb=True, return_tensors="pt")

        with torch.no_grad():
            outputs = model.generate(**inputs, max_length=496)
        caption = processor.batch_decode(outputs, skip_special_tokens=True)[0]

        return caption
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Tombol Detect & Caption
detect_button = st.button("Generate", use_container_width=True)

# Aksi setelah tombol ditekan
if detect_button:
    if st.session_state.image:
        st.write("Processing...")
        progress_bar()
        
        # Cek tipe data
        if isinstance(st.session_state.image, Image.Image):
            image_path = "temp_image.jpg"
            st.session_state.image.save(image_path)
        else:
            image_path = st.session_state.image
        
        # Deteksi menggunakan YOLO
        result_image = yolo_detect(image_path)
        
        # Captioning dengan PaliGemma
        caption_result = generate_caption(image_path)


        # Download
        def download(labeled_image_path, caption_text):
            # Simpan Gambar Berlabel
            labeled_image = Image.open(labeled_image_path)
            download_image_path = "labeled_image.jpg"
            labeled_image.save(download_image_path)

            # Simpan Caption sebagai File Teks
            caption_file = "caption.txt"
            with open(caption_file, "w") as file:
                file.write(caption_text)

                # Fungsi untuk Reset Input State
            def reset_input_state():
                st.session_state.uploading_way = None
                st.session_state.image = None
            
            # Tombol Download Gambar
            col1, col2 = st.columns(2, gap="small")

            with col1:
                # Tombol Download Gambar
                with open(download_image_path, "rb") as file:
                    st.download_button(
                        label="Download Labeled Image",
                        data=file,
                        file_name=download_image_path,
                        mime="image/jpeg",
                        on_click=reset_input_state
                    )
            
            with col2:
                # Tombol Download Caption
                with open(caption_file, "rb") as file:
                    st.download_button(
                        label="Download Caption",
                        data=file,
                        file_name=caption_file,
                        mime="text/plain",
                        on_click=reset_input_state
                    )

        # Tampilkan gambar berlabel dan caption
        if result_image and caption_result:
            st.image(result_image, caption="Labeled Image", use_container_width=True)
            st.markdown(f"<p>{caption_result}</p>", unsafe_allow_html=True)
            st.success("Detection and captioning complete!")
            download(result_image, caption_result)

        # Reset session state
        st.session_state.image = None
        st.session_state.uploading_way = None
    else:
        st.warning("Please upload an image first!")