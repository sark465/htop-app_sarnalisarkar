from flask import Flask, jsonify, render_template_string
import os
import subprocess
from datetime import datetime
import pytz
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to the htop App</h1><p>Visit <a href='/htop'>/htop</a> to see server information.</p>"

@app.route('/htop')
def htop():
    try:
        # Get server time in IST
        tz = pytz.timezone('Asia/Kolkata')
        server_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

        # Get the system username
        username = os.getenv('USER') or os.getlogin()

        # Get the top output
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')

        # Log the request
        logging.info("Received request for /htop")

        # Render the output in HTML
        return render_template_string(f"""
        <html>
            <body>
                <h1>Name: Sarnali Sarkar</h1>
                <h2>Username: {username}</h2>
                <h2>Server Time (IST): {server_time}</h2>
                <h2>TOP output:</h2>
                <pre>{top_output}</pre>
            </body>
        </html>
        """)
    except Exception as e:
        logging.error("Error while processing /htop: %s", e)
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
