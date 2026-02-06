#!/bin/bash

for i in G
do
    cp -r 000_fm2_wSC_template 001_${i}_fm2_wSC
    sed -i "s/X/${i}/g" 001_${i}_fm2_wSC/003_polyala.seq
done
echo ""
echo "Success!"
echo ""
echo "... now ..."
echo ""

# Pre-proline
echo "Do Pre-proline manually!"
echo 'cp -r 000_fm2_wSC_template 001_X_fm2_wSC'
echo "Change 26 X to A and 27 A to P."
echo ""

# Pre-proline
echo "Do proline-proline manually!"
echo 'cp -r 000_fm2_wSC_template 001_Z_fm2_wSC'
echo "Change 26 X to P and 27 A to P."
echo ""
