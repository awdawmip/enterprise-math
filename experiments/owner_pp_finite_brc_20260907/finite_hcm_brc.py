"""Finite complete-difference data as a positive BRC word ensemble.

The carrier has labelled binary words of a fixed length d. These are abstract
branch labels, not additional native spatial axes. The histogram observes only
actual positive word weights and multiplicities; it forgets word identities.
The factorial-moment readout implemented here is not a power-moment claim.
"""

from __future__ import annotations

from fractions import Fraction as F
from math import comb
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
from enterprise_math.brc_histogram import WeightHistogram, histogram_recoalesce, histogram_serial

SCHEMA = "owner_finite_hcm_brc_v1"
SCOPE = "FINITE_EXCHANGEABLE_WORDS_AND_SYMMETRIC_FACTORIAL_OBSERVATIONS_ONLY"
MAX_SCALAR_BITS = 12000


class ResourceLimit(ValueError):
    pass


def _sequence(values, max_degree=256):
    if type(max_degree) is not int or max_degree < 0:
        raise ValueError("max_degree must be a nonnegative integer")
    if type(values) not in (list, tuple) or not values:
        raise TypeError("nonempty list or tuple of exact rationals required")
    if len(values) - 1 > max_degree:
        raise ResourceLimit("declared finite degree budget exceeded")
    if any(type(v) not in (int, F) for v in values):
        raise TypeError("moment inputs must be int or Fraction, never float or bool")
    result = tuple(F(v) for v in values)
    for value in result:
        _scalar_budget(value)
    return result


def _scalar_budget(value):
    if max(value.numerator.bit_length(), value.denominator.bit_length()) > MAX_SCALAR_BITS:
        raise ResourceLimit("exact rational scalar exceeds the 12000-bit representation budget")


def _text(q):
    q = F(q)
    _scalar_budget(q)
    return f"{q.numerator}/{q.denominator}"


def _read(q):
    if not isinstance(q, str):
        raise ValueError("canonical rational string required")
    parts = q.split("/")
    if len(parts) != 2:
        raise ValueError("canonical rational must have one slash")
    if any(len(part) > 4000 for part in parts):
        raise ResourceLimit("rational text exceeds the declared representation budget")
    value = F(q)
    if q != _text(value):
        raise ValueError("rational string must be reduced p/q")
    return value


def _exact_record(value, *, depth=0, budget=None):
    """Validate primitive certificate types before any equality comparisons."""
    if budget is None:
        budget = [20000]
    budget[0] -= 1
    if budget[0] < 0:
        raise ResourceLimit("certificate node budget exceeded")
    if depth > 10:
        raise ValueError("certificate nesting exceeds its closed schema")
    if type(value) is str:
        if len(value) > 100000:
            raise ResourceLimit("certificate scalar size budget exceeded")
    elif type(value) is int:
        if value.bit_length() > 400000:
            raise ResourceLimit("certificate integer size budget exceeded")
    elif type(value) is list:
        for child in value:
            _exact_record(child, depth=depth+1, budget=budget)
    elif type(value) is dict and all(type(key) is str for key in value):
        for child in value.values():
            _exact_record(child, depth=depth+1, budget=budget)
    else:
        raise ValueError("certificate must use exact dict/list/string/integer values")


def terminal_weights(h, *, max_degree=256):
    """Per-word weights beta_j = (-1)^(d-j) Delta^(d-j) h_j."""
    h = _sequence(h, max_degree)
    d = len(h) - 1
    return tuple(sum(((-1)**a * comb(d-j, a) * h[j+a]
                      for a in range(d-j+1)), F(0)) for j in range(d+1))


def _histogram(beta, multiplicities):
    counts = {}
    for weight, count in zip(beta, multiplicities):
        if weight < 0:
            raise ValueError("negative per-word mass has no positive BRC realization")
        if weight and count:
            counts[weight] = counts.get(weight, 0) + count
    return WeightHistogram.from_counts(counts)


