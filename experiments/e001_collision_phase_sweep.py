"""E001.6 deterministic sweep of the 1D spatial-collapse / motion phase plane."""

from enterprise_math.collision_phase_diagram import (
    approach_phase_1d,
    collision_phase_1d,
    minimum_factor_for_static_no_skip_1d,
)


def print_crossing_table(radius_sum: int, max_factor: int = 6, max_step: int = 8) -> None:
    print(f"radius_sum={radius_sum}")
    header = "d\\s " + " ".join(f"{step:>3}" for step in range(1, max_step + 1))
    print(header)
    for factor in range(max_factor, 0, -1):
        row = []
        for step in range(1, max_step + 1):
            phase = collision_phase_1d(radius_sum, factor, step)
            row.append("CAP" if phase.static_no_skip_guaranteed else "SKP")
        print(f"{factor:>3} " + " ".join(f"{item:>3}" for item in row))
    print(
        "minimum_capture_factor_by_step="
        f"{tuple((step, minimum_factor_for_static_no_skip_1d(radius_sum, step)) for step in range(1, max_step + 1))}"
    )


def print_refinement_path(primitive_gap: int, radius_sum: int, relative_step: int) -> None:
    print(
        f"refinement_path gap={primitive_gap} radius_sum={radius_sum} relative_step={relative_step}"
    )
    start_factor = max(
        primitive_gap + 2,
        minimum_factor_for_static_no_skip_1d(radius_sum, relative_step) + 2,
    )
    for factor in range(start_factor, 0, -1):
        phase = approach_phase_1d(
            primitive_gap=primitive_gap,
            radius_sum=radius_sum,
            collapse_factor=factor,
            relative_step=relative_step,
        )
        print(
            f"d={factor} status={phase.status} band={phase.interaction_band_states} "
            f"skip_witness={phase.skip_witness}"
        )


def main() -> None:
    print_crossing_table(radius_sum=0)
    print_crossing_table(radius_sum=2)
    print_refinement_path(primitive_gap=3, radius_sum=0, relative_step=2)
    print_refinement_path(primitive_gap=5, radius_sum=1, relative_step=6)


if __name__ == "__main__":
    main()
