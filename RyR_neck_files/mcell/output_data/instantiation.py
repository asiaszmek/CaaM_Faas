# WARNING: This is an automatically generated file and will be overwritten
#          by CellBlender on the next model export.

import os
import shared
import mcell as m

from parameters import *
from subsystem import *
from geometry import *
MODEL_PATH = os.path.dirname(os.path.abspath(__file__))


# ---- instantiation ----

# ---- release sites ----

# ---- surface classes assignment ----

Mushroom_dendrite_PSD.surface_class = PSD
# OuterCube
Cube.surface_class = Surface_cube
# SA_reflective
SA.surface_class = SA_membrane
# Mushroom_transparent
Mushroom_transparent.surface_class = Ions_mushroom
# Cylinder_reflective
Mushroom_dendrite_cylinder_reflect.surface_class = Cylinder_reflective
# ---- compartments assignment ----

Release_Site_1 = m.ReleaseSite(
    name = 'Release_Site_1',
    complex = m.Complex('Ca2'),
    region = Mushroom_transparent - SA,
    concentration = Ca_cyto_IC
)

Release_Site_2 = m.ReleaseSite(
    name = 'Release_Site_2',
    complex = m.Complex('PMCA', orientation = m.Orientation.UP),
    region = Mushroom_dendrite_head,
    density = PMCA_IC_HEAD
)

Release_Site_3 = m.ReleaseSite(
    name = 'Release_Site_3',
    complex = m.Complex('PMCA', orientation = m.Orientation.UP),
    region = Mushroom_dendrite_neck,
    density = PMCA_IC_NECK
)

Release_Site_4 = m.ReleaseSite(
    name = 'Release_Site_4',
    complex = m.Complex('NCX', orientation = m.Orientation.UP),
    region = Mushroom_dendrite_head,
    density = NCX_IC_HEAD
)

Release_Site_5 = m.ReleaseSite(
    name = 'Release_Site_5',
    complex = m.Complex('NCX', orientation = m.Orientation.UP),
    region = Mushroom_dendrite_neck,
    density = NCX_IC_NECK
)

Release_Site_6 = m.ReleaseSite(
    name = 'Release_Site_6',
    complex = m.Complex('Bm'),
    region = Mushroom_transparent - SA,
    concentration = Bm_IC
)

Release_Site_7 = m.ReleaseSite(
    name = 'Release_Site_7',
    complex = m.Complex('Bf', orientation = m.Orientation.UP),
    region = Mushroom_dendrite_spine,
    density = Bf_IC
)

Release_Site_8 = m.ReleaseSite(
    name = 'Release_Site_8',
    complex = m.Complex('VSCC_0', orientation = m.Orientation.UP),
    region = Mushroom_dendrite_spine,
    density = VSCC_IC
)

Release_Site_9 = m.ReleaseSite(
    name = 'Release_Site_9',
    complex = m.Complex('NMDAR_0', orientation = m.Orientation.UP),
    region = Mushroom_dendrite_PSD,
    number_to_release = n_NMDAR
)

Release_Site_10 = m.ReleaseSite(
    name = 'Release_Site_10',
    complex = m.Complex('AMPAR_0', orientation = m.Orientation.UP),
    region = Mushroom_dendrite_PSD,
    number_to_release = n_AMPAR
)

Release_Site_11 = m.ReleaseSite(
    name = 'Release_Site_11',
    complex = m.Complex('glu'),
    shape = m.Shape.SPHERICAL,
    location = (-0.1771, 0.3303, 0.8808),
    site_diameter = 0,
    number_to_release = n_glu1
)

Release_Site_12 = m.ReleaseSite(
    name = 'Release_Site_12',
    complex = m.Complex('Ca2_ER'),
    region = SA,
    concentration = Ca_ER_IC
)

Release_Site_13 = m.ReleaseSite(
    name = 'Release_Site_13',
    complex = m.Complex('SERCAx', orientation = m.Orientation.UP),
    region = SA,
    density = SERCA_IC
)

Release_Site_14 = m.ReleaseSite(
    name = 'Release_Site_14',
    complex = m.Complex('RyR_C(a~0, i~0)', orientation = m.Orientation.UP),
    region = SA_neck,
    number_to_release = 60
)

Release_Site_17 = m.ReleaseSite(
    name = 'Release_Site_17',
    complex = m.Complex('PMCA', orientation = m.Orientation.UP),
    region = Mushroom_dendrite_cylinder_receptors,
    density = PMCA_IC_HEAD
)

Release_Site_18 = m.ReleaseSite(
    name = 'Release_Site_18',
    complex = m.Complex('NCX', orientation = m.Orientation.UP),
    region = Mushroom_dendrite_cylinder_receptors,
    density = NCX_IC_HEAD
)

Release_Site_19 = m.ReleaseSite(
    name = 'Release_Site_19',
    complex = m.Complex('glu'),
    shape = m.Shape.SPHERICAL,
    location = (-0.2641, -0.1785, 0.9758),
    site_diameter = 0,
    number_to_release = n_glu2
)

# ---- create instantiation object and add components ----

instantiation = m.Instantiation()
instantiation.add_geometry_object(Cube)
instantiation.add_geometry_object(Mushroom_dendrite)
instantiation.add_geometry_object(Mushroom_transparent)
instantiation.add_geometry_object(SA)
instantiation.add_geometry_object(presynapse_PSD1)
instantiation.add_geometry_object(presynapse_PSD2)
instantiation.add_release_site(Release_Site_1)
instantiation.add_release_site(Release_Site_2)
instantiation.add_release_site(Release_Site_3)
instantiation.add_release_site(Release_Site_4)
instantiation.add_release_site(Release_Site_5)
instantiation.add_release_site(Release_Site_6)
instantiation.add_release_site(Release_Site_7)
instantiation.add_release_site(Release_Site_8)
instantiation.add_release_site(Release_Site_9)
instantiation.add_release_site(Release_Site_10)
instantiation.add_release_site(Release_Site_11)
instantiation.add_release_site(Release_Site_12)
instantiation.add_release_site(Release_Site_13)
instantiation.add_release_site(Release_Site_14)
instantiation.add_release_site(Release_Site_17)
instantiation.add_release_site(Release_Site_18)
instantiation.add_release_site(Release_Site_19)

# load seed species information from bngl file
instantiation.load_bngl_compartments_and_seed_species(os.path.join(MODEL_PATH, 'model.bngl'), None, shared.parameter_overrides)