def histogram_record(histogram):
    return dict(entries=[dict(weight=_text(q), count=c) for q, c in histogram.entries],
                branch_count=histogram.count, total_mass=_text(histogram.total_mass))


def build_certificate(h, *, max_degree=256):
    h = _sequence(h, max_degree)
    d, beta = len(h)-1, terminal_weights(h, max_degree=max_degree)
    negative = next((j for j, value in enumerate(beta) if value < 0), None)
    certificate = dict(schema=SCHEMA, degree=d, input_h=[_text(v) for v in h],
                       beta=[_text(v) for v in beta],
                       scope=SCOPE)
    if negative is not None:
        certificate.update(status="OBSTRUCTED", obstruction=dict(
            r=negative, k=d-negative, signed_difference=_text(beta[negative])))
    else:
        certificate.update(status="REALIZED", layers=[dict(j=j, word_count=comb(d, j),
            per_word_mass=_text(value), total_layer_mass=_text(comb(d, j)*value))
            for j, value in enumerate(beta) if value],
            histogram=histogram_record(_histogram(beta, [comb(d, j) for j in range(d+1)])),
            power_moment_measure="UNCLASSIFIED")
    result = verify_certificate(h, certificate, max_degree=max_degree)
    if result["status"] == "UNVERIFIED":
        raise ResourceLimit(result["reason"])
    if not result["valid"]:
        raise ArithmeticError("constructed certificate failed original-data verification")
    return certificate


def verify_certificate(h, certificate, *, max_degree=256):
    """Check the triangular factorial readout against every original h_a.

    This reconstruction does not rerun the producing finite differences.
    Invertibility follows from the nonzero triangular diagonal, so the beta
    values are uniquely determined. A negative beta is an exact obstruction
    to the declared exchangeable/symmetric readouts. It does not exclude an
    arbitrary nonexchangeable ensemble having just one fixed prefix sequence.
    """
    try:
        h = _sequence(h, max_degree)
        d = len(h)-1
        if type(certificate) is not dict:
            raise ValueError("certificate must be an exact dict")
        status = certificate.get("status")
        base_fields = {"schema", "degree", "input_h", "beta", "scope", "status"}
        if status == "REALIZED":
            fields = base_fields | {"layers", "histogram", "power_moment_measure"}
        elif status == "OBSTRUCTED":
            fields = base_fields | {"obstruction"}
        else:
            raise ValueError("unknown certificate status")
        if set(certificate) != fields:
            raise ValueError("certificate fields do not match the declared status")
        for key in ("input_h", "beta"):
            if type(certificate[key]) is not list or len(certificate[key]) != d+1:
                raise ValueError("wrong finite vector container or length")
        if status == "REALIZED":
            if type(certificate["layers"]) is not list or len(certificate["layers"]) > d+1:
                raise ValueError("wrong layer container or length")
            histogram = certificate["histogram"]
            if (type(histogram) is not dict or set(histogram) != {"entries", "branch_count", "total_mass"}
                    or type(histogram["entries"]) is not list or len(histogram["entries"]) > d+1):
                raise ValueError("wrong histogram container or length")
        _exact_record(certificate)
        if (certificate.get("schema") != SCHEMA or type(certificate.get("degree")) is not int
                or certificate["degree"] != d or certificate.get("input_h") != [_text(v) for v in h]
                or certificate.get("scope") != SCOPE):
            raise ValueError("original sequence binding mismatch")
        beta = tuple(_read(v) for v in certificate["beta"])
        if len(beta) != d+1:
            raise ValueError("wrong beta vector length")
        for a in range(d+1):
            if sum((comb(d-a, j-a)*beta[j] for j in range(a, d+1)), F(0)) != h[a]:
                raise ValueError("original factorial readout identity failed")
        negative = next((j for j, value in enumerate(beta) if value < 0), None)
        if negative is not None:
            if (certificate.get("status") != "OBSTRUCTED" or certificate.get("obstruction") !=
                    dict(r=negative, k=d-negative, signed_difference=_text(beta[negative]))):
                raise ValueError("negative finite difference witness mismatch")
        else:
            expected = [dict(j=j, word_count=comb(d, j), per_word_mass=_text(value),
                             total_layer_mass=_text(comb(d, j)*value))
                        for j, value in enumerate(beta) if value]
            histogram = _histogram(beta, [comb(d, j) for j in range(d+1)])
            if (certificate.get("status") != "REALIZED" or certificate.get("layers") != expected
                    or certificate.get("histogram") != histogram_record(histogram)
                    or certificate.get("power_moment_measure") != "UNCLASSIFIED"):
                raise ValueError("positive branch carrier or observation mismatch")
        return dict(valid=True, status="OBSTRUCTED" if negative is not None else "REALIZED",
                    reason="all original factorial identities verified")
    except ResourceLimit as error:
        return dict(valid=False, status="UNVERIFIED", reason=str(error))
    except (ValueError, TypeError, KeyError, AttributeError, ZeroDivisionError) as error:
        return dict(valid=False, status="INVALID_CERTIFICATE", reason=str(error))


