"""ECU supervisory state machine (concept, simulation only).

Mirrors the control-flow sequence of the concept:
INIT -> SAFETY_CHECK -> CRANK_SYNC -> RUN -> STOP, with FAULT as a latched
safe state. Limits are PLACEHOLDERS and must come from engine-specific
validation before any real use. Not safety-certified. Not for use on hardware.
"""
from dataclasses import dataclass
from enum import Enum, auto


class ECUState(Enum):
    INIT = auto()
    SAFETY_CHECK = auto()
    CRANK_SYNC = auto()
    RUN = auto()
    FAULT = auto()
    STOP = auto()


@dataclass
class SensorSnapshot:
    crank_synced: bool = False
    tdc_detected: bool = False
    coolant_temp_c: float = 25.0
    intake_pressure_bar: float = 1.0
    peak_pressure_bar: float = 0.0
    h2_leak_detected: bool = False
    stop_requested: bool = False


@dataclass
class SafetyLimits:
    max_coolant_temp_c: float = 110.0        # placeholder
    max_intake_pressure_bar: float = 2.0     # placeholder
    max_peak_pressure_bar: float = 95.0      # placeholder (peak-pressure limit)


class ECUStateMachine:
    def __init__(self, limits: SafetyLimits | None = None):
        self.limits = limits or SafetyLimits()
        self.state = ECUState.INIT
        self.fault_reason: str | None = None

    def _violation(self, s: SensorSnapshot) -> str | None:
        l = self.limits
        if s.h2_leak_detected:
            return "hydrogen leak detected"
        if s.coolant_temp_c > l.max_coolant_temp_c:
            return "coolant over-temperature"
        if s.intake_pressure_bar > l.max_intake_pressure_bar:
            return "intake pressure above limit"
        if s.peak_pressure_bar > l.max_peak_pressure_bar:
            return "peak cylinder pressure above limit"
        return None

    def step(self, s: SensorSnapshot) -> ECUState:
        if self.state in (ECUState.FAULT, ECUState.STOP):
            return self.state  # latched

        reason = self._violation(s)
        if reason and self.state != ECUState.INIT:
            self.fault_reason, self.state = reason, ECUState.FAULT
            return self.state

        if self.state == ECUState.INIT:
            self.state = ECUState.SAFETY_CHECK
        elif self.state == ECUState.SAFETY_CHECK:
            self.state = ECUState.CRANK_SYNC
        elif self.state == ECUState.CRANK_SYNC:
            if s.crank_synced and s.tdc_detected:
                self.state = ECUState.RUN
        elif self.state == ECUState.RUN:
            if s.stop_requested:
                self.state = ECUState.STOP
        return self.state

    def reset(self) -> None:
        """Explicit operator reset out of FAULT/STOP."""
        self.state, self.fault_reason = ECUState.INIT, None
