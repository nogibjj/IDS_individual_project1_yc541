install:
	pip install --upgrade pip &&\\
		pip install -r requirements.txt

test:
	pytest --nbval notebook_name.ipynb
	python -m pytest -vv --cov=lib data_analysis1.py data_analysis2.py

format:	
	black *.py 

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py lib/*.py

deploy:
	# deploy goes here

all: install lint test format deploy