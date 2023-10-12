from flask import Flask, jsonify,request,render_template
from database.database_handler import get_value,  set_value


app = Flask(__name__)
####################################################################################################
@app.route("/")
def template():
    return render_template("index.html", x=get_value('x'), y=get_value('y'), z=get_value('z'), k=get_value('k'))

@app.route("/s")
def template_s():


    html = ""
    for i in range(1, 201):
        line = f"s{i}: " + str(get_value(f"s{i}")) + " , "
        html += line
    return render_template("s.html", s=html)

####################################################################################################

@app.route("/get_value", methods=["GET"])
def get_value_route():
    index = request.args.get("index")
    value = int(get_value(index))
    return jsonify(value=value)

@app.route("/set_value", methods=["POST"])
def set_value_route():
    index = request.form.get("index")
    value = request.form.get("value")
    set_value(index, value)
    return jsonify(success=True)


####################################################################################################

@app.route("/out", methods=["GET"])
def out():
    
    result = ""
    x = int(get_value('x'))
    k = int(get_value('k'))

    for i in range(200):
        value = (x + i + k) * int(get_value(f"s{i+1}"))
        result +=  str(value) + "," 
    
    result = result[:-2]
    return jsonify(result=result)