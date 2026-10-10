"""Concept-stage reference models for a hydrogen six-stroke ECU (simulation only)."""
from .cycle_schedule import Stroke, build_schedule, stroke_at
from .state_machine import ECUState, SensorSnapshot, SafetyLimits, ECUStateMachine

__all__ = ["Stroke", "build_schedule", "stroke_at", "ECUState",
           "SensorSnapshot", "SafetyLimits", "ECUStateMachine"]
__version__ = "0.1.0"
