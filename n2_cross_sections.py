# %%
#from pathlib import Path
from pickle import dump, load
import numpy as np
#import pandas as pd
#import matplotlib as mpl
#from matplotlib.pyplot import plot as plt

# %%
def pkl_dict(pkl_filename:str, action:str, desired_dict=None, debug=False):
    #pkl_dir = f'pkl'
    #Path(pkl_dir).mkdir(parents=True, exist_ok=True)
    pkl_file = f'pkl/{pkl_filename}'
    if action == 'dump':
        with open(pkl_file, 'w+b', ) as f:
            dump(desired_dict, f)
    elif action == 'load':
        with open(pkl_file, 'r+b') as f:
            desired_dict = load(f)
        if debug: print(f"len(desired_dict): {len(desired_dict)}")
        return desired_dict
    else:
        raise Exception('implemented options are load and dump')

def print_active_states(states_dict, exclude_states_list):
    for _, (state_key, state_dict) in enumerate(states_dict.items()):
        if state_key not in exclude_states_list:
            print(f"{state_dict['name']} {state_key}")

# %%
# Electron energies used to compute the partial and total cross sections in the pkl files
incident_electron_energy = np.concatenate((np.linspace(1,100,199), 
                                          np.linspace(110,1000,90), 
                                          np.linspace(1100,10000,90)))

n2_exclude_states = ['n2_1Ag2', 'n2_1Ag3', 'n2_1Ag4', 
                     'n2_3Ag1', 'n2_3Ag2',
                     'n2_1B1g1', 'n2_1B1g2',
                     'n2_3B1g1', 'n2_3B1g2',
                     'n2_1B3u2', 'n2_3B1u3',
                     'n2_1B1u1',
                     'n2_1B3u1', 'n2_1B3u2', 'n2_1B3u3',
                     'n2_3B3u2', 'n2_3B3u3',
                     'n2_3Au1']

n2p_exclude_states = ['n2p_2Ag2', 
                      'n2p_2B2g2',
                      'n2p_2Au1', 
                      'n2p_2Au2', 
                      'n2p_2B1u2', 'n2p_2B1u3',
                      'n2p_2B3u2',
                      'n2p_2Au1',
                      'n2p_4Au1']

n2_pkl_filename = 'n2.pkl'
n2p_pkl_filename = 'n2p.pkl'
n2_partial_cs_pkl_filename = 'n2n2p_pcs.pkl'
n2_lumped_cs_pkl_filename = 'n2n2p_lcs.pkl'

n2_states_dict = pkl_dict(n2_pkl_filename, action='load', debug=False)
n2p_states_dict = pkl_dict(n2p_pkl_filename, action='load', debug=False)

print_active_states(n2_states_dict, n2_exclude_states)
print_active_states(n2p_states_dict, n2p_exclude_states)

n2_partial_cross_sections = pkl_dict(n2_partial_cs_pkl_filename, action='load', debug=False)
n2_lumped_cross_sections = pkl_dict(n2_lumped_cs_pkl_filename, action='load', debug=False)

# the partial and total cross sections are held in nested dictionaries, with the final array
# of cross sections (m^2) having been computed at the incident electron energy (eV) in the array above
# n2_partial_cross_sections['n2 state (p)']['n2p state (pp)'][vp][vpp] = np.array(cross sections at electron incident energies)
# n2_lumped_cross_sections['n2 state (p)']['n2p state (pp)'][vp] = np.array(cross sections summation over vpp at electron incident energies)
# %%
n2_partial_cross_sections.keys()
# %%
n2_partial_cross_sections['n2_1Ag1'].keys()
# %%
n2_partial_cross_sections['n2_1Ag1']['n2p_2Ag1'].keys()
# %%
n2_partial_cross_sections['n2_1Ag1']['n2p_2Ag1'][0].keys()
# %%
n2_partial_cross_sections['n2_1Ag1']['n2p_2Ag1'][0][0]
# %%
n2_lumped_cross_sections.keys()
# %%
n2_lumped_cross_sections['n2_1Ag1'].keys()
# %%
n2_lumped_cross_sections['n2_1Ag1']['n2p_2Ag1'].keys()
# %%
n2_lumped_cross_sections['n2_1Ag1']['n2p_2Ag1'][0]
# %%
