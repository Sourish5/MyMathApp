from flask import Flask,render_template,request
import json 
import requests

app = Flask(__name__)

@app.route("/",methods=["GET", "POST"])

def fetchData():
    if request.method == "POST":
        expression = request.form['expression']
        operation = request.form['operation']

        data = f"https://newton.now.sh/api/v2/{operation.lower()}/{expression.lower()}"
        formatted_data = requests.get(data).json()
       
        answer = formatted_data["result"]

        return render_template("index.html", expression=expression, result=answer)

    return render_template("index.html", expression="", result="")

if __name__ == "__main__":
    app.run(debug=True)
