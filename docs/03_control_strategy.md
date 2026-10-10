# 03 — Control Strategy

## 1. Injection
End-of-injection (EOI) is scheduled from a map indexed by **engine speed** and **intake pressure**. In simulation, EOI moves progressively later (less negative °BTDC) with increasing speed across 1000, 3000 and 5000 rpm, and varies non-monotonically with intake pressure at each speed (see Fig. 2 in [05](05_results_summary.md)).

## 2. Spark timing
- Spark advance is referenced to **MBT** (maximum brake torque) and trimmed to **MBT − 1 %** where appropriate, a common practice to trade a small torque loss for lower knock/peak-pressure risk.
- The **3rd** and **5th** power strokes carry **separate** advance values, because the charge state differs between the two events. In simulation the 5th-stroke MBT advance sits below the 3rd-stroke value across the swept parameter range (Fig. 4).
- Spark advance across the speed range in the performance map runs from roughly 6° at 1000 rpm to the low 20s of degrees at 5000 rpm (Fig. 1).

## 3. Combustion monitoring
Metrics per power stroke: peak cylinder pressure, peak-pressure position (PPP), IMEP, and COV of IMEP. Simulated trends: 5th-stroke IMEP peaks near −20° spark timing (Fig. 6; the 5th-stroke COV trend is flagged for review in [05](05_results_summary.md)), while normalised peak pressure falls and PPP changes as spark is retarded (Fig. 5).

## 4. Protection
| Function | Concept action |
|---|---|
| Peak-pressure limit | Retard spark / reduce load; FAULT if exceeded |
| Hydrogen leak | Immediate FAULT, inhibit injection and spark |
| Over-temperature | FAULT |
| Boost / intake pressure limit | Limit and FAULT |
| Loss of crank sync | Return to CRANK_SYNC; no injection until TDC re-established |

All limit values are **placeholders**.

## 5. Load-adaptive fuelling (concept)
Slope/terrain-aware fuel correction is envisaged as a higher-level feature that adjusts fuel delivery from vehicle-load estimates. It is described only at concept level and is not modelled here.
