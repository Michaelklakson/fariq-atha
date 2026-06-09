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
    app.run(debug=True, port=3000)