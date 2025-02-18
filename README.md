# isc-paper-data-2024
Cross section data for semi-classical approach to computing vibrationally resolved ionization cross sections for molecular nitrogen.

The cross sections were computed at incident electron energies (eV) using np.concatenate((np.linspace(1,100,199), np.linspace(110,1000,90), np.linspace(1100,10000,90))).

The partial cross sections (m^2) were computed for n2(state (p))(v') -> n2p(state pp)(v'').
The lumped partial cross sections (m^2) are summed over v'': n2(state p)(v') -> sum[over vpp](n2p(state pp)(v'')). The lumped cross sections are generated from the partial cross sections based on the v' dissociation limit, and the FCF p',v' -> p'' closure relation where the max v'' is the v'' needed for the closure relation.

The n2n2p_pcs.pkl file contains the partial cross sections.
The n2n2p_lcs.pkl file contains the lumped cross sections.

The environment.yml contains the necessary packages to import the pkl files and convert them into nested dictionaries for the state to state interactions, with the cross sections being contained in a numpy array. Once imported, the cross sections can be freely exported or converted into the desired data format. 