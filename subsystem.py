# WARNING: This is an automatically generated file and will be overwritten
#          by CellBlender on the next model export.

import os
import shared
import mcell as m

from parameters import *

# ---- subsystem ----

MODEL_PATH = os.path.dirname(os.path.abspath(__file__))

PSD = m.SurfaceClass(
    name = 'PSD',
    type = m.SurfacePropertyType.REACTIVE
)

Surface_base = m.SurfaceClass(
    name = 'Surface_base',
    type = m.SurfacePropertyType.TRANSPARENT,
    affected_complex_pattern = m.Complex('Ca2', orientation = m.Orientation.DOWN)
)

Surface_cube = m.SurfaceClass(
    name = 'Surface_cube',
    type = m.SurfacePropertyType.ABSORPTIVE,
    affected_complex_pattern = m.AllMolecules
)

Ions_mushroom = m.SurfaceClass(
    name = 'Ions_mushroom',
    type = m.SurfacePropertyType.TRANSPARENT,
    affected_complex_pattern = m.AllMolecules
)

Cylinder_reflective = m.SurfaceClass(
    name = 'Cylinder_reflective',
    type = m.SurfacePropertyType.REFLECTIVE,
    affected_complex_pattern = m.AllMolecules
)

Cylinder_side = m.SurfaceClass(
    name = 'Cylinder_side',
    type = m.SurfacePropertyType.TRANSPARENT,
    affected_complex_pattern = m.AllMolecules
)

SA_membrane = m.SurfaceClass(
    name = 'SA_membrane',
    type = m.SurfacePropertyType.REFLECTIVE,
    affected_complex_pattern = m.AllMolecules
)

rxn_VSCC = m.ReactionRule(
    name = 'rxn_VSCC',
    reactants = [ m.Complex('VSCC') ],
    products = [ m.Complex('VSCC'), m.Complex('Ca2@IN', compartment_name = 'IN') ],
    variable_rate = vscc_rate_scaled
)

unnamed_reaction_rule_8 = m.ReactionRule(
    name = 'unnamed_reaction_rule_8',
    reactants = [ m.Complex('VSCC_0') ],
    products = [ m.Complex('VSCC_1') ],
    variable_rate = vscc_1_forward_scaled
)

unnamed_reaction_rule_9 = m.ReactionRule(
    name = 'unnamed_reaction_rule_9',
    reactants = [ m.Complex('VSCC_1') ],
    products = [ m.Complex('VSCC_2') ],
    variable_rate = vscc_2_forward_scaled
)

unnamed_reaction_rule_10 = m.ReactionRule(
    name = 'unnamed_reaction_rule_10',
    reactants = [ m.Complex('VSCC_2') ],
    products = [ m.Complex('VSCC_3') ],
    variable_rate = vscc_3_forward_scaled
)

unnamed_reaction_rule_11 = m.ReactionRule(
    name = 'unnamed_reaction_rule_11',
    reactants = [ m.Complex('VSCC_3') ],
    products = [ m.Complex('VSCC') ],
    variable_rate = vscc_4_forward_scaled
)

unnamed_reaction_rule_20 = m.ReactionRule(
    name = 'unnamed_reaction_rule_20',
    reactants = [ m.Complex('NMDAR') ],
    products = [ m.Complex('NMDAR_B') ],
    variable_rate = k_B_rate
)

rxn_NMDAR = m.ReactionRule(
    name = 'rxn_NMDAR',
    reactants = [ m.Complex('NMDAR') ],
    products = [ m.Complex('NMDAR'), m.Complex('Ca2@IN', compartment_name = 'IN') ],
    variable_rate = nmdar_rate_scaled
)

unnamed_reaction_rule_29 = m.ReactionRule(
    name = 'unnamed_reaction_rule_29',
    reactants = [ m.Complex('VSCC_1') ],
    products = [ m.Complex('VSCC_0') ],
    variable_rate = vscc_1_reverse_scaled
)

unnamed_reaction_rule_30 = m.ReactionRule(
    name = 'unnamed_reaction_rule_30',
    reactants = [ m.Complex('VSCC_2') ],
    products = [ m.Complex('VSCC_1') ],
    variable_rate = vscc_2_reverse_scaled
)

unnamed_reaction_rule_31 = m.ReactionRule(
    name = 'unnamed_reaction_rule_31',
    reactants = [ m.Complex('VSCC_3') ],
    products = [ m.Complex('VSCC_2') ],
    variable_rate = vscc_3_reverse_scaled
)

unnamed_reaction_rule_32 = m.ReactionRule(
    name = 'unnamed_reaction_rule_32',
    reactants = [ m.Complex('VSCC') ],
    products = [ m.Complex('VSCC_3') ],
    variable_rate = vscc_4_reverse_scaled
)

unnamed_reaction_rule_33 = m.ReactionRule(
    name = 'unnamed_reaction_rule_33',
    reactants = [ m.Complex('NMDAR_B') ],
    products = [ m.Complex('NMDAR') ],
    variable_rate = k_U_rate
)

