.PHONY: clean_build clean_pyc

# inspired by: https://krzysztofzuraw.com/blog/2016/makefiles-in-python-projects.html

clean: clean_build clean_pyc

clean_pyc:
	@echo "Remove python artifacts."
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean_build:
	@echo "Remove build artifacts."
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

test:
	python3 -m unittest discover -v fsm "*_test.py"
