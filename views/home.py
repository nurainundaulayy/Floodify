import streamlit as st
import requests
from streamlit_lottie import st_lottie
# from PIL import Image


# --- ASSETS ---
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_animation_cover = "https://lottie.host/8ce8c83b-97d6-462a-8018-1d62ada90eae/Gs3hychMqc.json"
lottie_animation_chatbot = "https://lottie.host/a84c42fb-361c-47aa-9e4e-2e367156d9da/nAfQlwchLx.json"
lottie_animation_dashboard = "https://lottie.host/fb4754d6-54bf-409c-9260-210edb861d79/4PNhXFJ1wE.json"
lottie_animation_personalchat = "https://lottie.host/8cab83e1-5342-4ec2-8dd5-f9b4dbe741bb/0Ae4Q4L0jy.json"
img_fitur1 = "https://lottie.host/1681d2b1-0892-4ba0-8729-391eaee96f5a/kcTTxJGwlr.json"
img_fitur2 = "images/fitur2_img.png"
img_fitur3 = "images/fitur3_img.png"


# --- PAGE CONFIG ---
logo = "images/FLOODIFY2.png"
st.set_page_config(page_title="FLOODIFY WEB", page_icon=logo, layout="wide")

# --- HEADER SECTION ---
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("FLOODIFY")
        st.subheader("Transform flood images into life-saving insights")
    with right_column:
        st.image(logo,width=300)

# --- OVERVIEW SECTION ---
with st.container():
    st.write("---")
    st.header("Why FLOODIFY?")
    c1, c2, c3 = st.columns(3)
    with c1:
        img_col, text_col = st.columns((1,2), vertical_alignment="center")
        with img_col:
            st_lottie(img_fitur1)
        with text_col:
            st.html("<h5>Hmmmm</h5>")
    with c2:
        img_col, text_col = st.columns((1,2), vertical_alignment="center")
        with img_col:
            st_lottie(img_fitur1)
        with text_col:
            st.html("<h5>Hmmmm</h5>")
    with c3:
        img_col, text_col = st.columns((1,2), vertical_alignment="center")
        with img_col:
            # st.image(img_fitur3)
            st_lottie(img_fitur1)
        with text_col:
            st.html("<h5>Hmmmm</h5>") 

# --- CHATBOT DESCRIPTION ---
with st.container():
    
    st.write("---")
    left_column, right_column = st.columns((1,2), vertical_alignment="center")
    with left_column:
        st_lottie(lottie_animation_chatbot, height=300, key="chatbot-animation")        
    with right_column:
        st.header("Let't try to detect!")
        st.html("<p>Hmmmmmm</p>")
        st.switch_page("views/detect.py")

        # Styling for buttons side by side using flexbox
        st.markdown(
            '''
            <style>
                .button-container {
                    display: flex;
                    gap: 20px;  /* Adds space between buttons */
                }
                .hover-link {
                    background-color: #0e1117;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    outline: 1px solid #41444c;
                    text-decoration: none;
                    transition: background-color 0.3s ease, transform 0.3s ease;
                }
                .hover-link:hover {
                    background-color: #333;
                    transform: scale(1.05);
                }
            </style>
            <div class="button-container">
                <a class="hover-link" href="https://nutricare-1000-by-nutriteam.streamlit.app/informasi" target="_blank">
                    Baca Informasi
                </a>
                <a class="hover-link" href="https://nutricare-1000-by-nutriteam.streamlit.app/chatbot" target="_blank">
                    Tanya Chatbot
                </a>
            </div>
            ''',
            unsafe_allow_html=True
        )


        
    
# --- CHATBOT DESCRIPTION ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns((1,2), vertical_alignment="center")
    with left_column:
        st_lottie(lottie_animation_personalchat, height=300, key="chatbot")
    with right_column:
        st.header("Pemantauan 1000 HPK secara Personal")
        st.html("<p>Mari memelihara 1000 Hari Pertama Kehidupan (HPK) bersama! NutriCare 1000 Chatbot siap memantau kondisi gizi ibu dan bayi, memberikan saran dan informasi, serta kemudahan konsultasi. Bersama NutriCare 1000, kita wujudkan generasi bebas stunting sejak awal kehidupan!</p>")
        st.markdown(
        '''
        <style>
            .hover-link {
                background-color: #0e1117;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                outline: 1px solid #41444c;
                text-decoration: none;
                transition: background-color 0.3s ease, transform 0.3s ease;
            }
            .hover-link:hover {
                background-color: #333;
                transform: scale(1.05);
            }
        </style>
        <a class="hover-link" href="https://t.me/nutricare1000hpk_bot" target="_blank">
            Buka Chatbot
        </a>
        ''',
        unsafe_allow_html=True
        )
        



# --- DASHBOARD DESCRIPTION ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns((2,1), vertical_alignment="center")
    with left_column:
        st.header("NutriCare 1000 Dashboard Monitoring")
        st.html("<p>Dashboard ini menyajikan visualisasi data agregat pengguna untuk memantau demografi ibu dan anak, kondisi kesehatan ibu hamil, dan tumbuh kembang anak di masa1000 Hari Pertama Kehidupan (HPK). Informasi dari dashboard ini dapat dijadikan dasar dalam perumusan kebijakan pencegahan stunting berbasis data. Yuk pantau kondisinya!</p>")
        #st.button("Buka Dashboard")
        st.markdown(
        '''
        <style>
            .hover-link {
                background-color: #0e1117;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                outline: 1px solid #41444c;
                text-decoration: none;
                transition: background-color 0.3s ease, transform 0.3s ease;
            }
            .hover-link:hover {
                background-color: #333;
                transform: scale(1.05);
            }
        </style>
        <a class="hover-link" href="https://nutricare-1000-by-nutriteam.streamlit.app/dashboard" target="_blank">
            Buka Dashboard
        </a>
        ''',
        unsafe_allow_html=True
        )
    with right_column:
        st_lottie(lottie_animation_dashboard, height=300, key="dashboard-animation")


