

all: tests

install:
	pip install -r .requirments.txt

.PHONY: tests
tests:
	python -m unittest discover -p "*Test.py" -s tests/

clean:
	find . -name "*.pyc" -delete

start-server:
	./server.py
