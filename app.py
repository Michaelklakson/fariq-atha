import subprocess
import time
import os
from flask import Flask, render_template
import streamlit as st

# ==========================================
# 1. KODE FLASK (Membaca templates/index.html)
# ==========================================
app = Flask(__name__)

@app.route('/')
def home():
    # Data ini yang akan dikirim dan dibaca oleh {{ data.nama }}, dll di index.html kamu
    data = {
        "nama": "Fariq Attha Gifari",
        "umur": 20,
        "status": "Mahasiswa di Politeknik Caltex Riau"
    }
    return render_template('index.html', data=data)


# ==========================================
# 2. TRIK AGAR BISA JALAN DI STREAMLIT CLOUD
# ==========================================
st.set_page_config(page_title="CV Fariq Atta", layout="wide")

# Jalankan Flask di latar belakang pada port 8502
@st.cache_resource
def run_flask():
    import threading
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=8502, debug=False, use_reloader=False), daemon=True).start()

# Panggil fungsi untuk menyalakan server Flask
run_flask()

# Beri jeda 1 detik agar Flask benar-benar siap
time.sleep(1)

# Tampilkan aplikasi Flask di dalam halaman Streamlit menggunakan iframe
st.markdown("<h3 style='text-align: center; color: #4F46E5;'>Web Profile Berhasil Dihosting!</h3>", unsafe_allow_html=True)
st.components.v1.iframe("http://localhost:8502", height=700, scrolling=True)
