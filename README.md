# Interactive mathematics for data science

## Description
The goal is to present mathematical fields related to data science in an interactive way using jupyter notebooks. 

## Learning principles
- **Intuition:** Build a feeling behind every concept and formula. Intuition compresses and abstracts the information behind processes and allows one to be faster and more efficient. 
- **Visualization:** Humans are visual beings. Thus visualizing as much as possible helps build intuition fast.
- **Interactivity:** One step beyond visualization is interactivity. Visualization helps getting a static feeling for entities, while interaction allows learing how objects behave during change.
- **Purpose:** Understand why different entities were introduced and what problems they solve. Having a purpose gives value to mathematical concepts and makes them interesting.

## Setup - for Linux or MacOS
- Locally
    - Install jupyter notebook. A simple way to do that is by installing [anaconda](https://www.anaconda.com/download/#linux).
    - Run jupyter on the directory of the project.
    
- In a docker container:
    - Build a docker image running `./build_docker_image.sh`.
    - Launch a container with the image running `./run_docker_container.sh`.

## Contents
1. Liner Algebra
    1. [Vectors](linear_algebra/part_1__vectors.ipynb)
    1. [Linear transformations and matrices](linear_algebra/part_2__linear_transformations_and_matrices.ipynb)
    1. [Popular operations on transformations](linear_algebra/part_3__popular_operations_on_transformations.ipynb)
    1. [Decompositions of transformations](linear_algebra/part_4_decompositions_of_trasformations.ipynb)
1. Tensor Algebra (TBA)

## License
[MIT License](https://github.com/koulakis/interactive-math-for-data-science/blob/master/LICENSE)
