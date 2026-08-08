"""Centered-prime geometry of P018 factor proof slack.

For center c=k+1, a symmetric prime pair c-r,c+r corresponds to the
near-diagonal first-factor shell indexed by p=c-r.  Under the Stage-8 size
condition p>r^2, the *smallest* positive symmetric prime radius is exactly one
more than the factor proof slack.

This is an elementary change of variables around the square-basin center.  It
does not assert that every center has a symmetric prime pair and does not prove
Goldbach-type conjectures.
"""

from __future__ import annotations

from .factor_precision import first_factor_shell
from .legendre import is_prime
from .prime_gap_slack import factor_proof_slack, near_diagonal_shell_data


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def centered_prime_pair(center: int, radius: int) -> tuple[int, int] | None:
    """Return (c-r,c+r) when both are prime, otherwise None."""
    _require_positive("center", center)
    _require_positive("radius", radius)
    if radius >= center:
        return None
    left = center - radius
    right = center + radius
    if is_prime(left) and is_prime(right):
        return left, right
    return None


def centered_prime_radius(center: int) -> int | None:
    """Smallest positive radius giving a symmetric pair of distinct primes."""
    _require_positive("center", center)
    for radius in range(1, center):
        if centered_prime_pair(center, radius) is not None:
            return radius
    return None


def centered_shell_data(center: int, radius: int) -> dict[str, object]:
    """Re-express the Stage-8 near-diagonal shell around center c=k+1."""
    _require_positive("center", center)
    _require_positive("radius", radius)
    if radius >= center:
        raise ValueError("radius must be smaller than center")
    k = center - 1
    slack = radius - 1
    left = center - radius
    if left < 3 or not is_prime(left):
        raise ValueError("left centered state must be an odd prime")
    if left <= radius * radius:
        raise ValueError("centered theorem requires left prime > radius^2")
    data = near_diagonal_shell_data(k, slack)
    right = center + radius
    expected = centered_prime_pair(center, radius)
    if bool(data["nonempty"]) != (expected is not None):
        raise AssertionError("centered prime pair disagreed with near-diagonal shell")
    if data["p"] != left or data["q"] != right:
        raise AssertionError("centered coordinates disagreed with Stage-8 variables")
    if data["shell"]:
        n = data["shell"][0]
        if n != center * center - radius * radius:
            raise AssertionError("shell state lost difference-of-squares localization")
    return {
        "center": center,
        "radius": radius,
        "k": k,
        "left_prime": left,
        "right_candidate": right,
        "pair": expected,
        "shell": data["shell"],
        "nonempty": bool(data["nonempty"]),
        "square_offset": radius * radius,
    }


def slack_centered_radius_equivalence(k: int) -> dict[str, int | bool]:
    """Verify sigma(k)+1 is the minimal centered-prime radius in its theorem range.

    The theorem applies when H(k)=k-s is an odd prime and H(k)>(s+1)^2.
    """
    _require_positive("k", k)
    slack = factor_proof_slack(k)
    radius = slack + 1
    center = k + 1
    left = center - radius
    if left < 3 or left <= radius * radius:
        raise ValueError("actual factor horizon is outside the centered theorem range")
    if not is_prime(left):
        raise AssertionError("positive factor horizon must be prime")
    pair = centered_prime_pair(center, radius)
    if pair is None:
        raise AssertionError("actual near-diagonal slack failed to create prime pair")
    minimal = centered_prime_radius(center)
    if minimal != radius:
        raise AssertionError("factor proof slack did not equal minimal centered radius")
    shell = first_factor_shell(k, left)
    expected_state = center * center - radius * radius
    if shell != [expected_state]:
        raise AssertionError("last shell was not the centered difference-of-squares state")
    return {
        "k": k,
        "center": center,
        "slack": slack,
        "radius": radius,
        "left_prime": pair[0],
        "right_prime": pair[1],
        "square_offset": radius * radius,
        "verified": True,
    }


def fixed_slack_centered_criterion(k: int, slack: int) -> dict[str, object]:
    """Characterize sigma(k)=s by the first centered prime radius s+1.

    Assumes p=k-s is an odd prime with p>(s+1)^2.  Under this hypothesis,
    sigma(k)=s iff radius s+1 is a centered prime pair and no smaller positive
    radius is a centered prime pair.
    """
    _require_positive("k", k)
    _require_natural("slack", slack)
    if slack >= k:
        raise ValueError("slack must be smaller than k")
    center = k + 1
    radius = slack + 1
    left = center - radius
    if left < 3 or not is_prime(left):
        raise ValueError("k-slack must be an odd prime")
    if left <= radius * radius:
        raise ValueError("criterion requires k-slack>(slack+1)^2")
    pair_at_radius = centered_prime_pair(center, radius) is not None
    smaller_pair = next(
        (
            r
            for r in range(1, radius)
            if centered_prime_pair(center, r) is not None
        ),
        None,
    )
    criterion = pair_at_radius and smaller_pair is None
    actual = factor_proof_slack(k) == slack
    if criterion != actual:
        raise AssertionError("fixed-slack centered-prime criterion failed")
    return {
        "k": k,
        "center": center,
        "slack": slack,
        "radius": radius,
        "pair_at_radius": pair_at_radius,
        "smaller_pair_radius": smaller_pair,
        "criterion": criterion,
        "actual": actual,
    }


def centered_radius_parity(k: int) -> dict[str, int | bool]:
    """For H(k)>2 in the near-diagonal range, record the forced radius parity."""
    data = slack_centered_radius_equivalence(k)
    radius = int(data["radius"])
    # center=k+1 and both centered primes are odd, so center and radius have
    # opposite parity; equivalently radius ≡ k (mod 2).
    verified = radius % 2 == k % 2
    if not verified:
        raise AssertionError("centered prime radius parity failed")
    return {"k": k, "radius": radius, "verified": True}
