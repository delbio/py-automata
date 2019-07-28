BASE_FOLDER := .
PACKAGENAME := fsm
PACKAGEPATH := $(BASE_FOLDER)/$(PACKAGENAME)

install:
	pip3 install $(PACKAGEPATH)

install_editable:
	pip3 install -e $(PACKAGEPATH)

uninstall:
	pip3 uninstall $(PACKAGENAME)

clean:
	make clean -C $(PACKAGEPATH)
