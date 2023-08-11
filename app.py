from flask import Flask, Blueprint, render_template
from blueprints.emailandnumberextractor.adrNumExtractor import adrNumExtractor_bp
from blueprints.urlshortener.urlshortener import urlshortener_bp
app = Flask(__name__)
app.register_blueprint(adrNumExtractor_bp)
app.register_blueprint(urlshortener_bp)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
