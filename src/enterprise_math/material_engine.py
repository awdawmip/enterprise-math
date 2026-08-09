"""End-to-end geometry-to-material history pipeline for stacked E001.

This module closes the *observational* half of the material engine:

    represented body-pair geometry
      -> common-collapse separation depth
      -> discrete deformation schedule
      -> explicit loading/return operator programs
      -> branch-aware material history
      -> realized cycle diagnostics.

It deliberately stops before changing body velocity/position.  A future
material-to-kinematics coupling law must be declared separately and may not infer
force, energy, mass, or impulse from the integer response sample by name alone.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_contact_history import (
    BodyPairState2D,
    ContactMaterialHistory2D,
    trace_contact_material_history,
)
from .material_cycle import MaterialCycleDiagnostics, material_cycle_diagnostics
from .material_program import MaterialProgramProfile


@dataclass(frozen=True)
class MaterialEngineObservation2D:
    """Compiled material program plus one observed finite contact history."""

    program: MaterialProgramProfile
    contact_history: ContactMaterialHistory2D
    cycle: MaterialCycleDiagnostics


def observe_material_engine_history(
    pair_states: tuple[BodyPairState2D, ...] | list[BodyPairState2D],
    program: MaterialProgramProfile,
) -> MaterialEngineObservation2D:
    """Evaluate one represented geometry history through a material program."""
    curve = program.as_curve_profile()
    contact_history = trace_contact_material_history(pair_states, curve)
    cycle = material_cycle_diagnostics(contact_history.material_states)
    if cycle.peak_index != contact_history.peak_deformation:
        raise AssertionError("cycle and contact history disagree on peak deformation")
    return MaterialEngineObservation2D(
        program=program,
        contact_history=contact_history,
        cycle=cycle,
    )
