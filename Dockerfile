from python:3
workdir /code
copy requirements.txt /code
run pip install -r requirements.txt
copy . /code/
