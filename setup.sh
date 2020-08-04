#!/bin/bash
# Script: setup.sh
# Purpose: Setup the Anaconda environment with dependencies
# Author: Piotr Stępień
# -------------------------------------------------------

conda env create --file environment.yml
conda activate vispy