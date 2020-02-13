Miller & Moresi - Alaska Moho Model with Notebooks
====================================

---

![Image showing map of results](https://www.dropbox.com/s/5s6uk6m3dlg5ysq/MohoSurfaceGradient-ClusteredGrids.png?raw=1)

_Preferred model, gradient and a comparison to heat flow data. The maps were
produced using the `cartopy` package. Instructions for reproducing these
maps are in the notebooks supplied with this package_

---


This package is a self-consistent packaging of the Miller & Moresi Alaska Moho model.
There are many ways to access this package.

It contains

   - This information
   - Scripts to install documentation and examples
   - Jupyter notebooks for manipulating the data
   - Jupyter notebooks for recreating our work

A demo is available on [mybinder.org](http://mybinder.org) - open the notebook `A0-Index.ipynb`
to begin. The 'current' version with any updates / errata is here:

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/lmoresi/miller-moho-binder/master)

This is exactly the published version (1.0), warts and all.

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/lmoresi/miller-moho-binder/publication)


Site Map
--------

The jupyter notebooks provided as examples are given below

   - A1: Raw data, convert and save
   - A2: Raw data - plot quality information
   - A3: Triangulating and interpolating raw data
   - A4: Plotting moho and moho slope
   - A5: Interactive 3D plot
   - A6: Convert Models to Regular XYZ grid

There are further notebooks that allow you to reproduce our work in creating the
prefered model and these can be browsed in the `ModelConstruction` directory


---

![Image showing quality scores on a map](https://www.dropbox.com/s/n6y4c8h0eauvuhv/ErrorsAndScores.png?raw=1)

_We constructed our model by fitting surfaces to the observed points and recording the capacity
of the model to predict information at points not included in the model construction. The
quality of the model at each point was given an integer score and this was used to weight information
in the final fitting process_



Installation
-----------

The package can be installed standalone using `pip`
or it can be run through docker without needing specific installation.

These notebooks can be viewed with jupyter but will only run if all the software dependencies have
been installed (see [Installation through `pip`](#Installation-through-pip) below.

In nearly every instance we recommend using the (self-contained) docker version.
We have provided some useful `bash` shortcuts that make the docker commands
easier to remember (see [Installation through docker](#Installation-through-docker) below).



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
docker run --rm lmoresi/docker-miller-moho:latest bash_utils > msmoho_bash_utils.sh
source msmoho_bash_utils.sh
```

Install the documentation / scripts and notebooks in the current directory
```bash
# print help message (i.e. usage)
source msmoho_bash_utils.sh
msmoho-docker-sh install_examples
```

Run a local python script  

```bash
# run  my_script.py with python in the docker container
source msmoho_bash_utils.sh
msmoho-docker-sh my_script.py

```

### Installation through pip (or conda)

The installation of the python package is straightforward but
there is a dependency on numpy and on stripy which may require
an installed fortran compiler. If this proves problematic, the
docker version may simply be the best choice.

```bash
   #! /bin/env bash
   # install the main package
   # stripy and numpy are installed as dependencies by pip
   # but we can do this explicitly to manage versions and
   # check for errors

   pip install numpy
   pip install stripy

   # stripy and numpy
   # as they embed fortran and C packages
   # miller_alaskamoho_srl2018 itself is pure python

   pip install miller_alaskamoho_srl2018
```

The following script tests the installation:

```python
    #! /bin/env python
    import numpy as np
    try:
        import miller_alaskamoho_srl2018 as alaskamoho
    except ImportError:
        print ("Problem importing the alaska moho package")

    # Check the data files exist / can be read
    # [('lon', '<f8'), ('lat', '<f8'), ('moh', '<f8') ... etc
    # [-174.197495 -171.703506 -170.247696 -168.854996 -168.161896]
    # [43.61043017 34.75098075 37.34819411]

    mohoraw = alaskamoho.MohoErr
    print(mohoraw.dtype)
    print(mohoraw['lon'][0:5])
    print(mohoraw['moh'][0:5])

    # Check to see if the interpolator works
    # [43.61043017 34.75098075 37.34819411]

    moho_model = alaskamoho.MohoModel_opt
    lons = np.array([-150, -155, -160])
    lats = np.array([60, 65, 70])
    print(moho_model.value_at_lonlat_degrees(lons, lats, order=1))

    # install documentation in user-specified location
    # Should install in the current directory as AlaskaMohoExamples

    alaskamoho.documentation.install_documentation(path=None)
```

If you install the documentation in the form of jupyter notebooks, then to view them,
you also need to install some dependencies. Specifically:


```bash

   # The jupyter notebook system (and dependencies)
   pip install jupyter

   # scipy is used in some examples
   pip install scipy

   # cartopy is used to plot examples
   # (may be necessary to install the shapely package first)

   pip install --no-binary :all: shapely
   pip install cartopy

   # We need litho1pt0 to re-build the model files

   pip install litho1pt0

   # We use lavavu for the interactive visualisation of the surfaces

   pip install lavavu

   # pip install gdal is optional: it is used for shaded relief images of the
   # maps and also requires a download of the relevant image file.

   pip install gdal
```


If you only wish to browse the documentation / examples or see how we built the model, why not use the docker version !
