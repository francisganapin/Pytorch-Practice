from flask import Flask,jsonify


app = Flask(__name__)

@app.route("/protein")
def get_protein():
    return jsonify({
        "name":"Whhey Isolate",
        "serving_size":"30g",
        "protein_content":"25g"
    })

if __name__ == '__main__':
    app.run(debug=True)