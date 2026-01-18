from flask import Flask
from flask import redirect,url_for,render_template
from flask import request
#
app=Flask(__name__,
          template_folder="templates",
          static_folder="static")
#
@app.route("/thankyou/get1=<formget1>")
def thankyou(formget1):
    strFormGet1=f"{formget1}"
    strOut=f"Thank you, "+strFormGet1+"<BR>"
    strOut=strOut+"This is a response.<BR>"
    strOut=strOut+"Welcome.<BR>"
    return strOut
#
@app.route("/formget",methods=["POST","GET"])
def formget():
    if(request.method == "POST"):
        strFormGet1=request.form["formget1"]
    else:
        strFormGet1=request.args.get("formget1")
#
    dictIn=dict()
    dictIn["FormGet1"]=strFormGet1
# 
    strOut = redirect(url_for("thankyou",
                        formget1=strFormGet1))
    return strOut
#
@app.route("/")
def home():
    return render_template("index.html")
#
if(__name__ == "__main__"):
    app.run(host='0.0.0.0',port=80,debug=True)
#
