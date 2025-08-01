from flask import Blueprint, render_template, request
from .scraper import fetch_case_data

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    case_data = None
    error = None
    if request.method == "POST":
        case_type = request.form["case_type"]
        case_number = request.form["case_number"]
        filing_year = request.form["filing_year"]

        try:
            case_data = fetch_case_data(case_type, case_number, filing_year)
        except Exception as e:
            error = str(e)

    return render_template("index.html", case_data=case_data, error=error)
