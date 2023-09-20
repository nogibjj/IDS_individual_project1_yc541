install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

test:
	python -m pytest -vv test_*.py

format:
	black *.py

lint:
	make movefile
	ruff check ./*.py
	make restorefile 

all: install lint test format