#!/usr/bin/env python

from __future__ import print_function
from __future__ import with_statement
from __future__ import division
import os
import sys
import csv
import glob
import math
from tqdm import tqdm
import pandas as pd
import argparse
from Bio.PDB import *

def join_dihedral_cs(pdb_folder, cs_folder, output_filename, begin, end, resi_choice):
    ### some safety precautions ###
    resi_choice = resi_choice.upper()
    ### get the *.pdb file names ###
    pdbs = glob.glob(pdb_folder + "/*.pdb")
    parser = PDBParser(QUIET=True)
    ### THE DATAFRAME ###
    columns = ['#res', 'aa', 'phi', 'psi', 'ca', 'cb', 'c', 'n']
    df = pd.DataFrame(columns=columns)
    ### process each PDB separately ###
    for pdb in pdbs:  # UNCOMMENT when running with sbatch
        # for pdb in tqdm(pdbs): # COMMENT IN when running sbatch
        # (shows progress in the terminal)
        filename_core = pdb.split("/")[-1].split(".")[0]
        cs_path = cs_folder + "/" + filename_core + ".cs"
        ### check the *.cs file name ###
        if not os.path.isfile(cs_path):
            print("Error for file {}".format(filename_core))
            print("The PDB file and CS file don't have matching file cores\n")
            continue
            
        print(pdb)

        ### get the CS data ###
        current_aas = dict()
        CAs = dict()
        CBs = dict()
        COs = dict()
        Ns = dict()
        chem_shifts = {'CA': CAs, 'CB': CBs, 'CO': COs, 'N': Ns}
        with open(cs_path, 'r') as handle:
            body_flag = False
            for line in handle:
                if body_flag:
                    if line.strip() != "stop_":  # stop_ means the CS data has ended
                        atm_nr, res_nr, aa, at_id, at_id2, cs, dot, one = line.strip().split()
                        res_nr = int(res_nr)
                        if at_id == 'CA':
                            chem_shifts['CA'][res_nr] = float(cs)
                            current_aas[res_nr] = aa
                        elif at_id == 'CB':
                            chem_shifts['CB'][res_nr] = float(cs)
                            current_aas[res_nr] = aa
                        elif at_id == 'C':  # "C" is used for CO/C' atom!
                            chem_shifts['CO'][res_nr] = float(cs)
                            current_aas[res_nr] = aa
                        elif at_id == 'N':
                            chem_shifts['N'][res_nr] = float(cs)
                            current_aas[res_nr] = aa
                elif line.strip() == "_Chem_shift_ambiguity_code":  # start signal
                    body_flag = True

        ### some corrections to input ###
        if begin == 1:
            begin = 2
        if end == max(current_aas.keys()):
            end = max(current_aas.keys())
        if begin < min(current_aas.keys()):
            begin = min(current_aas.keys())
        if end > max(current_aas.keys()):
            end = max(current_aas.keys())

        ### get the dihedral data ...      ###
        ### ... combine with CS data ...   ###
        ### ... and store in a dictionary. ###
        data = parser.get_structure('conformer', pdb)
        for model in data.get_models():
            for chain in model.get_chains():
                res_names = []
                for residue in chain.get_residues():
                    res_names.append(residue.get_resname())
                poly = Polypeptide.Polypeptide(chain)
                phis_psis = poly.get_phi_psi_list()
                res_list = list(chain.get_residues())
                for m, n in zip(res_list, phis_psis):
                    i = int(m.id[1])
                    if begin <= i <= end:  # synuclein: 1-140
                        if m.get_resname() == resi_choice:
                            if m.get_resname() == "GLY":
                                df.loc[len(df)] = [
                                    i,
                                    m.get_resname(),
                                    n[0] * 180 / math.pi,
                                    n[1] * 180 / math.pi,
                                    chem_shifts['CA'][i],
                                    0.000 ,
                                    chem_shifts['CO'][i],
                                    chem_shifts['N'][i],
                                ]
                            elif m.get_resname() == "PRO":
                                df.loc[len(df)] = [
                                    i,
                                    m.get_resname(),
                                    n[0] * 180 / math.pi,
                                    n[1] * 180 / math.pi,
                                    chem_shifts['CA'][i],
                                    chem_shifts['CB'][i],
                                    chem_shifts['CO'][i],
                                    0.000,
                                ]
                            else:
                                if i not in chem_shifts['N']:
                                    print(f"Warning: Missing 'N' value for residue {i} in file {filename_core}")
                                else:
                                    df.loc[len(df)] = [
                                        i,
                                        m.get_resname(),
                                        n[0] * 180 / math.pi,
                                        n[1] * 180 / math.pi,
                                        chem_shifts['CA'][i],
                                        chem_shifts['CB'][i],
                                        chem_shifts['CO'][i],
                                        chem_shifts['N'][i],
                                    ]

    ### write to file ###
    df.to_csv(output_filename,
              sep="\t",
              index=False,
              float_format='%8.3f',
              quoting=csv.QUOTE_NONE,
              escapechar="\\"
              )

''' Join the information from the folders with PDB files and files containing PPM predictions. 
    The result is a single file that contains the phi, psi, and all CS for the analyzed amino acid. 
'''

import sys
import glob
import argparse
from Bio.Data.IUPACData import protein_letters_1to3 as one2three

def main():
    # List of all amino acids you need to process
    amino_acids = ["A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T"]
    
    for i in amino_acids: 
        input_folder_pdb = f"005_{i}_fm2_fixbb"
        input_folder_cs = f"008_{i}_fm2_cs"
        # I updated the filename to reflect that we are getting 25-27
        output_path = f"011_{i}_rama_cs/{i}_100K_allres_25_27.out"
        
        # ... (keep your existing if/elif logic for X and Z) ...
        else:
            aa1 = i
            aa3 = '{}'.format(one2three[aa1].upper())

        # Call the function for the range 25 to 27
        join_dihedral_cs(
            input_folder_pdb,
            input_folder_cs,
            output_path,
            25,  # Start at neighbor 25
            27,  # End at neighbor 27
            aa3, # Your variable central residue
        )

if __name__ == "__main__":
    main()