def prefix_observation_histogram(h, r, k, *, max_degree=256):
    """Fix r designated ones and k designated zeros in the same d-word.

    The remaining d-r-k positions retain their combinatorial multiplicities.
    Its mass is (-1)^k Delta^k h_r. No independence assumption is made.
    """
    h = _sequence(h, max_degree)
    d = len(h)-1
    if type(r) is not int or type(k) is not int or min(r, k) < 0 or r+k > d:
        raise ValueError("need nonnegative integers r,k with r+k<=d")
    beta = terminal_weights(h, max_degree=max_degree)
    counts = [comb(d-r-k, j-r) if r <= j <= d-k else 0 for j in range(d+1)]
    return _histogram(beta, counts)


def coefficient_histogram(h, k, *, max_degree=256):
    """Mark k of a word's zero positions; observe the Bhat coefficient.

    Branches are pairs (word, marked-zero-subset). Each pair keeps the word's
    original positive mass; unit choices are joined using actual BRC serial
    and alternative operations. The coefficient is a mass, not a branch count.
    """
    h = _sequence(h, max_degree)
    d = len(h)-1
    if type(k) is not int or not 0 <= k <= d:
        raise ValueError("need integer 0<=k<=d")
    beta = terminal_weights(h, max_degree=max_degree)
    if any(value < 0 for value in beta):
        raise ValueError("negative word mass has no positive BRC coefficient carrier")
    result = WeightHistogram.from_weights(())
    for j, value in enumerate(beta):
        if value and k <= d-j:
            word_layer = WeightHistogram.from_counts({value: comb(d, j)})
            choices = WeightHistogram.from_counts({F(1): comb(d-j, k)})
            result = histogram_recoalesce(result, histogram_serial(word_layer, choices))
    return result


def verify_square_obstruction(h, polynomial, *, max_degree=256):
    """A negative value on p(u)^2 excludes every positive power-moment measure.

    A nonnegative result is UNDETERMINED, never a feasibility certificate.
    """
    h, polynomial = _sequence(h, max_degree), _sequence(polynomial, max_degree)
    if 2*(len(polynomial)-1) >= len(h):
        raise ValueError("square degree exceeds the supplied moments")
    value = sum((a*b*h[i+j] for i, a in enumerate(polynomial)
                 for j, b in enumerate(polynomial)), F(0))
    return dict(status="NO_POSITIVE_POWER_MOMENT_MEASURE" if value < 0 else "UNDETERMINED",
                square_readout=_text(value), polynomial=[_text(v) for v in polynomial],
                scope="supplied power moments; any positive measure on the real line")
