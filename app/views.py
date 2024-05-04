from app import app
from flask import render_template, request
from util import gpt_solve_prob, math_ocr_latex
from PIL import Image
import base64


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    image = request.files["img"]
    img = Image.open(image)

    latex_problem = math_ocr_latex(img)
    solution = gpt_solve_prob(latex_problem)
    solution_fmt = solution.split("\n")
    print(latex_problem)
    print(solution)

    return render_template("result.html", solution=solution_fmt)
