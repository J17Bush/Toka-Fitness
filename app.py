from flask import Flask, render_template
from datetime import timedelta ,datetime

app = Flask(__name__)
app.secret_key ="hello"
import routes
app.permanent_session_lifetime = timedelta(5)


if __name__ == "__main__":
    app.run(debug=True)

 