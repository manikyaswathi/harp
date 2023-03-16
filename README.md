[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

HARP - full form
==============================================================

Overview
--------

<DESCRIPOTION>

Installation
------------
* Dependency: Linux, Python 3.9+, psutil
* On supercomputers it should be installed at a location accessible from the parallel file system
* Fowwlow the steps to set up Harp as a loadable software module:
  ```bash
  git clone https://github.com/ICICLE-ai/harp.git
  cd harp
  chmod 755 *
  ./install-osc-harp.sh
  ```
* Follow the installtion prompts to proceed with the setup. This setup installs CODAR Cheetah (https://github.com/CODARcode/cheetah), TensorFlow, psutil, pandas and scikit-learn and configures the Harp framework. It takes abiut 30-40 mins to finish the setup.
* Harp has been tested on Ownes (OSC), and standalone Linux computers

##### Loading the HARO module to execute
  [WILL UPDATE THIS]
   ```bash
   module use $HOME/osc_apps/lmodfiles
  module load harp 
  export CONDA_HOME=<path_to_miniconda>/miniconda3
  harp <Confilguration-file.json>
   ```
NOTE
-------------
Things to consider while using the framework
1. The installer creates a conda environmnet "harp_env" and uses this environmentto execute the framework. Please delete the evironment if it already exists with this name for this version of framework. It uses the name "harp_env" at couple of places hardcoded (while executing CODARCheetah) and hence is mandated to use the same environment name for this release. 

Documentation
-------------
<LINK TO VIDEO> 
<LINK TO PPT>

Releases
--------
The current release is [1.0](https://github.com/<RELEASE PATH>).

### Supported Systems
System Name | Cheetah Support 
:-----------| :---------------
Local Linux machines | :white_check_mark: 
Owens (OSC) | :white_check_mark: 

Authors
-------


Citing Harp
--------------
<Paper>

Reporting Bugs
--------------
Please open an issue on the [github issues](https://github.com/<PATH>/issues) page to report a bug.

License
-------
Harp is licensed under the https://opensource.org/licenses/BSD-3-Clause
