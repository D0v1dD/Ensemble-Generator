#!/bin/bash
#Change seq file as needed 
SEQ_FILE="003_polyala.seq"

NUM_CONFORMERS=100000

AALEN=51

​
#Adjust directories as needed
FM2_EXEC="/FM_package/fm2"

DLIB="/FM_package/phi_psi_database_loop_glysymm"

FORT0="/FM_package/fort.0"

FM2_FOLDER_PATH="/FM_package/"

​

#cp $DLIB .

#cp $FORT0 .

cp -f $FM2_FOLDER_PATH/toppar_mcr .

cp -f $FM2_FOLDER_PATH/toppar .

​

$FM2_EXEC $AALEN $NUM_CONFORMERS 0 $SEQ_FILE $FORT0 $DLIB out


