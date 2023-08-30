#!/bin/bash

# This is the location to store all 
export HARP_STORE="$SCRATCH/HARP_STORE"
mkdir -p $HARP_STORE
# This is the location for storing temp emulated data - logs, oputput files, etc. 
export TARGET_APP="$SCRATCH/TARGET_APP"
mkdir -p $TARGET_APP


echo "Copying the application to be profiled (the complete folder path to the application should be provided)"
cp -R /app/examples/* $TARGET_APP/.
chmod -R 755 $TARGET_APP/*
export APP_HOME="$TARGET_APP/01-eulers_number"
cd $APP_HOME
harp pipeline_config.json

