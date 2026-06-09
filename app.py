import streamlit as st

# Set agar tampilan penuh (wide)
st.set_page_config(page_title="CV Fariq Atta", layout="centered")

# Data Profil
data = {
    "nama": "Fariq Attha Gifari",
    "umur": 20,
    "status": "Mahasiswa di Politeknik Caltex Riau"
}

# Memasukkan CSS Tailwind dan HTML langsung ke Streamlit
st.html(f"""
    <script src="https://cdn.tailwindcss.com"></script>
    <div class="flex items-center justify-center p-4">
        <div class="bg-white shadow-2xl rounded-3xl p-10 max-w-lg w-full text-center border border-gray-100">
            <div class="mb-6">
                <img src="https://via.placeholder.com/150" 
                     class="w-36 h-36 mx-auto rounded-full border-4 border-indigo-500 shadow-lg">
            </div>

            <h1 class="text-3xl font-bold text-gray-800">
                {data['nama']}
            </h1>

            <p class="text-indigo-600 font-medium mt-2">
                {data['status']}
            </p>

            <div class="mt-4">
                <span class="bg-indigo-100 text-indigo-700 px-4 py-1 rounded-full text-sm">
                    {data['umur']} Tahun
                </span>
            </div>

            <div class="border-t my-6"></div>

            <div class="space-y-2 text-gray-600">
                <p>🎓 Mahasiswa aktif</p>
                <p>📍 Politeknik Caltex Riau</p>
            </div>

            <div class="mt-8">
                <a href="#" class="bg-indigo-600 text-white px-6 py-2 rounded-full shadow hover:bg-indigo-700 transition inline-block">
                    Contact Me
                </a>
            </div>
        </div>
    </div>
""")
