[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

# HARP - HPC Application Runtime Predictor

## Overview

Researchers use high-performance computing (HPC) cyberinfrastructures (CI) like Ohio Supercomputer (OSC) or Texas Advanced Computing Center (TACC) to execute computationally intensive diverse scientific workflows. Some workflows are heavy on IO, like genome sequencing (cleaning and assembly), while others, like training DNNs, could be compute (and memory) intensive. Each workflow has a unique resource requirement, and it is essential to profile and understand these needs to allocate shared resources for optimal utilization of the cyberinfrastructure. These resources are expensive, and several jobs compete to get these allocations, sometimes with reasonable wait times (while requesting enormous resources for a long time). Estimating the expected resources for optimally utilizing the compute and memory is challenging especially considering the need for sufficient history to enable these predictions tailored for unique workflows and execution environments. We explored and established a framework (as shown in Figure 1) that pipelines the solutions to address these challenges. The framework is configured to generate a history of executions and train suitable regression models to estimate the approximate execution time for a targeted application.


<!-- 
![alt text](https://github.com/manikyaswathi/harp/tree/main/Documents/HARP_Pipeline.png?raw=true)

![alt text](https://github.com/manikyaswathi/harp/tree/main/Documents/Folder_Structure.png?raw=true)

 -->
 
<!--  ![HARP Pipeline](Documents/HARP_Pipeline.png) -->
<img src="https://github.com/ICICLE-ai/harp/blob/main/Documents/HARP_Pipeline.png" alt="HARP Pipeline" width=75% height=75% class="center">
          Figure 1: The Proposed Framework: training data generation, building regression models & selecting the best model based on custom criteria
  
  
### Components and Characteristics of the Framework (from Figure 1):
1. **Generating and Preparing Training Data:** This module automatically and systematically generates comprehensive, diverse "scaled-down(SD)" and limited, selective "full-scale(FS)" runs with minimal human intervention. We use Cheetah (https://github.com/CODARcode/cheetah) to execute the target application with the pre-defined data generation configurations (SD and FS) to generate the history-of-runs training data.
2. **Building Regression Models:** This module standardizes and prepares the data, trains the selected off-the-shelf regression models with the appropriate hyper-parameters, and stores them for inference. In this phase, the data generated in the first phase is processed to train regression models. Redundant features are eliminated, outliers are removed, and features are transformed to reduce the dimensionality before training the regression models. 
3. **Selecting Appropriate Prediction Model:** This module selects the most appropriate regression model from a pool of trained models from phase 2 with respect to a given policy and target application
Note: the framework id built on TensorFlow Framework.
  
<!--  ![Application Folder Structure and Files](Documents/Folder_Structure.png) -->
 
<img src="https://github.com/ICICLE-ai/harp/blob/main/Documents/Folder_Structure.png" alt="Application Folder Structure and Files" width=75% height=75% class="center">
              Figure 2: Shows the target-application execution endpoint and the harp application folder structure. 

 
## Installation
* Dependency: Linux, Python 3.9+, git, pip, mpich, psutil, jq(command line JSOM parser https://stedolan.github.io/jq/)
* On supercomputers (OSC), it should be installed at a location accessible from the parallel file system
### **Follow these steps to set up Harp as a loadable software module on Ohio Supercomputer (OSC):**
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
#### Loading the HARP module on OSC
   ```bash
  module use $HOME/osc_apps/lmodfiles
  module load harp 
  export CONDA_HOME=<path_to_miniconda>/miniconda3
  source $CONDA_HOME/bin/activate
  source activate harp_env
   ```
**NOTE**

Things to consider while installing the framework on OSC
1. [OSC Installation] The installer creates a conda environment, "harp_env" on OSC and uses this environment to execute the framework. The environment name is used in a couple of Cheetash configurations and hence is mandated to use the same name, "harp_env," while installing the application. Please delete the environment if it already exists with this name before installing the framework.
2. Upon successful installation, the install script will return the below response:
 (OSC Install Script) Generating Module File Step: /users/PAS0536/swathivm/osc_apps/lmodfiles/harp/1.0.lua
 (OSC Install Script) Generating Module File Step Finished
 Finished at Thu Mar 16 11:44:13 EDT 2023
 Execution time: 1965 seconds

### **Follow these steps to setup the HARP framework on a standalone Linux system:**
* Use these commands to install the dependencies using pip
  ```bash
  pip install psutil
  pip install tensorflow
  pip install pandas
  pip install scikit-learn
  ```
* Download the source code into the <install-dir> and set it to HARP_HOME
  ```bash
  git clone https://github.com/ICICLE-ai/harp.git
  export HARP_HOME=<path-to-download-folder>/harp
  ```
* Install Cheetah
  ```bash
  cd $HARP_HOME/cheetah
  pip install --editable .
  ```
* Ensure the scripts have '**execute**' privileges
  ```bash
  cd $HARP_HOME/pipeline/bin/local
  chmod 755 harp
  cd $HARP_HOME/cheetah/bin
  chmod 755 *
  ```
* Set the HARP pipeline and Cheetah binaries in the PATH
  ```bash
  export PATH=$HARP_HOME/pipeline/bin/local:$HARP_HOME/cheetah/bin:$PATH
  ```
 The HARP pipeline is ready to used once the HARP_HOME and binaries are set in PATH. 
 
**NOTE**

Things to consider while installing the dependencies on stand-alone linux systems:
1. if you do not have root or admin proviledge on the system, please consult your package manager on how to install mpich and opetr dependencies. 

 
Harp has been tested on Ownes and Pitzer (OSC) and a standalone Linux system.

   
## Using HARP to profile an application and predict the execution time
1. Navigate to the target application folder and copy the all the files from /Post_Execution_Scripts/basic into the the current folder. For more details about the type of application categories and profiling, please read the document or PPT <ADD LINK>. 
2. Edit path in post-script.sh to point to the target application directory
3. Execute the framework as per the configurations in file 'train_config.json' as follows:
 ```bash
  cd <path_to_application>
  chmod 755 *
  harp <pipeline-configration>.json
  ```
4. The results of the framework are stored in the predictions.json file under the target application folder.
Please find the sample application under the example folder and follow the read-me file to execute the framework against profiling and estimating the resource needs.



Releases
--------
The current release is [1.0.0](https://github.com/ICICLE-ai/harp).

### Supported Systems
System Name | Cheetah Support | CPU | GPU 
:-----------| :---------------| :---------------| :---------------
Local Linux machines | :white_check_mark: | :white_check_mark: 
Owens (OSC) | :white_check_mark: | :white_check_mark: | :white_check_mark: 
Pitzer (OSC) | :white_check_mark: | :white_check_mark: | :white_check_mark: 

Citing HARP
--------------
Please cite the following paper if using HARP:
 S. Vallabhajosyula and R. Ramnath, "Establishing a Generalizable Framework for Generating Cost-Aware Training Data and Building Unique Context-Aware Walltime Prediction Regression Models," 2022 IEEE Intl Conf on Parallel & Distributed Processing with Applications, Big Data & Cloud Computing, Sustainable Computing & Communications, Social Computing & Networking (ISPA/BDCloud/SocialCom/SustainCom), Melbourne, Australia, 2022, pp. 497-506, doi: 10.1109/ISPA-BDCloud-SocialCom-SustainCom57177.2022.00070.

Other papers:
 Vallabhajosyula, Manikya Swathi, and Rajiv Ramnath. "Towards Practical, Generalizable Machine-Learning Training Pipelines to build Regression Models for Predicting Application Resource Needs on HPC Systems." Practice and Experience in Advanced Research Computing. 2022. 1-5.


Reporting Bugs and Contribution
--------------------------------
Please open an issue on the [github issues](https://github.com/manikyaswathi/harp/issues) page to report a bug.

HARP is an open-source repository, and we invite the community to collaborate and include their workflows into the framework to profile their applications. Create a pull request to add your changes to the dev branch.


License
-------
The HARP is licensed under the https://opensource.org/licenses/BSD-3-Clause

 
 # Acknowledgements

*This work has been funded by grants from the National Science Foundation, including the ICICLE AI Institute (OAC 2112606) and EAGER (OAC 1945347)*
