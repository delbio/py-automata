BASE_FOLDER := .
PACKAGEFOLDER := fsm
PACKAGEPATH := $(BASE_FOLDER)/$(PACKAGEFOLDER)
PACKAGENAME := fsm-engine

install:
	pip3 install $(PACKAGENAME)

install_from_test_pypi:
	pip3 install --index-url https://test.pypi.org/simple/ --no-deps $(PACKAGENAME)

install_local:
	pip3 install $(PACKAGEPATH)

install_local_editable:
	pip3 install -e $(PACKAGEPATH)

uninstall:
	pip3 uninstall $(PACKAGENAME)

clean:
	make clean -C $(PACKAGEPATH)
