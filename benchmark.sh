#!/bin/bash
GPU_NAME=${1:-"2080Ti"}
GPU_INDEX=${2:-0}

export CUDA_VISIBLE_DEVICES=$GPU_INDEX

PLATFORMS=(
    CUDA
    OpenCL
)

PRECISIONS=(
    single
    mixed
    double
)

TESTS=(
    gbsa
    rf
    pme
    apoa1rf
    apoa1pme
    apoa1ljpme
    amoebagk
    amoebapme
)

DIR_OUTPUT="output/${GPU_NAME}"

mkdir -p $DIR_OUTPUT

for precision in "${PRECISIONS[@]}"; do
    for platform in "${PLATFORMS[@]}"; do
        for test in "${TESTS[@]}"; do
            output_file="${DIR_OUTPUT}/${precision}_${platform}_${test}.txt"
            unbuffer python benchmark.py --platform=$platform --test=$test --precision=$precision |& tee $output_file
        done        
    done
done
