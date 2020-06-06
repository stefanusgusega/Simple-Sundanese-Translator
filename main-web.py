from flask import Flask,redirect,url_for,render_template,request
from BoyerMoore import MatchWithBoyerMoore
from KMP import MatchWithKMP
from Regex import MatchWithRegex

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():
    # return render_template("index.html")
    if (request.method == "POST"):
        sentence = request.form["sent"]
        if (request.form["trans"] == "Indonesian - Sundanese (KMP)"):
            return redirect(url_for("translate",sent=sentence,indotosunda=True,met="kmp"))
        elif (request.form["trans"] == "Indonesian - Sundanese (Boyer-Moore)"):
            return redirect(url_for("translate",sent=sentence,indotosunda=True,met="bm"))
        elif (request.form["trans"] == "Indonesian - Sundanese (RegEx)"):
            return redirect(url_for("translate",sent=sentence,indotosunda=True,met="re"))
        elif (request.form["trans"] == "Sundanese - Indonesian (KMP)"):
            return redirect(url_for("translate",sent=sentence,indotosunda=False,met="kmp"))
        elif (request.form["trans"] == "Sundanese - Indonesian (BM)"):
            return redirect(url_for("translate",sent=sentence,indotosunda=False,met="bm"))
        elif (request.form["trans"] == "Sundanese - Inedonesian (RegEx)"):
            return redirect(url_for("translate",sent=sentence,indotosunda=False,met="re"))
    else:
        return render_template("index.html")
    

@app.route("/translate/<sent>/<indotosunda>/<met>",methods=["POST","GET"])
def translate(sent,indotosunda,met):
    if (request.method == "GET"):
        if (indotosunda):
            if (met == "kmp"):
                a = MatchWithKMP(sent,True)
                a.solve()
                result=a.translated
                return render_template("translate.html",old=sent, new=result, indosunda=indotosunda)
            elif (met=="bm"):
                a = MatchWithBoyerMoore(sent,True)
                a.solve()
                result=a.translated
                return render_template("translate.html",old=sent, new=result, indosunda=indotosunda)
            elif (met=="re"):
                a = MatchWithRegex(sent,True)
                a.solve()
                result=a.translated
                return render_template("translate.html",old=sent, new=result, indosunda=indotosunda)
        else:
            if (met == "kmp"):
                a = MatchWithKMP(sent,False)
                a.solve()
                result=a.translated
                return render_template("translate.html",old=sent, new=result, indosunda=indotosunda)
            elif (met=="bm"):
                a = MatchWithBoyerMoore(sent,False)
                a.solve()
                result=a.translated
                return render_template("translate.html",old=sent, new=result, indosunda=indotosunda)
            elif (met=="re"):
                a = MatchWithRegex(sent,False)
                a.solve()
                result=a.translated
                return render_template("translate.html",old=sent, new=result, indosunda=indotosunda)
    else:
        sentence = request.form["sent"]
        if (request.form["trans"] == "Indonesian - Sundanese (KMP)"):
            return redirect(url_for("translate",sent=sentence,indotosunda=True,met="kmp"))
        elif (request.form["trans"] == "Indonesian - Sundanese (Boyer-Moore)"):
            return redirect(url_for("translate",sent=sentence,indotosunda=True,met="bm"))
        elif (request.form["trans"] == "Indonesian - Sundanese (RegEx)"):
            return redirect(url_for("translate",sent=sentence,indotosunda=True,met="re"))
        elif (request.form["trans"] == "Sundanese - Indonesian (KMP)"):
            return redirect(url_for("translate",sent=sentence,indotosunda=False,met="kmp"))
        elif (request.form["trans"] == "Sundanese - Indonesian (BM)"):
            return redirect(url_for("translate",sent=sentence,indotosunda=False,met="bm"))
        elif (request.form["trans"] == "Sundanese - Inedonesian (RegEx)"):
            return redirect(url_for("translate",sent=sentence,indotosunda=False,met="re"))
    # if (no == 1):
    #     a = MatchWithKMP(sent,False)
    #     a.solve()
    #     result=a.translated
    #     return f"<h1>{result}</h1>"
    # elif (no == 2):
    #     a = MatchWithKMP(sent,True)
    #     a.solve()
    #     sent=a.translated
    #     return f"<h1>{sent}</h1>"
    # elif (no == 3):
    #     a = MatchWithKMP(sent,True)
    #     a.solve()
    #     sent=a.translated
    #     return f"<h1>{sent}</h1>"
    # elif (no == 4):
    #     a = MatchWithKMP(sent,False)
    #     a.solve()
    #     sent=a.translated
    #     return f"<h1>{a.translated}</h1>"
    # elif (no == 5):
    #     a = MatchWithBoyerMoore(sent,False)
    #     a.solve()
    #     sent=a.translated
    #     return f"<h1>{a.translated}</h1>"
    # elif (no == 6):
    #     a = MatchWithKMP(sent,True)
    #     a.solve()
    #     sent=a.translated
    #     return f"<h1>{sent}</h1>"
    # else:
    #     return f"<h1>{sent}</h1>"


@app.route("/login", methods=["POST","GET"])
def login():
    if (request.method == "POST"):
        user = request.form["nm"]
        return redirect(url_for("user",usr=user))
    else:
        return render_template("login.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

@app.route("/test")
def test():
    return render_template("new.html")

# @app.route("/<name>")
# def user(name):
#     return f"Hello {name}"

# @app.route("/admin")
# def admin():
#     return redirect(url_for("user", name="Admin!"))
if __name__ == "__main__":
    app.run(debug=True)