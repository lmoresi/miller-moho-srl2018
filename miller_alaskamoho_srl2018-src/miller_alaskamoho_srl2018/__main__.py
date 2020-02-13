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


import sys

from . import documentation

num_args = len(sys.argv) - 1

if "help" in sys.argv or num_args==0:
    print("module arguments: ")
    print("   help")
    print("   install_notebooks [path]")


if "install_notebooks" in sys.argv:
    if num_args == 2:
        path = sys.argv[-1]
        documentation.install_documentation(path)
        print("Installing notebooks in {}".format(path))
    else:
        documentation.install_documentation()
        print("Installing notebooks in current working directory")
