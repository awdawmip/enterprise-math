"""E001 material-oscillator invariant probe.

The probe prints integer-only evidence for four structures:

1. the precision/turn dead-zone threshold;
2. an intrinsic first loading lobe;
3. exact collapse loss certificates;
4. path dependence from intermediate projections and curve-transform order.
"""

from enterprise_math.material_invariants import (
    first_resolved_loading_lobe,
    hardening_composition_defect,
    parameter_rotation,
    parameter_rotation_minimum_transverse_amplitude,
    projection_history_comparison,
    softening_composition_defect,
    toward_zero_loss_certificate,
)
from enterprise_math.material_oscillator import TOWARD_ZERO, projected_rotation_step
from enterprise_math.material_response import hardening_sample, softening_sample


def main() -> None:
    print("dead_zone_thresholds")
    for m in (4, 10, 20, 40):
        threshold = parameter_rotation_minimum_transverse_amplitude(m)
        print(f"m={m} minimum_amplitude={threshold} resolved_condition=m<2A")

    rotation = parameter_rotation(20)
    profile = first_resolved_loading_lobe(1000, rotation)
    print("loading_lobe")
    print(f"samples={profile}")

    state = (1000, 0)
    print("first_steps")
    for index in range(5):
        report = projected_rotation_step(*state, rotation, TOWARD_ZERO)
        certificate = toward_zero_loss_certificate(*state, rotation)
        print(
            f"step={index} before={state} after={report.after} "
            f"norm_loss={report.norm_sq_loss} scaled_loss_certificate={certificate}"
        )
        state = report.after

    comparison = projection_history_comparison(100, rotation, 16)
    print("history_projection_defect")
    print(f"terminal={comparison.terminal}")
    print(f"stepwise={comparison.stepwise}")
    print(f"defect={comparison.defect} l1={comparison.l1_defect}")

    print("curve_composition")
    amplitude = 5
    sample = 4
    print(
        "hardening_order="
        f"{hardening_sample(hardening_sample(sample, amplitude, 3), amplitude, 2)},"
        f"{hardening_sample(hardening_sample(sample, amplitude, 2), amplitude, 3)}"
    )
    print(
        "hardening_direct_vs_staged_defect="
        f"{hardening_composition_defect(sample, amplitude, 2, 3)}"
    )

    amplitude = 4
    sample = 1
    print(
        "softening_order="
        f"{softening_sample(softening_sample(sample, amplitude, 3), amplitude, 2)},"
        f"{softening_sample(softening_sample(sample, amplitude, 2), amplitude, 3)}"
    )
    print(
        "softening_direct_vs_staged_defect="
        f"{softening_composition_defect(sample, amplitude, 2, 3)}"
    )


if __name__ == "__main__":
    main()
