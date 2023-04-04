#!/bin/bash

scapper_file=DataScrapper.py

cp /<download_dir>/harp/examples/01-eulers_number/$scapper_file $scapper_file

python $scapper_file "train"


