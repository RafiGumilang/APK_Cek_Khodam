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

# CSS untuk styling (tidak berubah)
st.markdown("""
<style>
    /* ... (CSS yang sama seperti sebelumnya) ... */
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
        
        img = load_image(st.session_state.gambar)
        if img:
            st.markdown("<div class='image-container'>", unsafe_allow_html=True)
            st.image(img, caption=st.session_state.hasil, use_column_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.error(f"Maaf, gambar khodam {st.session_state.gambar} tidak tersedia saat ini.")

# Tambahan: Fun Facts tentang Khodam (tidak berubah)
if st.checkbox("Tampilkan Fun Facts tentang Khodam"):
    # ... (kode yang sama seperti sebelumnya) ...

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Dibuat dengan ❤️ oleh Ragum | © 2024</p>", unsafe_allow_html=True)