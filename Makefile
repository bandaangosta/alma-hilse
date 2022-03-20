all: run

clean:
	rm -rf venv && rm -rf *.egg-info && rm -rf dist && rm -rf build #&& rm -rf *.log*

venv:
	python3 -m venv venv && venv/bin/pip install -e .

venv-test: venv
	venv/bin/pip install -e .[test]

run: venv
	venv/bin/python -m alma-hilse

test:
	venv/bin/python -m pytest -v

build:
	python3 setup.py sdist bdist_wheel