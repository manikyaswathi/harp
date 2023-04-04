[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

HARP - HPC Application Resource Predictor
==============================================================

Overview
--------

Researchers use high-performance computing (HPC) cyberinfrastructures (CI) like Ohio Supercomputer (OSC) or Texas Advanced Computing Center (TACC) to execute computationally intensive diverse scientific workflows. Some workflows are heavy on IO, like genome sequencing (cleaning and assembly), while others, like training DNNs, could be compute (and memory) intensive. Each workflow has a unique resource requirement, and it is essential to profile and understand these needs to allocate shared resources for optimal utilization of the cyberinfrastructure. These resources are expensive, and several jobs compete to get these allocations, sometimes with reasonable wait times (while requesting enormous resources for a long time). Estimating the expected resources for optimally utilizing the compute and memory is challenging especially considering the need for sufficient history to enable these predictions tailored for unique workflows and execution environments. We explored and established a framework (as shown in Figure 1) that pipelines the solutions to address these challenges. The framework is configured to generate a history of executions and train suitable regression models to estimate the approximate execution time for a targeted application.


<!-- 
![alt text](https://github.com/manikyaswathi/harp/tree/main/Documents/HARP_Pipeline.png?raw=true)

![alt text](https://github.com/manikyaswathi/harp/tree/main/Documents/Folder_Structure.png?raw=true)

 -->
 
<!--  ![HARP Pipeline](Documents/HARP_Pipeline.png) -->
<img src="https://github.com/ICICLE-ai/harp/blob/main/Documents/HARP_Pipeline.png" alt="HARP Pipeline" width=75% height=75% class="center">
          Figure 1: The Proposed Framework: training data generation, building regression models & selecting the best model based on custom criteria
  
  
**Components and Characteristics of the framework (from figure 1)**:
**Generating and Preparing Training Data:** This module automatically and systematically generates comprehensive, diverse "scaled-down(SD)" and limited, selective "full-scale(FS)" runs with minimal human intervention. We use Cheetah (https://github.com/CODARcode/cheetah) to execute the target application with the pre-defined data generation configurations (SD and FS) to generate the history-of-runs training data.

**Building Regression Models:** This module standardizes and prepares the data, trains the selected off-the-shelf regression models with the appropriate hyper-parameters, and stores them for inference. In this phase, the data generated in the first phase is processed to train regression models. Redundant features are eliminated, outliers are removed, and features are transformed to reduce the dimensionality before training the regression models. 

**Selecting Appropriate Prediction Model:** this module selects the most appropriate regression model from a pool of trained models from phase 2 with respect to a given policy and target application
  
  
<!--  ![Application Folder Structure and Files](Documents/Folder_Structure.png) -->
 
<img src="https://github.com/ICICLE-ai/harp/blob/main/Documents/Folder_Structure.png" alt="Application Folder Structure and Files" width=75% height=75% class="center">
              Figure 2: Shows the target-application execution endpoint and the harp application folder structure. 

 
 
 
Installation
------------
* Dependency: Linux, Python 3.9+, git, pip, mpich, psutil, jq(command line JSOM parser https://stedolan.github.io/jq/)
* On supercomputers (OSC), it should be installed at a location accessible from the parallel file system
* **Follow these steps to set up Harp as a loadable software module on Ohio Supercomputer (OSC):**
  ```bash
  git clone https://github.com/ICICLE-ai/harp.git
  cd harp
  chmod 755 install-osc-harp.sh
  ./install-osc-harp.sh
  ```
  If the installation fails, please re-run the script 'install-osc-harp.sh' after deleting the environment 'harp-env' and running the cleanup.sh in the install directory. 
  ```bash
  conda remove --name harp-env --all
  ./cleanup.sh
  ```
This setup installs miniconda, CODAR Cheetah (https://github.com/CODARcode/cheetah), TensorFlow, psutil, pandas, and scikit-learn and configures the Harp framework. Follow the installation prompts to proceed with the setup. This installation takes about 30-40 mins to finish the setup on Owens login-node.
* **Follow these steps to setup the HARP framework on a standalone Linux system:**
  ```bash
  pip install psutil
  pip install tensorflow
  pip install pandas
  pip install scikit-learn
  ```
  Download the source code into the <install-dir>
  ```bash
  git clone https://github.com/ICICLE-ai/harp.git
  ```
    Ensure the scripts have '**execute**' privileges
  ```bash
  cd <install-dir>/harp/pipeline/bin/local
  chmod 755 harp
  cd <install-dir>/cheetah/bin
  chmod 755 *
  ```
  Set the HARP pipeline and Cheetah binaries in the PATH and set the install-dir in HARP_HOME
  ```bash
  export PATH=<install-dir>/harp/pipeline/bin/local:<install-dir>/cheetah/bin:$PATH
  export HARP_HOME=<install-dir>
  ```
* Harp has been tested on Ownes and Pitzer (OSC) and a standalone Linux system.

### Loading the HARP module 
   ```bash
  module use $HOME/osc_apps/lmodfiles
  module load harp 
  export CONDA_HOME=<path_to_miniconda>/miniconda3
   ```
   
### Using HARP to profile an application and predict the execution time
1. Navigate to the target application folder and copy the all the files from /Post_Execution_Scripts/basic into the the current folder. For more details about the type of application categories and profiling, please read the document or PPT <ADD LINK>. 
2. Edit path in post-script.sh to point to the target application directory
3. Execute the framework as per the configurations in file 'train_config.json' as follows:
 ```bash
  cd <path_to_application>
  chmod 755 *
  harp <pipeline-configration>.json
  ```
4. The results of the framework are stored in the predictions.json file under the target application folder.
Please find the sample application under the example folder and follow the read-me file to execute the framework against profiling and estimating the resource needs

NOTE
-------------
Things to consider while using the framework
 1.[OSC Installation] The installer creates a conda environment, "harp_env" on OSC and uses this environment to execute the framework. The environment name is used in a couple of Cheetash configurations and hence is mandated to use the same name, "harp_env," while installing the application. Please delete the environment if it already exists with this name before installing the framework.
 2. The below response:
  (OSC Install Script) Generating Module File Step: /users/PAS0536/swathivm/osc_apps/lmodfiles/harp/1.0.lua
  (OSC Install Script) Generating Module File Step Finished
  Finished at Thu Mar 16 11:44:13 EDT 2023
  Execution time: 1965 seconds

Releases
--------
The current release is [1.0.0](https://github.com/ICICLE-ai/harp).

### Supported Systems
System Name | Cheetah Support | CPU | GPU 
:-----------| :---------------| :---------------| :---------------
Local Linux machines | :white_check_mark: | :white_check_mark: 
Owens (OSC) | :white_check_mark: | :white_check_mark: | :white_check_mark: 
Pitzer (OSC) | :white_check_mark: | :white_check_mark: | :white_check_mark: 

Citing Harp
--------------
Vallabhajosyula, Manikya Swathi, and Rajiv Ramnath. "Towards Practical, Generalizable Machine-Learning Training Pipelines to build Regression Models for Predicting Application Resource Needs on HPC Systems." Practice and Experience in Advanced Research Computing. 2022. 1-5.

 Vallabhajosyula, Swathi, and Rajiv Ramnath. "Establishing a Generalizable Framework for Generating Cost-Aware Training Data and Building Unique Context-Aware Walltime Prediction Regression Models." 20th IEEE International Symposium on Parallel and Distributed Processing with Applications (ISPA 2022). December 2022

Reporting Bugs
--------------
Please open an issue on the [github issues](https://github.com/manikyaswathi/harp/issues) page to report a bug.

License
-------
The HARP is licensed under the https://opensource.org/licenses/BSD-3-Clause

 
 # Acknowledgements

*This work has been funded by grants from the National Science Foundation, including the ICICLE AI Institute (OAC 2112606) and EAGER (OAC 1945347)*