rxn_SERCA3_leak = m.ReactionRule(
    name = 'rxn_SERCA3_leak',
    reactants = [ m.Complex('Ca2_ER@IN', compartment_name = 'IN'), m.Complex('SA_membrane') ],
    products = [ m.Complex('Ca2@OUT', compartment_name = 'OUT') ],
    fwd_rate = k_SERCA3_leak
)

# ---- create subsystem object and add components ----

subsystem = m.Subsystem()
subsystem.add_surface_class(PSD)
subsystem.add_surface_class(Surface_base)
subsystem.add_surface_class(Surface_cube)
subsystem.add_surface_class(Ions_mushroom)
subsystem.add_surface_class(Cylinder_reflective)
subsystem.add_surface_class(Cylinder_side)
subsystem.add_surface_class(SA_membrane)
subsystem.add_reaction_rule(rxn_VSCC)
subsystem.add_reaction_rule(unnamed_reaction_rule_8)
subsystem.add_reaction_rule(unnamed_reaction_rule_9)
subsystem.add_reaction_rule(unnamed_reaction_rule_10)
subsystem.add_reaction_rule(unnamed_reaction_rule_11)
subsystem.add_reaction_rule(unnamed_reaction_rule_20)
subsystem.add_reaction_rule(rxn_NMDAR)
subsystem.add_reaction_rule(unnamed_reaction_rule_29)
subsystem.add_reaction_rule(unnamed_reaction_rule_30)
subsystem.add_reaction_rule(unnamed_reaction_rule_31)
subsystem.add_reaction_rule(unnamed_reaction_rule_32)
subsystem.add_reaction_rule(unnamed_reaction_rule_33)
subsystem.add_reaction_rule(rxn_SERCA3_leak)

# load subsystem information from bngl file
subsystem.load_bngl_molecule_types_and_reaction_rules(os.path.join(MODEL_PATH, 'model.bngl'), shared.parameter_overrides)

