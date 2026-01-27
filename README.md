# Ensemble-Generator

Files utlizied to generate Ensemble of 100K Protein Structures. Structures were made by Rosetta and Flexible Meccano, and Chemical Shifts were determined by PPM_One 


Summary of Contents:
|File Name        | Description |    
|:----------------|:------------|
|000_make_folders.sh| Script creating folders for all the amino acids |
|002_make_the2klists.sh|  |
|004A_make_fixbb_folders.sh| |
|004B_submit_all_fixbb.sh| |
|005_make_cs_folders.sh| |
|006_submit_predict_cs.sh| |
|007_make_joined_rama_cs_folders.sh| Script joining the Ramachandran plots and Chemical Shifts|
|008_run_all_join_dihedral_cs.py| Python Script for gathering Chemical Shifts onto one file|

Rosetta  Version Utilized was 3.14

Python Libraries can be all installed via 
(pip install file.py)
