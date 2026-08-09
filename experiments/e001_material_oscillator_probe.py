"""Deterministic integer-only comparison of three E001 material curve bases.

Run with:

    PYTHONPATH=src python experiments/e001_material_oscillator_probe.py

No result from this script is promoted to a physical material law.
"""

from enterprise_math.material_oscillator import (
    TOWARD_ZERO,
    PythagoreanRotation,
    digital_circle_quarter,
    digital_circle_radial_defect,
    projected_rotation_first_repeat,
    projected_rotation_orbit,
    recurrence_first_repeat,
    recurrence_sine_samples,
)
from enterprise_math.material_response import material_curve_profile


def main() -> None:
    amplitude = 1000
    rotation = PythagoreanRotation(399, 40, 401)

    rotation_orbit = projected_rotation_orbit(
        amplitude, rotation, steps=32, mode=TOWARD_ZERO
    )
    rotation_repeat = projected_rotation_first_repeat(
        amplitude, rotation, max_steps=5000, mode=TOWARD_ZERO
    )
    recurrence = recurrence_sine_samples(
        amplitude, rotation, sample_count=33, mode=TOWARD_ZERO
    )
    recurrence_repeat = recurrence_first_repeat(
        amplitude, rotation, max_steps=5000, mode=TOWARD_ZERO
    )
    digital = digital_circle_quarter(amplitude)

    quarter_basis = tuple(y for _x, y in rotation_orbit[:17])
    profile = material_curve_profile(
        quarter_basis,
        amplitude=amplitude,
        loading_power=2,
        return_power=1,
        return_retention=700,
    )

    max_digital_defect = max(
        digital_circle_radial_defect(amplitude, point) for point in digital
    )
    distinct_digital_y = len({y for _x, y in digital})

    print(f"rotation={rotation}")
    print(f"amplitude={amplitude}")
    print(f"rotation_quarter_y={quarter_basis}")
    print(f"rotation_first_repeat={None if rotation_repeat is None else rotation_repeat[:2]}")
    if rotation_repeat is not None:
        print(f"rotation_last_unique_state={rotation_repeat[2][-1]}")
    print(f"recurrence_prefix={recurrence}")
    print(f"recurrence_first_repeat={recurrence_repeat}")
    if recurrence_repeat is not None:
        print(f"recurrence_cycle_length={recurrence_repeat[1]-recurrence_repeat[0]}")
    print(f"digital_point_count={len(digital)}")
    print(f"digital_distinct_y={distinct_digital_y}")
    print(f"digital_max_radial_defect={max_digital_defect}")
    print(f"material_loading={profile.loading}")
    print(f"material_returning={profile.returning}")
    print(f"material_branch_gap={profile.branch_gap}")
    print(f"material_signed_area={profile.signed_area}")


if __name__ == "__main__":
    main()
