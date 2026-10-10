# 04 — Simulation Methodology

## Approach
A fully simulated concept study using 0D/1D engine modelling. In-cylinder combustion is represented with a predictive, turbulent-flame-entrainment sub-model whose calibration is anchored to optimal (MBT) spark timing, i.e. a spark-timing-referenced calibration idea (a single calibration multiplier is swept until predicted MBT matches the target).

## Workflow
1. Build a 0D/1D model of the six-stroke boxer-six engine on hydrogen.
2. Sweep spark timing and the calibration multiplier (TLS) for the 3rd and 5th power strokes.
3. Select settings consistent with MBT / MBT−1 % and with typical combustion-phasing indicators (peak-pressure position, CA50).
4. Generate speed/load maps (injection, spark) for 1000–5000 rpm.
5. Compare against a conventional hydrogen engine baseline to estimate the efficiency change.

## Key sweeps in this repository
| Figure | Sweep |
|---|---|
| Fig. 1 | IMEP vs. speed with spark advance annotated |
| Fig. 2 | End of injection vs. intake pressure at 1000/3000/5000 rpm |
| Fig. 3 | In-cylinder pressure vs. crank angle, both power strokes |
| Fig. 4 | MBT spark advance vs. TLS multiplier, 3rd vs. 5th stroke |
| Fig. 5 | Normalised peak pressure and PPP vs. spark timing |
| Fig. 6 | IMEP and COV vs. spark timing at 2000 rpm |

## Reproducibility
The model files and raw simulation outputs are not part of this concept repository. Figures are provided as images. Releasing model inputs and data is listed in the [roadmap](07_roadmap.md).
