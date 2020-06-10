#!/bin/bash
#SBATCH --job-name=website
#SBATCH --partition=fast
#SBATCH --ntasks=1
#SBATCH --time=22:00:00
#SBATCH --output=output/job-%j.out

source ~/env/bin/activate

echo "Start of Script"

echo "starting from index 4310"

python summarizer.py

echo "End of Script"
