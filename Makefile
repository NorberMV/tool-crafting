install-requirements:
	pip install -r requirements.txt

install-routing-chains.requirements:
	pip install -r routing-chains/requirements.txt

run-function-calling:
	python main.py

run-chain-routing:
	python routing-chains/main.py

pre-commit:
	pre-commit run --all-files
