# Power Transmission

## Problem

How can electrical power be transmitted over a long distance while reducing power lost as heat in the wires?

## Mental model

Power source → step-up transformer → transmission line → step-down transformer → load.

## Quantities in the current model

- Voltage: V
- Current: A
- Resistance: Ω
- Electrical power: W
- Line loss in the simple resistive model: P_loss = I²R

## Current files

- `current.py`: an early calculation of current and resistive power loss.
- `high_voltage.py`: a simple step-up/step-down transformer model and transmission-loss calculation.

## Assumptions and limitations

These scripts are learning models, not engineering design tools. The transformer ratio and load/source power assumptions are simplified. Before trusting a result, state whether the specified power is source power or load power, and whether the voltage is measured at the source or load.

The simple formula P_loss = I²R describes resistive loss for the modeled current and resistance. It does not by itself describe every part of a real AC transmission system.
