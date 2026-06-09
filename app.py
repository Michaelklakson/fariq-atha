import subprocess
import time
from flask import Flask, render_template
import streamlit as st

# ==========================================
# 1. BAGIAN KODE FLASK KAMU
# ==========================================
app = Flask(__name__)

@app.route('/')
def home():
    data = {
        "nama": "Fariq Attha Gifari",
        "umur": 20,
        "status": "Mahasiswa di Politeknik Caltex Riau"
    }
    return render_template('index.html', data=data)


# ==========================================
# 2. TRIK AGAR BISA JALAN DI STREAMLIT CLOUD
# ==========================================
# Streamlit Cloud akan selalu mengeksekusi file ini. 
# Kita gunakan Streamlit untuk memicu jalannya Flask.

st.set_page_config(page_title="Flask App on Streamlit", layout="wide")

# Jalankan Flask di latar belakang (background process) pada port 8502
@st.cache_resource
def run_flask():
    # Menjalankan Flask menggunakan thread terpisah agar tidak mengunci Streamlit
    import threading
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=8502, debug=False, use_reloader=False), daemon=True).start()

# Panggil fungsi untuk menyalakan server Flask
run_flask()

# Beri jeda 1 detik agar Flask benar-benar siap
time.sleep(1)

# Tampilkan aplikasi Flask di dalam halaman Streamlit menggunakan iframe
st.title("Aplikasi Flask Berhasil Dihosting!")
st.write("Berikut adalah tampilan dari Flask app kamu:")
st.components.v1.iframe("http://localhost:8502", height=600, scrolling=True)
