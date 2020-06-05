#!/bin/bash
#SBATCH --job-name=test    
#SBATCH --partition=fast
#SBATCH --ntasks=1
#SBATCH --time=10:00:00     
#SBATCH --output=test-job.%j.out  module load python

echo "Start of Script"


python together.py


echo "End of Script"