#!/bin/bash


# for each folder including the prePro (X) and ProPro (Z)
for i in G
do
      # Find matching files and append them to the list
    find 001_${i}_fm2_wSC -type f -name "?b_51.pdb"    >> 003_1klist_${i}.txt
    find 001_${i}_fm2_wSC -type f -name "??b_51.pdb"   >> 003_1klist_${i}.txt
    find 001_${i}_fm2_wSC -type f -name "???b_51.pdb"  >> 003_1klist_${i}.txt
    find 001_${i}_fm2_wSC -type f -name "????b_51.pdb" >> 003_1klist_${i}.txt
    find 001_${i}_fm2_wSC -type f -name "?????b_51.pdb" >> 003_1klist_${i}.txt
    find 001_${i}_fm2_wSC -type f -name "??????b_51.pdb" >> 003_1klist_${i}.txt

done


# Add ../ to all the paths so that fixbb script works afterwards
sed -i 's/^001_/..\/001_/g' 003_1klist_*
