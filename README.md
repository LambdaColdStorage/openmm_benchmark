# OpenMM Benchmark

### Goal

This repo benchmarks the performance of serveral molecular simulation task on different GPUs. We use the benchmark [script](https://github.com/openmm/openmm/blob/master/examples/benchmark.py) of the [OpenMM](https://github.com/openmm/openmm) library and run simulation with single/mixed/double precisions for eight different tasks, with both CUDA and OpenCL backend. 

Results can be found in these CSV files: 
* [Single Precision](https://github.com/lambdal/openmm_benchmark/blob/master/single_openmm_benchmark.csv)
* [Double Precision](https://github.com/lambdal/openmm_benchmark/blob/master/double_openmm_benchmark.csv)
* [Mixed Precision](https://github.com/lambdal/openmm_benchmark/blob/master/mixed_openmm_benchmark.csv).


### Installation

__Prerequisites__ 

CUDA 10.0 (You can get it via installing [Lambda Stack](https://lambdalabs.com/lambda-stack-deep-learning-software))

Anaconda
```
cd && wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh && bash Anaconda3-2020.02-Linux-x86_64.sh

# Type yes to accept th license terms

# Press Enter to confirm the installation location /home/$USERNAME/anaconda3

# Type no when asked "Do you wish the installer to initialize Anaconda3 by running conda init?"

# Close the current terminal and open a new one
conda config --set auto_activate_base false && rm Anaconda3-2020.02-Linux-x86_64.sh
```

__Create Conda Virtual Environment__

In a new terminal:

```
conda create --name venv_openmm
conda activate venv_openmm
conda install -c omnia/label/cuda100 -c conda-forge openmm
conda install -c eumetsat expect
conda install pandas=1.0.3
```

### Run Benchmark

```
git clone https://github.com/lambdal/openmm_benchmark.git

cd openmm_benchmark

conda activate venv_openmm

./benchmark.sh <GPU_NAME> <GPU_INDEX>

# Example
./benchmark.sh QuadroRTX8000 0
```

### Compile Results

```
python compile_results.py
```

