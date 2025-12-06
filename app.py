from datetime import datetime
from flask import Flask, render_template, request, jsonify
import torch
from model_def import RidershipNN

#Create app
app = Flask(__name__)

# Load model (use CUDA if available, otherwise use CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = RidershipNN().to(device)
state = torch.load("model.pth", map_location=device)

# renders index html page
@app.route("/")
def index():
    return render_template("index.html")

# /predict route called when the user presses the predict button
@app.route("/predict", methods=["POST"])
def predict():
    # data inputted by users on the website
    mean_temp = float(request.form["mean_temp"])
    precip = float(request.form["precip"])
    snow = float(request.form["snow"])
    date_str = request.form["date"]
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")

    # initializing the inputs relating to date
    month = date_obj.month
    day_of_week = date_obj.weekday()  # Monday = 0
    is_weekend = int(day_of_week >= 5)

    # initializing flags based on user input
    rain_flag = int(precip > 0)
    snow_flag = int(snow > 0)
    heat_flag = int(mean_temp > 25)
    freeze_flag = int(mean_temp < 0)

    # preparing the input of the model
    feature_vector = [
        mean_temp,
        precip,
        snow,
        month,
        day_of_week,
        is_weekend,
        rain_flag,
        snow_flag,
        heat_flag,
        freeze_flag,
    ]

    # Prepare tensor
    input_tensor = torch.tensor([feature_vector], dtype=torch.float32, device=device)

    # Predict
    with torch.no_grad():
        output = model(input_tensor)
        prediction = output.item()

    return jsonify({"prediction": round(prediction, 0)})

if __name__ == "__main__":
    app.run(debug=True)
