# Estimating walltime to execute "calc_e.py" with given configurations : Calculating Euler's number

**This code if from "https://github.com/CODARcode/cheetah"**

To demonstrate the usage of HARP with Cheetah, we will look at a simple Python3 script which calculates Euler's number (`e`) using two different methods. It takes three positional arguments: the first is a string describing which of the methods to use, the second is a parameter to the calculation method that describes how many iterations or how precise to try to make the calculation (meaning depends on the method), and the third is a precision to use with the stdandard library Decimal module in python. If the third argument is not specified, built in floating point is used instead.

## The application

The source code is contained in a single source file: [calc\_e.py](calc_e.py).
There are no dependencies other than python3.

# How to use HARP to estimate the walltime for the program calc_e.py?
The current folder '01-eulers_number' is called target application folder. 

1. Navigate to the target application folder and copy the all the files from /Post_Execution_Scripts/basic into the the current folder. For more details about the type of application categories and profiling, please read the document or PPT .
2. Edit the paths in "post_script.sh" to point to this folder (the target application folder). 
3. Edit the follwoing files bedore profiling the application
   - Set the OSC project account in the campaign files "*_campaign_*.py". 
    ```
      class GrayScott(Campaign):
        ...
        scheduler_options = {'owens_gpu': {'project':'<OSC-project-account>'}}
        ...
    ```
   - Adjust the paths for the "cheetah_app_directory" and "cheetah_campaign_file" keys in "pipeline_config.json" file to pointto the current directory.
    
4. Run the following commands (either in command line more or in sbatch script) to load HARP Module and activate the environmnet (** Only for OSC **)
  ```bash
  module use $HOME/osc_apps/lmodfiles
  module load harp 
  export CONDA_HOME=<path-to-conda-install>/miniconda3
  source $CONDA_HOME/bin/activate
  source activate harp_env
```
5. Run the following commands (either in command line more or in sbatch script) to execute the framwork from the target application folder
```bash
  cd <path to 01-eulers_number folder>
  chmod 755 *
  harp pipeline_config.json
```
**Before executing the harp, make sure to modify the absolute-paths in 'pipeline_config.json' file to the target application folder i.e. this example folder.**

3. The framework performs the following operations
  a. Generates training data with three different configurations (scaled-down, full-scale and test-data), copies it to the pipeline/applications/<application-name>/train folder for furher processing
  b. It pre-porcesses the data and transforms the training data using princple component analysis, upsamples full-scale executions to match scaled-down training samples and trains and stores the regression models with different configurations
  c. The regression model with better predictions (lower no. of under-predictions and lwer MAPE of over-estimations) suitable for euler training data is slected, and is used to predict the walltime estimations for thr test-data configurations.
The results of the frameowrk are stores in predictions.csv in the target application folder.

