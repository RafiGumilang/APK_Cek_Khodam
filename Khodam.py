import streamlit as st
import random
import os
from PIL import Image

# Fungsi untuk membersihkan nama file dari karakter tidak diinginkan
def clean_filename(filename):
    return filename.replace(" ", "_").lower()

# Fungsi untuk mengecek keberadaan khodam
def cek_khodam(nama):
    responses = [
        ("Anda Terlalu Suci", ["Anda_Terlalu_Suci.jpeg"]),
        ("Ifatcu", ["Ifatcu.jpg"]),
        ("Pocong Keram", ["Pocong_Keram.jpeg"]),
        ("Tuyul Mulet", [ "Tuyul_Mulet.jpeg"]),
        ("Haji Thoriq", ["Haji_Thoriq.jpeg"]),
        ("Macan Sumbing", ["macan_sumbing.jpeg"]),
        ("Tuyul Berhijab", ["Tuyul_Berhijab.jpeg"]),
        ("Kunti Bogel", ["Kunti_Bogel.jpeg"])
    ]
    response = random.choice(responses)
    hasil = response[0]
    gambar = clean_filename(random.choice(response[1]))
    return hasil, gambar

@st.cache_data(show_spinner=False)
def load_image(image_path):
    if os.path.exists(image_path):
        return Image.open(image_path)
    return None

# Konfigurasi halaman
st.set_page_config(page_title="Cek Khodam", page_icon="👻", layout="wide")

# CSS untuk styling
st.markdown("""
<style>
    body {
        background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
        background-attachment: fixed;
    }
    .stApp {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 10px;
        padding: 20px;
    }
    .big-font {
        font-size:30px !important;
        font-weight: bold;
        color: #1E1E1E;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .result-font {
        font-size:24px !important;
        color: #4A4A4A;
    }
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
        font-size: 18px;
        padding: 10px 24px;
        border-radius: 25px;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    .stButton>button:hover {
        background-color: #E04141;
        transform: translateY(-2px);
        box-shadow: 0 8px 15px rgba(0,0,0,0.3);
    }
    .image-container {
        text-align: center;
        animation: fadeIn 2s;
    }
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    @keyframes pulse {
        0% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.05);
        }
        100% {
            transform: scale(1);
        }
    }
    .stTextInput>div>div>input {
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 25px;
        padding: 10px 15px;
        border: none;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Judul aplikasi dengan animasi
st.markdown("<h1 style='text-align: center; color: #FF4B4B; animation: pulse 2s infinite;'>🔮 Cek Khodam 👻</h1>", unsafe_allow_html=True)

# Dua kolom untuk input dan hasil
col1, col2 = st.columns(2)

with col1:
    st.markdown("<p class='big-font'>Masukkan Nama Anda:</p>", unsafe_allow_html=True)
    nama = st.text_input("", key="nama_input")
    if st.button("Cek Khodam Anda"):
        if nama:
            with st.spinner('Sedang menghubungi alam gaib...'):
                hasil, gambar = cek_khodam(nama)
                st.session_state.hasil = hasil
                st.session_state.gambar = gambar
                st.session_state.cek_dilakukan = True

with col2:
    if 'cek_dilakukan' in st.session_state and st.session_state.cek_dilakukan:
        st.markdown(f"<p class='result-font'>Hasil pengecekan untuk <span style='color: #FF4B4B;'>{nama}</span>:</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='big-font'>{st.session_state.hasil}</p>", unsafe_allow_html=True)
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "images", st.session_state.gambar)
        img = load_image(image_path)
        if img:
            st.markdown("<div class='image-container'>", unsafe_allow_html=True)
            st.image(img, caption=st.session_state.hasil, use_column_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.error("Maaf, gambar khodam tidak tersedia saat ini.")

# Tambahan: Fun Facts tentang Khodam
if st.checkbox("Tampilkan Fun Facts tentang Khodam"):
    st.write("---")
    st.subheader("Fun Facts tentang Khodam")
    facts = [
        "Khodam adalah makhluk gaib dalam kepercayaan tradisional Indonesia.",
        "Beberapa orang percaya khodam bisa membantu dalam berbagai urusan.",
        "Ada berbagai jenis khodam dengan kemampuan yang berbeda-beda.",
        "Khodam sering dikaitkan dengan benda-benda pusaka.",
        "Dalam beberapa tradisi, khodam dianggap bisa diwariskan."
    ]
    for fact in facts:
        st.markdown(f"- {fact}")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Dibuat dengan ❤️ oleh Ragum | © 2024</p>", unsafe_allow_html=True)