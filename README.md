HARP Description

Researchers use high-performance computing (HPC) cyberinfrastructures (CI) like the Ohio Supercomputer (OSC) or Texas Advanced Computing Center (TACC) to execute computationally intensive diverse scientific workflows. Some workflows are heavy on IO, like genome sequencing (cleaning and assembly), while others, like training DNNs, could be compute (and memory) intensive. Each workflow has a unique resource requirement, and it is essential to profile and understand these needs to allocate shared resources for optimal utilization of the cyberinfrastructure. These resources are expensive, and several jobs compete to get these allocations, sometimes with reasonable wait times (while requesting enormous resources for a long time). Estimating the expected resources for optimally utilizing the compute and memory is challenging, especially considering the need for sufficient history to enable these predictions tailored for unique workflows and execution environments. We explored and established a framework (as shown in Figure 1) that pipelines the solutions to address these challenges. The framework is configured to generate a history of executions and train suitable regression models to estimate the approximate execution time for a targeted application.

How to Build HARP Pipeline Image
Please run the following commands to build the HARP Framework Image and store it in Dockerhub.

docker build -f Dockerfile_HARP_framework -t harp-framework:0.0.1 .
docker push <docker-namesapce>/harp-framework:0.0.1

Note: 
1. You should have a DockerHub Account and store the Image with public access. 
2. Docker Demaon and a client (or a Docker Desktop that bundles both the daemon and client) 


How to execute the HARP framework to profile an application:
HARP could be executed with or without the TAPIS framework. 
Executing HARP without TAPIS:
1. The HARP framework could be executed locally to profile an application and estimate resource requirements for different configurations. 


Use Case 1:
Executing HARP Framework locally with all components for profiling an application.
1. Build HARP Pipeline using commands in 'How to Build HARP Pipeline Image' or use the existing from 'ghcr.io/icicle-ai/harp-framework:0.0.1'.
2. Build an Image for the target application to profile by following the below instructions
a. Create a docker file for the target application from the Parent HARP Image of step 1.
FROM ghcr.io/icicle-ai/harp-framework:0.0.1
b. Copy the folder of the application to be profiled into the app folder. 
ADD examples /app/examples
c. Copy the "ProfileApplication.sh" of the profiler into the Image and set that as the entry point:
COPY ProfileApplication.sh /app/ProfileApplication.sh
ENTRYPOINT ["sh," "/app/ProfileApplication.sh"]

The "ProfileApplication.sh" files configure the HARP pipeline with writable folders to generate emulations and create and store models. 
 