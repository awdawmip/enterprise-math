"""Deterministic checkpoint probe for the stacked E001 material-response line.

Run with:

    PYTHONPATH=src python experiments/e001_material_state_probe.py

The script prints finite integer diagnostics only.  It does not claim a physical
constitutive law, force, energy, or calibrated material model.
"""

from enterprise_math.engineering_collision import Body2D
from enterprise_math.material_adjoint import material_adjoint_repair
from enterprise_math.material_basis import (
    digital_circle_y_basis,
    recurrence_quarter_basis,
    rotation_quarter_basis,
)
from enterprise_math.material_contact import observe_contact_material
from enterprise_math.material_hysteresis import LOADING, trace_deformation_schedule
from enterprise_math.material_iteration import (
    iterate_hardening,
    iterate_softening,
    softening_positive_fixed_threshold,
)
from enterprise_math.material_oscillator import PythagoreanRotation
from enterprise_math.material_projection import trace_toward_zero_projection_loss
from enterprise_math.material_projection_schedule import compare_projection_schedules
from enterprise_math.material_response import material_curve_profile


def main() -> None:
    amplitude = 1000
    rotation = PythagoreanRotation(399, 40, 401)

    rotation_basis = rotation_quarter_basis(amplitude, rotation)
    recurrence_basis = recurrence_quarter_basis(amplitude, rotation)
    digital_basis = digital_circle_y_basis(amplitude)

    profile = material_curve_profile(
        rotation_basis.samples,
        amplitude=amplitude,
        loading_power=2,
        return_power=1,
        return_retention=700,
    )
    schedule = tuple(range(len(profile.loading))) + tuple(
        range(len(profile.loading) - 2, -1, -1)
    )
    history = trace_deformation_schedule(profile, schedule, LOADING)

    projection = trace_toward_zero_projection_loss(
        (amplitude, 0), rotation, 16
    )
    cadence_a = compare_projection_schedules(
        (-20, -16), PythagoreanRotation(3, 4, 5), 2
    )
    cadence_b = compare_projection_schedules(
        (-20, -14), PythagoreanRotation(3, 4, 5), 2
    )

    contact = observe_contact_material(
        Body2D(0, 0, 0, 2),
        Body2D(1, 2, 0, 2),
        profile,
        LOADING,
    )
    adjoint = material_adjoint_repair(33, 100, 2)
    hardening = iterate_hardening(33, 100, 2)
    softening = iterate_softening(50, 100, 2)

    print(f"rotation_basis={rotation_basis}")
    print(f"recurrence_basis={recurrence_basis}")
    print(f"digital_basis={digital_basis}")
    print(f"material_branch_gap={profile.branch_gap}")
    print(f"material_signed_area={profile.signed_area}")
    print(f"history_state_count={len(history)}")
    print(f"history_turn_state={history[len(profile.loading)]}")
    print(f"projection_norm_sq_loss_16={projection.norm_sq_loss}")
    print(f"projection_scaled_detail_telescope={projection.scaled_norm_sq_loss}")
    print(f"cadence_sequential_gt_batched={cadence_a}")
    print(f"cadence_batched_gt_sequential={cadence_b}")
    print(f"contact_material={contact}")
    print(f"adjoint_boundary_repair={adjoint}")
    print(f"hardening_terminal={hardening.stabilized_at}")
    print(f"softening_threshold={softening_positive_fixed_threshold(100, 2)}")
    print(f"softening_terminal={softening.stabilized_at}")


if __name__ == "__main__":
    main()
