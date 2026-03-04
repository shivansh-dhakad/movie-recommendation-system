from flask import Flask, render_template
from flask_cors import CORS

from controller.loading_page import loading_bp
from controller.recommendor_system import recommendor_bp
app = Flask(__name__)
app.secret_key = "secret123"
CORS(app)
# register controller
app.register_blueprint(loading_bp)
app.register_blueprint(recommendor_bp)
@app.route("/")
def home():
    return render_template("loading_screen.html") 

@app.route("/recommendor")
def recommendor():
    return render_template("recommendor.html")

if __name__ == "__main__":
    app.run(debug=True)