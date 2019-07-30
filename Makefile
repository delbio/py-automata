BASE_FOLDER := .
PACKAGEFOLDER := fsm
PACKAGEPATH := $(BASE_FOLDER)/$(PACKAGEFOLDER)
PACKAGENAME := fsm-engine

install:
	pip3 install $(PACKAGEPATH)

install_editable:
	pip3 install -e $(PACKAGEPATH)

uninstall:
	pip3 uninstall $(PACKAGENAME)

clean:
	make clean -C $(PACKAGEPATH)
