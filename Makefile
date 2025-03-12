.PHONY: run install test clean

run:
	flask --app app/routes.py run --debug

install:
	pip install -r requirements.txt

test:
	python -m pytest

clean:
	find . -type d -name __pycache__ -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
