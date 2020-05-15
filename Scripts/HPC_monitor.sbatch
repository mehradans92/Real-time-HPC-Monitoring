#!/bin/bash
#SBATCH --partition standard
#SBATCH --time 0-120:00:00
#SBATCH -o HPC_MONITOR 
#SBATCH -N 1 
#SBATCH --cpus-per-task=1
#SBATCH --mail-type=ALL
####################################################
##########MACHINE SPECIFIC DETAILS GO HERE##########
####################################################
./scp.sh
