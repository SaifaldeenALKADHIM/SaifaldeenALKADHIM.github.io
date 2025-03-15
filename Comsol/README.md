# COMSOL Gas Discharge Tutorial

This tutorial provides a step-by-step guide for simulating gas discharge in COMSOL Multiphysics.

## Table of Contents
1. [Introduction](#introduction)
2. [Theory](#theory)
3. [COMSOL Setup](#comsol-setup)
4. [Simulation Results](#simulation-results)
5. [Conclusion](#conclusion)

## Introduction
Gas discharge is a phenomenon where an electric current flows through a gas, often resulting in light emission. This tutorial demonstrates how to simulate gas discharge using COMSOL Multiphysics.

## Theory
The physics of gas discharge involves solving the following equations:
- Poisson's equation
- Electron continuity equation
- Ion continuity equation

For more details, see the [theory document](https://github.com/SaifaldeenALKADHIM/SaifaldeenALKADHIM.github.io/blob/master/Comsol/theory/ElectricDischargeModuleUsersGuide.pdf).

## COMSOL Setup
1. Open COMSOL Multiphysics.
2. Create a new model and select **Plasma** from the physics list.
3. Define the geometry and materials.
4. Set up the boundary conditions and mesh.
5. Run the simulation.

For detailed instructions, see the [COMSOL model file](comsol_files/gas_discharge.mph).

## Simulation Results
The simulation results show the electric potential, electron density, and ion density distributions.

![Electric Potential](images/electric_potential.png)

For more results, see the [results folder](results/).

## Conclusion
This tutorial demonstrates how to simulate gas discharge in COMSOL Multiphysics. The results can be used to analyze plasma behavior in various applications.

---

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
