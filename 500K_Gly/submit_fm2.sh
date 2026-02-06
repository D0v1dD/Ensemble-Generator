

#!/bin/bash

​

#SBATCH --job-name=fm2

#SBATCH --partition=super

#SBATCH --nodes=1

#SBATCH --time=00-02:00:00

#SBATCH --output=single.%j.out

#SBATCH --error=single.%j.err

​

SEQ_FILE="003_polyala.seq"

NUM_CONFORMERS=500000

AALEN=51

​

FM2_EXEC="/home/yiling/data/Sakshi/230309_polyA_10Kensemble_pred/FM_package/fm2"

DLIB="/home/yiling/data/Sakshi/230309_polyA_10Kensemble_pred/FM_package/phi_psi_database_loop_glysymm"

FORT0="/home/yiling/data/Sakshi/230309_polyA_10Kensemble_pred/FM_package/fort.0"

FM2_FOLDER_PATH="/home/yiling/data/Sakshi/230309_polyA_10Kensemble_pred/FM_package/"

​

#cp $DLIB .

#cp $FORT0 .

cp -f $FM2_FOLDER_PATH/toppar_mcr .

cp -f $FM2_FOLDER_PATH/toppar .

​

$FM2_EXEC $AALEN $NUM_CONFORMERS 0 $SEQ_FILE $FORT0 $DLIB out


