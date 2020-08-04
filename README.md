# vispy
Vispy is the Python version of MATLAB vis created by Michał Ziemczonok. It allows a quick preview of a 3D volume, by showing a cross-section of the volume, across given axis at a given height. The height can be changed by dragging the clicked cursor up-down. Right mouse click toggles the cross-section to another axis.

## Prerequisites
- conda

## Installation
To install simply run the setup.sh script. It will create new conda environment called "vispy" and install the dependencies for the project.

## Usage
```
from vispy import vis

# Assuming the volume "vol" already exists
vis(vol)
```

## Author
- Piotr Stępień – _initial work_