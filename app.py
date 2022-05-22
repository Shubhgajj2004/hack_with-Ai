import os
from flask import Flask , render_template , request, url_for , redirect , jsonify

import openai
import requests,json


app =Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route('/')
def home():
    return render_template("temp.html")


@app.route('/learn_flask')
def learn_flask():
    return render_template("Flask_cour.html")

@app.route('/templates/first')
def first():
    return render_template('/flask_chapters/first.html')


@app.route('/create_code', methods=("GET", "POST"))
def create_code():
     if request.method == "POST" :
         code_in = request.form["code_in"]
         inst_in = request.form["inst_in"]
         response = openai.Edit.create(
            engine="code-davinci-edit-001",
            input=code_in,
            instruction=inst_in,
            temperature=0.5,
            top_p=1
         )          
         return redirect(url_for("create_code", result=response.choices[0].text))

     
     result = request.args.get("result")
     return render_template("AI_code/gen_code.html", result="Generated code:" if result is None else result)


@app.route('/create_code/process', methods=['POST'])
def process():
    
    code = request.form['name']
    if code :
         program = {
                "script" : code,
                "language": "python3",
                "versionIndex": "0",   
                "clientId": "98d1dddd58d0319280f7fc985c00a0e3",
                "clientSecret":"5599cf7a4690d6fb72e3f1abdbe89c1f6b976ef23515281b03ff179655dc022f"
            }

         url = "https://api.jdoodle.com/v1/execute"

         response = requests.post(url, json=program)
         data_json = json.loads(response.text)
          

         outcode = data_json['output']
         print(outcode)
         return jsonify({'output': outcode}) 
 
    
@app.route('/IDE')
def IDE():
    return render_template('online_ide.html')

@app.route('/debug', methods=['GET','POST'])
def debug():
     if request.method == "POST" :
         code_in = request.form["code_in"]
         inst_in = request.form["inst_in"]
         response = openai.Edit.create(
            engine="code-davinci-edit-001",
            input=code_in,
            instruction=inst_in,
            temperature=0.5,
            top_p=1
         )          
         return redirect(url_for("debug", result=response.choices[0].text))


     result = request.args.get("result")
     return render_template("AI_code/debug.html", result="Debugged code:" if result is None else result)


@app.route('/explain', methods=['GET','POST'])
def explain():
     if request.method == "POST" :
         code_in = request.form["code_in"]
         inst_in = request.form["inst_in"]
         response = openai.Edit.create(
            engine="code-davinci-edit-001",
            input=code_in,
            instruction=inst_in,
            temperature=0.5,
            top_p=1
         )          
         return redirect(url_for("explain", result=response.choices[0].text))


     result = request.args.get("result")
     return render_template("AI_code/explainer.html", result="Explanation:" if result is None else result)


if __name__ == "__main__":
    app.run(debug=True) 