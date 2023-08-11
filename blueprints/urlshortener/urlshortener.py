from flask import Flask, render_template, request, Blueprint
import pyshorteners
import pyperclip

urlshortener_bp = Blueprint("urlshortener_bp", __name__,
                            template_folder="templates", static_folder="static")


@urlshortener_bp.route('/urlshortener', methods=["GET", "POST"])
def urlshortener():
    # Gets the url from the form
    if request.method == "POST":
        url = request.form["url"]
        # Url gets shortened
        shortUrl = pyshorteners.Shortener().tinyurl.short(url)
        # Return shortened Url
        return render_template("urlshortener.html", shortUrl=shortUrl)
    # Return nothing when there's no url inputted
    return render_template("urlshortener.html", shortUrl="")
