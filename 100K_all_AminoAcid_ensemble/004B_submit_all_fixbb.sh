#!/bin/bash
#Set directories to the execution for rosetta 
#Set directories to resfile.txt

FIXBB_EXEC="/rosetta_bin_linux_3.14_bundle/rosetta.binary.linux.release-371/main/source/bin/fixbb.default.linuxgccrelease"
DB="/rosetta_bin_linux_3.14_bundle/rosetta.binary.linux.release-371/main/database"


for i in A C D E F G H I K L M N P Q R S T V Y W
do
    mkdir 005_${i}_fm2_fixbb
done

for listname in $( ls -1 003_*.txt ); do
    ## set output folder name
    listname_remove_end=${listname%.txt}
    amino_acid=${listname_remove_end#003_1klist_}
    outfolder=005_${amino_acid}_fm2_fixbb

    cd $outfolder
    $FIXBB_EXEC -database $DB -in:file:list ../$listname -in:file:fullatom -resfile "/resfile.txt" -multi_cool_annealer 6 -nstruct 1 -ignore_zero_occupancy false -ignore_unrecognized_res -ex1 -ex2 -extrachi_cutoff 0 -linmem_ig 10
    cd ..
done
