"""Status-preserving facade over reusable prime-related Enterprise Math methods.

This module owns no prime theorem and intentionally reimplements no owner
algorithm. It normalizes results, exposes provenance/status metadata, and
routes calls to canonical owner functions or explicitly admitted, status-preserving
maintenance adapters. Non-executable WIP methods remain registry-only.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, is_dataclass
from functools import lru_cache
from importlib.resources import files
import json
from typing import Any, Iterable

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
from .native_trisector_coupled_closure import (
    coupled_closure_certificate as _coupled_closure_certificate,
    native_trisector_coupled_certificate as _native_trisector_coupled_certificate,
    odd_sector_lane_certificate as _odd_sector_lane_certificate,
    split_hyperbola_orbit_certificate as _split_hyperbola_orbit_certificate,
)
from .p017_precision_horizon import least_witness_state, survivor_prime_horizon_data
from .p018_p023_power_free_action_basis import minimal_root_quotient_action_basis
from .r005a_sieve_quotients import (
    actual_transient_summary,
    finite_horizon_summary,
    normalize_distinct_set,
)


_INVENTORY_RESOURCE = "prime_method_inventory.json"
_INVENTORY_SUPPLEMENTS = (
    "prime_method_inventory_r005a_ingest.json",
    "prime_method_inventory_native_trisector_coupled_closure.json",
)


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
    resource_root = files("enterprise_math")
    inventory = json.loads(
        resource_root.joinpath(_INVENTORY_RESOURCE).read_text(encoding="utf-8")
    )
    methods = list(inventory["methods"])
    method_ids = {method["method_id"] for method in methods}
    allowed_toolization = set(inventory["toolization_status_vocabulary"])
    allowed_source = set(inventory["source_status_vocabulary"])

    for resource_name in _INVENTORY_SUPPLEMENTS:
        supplement = json.loads(
            resource_root.joinpath(resource_name).read_text(encoding="utf-8")
        )
        for method in supplement["methods"]:
            method_id = method["method_id"]
            if method_id in method_ids:
                raise ValueError(f"duplicate prime method_id across inventory: {method_id}")
            if method["toolization_status"] not in allowed_toolization:
                raise ValueError(
                    f"unknown toolization_status in {resource_name}: "
                    f"{method['toolization_status']}"
                )
            unknown_source = set(method["source_status"]) - allowed_source
            if unknown_source:
                raise ValueError(
                    f"unknown source_status in {resource_name}: "
                    + ", ".join(sorted(unknown_source))
                )
            methods.append(method)
            method_ids.add(method_id)

    merged = dict(inventory)
    merged["methods"] = methods
    merged["inventory_supplements"] = list(_INVENTORY_SUPPLEMENTS)
    return merged


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


def _validated_prime_set(primes: Iterable[int]) -> tuple[int, ...]:
    values = normalize_distinct_set(primes)
    nonprimes = tuple(value for value in values if not is_prime(value))
    if nonprimes:
        raise ValueError(
            "prime set contains nonprime values: " + ", ".join(map(str, nonprimes))
        )
    return values


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


def actual_sieve_transient_quotient(primes: Iterable[int]) -> PrimeToolResult:
    """Exact R005-A future quotient data for actual p^2 sieve activation."""

    prime_set = _validated_prime_set(primes)
    value = actual_transient_summary(prime_set)
    prefix = tuple(primes_up_to(max(prime_set))) == prime_set
    value["prime_prefix"] = prefix
    if prefix:
        expected = max(prime_set) + 1
        actual = value["union_support"]["preperiod"]
        if actual != expected:
            raise AssertionError("prime-prefix union transient formula disagreed")
        value["prime_prefix_union_preperiod"] = expected
    return _result(
        "r005a.actual_sieve_transient_quotient",
        value,
        "ENTERPRISE_SPECIALIZATION. Eratosthenes p^2 activation and next-strike "
        "implementation state are classical; this callable preserves the accepted "
        "exact relation-vs-union future-quotient specialization only.",
    )


def finite_horizon_sieve_quotient(
    primes: Iterable[int],
    horizon: int,
    *,
    language: str = "union_support",
    activation: str = "actual",
    segment_length: int | None = None,
    transitions: int | None = None,
    state_limit: int = 100_000,
) -> PrimeToolResult:
    """Exact bounded finite-horizon quotient analyzer for the R005-A sieve model."""

    if state_limit <= 0:
        raise ValueError("state_limit must be > 0")
    prime_set = _validated_prime_set(primes)
    value = finite_horizon_summary(
        prime_set,
        horizon,
        language=language,
        activation=activation,
        segment_length=segment_length,
        transitions=transitions,
        state_limit=state_limit,
    )
    return _result(
        "r005a.finite_horizon_sieve_quotient",
        value,
        "ENTERPRISE_SPECIALIZATION. Generic deterministic partition refinement and "
        "the generic segment/horizon block law are prior art / existing Enterprise "
        "continuation theory. This is an exact bounded prime-sieve specialization.",
    )


def split_hyperbola_orbit_certificate(B: int, C: int, q: int) -> PrimeToolResult:
    """Prime Toolkit wrapper for the exact split-hyperbola sign-orbit certificate."""

    return _result(
        "native_filament.split_hyperbola_orbit_certificate",
        _split_hyperbola_orbit_certificate(B, C, q),
        "Support-level classical certificate; it does not invent universal-breaker semantics.",
    )


def odd_sector_lane_certificate(s: int, q: int) -> PrimeToolResult:
    """Prime Toolkit wrapper for controlled odd-sector lane/Joukowski certificates."""

    return _result(
        "native_filament.odd_sector_lane_certificate",
        _odd_sector_lane_certificate(s, q),
        "Only s=3 is native Enterprise geometry; other odd s are controlled comparators.",
    )


def coupled_closure_certificate(s: int, q_b: int) -> PrimeToolResult:
    """Prime Toolkit wrapper for the admitted longitudinal/transverse closure check."""

    return _result(
        "native_filament.coupled_closure_certificate",
        _coupled_closure_certificate(s, q_b),
        "q_b must already carry universal-breaker semantics; theorem-9 is breaker-coprime capacity only.",
    )


def native_trisector_coupled_certificate() -> PrimeToolResult:
    """One-call status-preserving certificate for the admitted native theorem node."""

    return _result(
        "native_filament.native_trisector_coupled_certificate",
        _native_trisector_coupled_certificate(),
        "AUDITED_RESEARCH_THEOREM only; Foundation review completed without Foundation admission and no novelty claim is implied.",
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
    "actual_sieve_transient_quotient",
    "finite_horizon_sieve_quotient",
    "split_hyperbola_orbit_certificate",
    "odd_sector_lane_certificate",
    "coupled_closure_certificate",
    "native_trisector_coupled_certificate",
    "list_methods",
    "method_record",
]
