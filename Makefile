install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

test:
	python -m pytest -vv test_*.py

format:
	black *.py

lint:
	ruff

all: install lint test format