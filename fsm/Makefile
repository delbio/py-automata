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
	tox

build_dist:
	python3 setup.py sdist bdist_wheel

upload_to_test_pypi:
	twine upload --verbose --repository-url https://test.pypi.org/legacy/ dist/*

publish_to_test_pypi: clean test build_dist upload_to_test_pypi

upload_to_pypi:
	twine upload --verbose dist/*

publish_to_pypi: clean test build_dist upload_to_pypi
