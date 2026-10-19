# Water Pumping

## Problem

How much power is needed to move water at a chosen flow rate to a higher elevation?

## Mental model

Flow rate → mass flow rate → total head → pressure rise → hydraulic power → input power after pump efficiency.

## Current model

`simulation.py` uses:
- Volume flow rate, Q: m³/s
- Mass flow rate, ṁ = ρQ: kg/s
- Total head: elevation difference plus assumed friction head, m
- Pressure difference: Δp = ρgH: Pa
- Hydraulic power: P = ṁgH = QΔp: W
- Input power: P_input = P_hydraulic / efficiency

## Assumptions and limitations

The current model treats the liquid as water with constant density, uses a simplified head-loss value, and represents pump efficiency as a single number. It is intended for learning and should not be used to select or operate real equipment without checking the actual system data.
