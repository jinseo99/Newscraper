#!/bin/bash
#SBATCH --job-name=website
#SBATCH --partition=fast
#SBATCH --ntasks=1
#SBATCH --time=22:00:00
#SBATCH --output=output/job-%j.out

echo "Start of Script"

echo output
echo "starting from index 4310"

python summarizer.py

echo "End of Script"