# set additional information about species and molecule types that cannot be stored in BNGL,
# elementary molecule types are already in the subsystem after they were loaded from BNGL
def set_bngl_molecule_types_info(subsystem):
    Ca2 = subsystem.find_elementary_molecule_type('Ca2')
    assert Ca2, "Elementary molecule type 'Ca2' was not found"
    Ca2.diffusion_constant_3d = 2.2e-6

    VSCC = subsystem.find_elementary_molecule_type('VSCC')
    assert VSCC, "Elementary molecule type 'VSCC' was not found"
    VSCC.diffusion_constant_2d = 0

    PMCA = subsystem.find_elementary_molecule_type('PMCA')
    assert PMCA, "Elementary molecule type 'PMCA' was not found"
    PMCA.diffusion_constant_2d = 0

    PMCA1 = subsystem.find_elementary_molecule_type('PMCA1')
    assert PMCA1, "Elementary molecule type 'PMCA1' was not found"
    PMCA1.diffusion_constant_2d = 0

    NCX = subsystem.find_elementary_molecule_type('NCX')
    assert NCX, "Elementary molecule type 'NCX' was not found"
    NCX.diffusion_constant_2d = 0

    NCX1 = subsystem.find_elementary_molecule_type('NCX1')
    assert NCX1, "Elementary molecule type 'NCX1' was not found"
    NCX1.diffusion_constant_2d = 0

    SERCA3x = subsystem.find_elementary_molecule_type('SERCA3x')
    assert SERCA3x, "Elementary molecule type 'SERCA3x' was not found"
    SERCA3x.diffusion_constant_2d = 0

    SERCA3x1 = subsystem.find_elementary_molecule_type('SERCA3x1')
    assert SERCA3x1, "Elementary molecule type 'SERCA3x1' was not found"
    SERCA3x1.diffusion_constant_2d = 0

    SERCA3x2 = subsystem.find_elementary_molecule_type('SERCA3x2')
    assert SERCA3x2, "Elementary molecule type 'SERCA3x2' was not found"
    SERCA3x2.diffusion_constant_2d = 0

    SERCA3y = subsystem.find_elementary_molecule_type('SERCA3y')
    assert SERCA3y, "Elementary molecule type 'SERCA3y' was not found"
    SERCA3y.diffusion_constant_2d = 0

    SERCA3y1 = subsystem.find_elementary_molecule_type('SERCA3y1')
    assert SERCA3y1, "Elementary molecule type 'SERCA3y1' was not found"
    SERCA3y1.diffusion_constant_2d = 0

    SERCA3y2 = subsystem.find_elementary_molecule_type('SERCA3y2')
    assert SERCA3y2, "Elementary molecule type 'SERCA3y2' was not found"
    SERCA3y2.diffusion_constant_2d = 0

    VSCC_0 = subsystem.find_elementary_molecule_type('VSCC_0')
    assert VSCC_0, "Elementary molecule type 'VSCC_0' was not found"
    VSCC_0.diffusion_constant_2d = 0

    VSCC_1 = subsystem.find_elementary_molecule_type('VSCC_1')
    assert VSCC_1, "Elementary molecule type 'VSCC_1' was not found"
    VSCC_1.diffusion_constant_2d = 0

    VSCC_2 = subsystem.find_elementary_molecule_type('VSCC_2')
    assert VSCC_2, "Elementary molecule type 'VSCC_2' was not found"
    VSCC_2.diffusion_constant_2d = 0

    VSCC_3 = subsystem.find_elementary_molecule_type('VSCC_3')
    assert VSCC_3, "Elementary molecule type 'VSCC_3' was not found"
    VSCC_3.diffusion_constant_2d = 0
    VSCC_3.custom_time_step = 1e-7

    NMDAR_0 = subsystem.find_elementary_molecule_type('NMDAR_0')
    assert NMDAR_0, "Elementary molecule type 'NMDAR_0' was not found"
    NMDAR_0.diffusion_constant_2d = 0
    NMDAR_0.custom_time_step = 1e-7

    NMDAR_1 = subsystem.find_elementary_molecule_type('NMDAR_1')
    assert NMDAR_1, "Elementary molecule type 'NMDAR_1' was not found"
    NMDAR_1.diffusion_constant_2d = 0

    NMDAR_2 = subsystem.find_elementary_molecule_type('NMDAR_2')
    assert NMDAR_2, "Elementary molecule type 'NMDAR_2' was not found"
    NMDAR_2.diffusion_constant_2d = 0

    NMDAR_D = subsystem.find_elementary_molecule_type('NMDAR_D')
    assert NMDAR_D, "Elementary molecule type 'NMDAR_D' was not found"
    NMDAR_D.diffusion_constant_2d = 0

    NMDAR_0B = subsystem.find_elementary_molecule_type('NMDAR_0B')
    assert NMDAR_0B, "Elementary molecule type 'NMDAR_0B' was not found"
    NMDAR_0B.diffusion_constant_2d = 0

    NMDAR_1B = subsystem.find_elementary_molecule_type('NMDAR_1B')
    assert NMDAR_1B, "Elementary molecule type 'NMDAR_1B' was not found"
    NMDAR_1B.diffusion_constant_2d = 0

    NMDAR_2B = subsystem.find_elementary_molecule_type('NMDAR_2B')
    assert NMDAR_2B, "Elementary molecule type 'NMDAR_2B' was not found"
    NMDAR_2B.diffusion_constant_2d = 0

    NMDAR_DB = subsystem.find_elementary_molecule_type('NMDAR_DB')
    assert NMDAR_DB, "Elementary molecule type 'NMDAR_DB' was not found"
    NMDAR_DB.diffusion_constant_2d = 0

    NMDAR = subsystem.find_elementary_molecule_type('NMDAR')
    assert NMDAR, "Elementary molecule type 'NMDAR' was not found"
    NMDAR.diffusion_constant_2d = 0

    NMDAR_B = subsystem.find_elementary_molecule_type('NMDAR_B')
    assert NMDAR_B, "Elementary molecule type 'NMDAR_B' was not found"
    NMDAR_B.diffusion_constant_2d = 0

    AMPAR_0 = subsystem.find_elementary_molecule_type('AMPAR_0')
    assert AMPAR_0, "Elementary molecule type 'AMPAR_0' was not found"
    AMPAR_0.diffusion_constant_2d = 0
    AMPAR_0.custom_time_step = 1e-7

    AMPAR_1 = subsystem.find_elementary_molecule_type('AMPAR_1')
    assert AMPAR_1, "Elementary molecule type 'AMPAR_1' was not found"
    AMPAR_1.diffusion_constant_2d = 0

    AMPAR_2 = subsystem.find_elementary_molecule_type('AMPAR_2')
    assert AMPAR_2, "Elementary molecule type 'AMPAR_2' was not found"
    AMPAR_2.diffusion_constant_2d = 0

    AMPAR_3 = subsystem.find_elementary_molecule_type('AMPAR_3')
    assert AMPAR_3, "Elementary molecule type 'AMPAR_3' was not found"
    AMPAR_3.diffusion_constant_2d = 0

    AMPAR_4 = subsystem.find_elementary_molecule_type('AMPAR_4')
    assert AMPAR_4, "Elementary molecule type 'AMPAR_4' was not found"
    AMPAR_4.diffusion_constant_2d = 0

    AMPAR_5 = subsystem.find_elementary_molecule_type('AMPAR_5')
    assert AMPAR_5, "Elementary molecule type 'AMPAR_5' was not found"
    AMPAR_5.diffusion_constant_2d = 0

    AMPAR = subsystem.find_elementary_molecule_type('AMPAR')
    assert AMPAR, "Elementary molecule type 'AMPAR' was not found"
    AMPAR.diffusion_constant_2d = 0

    glu = subsystem.find_elementary_molecule_type('glu')
    assert glu, "Elementary molecule type 'glu' was not found"
    glu.diffusion_constant_3d = 2.2e-6
    glu.custom_time_step = 1e-7

    Ca2_ER = subsystem.find_elementary_molecule_type('Ca2_ER')
    assert Ca2_ER, "Elementary molecule type 'Ca2_ER' was not found"
    Ca2_ER.diffusion_constant_3d = 2.2e-6


set_bngl_molecule_types_info(subsystem)
