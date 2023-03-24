#!/bin/bash

scapper_file=DataScrapper.py

pwd

cp /fs/scratch/PAS0536/Swathi/InstallerTest/harp/cheetah/examples/01-eulers_number/$scapper_file $scapper_file

python $scapper_file "train"


