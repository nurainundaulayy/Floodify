import streamlit as st
from PIL import Image
import time
import requests
from streamlit_lottie import st_lottie
# from PIL import Image


# --- ASSETS ---
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_animation_chatbot = "https://lottie.host/62b484e8-e1cc-4e2a-bf9d-86bd6cfbb3a6/Gd8ImoizWM.json"
lottie_animation_cover = "https://lottie.host/8ce8c83b-97d6-462a-8018-1d62ada90eae/Gs3hychMqc.json"

img_stunting = "images/stunting1.png"

# Pengaturan Halaman
st.set_page_config(page_title="Info Stunting", layout="wide")

# --- HEADER SECTION ---
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("Pahami Stunting, Selamatkan Generasi Emas!")
    with right_column:
        st_lottie(lottie_animation_cover, height=200, key="cover-animation")

# Garis Pembatas
st.markdown("---")

# Section 1: Apa itu Stunting?
st.markdown("### Apa itu Stunting?")
col1, col2 = st.columns([1, 2], vertical_alignment="center")
with col1:
    st.image(img_stunting, use_container_width=True)
with col2:
    st.markdown(
        """
        Stunting adalah gangguan pertumbuhan serius yang dialami anak-anak, ditandai dengan tinggi badan yang berada di bawah standar yang ditetapkan oleh World Health Organization (WHO). 
        Stunting dapat  terjadi  mulai  janin  masih  dalam  kandungan  dan  baru nampak  saat  anak  berusia  dua  tahun (Kementerian  Kesehatan  Republik  Indonesia,  2016).
        Kondisi ini umumnya disebabkan oleh kekurangan gizi kronis dan infeksi berulang yang menghambat pertumbuhan fisik optimal. 
        """
    )

# Garis Pembatas
st.markdown("---")

# Section 2: Fakta tentang Stunting
st.markdown("### Prevalensi Stunting")
fact_col1, fact_col2, fact_col3 = st.columns(3)
with fact_col1:
    st.metric("Global", "22,3%")
with fact_col2:
    st.metric("Indonesia", "27,7%")
with fact_col3:
    st.metric("Target Indonesia", "14%")

# Garis Pembatas
st.markdown("---")

