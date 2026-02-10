# Ensemble-Generator

Files used in generating 100K Ensemble Protein Structures. Structures were made by using Rosetta and Flexible Meccano, and Chemical Shifts were determined by PPM_One. 

Core Scripts can be found in 100K_all_AminoAcid_ensemble, other folders contain additional created ensembles 

Summary of Contents:
|File Name        | File Description |    
|:----------------|:------------|
|000_make_folders.sh| Script creating folders for all the amino acids |
|002_make_the2klists.sh| Script matching files and appending into a singular text file|
|004A_make_fixbb_folders.sh| Creates folders for fixed backbone of structures|
|004B_submit_all_fixbb.sh| Script applies fixing of backbone on structures|
|005_make_cs_folders.sh| Creates folders to place the chemical shift prediction values|
|006_submit_predict_cs.sh| Script submitting structures into PPM_One|
|007_make_joined_rama_cs_folders.sh| Creates folders for analysis on ensemble results|
|008_run_all_join_dihedral_cs.py| Python script gathers Phi, Psi, and Chemical Shifts onto one file|


Python Dependencies are within __pyproject.toml__ and can be installed by:

```
python -m install python .
```

Rosetta Version used was 3.14 release 371
* Rosetta can be downloaded [here](https://downloads.rosettacommons.org/downloads/academic) 
* Flexible Meccano can be obtained [here](https://www.ibs.fr/fr/communication/production-scientifique/logiciels/flexible-meccano)
* PPM_One can be obtained [here](https://github.com/UD-CRPL/ppm_one)
