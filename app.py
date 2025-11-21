from flask import Flask, render_template, request, jsonify
import torch
import numpy as np

from model_def import RidershipNN

app = Flask(__name__)

# Load model
model = RidershipNN()
model.load_state_dict(torch.load("model.pth", map_location=torch.device("cpu")))
model.eval()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    mean_temp = float(request.form["mean_temp"])
    precip = float(request.form["precip"])
    snow = float(request.form["snow"])

    # Prepare tensor
    input_data = np.array([[mean_temp, precip, snow]], dtype=np.float32)
    input_tensor = torch.tensor(input_data)

    # Predict
    with torch.no_grad():
        output = model(input_tensor)
        prediction = output.item()

    return jsonify({"prediction": round(prediction, 2)})

if __name__ == "__main__":
    app.run(debug=True)