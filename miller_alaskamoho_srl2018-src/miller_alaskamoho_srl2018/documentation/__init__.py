"""
Copyright 2017 Louis Moresi

This file is part of miller_alaskamoho_srl2018.

miller_alaskamoho_srl2018 is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or any later version.

miller_alaskamoho_srl2018 is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with miller_alaskamoho_srl2018.  If not, see <http://www.gnu.org/licenses/>.
"""

import pkg_resources as _pkg_resources
from distutils import dir_util as _dir_util

def install_documentation(path="./AlaskaMohoExamples"):
    """Install the example notebooks for litho1pt0 in the given location

    WARNING: If the path exists, the Notebook files will be written into the path
    and will overwrite any existing files with which they collide. The default
    path ("./AlaskaMohoExamples") is chosen to make collision less likely / problematic

    The documentation for this module is in the form of jupyter notebooks.

    Some dependencies exist for the notebooks to be useful:

       - matplotlib: for some diagrams
       - cartopy: for plotting map examples

    Some dependencies are explicitly imported into the notebooks including:

       - stripy (for interpolating on the sphere)
       - numpy
       - scipy (for k-d tree point location)

    """

    ## Question - overwrite or not ? shutils fails if directory exists.

    Notebooks_Path = _pkg_resources.resource_filename('miller_alaskamoho_srl2018', 'Notebooks')

    ct = _dir_util.copy_tree(Notebooks_Path, path, preserve_mode=1, preserve_times=1, preserve_symlinks=1, update=0, verbose=1, dry_run=0)

    return
