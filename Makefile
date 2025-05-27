.PHONY := pip-install-deps
pip-install-deps:
	python3 -m pip install -r requirements.txt

.PHONY := conda-install-deps
conda-install-deps:
	conda install --file requirements.txt

.PHONY := build
build:
	jupyter-book build pism-tutorials-jupyterbook

.PHONY := local-deploy
local-deploy: build
	-python3 -m http.server -d pism-tutorials-jupyterbook/_build/html
