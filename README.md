# sales-data-analysis

A web-based application built using Flask, Pandas, and Matplotlib to analyze and visualize sales data.

## Features

- Upload and analyze sales data in CSV format
- Display uploaded data in a structured table
- Show key statistics:
  - Average sales per product
  - Highest selling product
  - Lowest selling product
- Generate and display a sales trend chart
- User-friendly and responsive interface

## Setup

Follow these steps to run the project locally:

1. Install required packages  
   (Make sure Python is installed):
   ```bash
   pip install flask pandas matplotlib
2.Run the application and access the dashboard:
    python app.py
# Open your browser and go to:
# http://localhost:5000

# Upload your sales_data.csv file in the format:
# Date,Product,Sales
# 2024-01-01,Product A,200
# 2024-01-02,Product B,150

# After uploading, you’ll be redirected to the dashboard
# which shows:
# - Raw data table
# - Summary statistics
# - Sales trend chart




