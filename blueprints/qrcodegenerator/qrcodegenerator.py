from flask import Blueprint, render_template
import pyqrcode

qrcodegenerator_bp = Blueprint("qrcodegenerator_bp", __name__,
                               template_folder="templates", static_folder="static", url_prefix="/qrcodegen")


@qrcodegenerator_bp.route("/")
def qrcodegen():
    return render_template("qrcodegenerator.html")
