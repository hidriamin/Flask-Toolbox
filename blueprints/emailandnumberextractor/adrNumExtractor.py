import re
from flask import Blueprint, render_template, request

adrNumExtractor_bp = Blueprint(
    "adrNumExtractor_bp", __name__, template_folder="templates", static_folder="static", url_prefix="/extractor")


@adrNumExtractor_bp.route("/", methods=["GET", "POST"])
def extractor():
    if request.method == "POST":
        # Phone number regex
        phoneRegex = re.compile(r"""(
        (\+\s?216 | 00\s?216 | \(\+\s?216\) | \(00\s?216\))? #Tunisian country code
        \s?\d\s?-?\d\s?-?\d\s?-?\d\s?-?\d\s?-?\d\s?-?\d\s?-?\d\s?-? #number
        )""", re.VERBOSE)
        # Email regex
        emailRegex = re.compile(r"""[a-zA-Z0-9]+ #first part
        @ #@
        [a-zA-Z0-9.\-]+ #domain name(first part)
        \. #dot
        [a-zA-Z0-9.\-]{2,3} #domain name last part (exemple: .com .net)""", re.VERBOSE)

        # get the user text
        text = request.form["user_text"]

        # match the phone number and email regex
        phoneNumberMatch = phoneRegex.findall(text)
        emailAdresses = emailRegex.findall(text)

        # only use the first item in each tuple because it's the full number
        phoneNumbers = []
        for num in phoneNumberMatch:
            phoneNumbers.append(num[0])

        # format the list
        phoneNumberList = "\n".join(phoneNumbers)
        emailList = ",\n".join(emailAdresses)

        return render_template("extractor.html", phoneNumberList=phoneNumberList, emailList=emailList)

    return render_template("extractor.html", phoneNumberList="", emailList="")
