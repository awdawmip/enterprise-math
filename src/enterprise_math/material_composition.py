"""Finite composition laws for E001 material curve transforms.

For the scale-preserving hardening and softening operators, nested transforms
are bounded above by the single transform with product exponent, but projection
and integer-root collapse can make the inequality strict.  The nested operators
also need not commute.

Thus composition order is retained as material/history structure rather than
being silently replaced by one aggregate exponent.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_response import hardening_sample, softening_sample


@dataclass(frozen=True)
class MaterialCompositionReport:
    """One two-operator composition compared with reverse order and product power."""

    sample: int
    amplitude: int
    first_power: int
    second_power: int
    forward: int
    reverse: int
    product_power_value: int
    forward_defect: int
    reverse_defect: int
    commutator: int


def _validate(sample: int, amplitude: int, first_power: int, second_power: int) -> None:
    if isinstance(amplitude, bool) or not isinstance(amplitude, int) or amplitude <= 0:
        raise ValueError("amplitude must be a positive integer")
    if isinstance(sample, bool) or not isinstance(sample, int) or not 0 <= sample <= amplitude:
        raise ValueError("sample must be an integer in 0..amplitude")
    for name, power in (("first_power", first_power), ("second_power", second_power)):
        if isinstance(power, bool) or not isinstance(power, int) or power <= 0:
            raise ValueError(f"{name} must be a positive integer")


def hardening_composition_report(
    sample: int,
    amplitude: int,
    first_power: int,
    second_power: int,
) -> MaterialCompositionReport:
    """Compare H_first(H_second(s)), reverse order, and H_(first*second)(s)."""
    _validate(sample, amplitude, first_power, second_power)
    forward = hardening_sample(
        hardening_sample(sample, amplitude, second_power),
        amplitude,
        first_power,
    )
    reverse = hardening_sample(
        hardening_sample(sample, amplitude, first_power),
        amplitude,
        second_power,
    )
    direct = hardening_sample(sample, amplitude, first_power * second_power)
    if forward > direct or reverse > direct:
        raise AssertionError("nested hardening exceeded product-power upper bound")
    return MaterialCompositionReport(
        sample=sample,
        amplitude=amplitude,
        first_power=first_power,
        second_power=second_power,
        forward=forward,
        reverse=reverse,
        product_power_value=direct,
        forward_defect=direct - forward,
        reverse_defect=direct - reverse,
        commutator=forward - reverse,
    )


def softening_composition_report(
    sample: int,
    amplitude: int,
    first_power: int,
    second_power: int,
) -> MaterialCompositionReport:
    """Compare G_first(G_second(s)), reverse order, and G_(first*second)(s)."""
    _validate(sample, amplitude, first_power, second_power)
    forward = softening_sample(
        softening_sample(sample, amplitude, second_power),
        amplitude,
        first_power,
    )
    reverse = softening_sample(
        softening_sample(sample, amplitude, first_power),
        amplitude,
        second_power,
    )
    direct = softening_sample(sample, amplitude, first_power * second_power)
    if forward > direct or reverse > direct:
        raise AssertionError("nested softening exceeded product-power upper bound")
    return MaterialCompositionReport(
        sample=sample,
        amplitude=amplitude,
        first_power=first_power,
        second_power=second_power,
        forward=forward,
        reverse=reverse,
        product_power_value=direct,
        forward_defect=direct - forward,
        reverse_defect=direct - reverse,
        commutator=forward - reverse,
    )
