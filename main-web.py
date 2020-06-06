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
        elif (request.form["trans"] == "Sundanese - Indonesian (Boyer-Moore)"):
            return redirect(url_for("translate",sent=sentence,indotosunda=False,met="bm"))
        elif (request.form["trans"] == "Sundanese - Indonesian (RegEx)"):
            return redirect(url_for("translate",sent=sentence,indotosunda=False,met="re"))
    else:
        return render_template("index.html")
    

@app.route("/translate/<sent>/<indotosunda>/<met>",methods=["POST","GET"])
def translate(sent,indotosunda,met):
    if (request.method == "GET"):
        if (indotosunda == "True"):
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
                return render_template("translate.html",old=sent, new=result, indosunda=False)
            elif (met=="bm"):
                a = MatchWithBoyerMoore(sent,False)
                a.solve()
                result=a.translated
                return render_template("translate.html",old=sent, new=result, indosunda=False)
            elif (met=="re"):
                a = MatchWithRegex(sent,False)
                a.solve()
                result=a.translated
                return render_template("translate.html",old=sent, new=result, indosunda=False)
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
        elif (request.form["trans"] == "Sundanese - Indonesian (Boyer-Moore)"):
            return redirect(url_for("translate",sent=sentence,indotosunda=False,met="bm"))
        elif (request.form["trans"] == "Sundanese - Indonesian (RegEx)"):
            return redirect(url_for("translate",sent=sentence,indotosunda=False,met="re"))

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)