[![License: GPL-3.0](https://img.shields.io:/github/license/pism/pypac)](https://opensource.org/licenses/GPL-3.0)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)



# pism-tutorials <img src="https://raw.githubusercontent.com/pism/pism-tutorials/main/pism-tutorials-jupyterbook/img/pism_logo.png" width=80 />


Welcome to _pism-tutorials_ using <img src="https://raw.githubusercontent.com/executablebooks/jupyter-book/master/docs/images/logo-square.svg" width=40 /> Jupyter Book.

[![This shows simulated Greenland surface speeds at 2300 based on an RCP 8.5 Scenario.](pism-tutorials-jupyterbook/img/header_greenland.jpg)](https://svs.gsfc.nasa.gov/13233/)


## Installation

Get pism-tutorials source from GitHub:

    $ git clone git@github.com:pism/pism-tutorials.git
    $ cd pism-tutorials

Optionally create Conda environment named *pism-tutorials*:

    $ conda env create -f environment.yml
    $ conda activate pism-tutorials

or using Mamba instead:

    $ mamba env create -f environment.yml
    $ mamba activate pism-tutorials

Install pism-tutorials:

    $ pip install .

Note that this will install _PISM_ using the `conda`-channel `pism`, currently only available for _osx-arm64_ and _linux_ architectures.

## Building a Jupyter Book

Run the following command in your terminal:

```bash
jb build .
```

If you would like to work with a clean build, you can empty the build folder by running:

```bash
jb clean .
```

If jupyter execution is cached, this command will not delete the cached folder.

To remove the build folder (including `cached` executables), you can run:

```bash
jb clean --all .
```
