from flask import Flask,request,jsonify

app = Flask(__name__)

proteins = []

@app.route("/proteins",methods=["GET"])
def get_proteins():
    return jsonify(proteins)

@app.route("/proteins",methods=['POST'])
def add_protein():
    data = request.get_json()
    protein_item = {
        "name":data.get("name"),
        "brand":data.get("brand"),
        "protein_content":data.get("protein_content"),
        "serving_size":data.get("serving_size")
    }
    proteins.append(protein_item)
    return jsonify({"message":"Protein added","item":protein_item})


if __name__ == "__main__":
    app.run(debug=True)