# Simulation Lab

A personal learning lab for turning real-world questions into mental models, mathematical models, and Python simulations.

The project is organized around **problems and systems**, not school subjects. Mathematics, physics, chemistry, and biology are tools used wherever a problem needs them.

## Learning loop

1. **Choose a question** about something in the real world.
2. **Draw the mental model**: identify components, quantities, and relationships.
3. **State assumptions and units** before writing equations.
4. **Turn the model into Python instructions**.
5. **Run experiments** by changing inputs and observing outputs.
6. **Check the result** against physical intuition, units, and reliable references.
7. **Record what the model cannot explain yet**.

Paper is mainly for diagrams and relationships. Python handles repeated calculations. The model still needs human checking.

## Repository map

```text
sim_mpcb/
├── systems/
│   ├── power_transmission/   # Voltage, current, line resistance, power loss
│   └── water_pumping/        # Flow rate, head, pressure, and pump power
├── experiments/
│   ├── math/                 # Small mathematical models and calculations
│   └── neural_network/       # Small learning-model experiments
├── draw/                     # Existing drawings and visual notes
└── README.md
```

## Where should a new file go?

- Put it in `systems/<problem_name>/` when it models a real-world system or question.
- Put it in `experiments/<topic>/` when it is a small isolated exercise that is not yet part of a larger system.
- Add a shared utility only after at least two simulations genuinely need the same code. Avoid building infrastructure before it is useful.

## Current systems

| Problem | What it explores | Entry point |
|---|---|---|
| Power transmission | Current, voltage transformation, resistance, and power loss | `systems/power_transmission/` |
| Water pumping | Flow rate, mass flow rate, height, pressure, hydraulic power, and efficiency | `systems/water_pumping/simulation.py` |

## Current experiments

| Experiment | What it explores | Entry point |
|---|---|---|
| Math models | Functions, changing quantities, and integration | `experiments/math/` |
| Neural network | A tiny input-weight-bias learning loop | `experiments/neural_network/learning_loop.py` |

## Important modeling rule

A program can calculate correctly while representing the real world incorrectly. For every simulation, record what each variable means, its unit, the assumptions being made, and what is intentionally left out.
