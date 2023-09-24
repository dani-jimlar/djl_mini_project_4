all: install test format lint 

install:
	python3 -m pip install --upgrade pip 
	python3 -m pip install -r requirements.txt
	python3 -m pip install pytest-cov

test:
	#python -m pytest -vv --cov=source/test_*.py

format:	
	black source/*.py 

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

refactor: format lint	

all: install lint format test



