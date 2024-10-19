from flask import Flask
import os
from datetime import datetime
import pytz
import html

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <html>
        <body>
            <h1>Welcome to the htop App</h1>
            <p>Visit <a href="/htop">/htop</a> to see server information.</p>
        </body>
    </html>
    """

@app.route('/htop')
def htop():
    try:
        # Get server time in IST
        tz = pytz.timezone('Asia/Kolkata')
        server_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

        # Get the system username
        try:
            username = os.getlogin()  # This works for Unix/Linux
        except Exception as e:
            username = "Unable to retrieve username."

        # Static process output (for demonstration purposes)
        top_output = """
        PID    NAME                USERNAME
        1      init               root
        2      kthreadd           root
        3      rcu_sched          root
        4      ksoftirqd          root
        5      kworker            root
        """

        return f"""
        <html>
            <body>
                <h1>Name: Sarnali Sarkar</h1>
                <h2>Username: {html.escape(username)}</h2>
                <h2>Server Time (IST): {server_time}</h2>
                <h2>Process List:</h2>
                <pre>{html.escape(top_output)}</pre>
            </body>
        </html>
        """
    except Exception as e:
        return f"<h1>Internal Server Error</h1><p>{html.escape(str(e))}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
