Miller & Moresi - Alaska Moho Model with Notebooks
====================================

This package is a self-consistent packaging of the Miller & Moresi Alaska Moho model.
There are many ways to use this package.

It contains

   - This information
   - Scripts to install documentation and examples
   - Jupyter notebooks (like this one but with active code)
   - A docker container setup that can serve notebooks with all relevant software, data and dependencies

The package can be installed standalone using `pip`
or it can be run through docker without needing specific installation.

These notebooks can be viewed with jupyter but will only run if all the software dependencies have
been installed (see [Installation through `pip`](#Installation-through-pip) below

In nearly every instance we recommend using the (self-contained) docker version.
We have provided some useful `bash` shortcuts that make the docker commands
easier to remember (see [Installation through docker](#Installation-through-docker) below).


Jupyter Notebooks
----------------

The notebooks provided as examples are given below

   - [A1 - Raw data, convert and save.ipynb](A1 - Raw data, convert and save.ipynb)
   - [A2 - Raw data - plot quality information.ipynb](A2 - Raw data - plot quality information.ipynb)
   - [A3 - Triangulating and interpolating raw data.ipynb](A3 - Triangulating and interpolating raw data.ipynb)
   - [A4 - Plotting moho and moho slope.ipynb](A4 - Plotting moho and moho slope.ipynb)
   - [A5 - Interactive 3D plot.ipynb](A5 - Interactive 3D plot.ipynb)
   - [A6 - Convert Models to Regular XYZ grid.ipynb](A6 - Convert Models to Regular XYZ grid.ipynb)

There are further notebooks that allow you to reproduce our work in creating the
prefered model and these can be browsed [here](/tree/ModelConstruction)


Installation
-----------


### Installation through docker


First it is necessary to install the free __docker, community edition__ from the  [docker store](https://store.docker.com/search?offering=community&type=edition) for your platform.

```bash
# Download the image with the scripts and data
docker pull lmoresi/docker-miller-moho:latest
```

That's it !

To test the installation, try the following

####  Command line docker examples

This help message

```bash
# print help message (i.e. usage)
docker run --rm lmoresi/docker-miller-moho:latest help
```

Install the bash helpers in the current directory
```bash
# print help message (i.e. usage)
docker run --rm lmoresi/docker-miller-moho:latest bash_utils > moho_bash_utils.sh
source moho_bash_utils.sh
```

Install the documentation / scripts and notebooks in the current directory
```bash
# print help message (i.e. usage)
source moho_bash_utils.sh
moho-docker-sh install_examples
```

Run a local python script  

```bash
# run  my_script.py with python in the docker container
moho my_script.py

```
