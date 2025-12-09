# WARNING: This is an automatically generated file and will be overwritten
#          by CellBlender on the next model export.

import os
import shared
import mcell as m

from parameters import *
from subsystem import *
from geometry import *
MODEL_PATH = os.path.dirname(os.path.abspath(__file__))


# ---- observables ----

viz_output = m.VizOutput(
    mode = m.VizMode.CELLBLENDER,
    output_files_prefix = './viz_data/seed_' + str(SEED).zfill(5) + '/Scene',
    every_n_timesteps = 1
)

# ---- declaration of rxn rules defined in BNGL and used in counts ----

cterm_count_Ca2_species_Mushroom_transparent = m.CountTerm(
    species_pattern = m.Complex('Ca2'),
    region = Mushroom_transparent
)

count_Ca2_Mushroom_transparent = m.Count(
    name = 'Ca2_Mushroom_transparent',
    expression = cterm_count_Ca2_species_Mushroom_transparent,
    file_name = './react_data/seed_' + str(SEED).zfill(5) + '/Ca2_Mushroom_transparent.dat',
    every_n_timesteps = 1e-6/1e-8
)

cterm_count_Ca2_species = m.CountTerm(
    species_pattern = m.Complex('Ca2')
)

count_Ca2_World = m.Count(
    name = 'Ca2_World',
    expression = cterm_count_Ca2_species,
    file_name = './react_data/seed_' + str(SEED).zfill(5) + '/Ca2_World.dat',
    every_n_timesteps = 1e-6/1e-8
)

cterm_count_CaBm_species_Mushroom_transparent = m.CountTerm(
    species_pattern = m.Complex('CaBm'),
    region = Mushroom_transparent
)

count_CaBm_Mushroom_transparent = m.Count(
    name = 'CaBm_Mushroom_transparent',
    expression = cterm_count_CaBm_species_Mushroom_transparent,
    file_name = './react_data/seed_' + str(SEED).zfill(5) + '/CaBm_Mushroom_transparent.dat',
    every_n_timesteps = 1e-6/1e-8
)

cterm_count_CaBf_species = m.CountTerm(
    species_pattern = m.Complex('CaBf')
)

count_CaBf_World = m.Count(
    name = 'CaBf_World',
    expression = cterm_count_CaBf_species,
    file_name = './react_data/seed_' + str(SEED).zfill(5) + '/CaBf_World.dat',
    every_n_timesteps = 1e-6/1e-8
)

cterm_count_Bf_species_Mushroom_transparent = m.CountTerm(
    species_pattern = m.Complex('Bf'),
    region = Mushroom_transparent
)

count_Bf_Mushroom_transparent = m.Count(
    name = 'Bf_Mushroom_transparent',
    expression = cterm_count_Bf_species_Mushroom_transparent,
    file_name = './react_data/seed_' + str(SEED).zfill(5) + '/Bf_Mushroom_transparent.dat',
    every_n_timesteps = 1e-6/1e-8
)

cterm_count_Bm_species_Mushroom_transparent = m.CountTerm(
    species_pattern = m.Complex('Bm'),
    region = Mushroom_transparent
)

count_Bm_Mushroom_transparent = m.Count(
    name = 'Bm_Mushroom_transparent',
    expression = cterm_count_Bm_species_Mushroom_transparent,
    file_name = './react_data/seed_' + str(SEED).zfill(5) + '/Bm_Mushroom_transparent.dat',
    every_n_timesteps = 1e-6/1e-8
)

cterm_count_VSCC_species = m.CountTerm(
    species_pattern = m.Complex('VSCC')
)

count_VSCC_World = m.Count(
    name = 'VSCC_World',
    expression = cterm_count_VSCC_species,
    file_name = './react_data/seed_' + str(SEED).zfill(5) + '/VSCC_World.dat',
    every_n_timesteps = 1e-6/1e-8
)

cterm_count_NMDAR_species = m.CountTerm(
    species_pattern = m.Complex('NMDAR')
)

count_NMDAR_World = m.Count(
    name = 'NMDAR_World',
    expression = cterm_count_NMDAR_species,
    file_name = './react_data/seed_' + str(SEED).zfill(5) + '/NMDAR_World.dat',
    every_n_timesteps = 1e-6/1e-8
)

cterm_count_PMCA1_species = m.CountTerm(
    species_pattern = m.Complex('PMCA1')
)

count_PMCA1_World = m.Count(
    name = 'PMCA1_World',
    expression = cterm_count_PMCA1_species,
    file_name = './react_data/seed_' + str(SEED).zfill(5) + '/PMCA1_World.dat',
    every_n_timesteps = 1e-6/1e-8
)

cterm_count_NCX1_species = m.CountTerm(
    species_pattern = m.Complex('NCX1')
)

count_NCX1_World = m.Count(
    name = 'NCX1_World',
    expression = cterm_count_NCX1_species,
    file_name = './react_data/seed_' + str(SEED).zfill(5) + '/NCX1_World.dat',
    every_n_timesteps = 1e-6/1e-8
)

cterm_count_Ca2_species_SA = m.CountTerm(
    species_pattern = m.Complex('Ca2'),
    region = SA
)

count_Ca2_SA = m.Count(
    name = 'Ca2_SA',
    expression = cterm_count_Ca2_species_SA,
    file_name = './react_data/seed_' + str(SEED).zfill(5) + '/Ca2_SA.dat',
    every_n_timesteps = 1e-6/1e-8
)

cterm_count_Ca2_ER_species_SA = m.CountTerm(
    species_pattern = m.Complex('Ca2_ER'),
    region = SA
)

count_Ca2_ER_SA = m.Count(
    name = 'Ca2_ER_SA',
    expression = cterm_count_Ca2_ER_species_SA,
    file_name = './react_data/seed_' + str(SEED).zfill(5) + '/Ca2_ER_SA.dat',
    every_n_timesteps = 1e-6/1e-8
)

cterm_count_RyR_O_species = m.CountTerm(
    species_pattern = m.Complex('RyR_O')
)

count_RyR_O_World = m.Count(
    name = 'RyR_O_World',
    expression = cterm_count_RyR_O_species,
    file_name = './react_data/seed_' + str(SEED).zfill(5) + '/RyR_O_World.dat',
    every_n_timesteps = 1e-6/1e-8
)

cterm_count_Ca2_species_Mushroom_dendrite = m.CountTerm(
    species_pattern = m.Complex('Ca2'),
    region = Mushroom_dendrite
)

count_Ca2_Mushroom_dendrite = m.Count(
    name = 'Ca2_Mushroom_dendrite',
    expression = cterm_count_Ca2_species_Mushroom_dendrite,
    file_name = './react_data/seed_' + str(SEED).zfill(5) + '/Ca2_Mushroom_dendrite.dat',
    every_n_timesteps = 1e-6/1e-8
)

# ---- create observables object and add components ----

observables = m.Observables()
#observables.add_viz_output(viz_output)
observables.add_count(count_Ca2_Mushroom_transparent)
observables.add_count(count_Ca2_World)
observables.add_count(count_CaBm_Mushroom_transparent)
observables.add_count(count_CaBf_World)
observables.add_count(count_Bf_Mushroom_transparent)
observables.add_count(count_Bm_Mushroom_transparent)
observables.add_count(count_VSCC_World)
observables.add_count(count_NMDAR_World)
observables.add_count(count_PMCA1_World)
observables.add_count(count_NCX1_World)
observables.add_count(count_Ca2_SA)
observables.add_count(count_Ca2_ER_SA)
observables.add_count(count_RyR_O_World)
observables.add_count(count_Ca2_Mushroom_dendrite)
