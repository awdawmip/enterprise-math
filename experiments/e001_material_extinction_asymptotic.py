"""External benchmark pressure test for projected-rotation extinction time.

This experiment intentionally imports ``math.pi`` only as an external comparison
constant.  The intrinsic oscillator and extinction dynamics live in integer-only
``src/enterprise_math`` and do not depend on pi, sin, cos, or floating arithmetic.

Observed ratios near pi/2 are COMPUTATIONAL evidence only.  The script is meant
to search for denominator/angle/amplitude dependence and counterexamples, not to
state an asymptotic theorem.
"""

from math import gcd, isqrt, pi

from enterprise_math.material_oscillator import (
    TOWARD_ZERO,
    PythagoreanRotation,
    projected_rotation_step,
)


def primitive_pythagorean_rotations(max_c: int):
    for c in range(2, max_c + 1):
        for a in range(1, c):
            b_sq = c * c - a * a
            b = isqrt(b_sq)
            if b <= 0 or b * b != b_sq or a > b:
                continue
            if gcd(gcd(a, b), c) != 1:
                continue
            yield PythagoreanRotation(a, b, c)


def extinction_time(amplitude: int, rotation: PythagoreanRotation) -> int:
    state = (amplitude, 0)
    step = 0
    # The intrinsic theorem says every nontrivial toward-zero orbit terminates.
    while state != (0, 0):
        state = projected_rotation_step(*state, rotation, TOWARD_ZERO).after
        step += 1
    return step


def main() -> None:
    amplitude = 5000
    max_c = 200
    benchmark = pi / 2
    rows = []
    for rotation in primitive_pythagorean_rotations(max_c):
        steps = extinction_time(amplitude, rotation)
        ratio = steps / amplitude
        rows.append(
            (
                rotation.c,
                rotation.a,
                rotation.b,
                steps,
                ratio,
                ratio - benchmark,
                abs(ratio - benchmark),
            )
        )

    rows.sort()
    print(f"amplitude={amplitude}")
    print(f"max_c={max_c}")
    print(f"external_pi_over_2={benchmark:.12f}")
    print("c,a,b,extinction_steps,steps_per_amplitude,signed_error,abs_error")
    for row in rows:
        c, a, b, steps, ratio, signed, absolute = row
        print(
            f"{c},{a},{b},{steps},{ratio:.12f},{signed:.12f},{absolute:.12f}"
        )

    if rows:
        best = min(rows, key=lambda row: row[-1])
        worst = max(rows, key=lambda row: row[-1])
        print(f"closest_to_pi_over_2={best}")
        print(f"farthest_from_pi_over_2={worst}")


if __name__ == "__main__":
    main()
