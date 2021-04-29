"""
Copyright 2018 Meghan S. Miller, Louis Moresi

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

from . import documentation

import os.path as path
import stripy as stripy
import numpy as _np
# import subprocess
# import shutil as shutil
import pkg_resources

from collections import OrderedDict as _OrderedDict


DATA_PATH      = pkg_resources.resource_filename('miller_alaskamoho_srl2018', 'Models/')
_MohoRaw_FILE  = pkg_resources.resource_filename('miller_alaskamoho_srl2018', 'Models/AlaskaMoho.npz')
_MohoErr_FILE  = pkg_resources.resource_filename('miller_alaskamoho_srl2018', 'Models/AlaskaMohoErrs.npz')
_MohoGrid_FILE = pkg_resources.resource_filename('miller_alaskamoho_srl2018', 'Models/AlaskaMohoErrs-AlaskaMohoFineGrid.npz')
_MohoGridL_FILE = pkg_resources.resource_filename('miller_alaskamoho_srl2018', 'Models/AlaskaMoLoErrs-AlaskaMohoFineGrid.npz')
_MohoGridH_FILE = pkg_resources.resource_filename('miller_alaskamoho_srl2018', 'Models/AlaskaMoHiErrs-AlaskaMohoFineGrid.npz')
_HeatFlowRaw_FILE = pkg_resources.resource_filename('miller_alaskamoho_srl2018', 'Models/AlaskaHeatFlow.npz')
_HeatFlowErr_FILE = pkg_resources.resource_filename('miller_alaskamoho_srl2018', 'Models/AlaskaHeatFlowErrs.npz')
_HeatFlowGrid_FILE = pkg_resources.resource_filename('miller_alaskamoho_srl2018', 'Models/AlaskaHeatFlowFineGrid.npz')


MohoRaw    = _np.load(_MohoRaw_FILE, allow_pickle=True)['alaska_moho']
MohoErr    = _np.load(_MohoErr_FILE, allow_pickle=True)['alaska_moho']
MohoGrid   = _np.load(_MohoGrid_FILE, allow_pickle=True)
_MohoGridL = _np.load(_MohoGridL_FILE, allow_pickle=True)
_MohoGridH = _np.load(_MohoGridH_FILE, allow_pickle=True)

_HeatFlowRaw  = _np.load(_HeatFlowRaw_FILE)['alaska_hf']
_HeatFlowErr  = _np.load(_HeatFlowErr_FILE)['alaska_heat_flow']
_HeatFlowGrid = _np.load(_HeatFlowGrid_FILE)

EarthRadius_km = 6371


class surface_model(object):
	"""
	General representation of the triangulated representing a single valued surface

	Triangulation
	-------------

	Provided by stripy

	"""

	def __init__(self, data_record, surface_record_id, slope_record_id=None, description="", tree=True, permute=True):


		import stripy
		import numpy as np

		lons_r = data_record['gridlons']
		lats_r = data_record['gridlats']

		self.lons_r = lons_r
		self.lats_r = lats_r
		self.description = description

		self.lons_d = np.degrees(lons_r)
		self.lats_d = np.degrees(lats_r)

		self.gridF = stripy.sTriangulation(lons_r%(2.0*np.pi), lats_r, permute=permute, tree=tree)
		self.surface = data_record[surface_record_id]

		try:
			self.surface_slope = data_record[slope_record_id] / EarthRadius_km
		except:
			self.surface_slope = np.ones_like(self.surface) * float('NaN')

		try:
			self.quality = data_record['quality']
		except:
			self.quality = np.ones_like(self.surface)


		return


	def _interpolate_to_lonlat(self, lons_d, lats_d, data, order=1):

		import numpy as np

		lons_r = np.radians(lons_d)
		lats_r = np.radians(lats_d)

		values, err = self.gridF.interpolate(lons_r, lats_r, data, order=order)

		return values

	def value_at_lonlat_degrees(self, lons_d, lats_d, order=1):

		return self._interpolate_to_lonlat(lons_d, lats_d, self.surface, order)


	def slope_at_lonlat_degrees(self, lons_d, lats_d, order=1):

		return self._interpolate_to_lonlat(lons_d, lats_d, self.surface_slope, order)

	def quality_at_lonlat_degrees(self, lons_d, lats_d, order=1):

		return self._interpolate_to_lonlat(lons_d, lats_d, self.quality, order)




## Use the general class definition to capture the moho models


MohoModel_min  = surface_model(MohoGrid,
						 surface_record_id='gridded_data_2',
 					     slope_record_id='gridded_data_slope_2',
 					     description="Surface with best fit to test data across all realisations")

MohoModel_opt  = surface_model(MohoGrid,
						 surface_record_id='gridded_data_1',
 					     slope_record_id='gridded_data_slope_1',
 					     description="Surface combining all data within 1% of the best fit model to the test data")

MohoModel_minj = surface_model(MohoGrid,
						 surface_record_id='gridded_data_3',
 					     slope_record_id='gridded_data_slope_3',
 					     description="Surface with best fit to test+training data across all realisations")


## Moho Surface Excluding deep picks

_MohoModelL_min  = surface_model(_MohoGridL,
						 surface_record_id='gridded_data_2',
 					     slope_record_id='gridded_data_slope_2',
 					     description="Surface with best fit to test data across all realisations")

_MohoModelL_opt  = surface_model(_MohoGridL,
						 surface_record_id='gridded_data_1',
 					     slope_record_id='gridded_data_slope_1',
 					     description="Surface combining all data within 1% of the best fit model to the test data")

_MohoModelL_minj = surface_model(_MohoGridL,
						 surface_record_id='gridded_data_3',
 					     slope_record_id='gridded_data_slope_3',
 					     description="Surface with best fit to test+training data across all realisations")


## Moho Surface Excluding shallow picks


_MohoModelH_min  = surface_model(_MohoGridH,
						 surface_record_id='gridded_data_2',
 					     slope_record_id='gridded_data_slope_2',
 					     description="Surface with best fit to test data across all realisations")

_MohoModelH_opt  = surface_model(_MohoGridH,
						 surface_record_id='gridded_data_1',
 					     slope_record_id='gridded_data_slope_1',
 					     description="Surface combining all data within 1% of the best fit model to the test data")

_MohoModelH_minj = surface_model(_MohoGridH,
						 surface_record_id='gridded_data_3',
 					     slope_record_id='gridded_data_slope_3',
 					     description="Surface with best fit to test+training data across all realisations")



## Heat flow data for reference


_HFModel_min  = surface_model(_HeatFlowGrid,
						 surface_record_id='gridded_data',
 					     description="Surface with best fit to test data across all realisations")

_HFModel_opt  = surface_model(_HeatFlowGrid,
						 surface_record_id='gridded_data_1pct_j',
 					     description="Surface combining all data within 1% of the best fit model to the test data")
