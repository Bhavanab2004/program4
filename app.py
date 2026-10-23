from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Flask Docker App</title>
        </head>
        <body style="font-family: Arial; text-align: center; margin-top: 100px;">
            <h1>Hello from Python Flask!</h1>
            <h2>Running inside Docker on Ubuntu 🚀</h2>
            <p>Your Dockerized Flask application is working.</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
