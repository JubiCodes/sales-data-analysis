from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

# Fix file path issue
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
DATA_PATH = os.path.join(BASE_DIR, "sales_data.csv")  

# Function to process sales data
def process_sales_data():
    if not os.path.exists(DATA_PATH):
        return None, None  

    df = pd.read_csv(DATA_PATH)
    
    # Basic stats
    avg_sales = df.groupby("Product")["Sales"].mean().round(2)
    max_sales = df.groupby("Product")["Sales"].max()
    min_sales = df.groupby("Product")["Sales"].min()
    
    sales_summary = pd.DataFrame({
        "Average Sales": avg_sales,
        "Highest Sales": max_sales,
        "Lowest Sales": min_sales
    }).reset_index()

    # Create and save graph
    plt.figure(figsize=(8, 4))
    df.groupby("Date")["Sales"].sum().plot(kind="line", marker="o")
    plt.xlabel("Date")
    plt.ylabel("Total Sales")
    plt.title("Sales Trend Over Time")
    plt.xticks(rotation=45)
    plt.grid()

    # Ensure static folder exists
    os.makedirs(os.path.join(BASE_DIR, "static"), exist_ok=True)

    plt.savefig(os.path.join(BASE_DIR, "static", "sales_chart.png"))
    plt.close()

    return df.to_html(classes="table table-striped"), sales_summary.to_html(classes="table table-bordered")

# Home Page (Upload CSV)
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        # Ensure backend folder exists before saving
        os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)

        file.save(DATA_PATH)  
        return redirect(url_for("dashboard"))

    return render_template("index.html")

# Dashboard Page (Show Sales Data & Graph)
@app.route("/dashboard")
def dashboard():
    sales_data, summary_table = process_sales_data()
    return render_template("dashboard.html", sales_data=sales_data, summary_table=summary_table)

if __name__ == "_main_":
    app.run(debug=True)