# 01 — Concept Overview

## Motivation
Hydrogen offers a route to near-zero-carbon operation of internal combustion engines (ICE) and aligns with national and global decarbonisation goals (India's National Green Hydrogen Mission; UN SDG 13). Retaining the ICE architecture preserves existing manufacturing and service infrastructure.

## Idea
A **six-stroke cycle** adds a second power event to each working cycle:

| Stroke | Name | Role |
|---|---|---|
| 1 | Intake | Fresh charge |
| 2 | Compression | First injection window; spark arming |
| 3 | Power #1 | First combustion event |
| 4 | Re-compression | Second injection window; spark arming |
| 5 | Power #2 | Second combustion event |
| 6 | Exhaust | Scavenging; residual / EGR management |

The stroke allocation is a concept assumption (see [06](06_assumptions_and_limitations.md)). The ECU's job is to coordinate crank/cam synchronisation, injection and spark for **both** power strokes, and to protect the engine from knock, over-pressure and hydrogen hazards.

## Engine layout
A horizontally opposed (boxer) six-cylinder configuration was chosen for the concept for its compact, low centre-of-gravity packaging and balanced reciprocating forces. The CAD view in `docs/assets/fig00_flat_six_cad.png` shows the intended arrangement with individual exhaust runners and a central supercharger/accessory drive region.

## Fuel and storage
Hydrogen, stored as a compressed gas on board. Storage pressure, tank sizing and refuelling are outside the scope of this ECU concept.

## Scope of this repository
In scope: ECU architecture, control strategy, simulation-based results, reference logic.
Out of scope: mechanical design detail, fuel-system hardware design, regulatory submission, bench or vehicle test.
