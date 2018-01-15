all: lint install test doc

test:
	coverage erase
	coverage run rt_hack/__init__.py
	coverage report -m

lint:
	find . -type f -name '*.py' | flake8

install:
	python3 setup.py install

doc:
	make -C docs html

live:
	find . -type f -name '*.py' | entr make test