# Section 3: Pentingnya 1000 HPK (Hari Pertama Kehidupan)
st.markdown("### Pentingnya 1000 HPK (Hari Pertama Kehidupan)")
causes = {
    "1000 HPK adalah golden period pertumbuhan anak": (
        "Masa seribu hari pertama kehidupan (1000 HPK), yang mencakup periode dari kehamilan hingga dua tahun pertama, merupakan golden period dalam perkembangan anak (Pusat Studi Pangan dan Gizi  Universitas Gadjah Mada, 2022). Pada masa ini, organ-organ penting seperti otak dan jantung mulai terbentuk. Selain itu, pertumbuhan fisik serta perkembangan kognitif berlangsung sangat pesat. Jika asupan gizi selama 1000 HPK tidak mencukupi, anak dapat mengalami gangguan pertumbuhan yang serius, termasuk stunting (Sudargo et al., 2018). Oleh karena itu, intervensi gizi dan kesehatan pada periode ini sangat menentukan kualitas hidup anak di masa depan."
    ),
    "Pemenuhan gizi ibu sejak masa kehamilan": (
        "Di Indonesia, kenaikan berat badan ibu yang tidak memadai dan kurangnya zat gizi selama kehamilan "
        "menyumbang 6 persen bayi dengan berat badan lahir rendah (BBLR). Bayi-bayi ini kemungkinan tidak mampu "
        "mengejar pertumbuhan dengan berat badan yang kurang, dimana kelahiran prematur menyebabkan 1 dari 4 anak "
        "mengalami stunting. Di sisi lain, kelebihan berat badan dan obesitas selama kehamilan meningkatkan risiko "
        "lahir mati dan kelahiran prematur. Gizi ibu yang baik dapat membantu memastikan bayi sehat sejak lahir dan "
        "mencegah berat badan lahir rendah dan stunting. "
        "[Pelajari lebih lanjut](https://www.unicef.org/indonesia/id/media/2686/file/Kerangka-Aksi-Gizi-Ibu-2019.pdf)"
    ),
    "Asupan ASI eksklusif selama 6 bulan pertama": (
        "Air Susu Ibu (ASI) merupakan sumber gizi utama bagi bayi pada 6 bulan pertama kehidupan. "
        "ASI eksklusif memberikan nutrisi seimbang yang meningkatkan daya tahan tubuh dan mendukung perkembangan bayi, "
        "serta melindunginya dari infeksi dan penyakit. Selain itu, untuk pencegahan stunting, setelah melahirkan, ibu dianjurkan melakukan inisiasi menyusu dini (IMD) dan memberikan kolostrum, yaitu ASI pertama setelah melahirkan yang kaya akan nutrisi."
    ),
    "Pemberian makanan pendamping ASI yang bergizi": (
        "Setelah usia 6 bulan, bayi membutuhkan makanan pendamping ASI (MPASI) yang kaya nutrisi "
        "seperti protein, lemak sehat, vitamin, dan mineral untuk mendukung kebutuhan gizi yang terus meningkat "
        "dan memastikan pertumbuhan yang optimal.Pemberian makanan pendamping ASI yang dimaksut ialah usaha mengenalkan makanan padat atau semi padat untuk melengkapi pemberian ASI dan berlangsung antara usia 6 bulan hingga 2 tahun. Makanan Pendamping ASI (MP ASI) yang tepat dan sesuai rekomendasi dapat membantu mencegah stunting. Di Indonesia sendiri, kasus stunting mengalami peningkatan mulai usia 6 bulan. Hal ini dikarenakan, ASI saja tidak dapat memenuhi seluruh kebutuhan energi, protein, vitamin dan mineral di usia tersebut. "
    ),
    "Pemeriksaan kesehatan dan imunisasi rutin": (
        "Pemeriksaan rutin memastikan bahwa bayi tumbuh sesuai standar kesehatan yang ideal. "
        "Imunisasi juga penting untuk melindungi anak dari berbagai penyakit yang dapat mengganggu pertumbuhan "
        "dan perkembangannya, serta mengurangi risiko stunting. Oleh karena itu, pastikan bayi mendapatkan imunisasi "
        "sesuai jadwal yang telah ditentukan\n\n "
        "Berikut informasi jadwal imunisasi berdasarkan Peraturan Menteri Kesehatan RI Nomor 12 Tahun 2017 Tentang Penyelenggaraan Imunisasi:\n\n"
        "- Bayi berumur 1 bulan: BCG dan Polio 1\n"
        "- Bayi berumur 2 bulan: DPT-HB-Hib 1 dan Polio 2\n"
        "- Bayi berumur 3 bulan: DPT-HB-Hib 2 dan Polio 3\n"
        "- Bayi berumur 4 bulan: DPT-HB-Hib 3, Polio 4, dan IPV\n"
    )
}

# Menampilkan informasi tentang setiap cause dengan expander dan progress bar
for i, (cause, explanation) in enumerate(causes.items()):
    with st.expander(cause):
        st.write(explanation)
        st.progress((i + 1) * 20)

# --- CHATBOT ---
with st.container():
    left_column, right_column = st.columns((2,1), vertical_alignment="center")
    with left_column:
        st.header("Ingin tau lebih banyak? Tanyakan pada Chatbot kami!")
        st.markdown("<br>", unsafe_allow_html=True)  # Adds a line break
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
        <a class="hover-link" href="https://nutricare-1000-by-nutriteam.streamlit.app/chatbot" target="_blank">
            Tanya Chatbot
        </a>
        ''',
        unsafe_allow_html=True
        )
    with right_column:
        st_lottie(lottie_animation_chatbot, height=300, key="dashboard-animation")

