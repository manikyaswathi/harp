# Estimating walltime to execute "calc_e.py" with given configurations : Calculating Euler's number

**This code if from "https://github.com/CODARcode/cheetah"**

To demonstrate the usage of HARP with Cheetah, we will look at a simple Python3
script which calculates Euler's number (`e`) using two different methods.
It takes three positional arguments: the first is a string describing which
of the methods to use, the second is a parameter to the calculation method
that describes how many iterations or how precise to try to make the
calculation (meaning depends on the method), and the third is a precision
to use with the stdandard library Decimal module in python. If the third
argument is not specified, built in floating point is used instead.

For this examples, we suppose that the application writer wants to understand
which method is 'better' - gets more digits correct in a short amount of time.
To do this, we need to run the application many times with different values
to the arguments and examine the output.

## The application

The source code is contained in a single source file: [calc\_e.py](calc_e.py).
There are no dependencies other than python3.

# How to use HARP to estimate the walltime for the program calc_e.py?
The current folder is called target application folder. 

1. Run the following commands (either in command line more or in sbatch script) to load HARP Module and set conda path
```bash
module use $HOME/osc_apps/lmodfiles
module load harp 
export CONDA_HOME=/users/PAS0536/swathivm/miniconda3
```
2. Run the following commands (either in command line more or in sbatch script) to execute the framwork from the target application folder
```bash
  cd <path to 01-eulers_number folder>
  chmod 755 *
  harp pipeline_config.json
```
3. The framework performs the following operations
a. Generates training data with three different configurations (scaled-down, full-scale and test-data), copies it to the pipeline/applications/<application-name>/train folder for furher processing
b. It pre-porcesses the data and transforms the training data using princple component analysis, upsamples full-scale executions to match scaled-down training samples and trains and stores the regression models with different configurations
c. The regression model with better predictions (lower no. of under-predictions and lwer MAPE of over-estimations) suitable for euler training data is slected, and is used to predict the walltime estimations for thr test-data configurations.
The results of the frameowrk are stores in predictions.csv in the target application folder.

