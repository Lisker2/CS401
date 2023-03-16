from flask import Flask,redirect, request,url_for,jsonify,render_template,make_response,json
import pandas as pd 
import os
import time

app = Flask(__name__)
model = pd.read_csv("data/test.csv")
#model = pd.read_csv("Project2/Flask/test.csv")
version = os.environ['version']
date = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

n = len(model["antecedents"])
for i in range(n):
    model["antecedents"][i]=model["antecedents"][i].strip("[]").split(",")
    model["consequents"][i]=model["consequents"][i].strip("[]").split(",")
    for j in range(len(model["antecedents"][i])):
        model["antecedents"][i][j] = model["antecedents"][i][j].strip("' ''.")
    for j in range(len(model["consequents"][i])):
        model["consequents"][i][j] = model["consequents"][i][j].strip(" ''.")


@app.route("/",methods=["POST","GET"])
def hello_world():
    if request.method == "POST":
        res = []
        d = request.get_json(force=True)
        data = d["songs"]
        n = len(model["antecedents"])
        
        for i in range(n):
            indata = True
            for j in model["antecedents"][i]:
                if j not in data:
                    indata = False

            if indata:
                for k in model["consequents"][i]:
                    if k not in res and k not in data:
                        res.append(k)

        json_res = {
            "songs":res,
            "version":version,
            "model_date":date
        }
        return jsonify(json_res)
    return "Hello"


@app.route("/req",methods=["POST","GET"])
def req():
    if request.method == "POST":
        data = request.form.get("name").split(",")
        res = []
        n = len(model["antecedents"])

        for i in range(n):
            indata = True
            for j in model["antecedents"][i]:
                if j not in data:
                    indata = False

            if indata:
                for k in model["consequents"][i]:
                    if k not in res and k not in data:
                        res.append(k)

        return render_template("front.html",res=res,version = version,date=date)
    return render_template("front.html")

if __name__ == "__main__":
    app.run(None,30507,None,True)