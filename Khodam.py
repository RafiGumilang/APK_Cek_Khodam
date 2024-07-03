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
        ("Anda Terlalu Suci", ["anda_terlalu_suci.jpeg"]),
        ("Ifatcu", ["ifatcu.jpg"]),
        ("Pocong Keram", ["pocong_keram.jpeg"]),
        ("Tuyul Mulet", ["tuyul_mulet.jpeg"]),
        ("Haji Thoriq", ["haji_thoriq.jpeg"]),
        ("Macan Sumbing", ["macan_sumbing.jpeg"]),
        ("Tuyul Berhijab", ["tuyul_berhijab.jpeg"]),
        ("Kunti Bogel", ["kunti_bogel.jpeg"])
    ]
    response = random.choice(responses)
    hasil = response[0]
    gambar = clean_filename(random.choice(response[1]))
    return hasil, gambar

@st.cache_data(show_spinner=False)
def load_image(image_name):
    base_path = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(base_path, "images", image_name)
    print(f"Trying to load image from: {image_path}")  # Untuk debugging
    if os.path.exists(image_path):
        return Image.open(image_path)
    print(f"Image not found: {image_path}")  # Untuk debugging
    return None

# Konfigurasi halaman
st.set_page_config(page_title="Cek Khodam", page_icon="👻", layout="wide")

# CSS untuk styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Creepster&family=Nosifer&display=swap');

    body {
        background: #1a0f30 url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='80' height='80' viewBox='0 0 80 80'%3E%3Cg fill='%23301934' fill-opacity='0.4'%3E%3Cpath fill-rule='evenodd' d='M11 0l5 20H6l5-20zm42 31a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM0 72h40v4H0v-4zm0-8h31v4H0v-4zm20-16h20v4H20v-4zM0 56h40v4H0v-4zm63-25a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm10 0a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM53 41a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm10 0a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm10 0a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm-30 0a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm-28-8a5 5 0 0 0-10 0h10zm10 0a5 5 0 0 1-10 0h10zM56 5a5 5 0 0 0-10 0h10zm10 0a5 5 0 0 1-10 0h10zm-3 46a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm10 0a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM21 0l5 20H16l5-20zm43 64v-4h-4v4h-4v4h4v4h4v-4h4v-4h-4zM36 13h4v4h-4v-4zm4 4h4v4h-4v-4zm-4 4h4v4h-4v-4zm8-8h4v4h-4v-4z'/%3E%3C/g%3E%3C/svg%3E") !important;
        background-attachment: fixed !important;
    }
    .stApp {
        background: transparent !important;
    }
    .main {
        background: rgba(26, 15, 48, 0.8) !important;
        backdrop-filter: blur(10px) !important;
        border-radius: 15px !important;
        padding: 30px !important;
        color: #e0e0e0 !important;
        border: 2px solid #4a0e0e;
        box-shadow: 0 0 20px rgba(74, 14, 14, 0.5);
    }
    h1 {
        font-family: 'Nosifer', cursive !important;
        color: #ff4b4b !important;
        text-shadow: 2px 2px 4px #000000, 0 0 20px #ff0000, 0 0 30px #ff4b4b;
    }
    .big-font {
        font-family: 'Creepster', cursive !important;
        font-size: 36px !important;
        font-weight: normal;
        color: #ffa500;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
    }
    .result-font {
        font-size: 28px !important;
        color: #ffd700;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }
    .stButton>button {
        background-color: #4a0e0e;
        color: #ffd700;
        font-family: 'Creepster', cursive !important;
        font-size: 24px;
        padding: 12px 30px;
        border-radius: 30px;
        border: 2px solid #ffd700;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    .stButton>button:hover {
        background-color: #630f0f;
        transform: translateY(-2px) scale(1.05);
        box-shadow: 0 8px 20px rgba(255,215,0,0.4);
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
        background-color: rgba(255, 255, 255, 0.1);
        color: #ffd700;
        font-family: 'Creepster', cursive !important;
        font-size: 20px;
        border-radius: 25px;
        padding: 10px 15px;
        border: 2px solid #4a0e0e;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    .stCheckbox {
        color: #ffd700;
    }
    .stMarkdown {
        color: #e0e0e0;
        font-family: Arial, sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# Ubah judul aplikasi
st.markdown("<h1 style='text-align: center; animation: pulse 2s infinite;'>🔮 Cek Khodam Mistis 👻</h1>", unsafe_allow_html=True)

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
        
        img = load_image(st.session_state.gambar)
        if img:
            st.markdown("<div class='image-container'>", unsafe_allow_html=True)
            st.image(img, caption=st.session_state.hasil, use_column_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.error(f"Maaf, gambar khodam {st.session_state.gambar} tidak tersedia saat ini.")

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

# Menutup div 'main'
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Dibuat dengan ❤️ oleh Ragum | © 2024</p>", unsafe_allow_html=True)