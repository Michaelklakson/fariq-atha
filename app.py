import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    data = {
        "nama": "Fariq Attha Gifari",
        "umur": 20,
        "status": "Mahasiswa di Politeknik Caltex Riau"
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    # Ambil port dari server hosting secara dinamis, jika tidak ada gunakan 5000 (default)
    port = int(os.environ.get("PORT", 5000))
    # Set host ke '0.0.0.0' agar aplikasi bisa diakses dari luar server lokal
    app.run(host='0.0.0.0', port=port)
