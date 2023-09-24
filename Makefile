all: install test format lint 

install:
	python3 -m pip install --upgrade pip 
	python3 -m pip install -r requirements.txt
	python3 -m pip install pytest-cov

test:
	#python -m pytest -vv --cov=source/test_*.py
	python -m pytest --nbval source/*.ipynb

format:	
	black source/*.py 
	nbqa black source/*.ipynb

lint:
	nbqa ruff --fix source/*.ipynb

refactor: format lint	

all: install lint format test

plot:
	python3 source/main.py

