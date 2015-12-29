

all: tests

.PHONY: tests
tests:
	python -m unittest discover -p "*Test.py" -s tests/

start-server:
	server/server.py
