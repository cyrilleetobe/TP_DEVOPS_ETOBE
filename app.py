from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head><title>Mon App Flask</title></head>
        <body style="background-color: #f0f2f5; font-family: Arial; text-align: center; padding-top: 50px;">
            <h1 style="color: #2c3e50;">Bonjour à tous !</h1>
            <p style="font-size: 20px;">Ceci est une simple application conteneurisée avec Docker par <strong>TonNom</strong>!</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)