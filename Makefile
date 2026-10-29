PYTHON ?= .venv/bin/python
MODULE ?= interpolate.secret_sharing

.PHONY: run interactive

run:
	$(PYTHON) -m $(MODULE)

interactive:
	$(PYTHON) -i -m $(MODULE)
