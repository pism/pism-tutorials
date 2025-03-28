[![License: GPL-3.0](https://img.shields.io:/github/license/pism/pypac)](https://opensource.org/licenses/GPL-3.0)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)


```{image} ./img/pism_logo.png
:alt: PISM Logo
:width: 25%
:align: left
```


# pism-tutorials


```{image} ./img/header_greenland.jpg
:alt: PISM Greenland Simulated Surface Speeds
:width: 75%
:align: center
```


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
