#!/bin/bash
#SBATCH --job-name=website
#SBATCH --partition=fast
#SBATCH --ntasks=1
#SBATCH --time=22:00:00
#SBATCH --output=output/job-%j.out

echo "Start of Script"

echo "job-"$JobID
echo "googlenews_results_03+49_06-04-2020.csv"
python summarizer.py

echo "End of Script"
