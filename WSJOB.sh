#!/bin/bash
#SBATCH --job-name=website
#SBATCH --partition=fast
#SBATCH --ntasks=1
#SBATCH --time=22:00:00
#SBATCH --output=out/job-%j.out

echo "Start of Script"

python main.py


echo "End of Script"
