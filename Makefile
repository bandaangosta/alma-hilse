clean:
	rm -rf venv && rm -rf *.egg-info && rm -rf dist && rm -rf build #&& rm -rf *.log*

venv:
	python3 -m venv venv && venv/bin/pip install -e .
	ln -sf $$(which python3) venv/bin/python3

venv-test: venv
	venv/bin/pip install -e .[test]

test:
	venv/bin/python -m pytest -v

build:
	python3 setup.py sdist bdist_wheel