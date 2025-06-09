from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route("/add",methods=['GET'])
def add():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get("b"))
        result = a + b
        return jsonify({'operation':'add','a':a,'b':b,'result':result})
    except Exception as e:
        return jsonify({"error":str(e)}),400
    

@app.route('/subtract',methods=['GET'])
def subtract():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = a - b
        return jsonify({'operation':'subtract','a':a,'b':b,'result':result})
    except Exception as e:
        return jsonify({"error":str(e)}),400
    

if __name__ == "__main__":
    app.run(debug=True)