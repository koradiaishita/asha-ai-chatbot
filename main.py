import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    """Render the index.html template with the embedded chatbot."""
    return render_template("index.html")

@app.route("/chatbot")
def chatbot():
    """Render the standalone chatbot.html file."""
    return send_from_directory('.', 'chatbot.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
