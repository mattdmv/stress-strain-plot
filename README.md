# Project: Stress-strain-plot
This is a simple python script that takes engineering stress-strain curve points from the .csv file of the selected material and calculates true stress-strain curve points with an option of plotting graph. 

**Packages used**: pandas, matplotlib, tkinter, math

## Stress-strain curve
In engineering and materials science, a stress–strain curve for a material gives the relationship between stress and strain. It is obtained by gradually applying load to a test coupon and measuring the deformation, from which the stress and strain can be determined.

## *+ Engineering stress-strain curve*
Consider a bar of original cross sectional area A0 being subjected to equal and opposite forces F pulling at the ends so the bar is under tension. The material is experiencing a stress defined to be the ratio of the force to the cross sectional area of the bar, as well as an axial elongation.

## *+ True stress-strain curve*
Due to the shrinking of section area and the ignored effect of developed elongation to further elongation, true stress and strain are different from engineering stress and strain.

## *+ Difference (shown on graph)*
Next graph shows difference between engineering stress-strain curve and true stress-strain curve
![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Stress_strain_ductile.svg/473px-Stress_strain_ductile.svg.png)

## How to use script
Many FEA (Finite Element Analysis) softwares require that material properties are input as .csv points of true stress-strain curve of selected material. However, material properties can in most cases be found as engineering stress-strain curve.
This script uses relation between those two curves and transforms engineering stress-strain datapoints into true stress-strain datapoints. Final output is graph and .csv file which can be directly input in FEA software prior to study. 
