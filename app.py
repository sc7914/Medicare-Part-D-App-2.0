from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    """Define main route into the website."""
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/process_medicare', methods=['POST'])
def process_medicare():
    input_data = request.form['inputData']
    # Process the input_data here
    medicare_result = f"Processed Medicare data: {input_data}"
    return render_template('index.html', medicare_result=medicare_result)

@app.route('/process_revenue', methods=['POST'])
def process_revenue():
    ticker = request.form['ticker']
    # Process the ticker here
    revenue_result = f"Processed Revenue data for ticker: {ticker}"
    return render_template('index.html', revenue_result=revenue_result)

@app.route('/process_exposure', methods=['POST'])
def process_exposure():
    exposure_value = request.form['exposureValue']
    # Process the exposure_value here
    exposure_result = f"Processed Exposure value: {exposure_value}"
    return render_template('index.html', exposure_result=exposure_result)

if __name__ == '__main__':
    app.run()