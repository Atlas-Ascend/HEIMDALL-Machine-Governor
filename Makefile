install:
	python -m pip install -e '.[dev]'

test:
	pytest -q

lint:
	ruff check src tests scripts

run:
	uvicorn heimdall.api:app --host 0.0.0.0 --port 8000

prove: test lint
	python scripts/proof_manifest.py
