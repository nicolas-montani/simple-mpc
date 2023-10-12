from flask import Flask, jsonify,request,render_template
import database.database_handler as dh
from handler.form_handler import form_handler


DATABASE = "database/numbers.dat"

# data format {"x": 1, "y": 2, z: 3, k: 4}
app = Flask(__name__)

####################################################################################################
@app.route("/")
def template():
    data = dh.read_bin(DATABASE)   
    return render_template("index.html", x=data['x'], y=data['y'], z=data['z'], k=data['k'])



####################################################################################################
# POST METHODS  
####################################################################################################
@app.route("/x", methods=["Post"])
def post_x():

    # read the posted values from the UI
    _json = request.json
    _x = _json['x']
    
    data = dh.read_bin(DATABASE)
    data['x'] = _x

    dh.write_bin(DATABASE, data)

    return jsonify("OK")


@app.route("/y", methods=["Post"])
def post_y():
    
        # read the posted values from the UI
        _json = request.json
        _y = _json['y']
        
        data = dh.read_bin(DATABASE)
        data['y'] = _y
    
        dh.write_bin(DATABASE, data)
    
        return jsonify("OK")

@app.route("/z", methods=["Post"])
def post_z():
    
        # read the posted values from the UI
        _json = request.json
        _z = _json['z']
        
        data = dh.read_bin(DATABASE)
        data['z'] = _z
    
        dh.write_bin(DATABASE, data)
    
        return jsonify("OK")

@app.route("/k", methods=["Post"])
def post_k():
    
        # read the posted values from the UI
        _json = request.json
        _k = _json['k']
        
        data = dh.read_bin(DATABASE)
        data['k'] = _k
    
        dh.write_bin(DATABASE, data)
    
        return jsonify("OK")

@app.route("/s", methods=["Post"])
def post_s():
    
        # read the posted values from the UI
        _json = request.json
        _s = _json['s']
        
        data = dh.read_bin(DATABASE)
        data['s'] = _s
    
        dh.write_bin(DATABASE, data)
    
        return jsonify("OK")

####################################################################################################
# PUT METHODS
####################################################################################################

@app.route("/z/times", methods=["PUT"])
def put_xty():
    """Get z from database"""
    data = dh.read_bin(DATABASE)
    data['z'] = data['x'] * data['y']
    dh.write_bin(DATABASE, data)
    return jsonify("OK")

@app.route("/z/plus", methods=["PUT"])
def put_xpy():
    """Get z from database"""
    data = dh.read_bin(DATABASE)
    data['z'] = data['x'] + data['y']
    dh.write_bin(DATABASE, data)
    return jsonify("OK")

@app.route("/z/minus", methods=["PUT"])
def put_xmy():
    """Get z from database"""
    data = dh.read_bin(DATABASE)
    data['z'] = data['x'] - data['y']
    dh.write_bin(DATABASE, data)
    return jsonify("OK")

@app.route("/z/divide", methods=["PUT"])
def put_xdy():
    """Get z from database"""
    data = dh.read_bin(DATABASE)
    try:
        data['z'] = data['x'] / data['y']
    except ZeroDivisionError:
        data['z'] = "Error: Division by zero"
    dh.write_bin(DATABASE, data)
    return jsonify("OK")

@app.route("/z/swap", methods=["PUT"])
def put_xsy():
    """Get z from database"""
    data = dh.read_bin(DATABASE)
    data['x'], data['y'] = data['y'], data['x']
    dh.write_bin(DATABASE, data)
    return jsonify("OK")


####################################################################################################
# GET METHODS  
####################################################################################################



@app.route("/x", methods=["GET"])
def get_x():
    """Get x from database"""
    data = dh.read_bin(DATABASE)
    return jsonify({"x": data['x']})

@app.route("/y", methods=["GET"])
def get_y():
    """Get y from database"""
    data = dh.read_bin(DATABASE)
    return jsonify({"y": data['y']})

@app.route("/z", methods=["GET"])
def get_z():
    """Get z from database"""
    data = dh.read_bin(DATABASE)
    return jsonify({"z": data['z']})

####################################################################################################
# Change Method
####################################################################################################
    
@app.route("/change", methods=["Post"])
def change():
    # read the posted values in the url
    cast = request.form['cast']
    server = request.form['server']
    method = request.form['method']
    key = request.form['key']
    value = request.form['value']
    operator = request.form['operator']

    response = str(form_handler(cast, server, method, key, value, operator)).replace("\\n", "")

    
    return jsonify(response)
    

if __name__ == "__main__":
    app.run(debug=True)