"""Six-stroke event schedule (concept assumption).

One working cycle spans 1080 deg crank angle (three crank revolutions), six
strokes of 180 deg each. Two of them are power strokes (3rd and 5th), each
preceded by its own hydrogen injection and spark event.

NOTE: This allocation is a concept-level assumption used to structure the
control logic. It is not a validated valve-timing or injection map.
"""
from dataclasses import dataclass
from typing import List

CYCLE_DEG = 1080.0
STROKE_DEG = 180.0


@dataclass(frozen=True)
class Stroke:
    index: int            # 1..6
    name: str
    start_deg: float      # crank angle from start of intake, deg
    end_deg: float
    ecu_event: str        # what the ECU is responsible for in this stroke


def build_schedule() -> List[Stroke]:
    spec = [
        ("Intake", "intake valve control; air metering"),
        ("Compression", "H2 injection window (end-of-injection from map); spark arming"),
        ("Power #1 (3rd stroke)", "spark at MBT-referenced advance; combustion monitoring"),
        ("Re-compression", "second H2 injection window; spark arming"),
        ("Power #2 (5th stroke)", "spark at 5th-stroke advance; combustion monitoring"),
        ("Exhaust", "exhaust valve control; residual / EGR management"),
    ]
    return [
        Stroke(i + 1, name, i * STROKE_DEG, (i + 1) * STROKE_DEG, ev)
        for i, (name, ev) in enumerate(spec)
    ]


def stroke_at(crank_deg: float) -> Stroke:
    """Return the stroke active at a crank angle (deg from start of intake)."""
    a = crank_deg % CYCLE_DEG
    return build_schedule()[int(a // STROKE_DEG)]


if __name__ == "__main__":
    for s in build_schedule():
        print(f"S{s.index} {s.start_deg:6.0f}-{s.end_deg:6.0f}  {s.name:<24} {s.ecu_event}")
