from flask import Flask, render_template

app = Flask(__name__, static_url_path='/')

@app.route('/')
def serve_html():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)