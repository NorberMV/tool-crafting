install-requirements.local:
	pip install -r requirements.txt

run:
	python main.py

pre-commit:
	pre-commit run --all-files
