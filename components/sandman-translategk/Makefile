.PHONY: all clean install doc sdist

all: install doc 

clean:
	rm -rf build dist sandman_translategk.egg-info requirements.txt
	#rm -rf docs/sphinx/source/code/*
	#make -C docs/sphinx clean

install: clean
	pip-compile requirements.in
	pip install -r requirements.txt
	python setup.py install

doc:
	sphinx-apidoc -o docs/sphinx/source/code ./sandman_translategk
	make -C docs/sphinx html latex

sdist: clean
	python setup.py sdist
