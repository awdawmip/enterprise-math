"""Status-preserving facade over reusable prime-related Enterprise Math methods.

This module owns no prime theorem and intentionally reimplements no owner
algorithm. It normalizes results, exposes provenance/status metadata, and
routes calls to current canonical owner functions only. Noncanonical/WIP
methods remain discoverable through the registry but are not executable here.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, is_dataclass
from functools import lru_cache
from importlib.resources import files
import json
from typing import Any

from .centered_prime_radius import slack_centered_radius_equivalence
from .factor_precision import first_factor_shell as _first_factor_shell
from .factor_precision import smallest_prime_factor
from .legendre import (
    binary_carry_square_interval_prime_count,
    carry_square_interval_prime_count,
    direct_square_interval_prime_count,
    is_prime,
    mobius_square_interval_prime_count,
    primes_up_to,
)
from .p017_precision_horizon import least_witness_state, survivor_prime_horizon_data
from .p018_p023_power_free_action_basis import minimal_root_quotient_action_basis


_INVENTORY_RESOURCE = "prime_method_inventory.json"


@dataclass(frozen=True)
class PrimeToolResult:
    """Normalized payload with theorem/provenance status kept next to the value."""

    method_id: str
    source_status: tuple[str, ...]
    mathematical_status: str
    toolization_status: str
    exactness: str
    source_ref: tuple[str, ...]
    value: Any
    warning: str | None = None

    def as_dict(self) -> dict[str, Any]:
        return {
            "method_id": self.method_id,
            "source_status": list(self.source_status),
            "mathematical_status": self.mathematical_status,
            "toolization_status": self.toolization_status,
            "exactness": self.exactness,
            "source_ref": list(self.source_ref),
            "value": _normalize(self.value),
            "warning": self.warning,
        }


def _normalize(value: Any) -> Any:
    if is_dataclass(value):
        return {key: _normalize(item) for key, item in asdict(value).items()}
    if isinstance(value, dict):
        return {str(key): _normalize(item) for key, item in value.items()}
    if isinstance(value, tuple):
        return [_normalize(item) for item in value]
    if isinstance(value, list):
        return [_normalize(item) for item in value]
    return value


@lru_cache(maxsize=1)
def _inventory() -> dict[str, Any]:
    resource = files("enterprise_math").joinpath(_INVENTORY_RESOURCE)
    return json.loads(resource.read_text(encoding="utf-8"))


def list_methods(toolization_status: str | None = None) -> tuple[dict[str, Any], ...]:
    """Return inventory records, optionally filtered by toolization status."""

    methods = _inventory()["methods"]
    if toolization_status is not None:
        allowed = set(_inventory()["toolization_status_vocabulary"])
        if toolization_status not in allowed:
            raise ValueError(
                "unknown toolization_status; expected one of "
                + ", ".join(sorted(allowed))
            )
        methods = [
            method
            for method in methods
            if method["toolization_status"] == toolization_status
        ]
    return tuple(dict(method) for method in methods)


def method_record(method_id: str) -> dict[str, Any]:
    """Return one exact inventory record by method_id."""

    for method in _inventory()["methods"]:
        if method["method_id"] == method_id:
            return dict(method)
    raise KeyError(f"unknown prime method_id: {method_id}")


def _result(method_id: str, value: Any, warning: str | None = None) -> PrimeToolResult:
    record = method_record(method_id)
    return PrimeToolResult(
        method_id=method_id,
        source_status=tuple(record["source_status"]),
        mathematical_status=record["mathematical_status"],
        toolization_status=record["toolization_status"],
        exactness=record["exactness"],
        source_ref=tuple(record["source_ref"]),
        value=_normalize(value),
        warning=warning,
    )


def bounded_primality(n: int) -> PrimeToolResult:
    """Exact bounded classical baseline; routes to legendre.is_prime."""

    return _result("classical.bounded_primality", is_prime(n))


def bounded_prime_enumeration(limit: int) -> PrimeToolResult:
    """Exact bounded classical baseline; routes to legendre.primes_up_to."""

    return _result("classical.prime_enumeration", primes_up_to(limit))


def least_factor_witness(n: int) -> PrimeToolResult:
    """Least prime divisor; for prime n the result is n itself."""

    value = smallest_prime_factor(n)
    warning = None
    if value == n:
        warning = (
            "The returned least prime divisor equals n, so n is prime on the "
            "owner oracle; this is not a proper-factor/compositeness witness."
        )
    return _result("classical.least_factor_witness", value, warning)


def least_visible_factor(n: int, cutoff: int) -> PrimeToolResult:
    """Least tested divisor <= cutoff; 0 means no visible divisor, not primality."""

    value = least_witness_state(n, cutoff)
    warning = None
    if value == 0:
        warning = "No tested factor is visible at this cutoff; 0 is not a prime certificate."
    elif value == n:
        warning = (
            "The visible prime divisor equals n itself; this is a self-divisor "
            "primality observation, not a proper-factor/compositeness witness."
        )
    return _result("p018.least_visible_factor", value, warning)


def first_factor_shell(k: int, prime: int) -> PrimeToolResult:
    """Exact first-factor shell inside k^2<n<(k+1)^2."""

    return _result("p018.first_factor_shell", _first_factor_shell(k, prime))


def proof_factor_horizon(k: int) -> PrimeToolResult:
    """Exact a-posteriori survivor-prime horizon and proof slack for one basin."""

    warning = (
        "This is the exact minimal cutoff obtained by classifying the actual "
        "basin composites. It is not an independent ex-ante bound proving "
        "prime existence in the basin."
    )
    return _result(
        "p018.survivor_prime_horizon",
        survivor_prime_horizon_data(k),
        warning,
    )


def square_basin_certificate(k: int) -> PrimeToolResult:
    """Cross-normalize the current exact direct/Mobius/carry basin identities."""

    direct = direct_square_interval_prime_count(k)
    mobius = mobius_square_interval_prime_count(k)
    carry = carry_square_interval_prime_count(k)
    binary = binary_carry_square_interval_prime_count(k)
    if len({direct, mobius, carry, binary}) != 1:
        raise AssertionError("owner square-basin exact identities disagreed")
    return _result(
        "p017.mobius_carry_binary",
        {
            "k": k,
            "prime_count": direct,
            "direct": direct,
            "mobius": mobius,
            "carry": carry,
            "binary_carry": binary,
            "verified_equal": True,
        },
        "Exact finite certificate; current Mobius/carry implementations are not scalable prime-counting algorithms.",
    )


def centered_prime_slack_coordinates(k: int) -> PrimeToolResult:
    """Convert exact factor slack to centered-prime coordinates in owner range."""

    warning = (
        "Owner theorem is conditional: H(k)=k-s must be an odd prime and "
        "H(k)>(s+1)^2. Outside that range the centered-radius identity is not "
        "global (the owner regression includes k=10 as a counterexample)."
    )
    return _result(
        "p018.centered_prime_radius",
        slack_centered_radius_equivalence(k),
        warning,
    )


def power_free_action_basis(max_state: int, root_exp: int) -> PrimeToolResult:
    """Query the canonical bounded one-step semantic action basis."""

    warning = (
        "This is the one-step r-power-free semantic action basis from #249. "
        "It is not the distinct prime primitive-instruction compiler from "
        "noncanonical Draft #333."
    )
    return _result(
        "p018_p023.power_free_action_basis",
        minimal_root_quotient_action_basis(max_state, root_exp),
        warning,
    )


__all__ = [
    "PrimeToolResult",
    "bounded_primality",
    "bounded_prime_enumeration",
    "least_factor_witness",
    "least_visible_factor",
    "first_factor_shell",
    "proof_factor_horizon",
    "square_basin_certificate",
    "centered_prime_slack_coordinates",
    "power_free_action_basis",
    "list_methods",
    "method_record",
]
