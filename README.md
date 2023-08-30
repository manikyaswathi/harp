HARP Description

Researchers use high-performance computing (HPC) cyberinfrastructures (CI) like Ohio Supercomputer (OSC) or Texas Advanced Computing Center (TACC) to execute computationally intensive diverse scientific workflows. Some workflows are heavy on IO, like genome sequencing (cleaning and assembly), while others, like training DNNs, could be compute (and memory) intensive. Each workflow has a unique resource requirement, and it is essential to profile and understand these needs to allocate shared resources for optimal utilization of the cyberinfrastructure. These resources are expensive, and several jobs compete to get these allocations, sometimes with reasonable wait times (while requesting enormous resources for a long time). Estimating the expected resources for optimally utilizing the compute and memory is challenging especially considering the need for sufficient history to enable these predictions tailored for unique workflows and execution environments. We explored and established a framework (as shown in Figure 1) that pipelines the solutions to address these challenges. The framework is configured to generate a history of executions and train suitable regression models to estimate the approximate execution time for a targeted application.

How to Build HARP Pipeline Image
Run the following commands to build HARP Frameowk Image and store it in Dockerhub

docker build -f Dockerfile_HARP_framework -t harp-framework:0.0.1 .
docker push <docker-namesapce>/harp-framework:0.0.1

Note: 
1. you should have a DockerHub Account and store the Image with public access. 
2. Docker Demaon and a client (or a Docker Desktop that bundles both the deamon and client) 


How to execute HARP framework to profile an application:
HARP could be executed with or without TAPIS framework. TAPIS <Description>
Executinh HARP without TAPIS:
1. HARP fremwork could be executed locally to profile an application and estimate resourse reqiremnets for different configurations. 


Use Case 1:
Executing HARP Framework locally with all componenets for profiling an application.
1. Build HARP Piepline using commands in 'How to Build HARP Pipeline Image' or use the exisiting from ''.
2. Build an Image for 