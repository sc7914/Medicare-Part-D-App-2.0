# Medicare-Part-D-App-2.0

## Setup

Create virtual environment:
*package includes .venv already*

```sh
conda create -n env python=3.12
```

Activate the environment:

```sh
conda activate env
```

Install packages:

```sh
#pip install requests
#pip install plotly
#pip install python-dotenv

# best practice to list the packages in the requirements.txt file:
pip install -r requirements.txt
```

## Usage

Medicare Part D spending:

```sh
python -m data.medicare
```
Medicare Part D spending:

```sh
python -m data.revenue
```

Medicare Part D spending:

```sh
python -m data.exposure
```

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=app/app.py flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app/app.py
flask run
```
