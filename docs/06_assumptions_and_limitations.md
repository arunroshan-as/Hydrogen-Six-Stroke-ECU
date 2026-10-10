# 06 — Assumptions and Limitations

## Assumptions
1. NXP S32G-VNP-RDB2 is the ECU platform (assumed; no hardware).
2. Boxer six-cylinder layout; gaseous hydrogen storage.
3. Stroke allocation: intake, compression, power, re-compression, power, exhaust.
4. Results are fully simulated; no engine data were used.
5. The efficiency gain (> 22 %) is relative to a conventional hydrogen engine baseline.

## Limitations
- **No experimental validation.** All curves are model outputs.
- **Combustion model.** Predictive entrainment models can be less accurate for hydrogen and ultra-lean operation because they do not explicitly capture intrinsic flame instabilities.
- **Hydrogen-specific risks** (pre-ignition, backfire, NOx, high peak pressure) are only partly represented. A peak-pressure limit is treated as the main constraint.
- **Multi-cylinder phasing.** With two power events per cylinder per 1080° cycle, an evenly spaced firing sequence for six cylinders is not automatic; the firing order is therefore marked TBD.
- **Cold start, transients, catalyst/aftertreatment** are not modelled.
- **Safety limits** are placeholders, not derived from component ratings.
- **Functional safety** (ISO 26262), cybersecurity and regulatory aspects are not addressed.

## Responsible use
Do not use any code or parameter in this repository to control a real engine, vehicle or hydrogen system.
