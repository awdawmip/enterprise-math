"""Independent rational interval-family negative-inertia certificates.

Standard-library only. This module proves statements about its supplied real
symmetric interval family. An independent producer must prove that a particular
Weil/reference matrix belongs to that family; labels and hashes do not do that.

Witness convention: A[permutation, permutation] = L D L**T. L is unit lower
triangular, D is a contiguous direct sum of rational 1x1/2x2 blocks.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import re


SCHEMA = "owner_rational_interval_inertia_v1"
SCOPE = "INPUT_INTERVAL_FAMILY_ONLY"
_Q_PATTERN = re.compile(r"-?(?:0|[1-9][0-9]*)/[1-9][0-9]*\Z")
_MAX_DIGITS = 100_000


class InvalidInput(ValueError):
    """Malformed exact input, label encoding or certificate."""


class ComputationBudgetExceeded(ValueError):
    """Declared size limit; this is not a mathematical inertia conclusion."""


def _int_from_decimal(text):
    # Avoid changing Python's process-global large-integer string setting.
    negative = text.startswith("-")
    digits = text[1:] if negative else text
    value = 0
    for start in range(0, len(digits), 9):
        chunk = digits[start:start + 9]
        value = value * 10**len(chunk) + int(chunk)
    return -value if negative else value


def _int_text(value):
    if value.bit_length() < 12000:
        return str(value)
    negative = value < 0
    value = abs(value)
    chunks = []
    while value:
        value, rem = divmod(value, 10**1000)
        chunks.append(rem)
    text = str(chunks[-1]) + "".join(str(c).zfill(1000) for c in reversed(chunks[:-1]))
    return ("-" if negative else "") + text


def _q_text(value):
    return _int_text(value.numerator) + "/" + _int_text(value.denominator)


def _q(value):
    if type(value) is int or type(value) is Fraction:
        result = Fraction(value)
    elif type(value) is str:
        if len(value) > 2 * _MAX_DIGITS + 2:
            raise ComputationBudgetExceeded("rational string exceeds digit budget")
        if not _Q_PATTERN.fullmatch(value):
            raise InvalidInput("rational strings must be canonical numerator/denominator")
        numerator, denominator = value.split("/")
        result = Fraction(_int_from_decimal(numerator), _int_from_decimal(denominator))
        if _q_text(result) != value:
            raise InvalidInput("rational string is not reduced canonical form")
    else:
        raise InvalidInput("rational entries require int/Fraction/canonical p/q; bool/float rejected")
    if max(result.numerator.bit_length(), result.denominator.bit_length()) > 3 * _MAX_DIGITS:
        raise ComputationBudgetExceeded("rational exceeds bit budget")
    return result


def _nonnegative_int(value, name):
    if type(value) is not int or value < 0:
        raise InvalidInput(f"{name} must be a nonnegative integer")
    return value


def _json_label(value, depth=0):
    if depth > 64:
        raise ComputationBudgetExceeded("labels exceed nesting budget")
    if value is None or type(value) in (bool, str):
        return value
    if type(value) is int:
        if value.bit_length() > 4096:
            raise ComputationBudgetExceeded("label integer exceeds bit budget")
        return value
    if type(value) is list:
        return [_json_label(v, depth + 1) for v in value]
    if type(value) is dict and all(type(k) is str for k in value):
        return {k: _json_label(v, depth + 1) for k, v in value.items()}
    raise InvalidInput("labels require exact JSON values (no floats, tuples or non-string keys)")


def _canonical_json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=True, allow_nan=False)


def _input(bounds, labels, max_dimension):
    if type(max_dimension) is not int or max_dimension < 1:
        raise InvalidInput("max_dimension must be a positive integer")
    if type(bounds) not in (list, tuple) or not bounds:
        raise InvalidInput("bounds must be a nonempty square matrix")
    n = len(bounds)
    if n > max_dimension:
        raise ComputationBudgetExceeded("matrix exceeds dimension budget")
    rows = []
    for row in bounds:
        if type(row) not in (list, tuple) or len(row) != n:
            raise InvalidInput("bounds must be square")
        parsed = []
        for entry in row:
            if type(entry) is not dict or set(entry) != {"lo", "hi"}:
                raise InvalidInput("each bound must have exactly lo and hi")
            lo, hi = _q(entry["lo"]), _q(entry["hi"])
            if lo > hi:
                raise InvalidInput("reversed interval")
            parsed.append((lo, hi))
        rows.append(parsed)
    for i in range(n):
        for j in range(i):
            if rows[i][j] != rows[j][i]:
                raise InvalidInput("bounds must be exactly symmetric")
    if type(labels) not in (list, tuple) or len(labels) != n:
        raise InvalidInput("one independent basis label is required per matrix row")
    canonical_labels = [_json_label(v) for v in labels]
    encoded_labels = [_canonical_json(v) for v in canonical_labels]
    if len(set(encoded_labels)) != n:
        raise InvalidInput("basis labels must be distinct as canonical JSON values")
    binding = {"bounds": [[{"lo": _q_text(lo), "hi": _q_text(hi)} for lo, hi in row]
                          for row in rows], "labels": canonical_labels}
    encoded = _canonical_json(binding).encode("ascii")
    if len(encoded) > 20_000_000:
        raise ComputationBudgetExceeded("input binding exceeds byte budget")
    digest = hashlib.sha256(encoded).hexdigest()
    midpoint = [[(lo + hi) / 2 for lo, hi in row] for row in rows]
    radius = [[(hi - lo) / 2 for lo, hi in row] for row in rows]
    delta = max(sum(row, Fraction(0)) for row in radius)
    return midpoint, delta, digest


def _eye(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def _shift(matrix, value):
    return [[entry + (value if i == j else 0) for j, entry in enumerate(row)]
            for i, row in enumerate(matrix)]


def _inertia_of_block(block):
    if len(block) == 1:
        value = block[0][0]
        return (int(value < 0), int(value == 0), int(value > 0))
    a, b, d = block[0][0], block[0][1], block[1][1]
    determinant = a * d - b * b
    trace = a + d
    if determinant < 0:
        return (1, 0, 1)
    if determinant > 0:
        if trace == 0:
            raise InvalidInput("impossible real symmetric 2x2 block signs")
        return (2, 0, 0) if trace < 0 else (0, 0, 2)
    if trace < 0:
        return (1, 1, 0)
    if trace > 0:
        return (0, 1, 1)
    return (0, 2, 0)


def _inertia_dict(counts):
    return dict(zip(("negative", "zero", "positive"), counts))


def _congruence(matrix):
    """Producer: exact symmetric elimination, allowing zero-diagonal 2x2 pivots."""
    n = len(matrix)
    schur = [row[:] for row in matrix]
    lower = _eye(n)
    permutation = list(range(n))
    blocks = []
    counts = [0, 0, 0]

    def swap(i, j, completed):
        if i == j:
            return
        schur[i], schur[j] = schur[j], schur[i]
        for row in schur:
            row[i], row[j] = row[j], row[i]
        permutation[i], permutation[j] = permutation[j], permutation[i]
        for col in range(completed):
            lower[i][col], lower[j][col] = lower[j][col], lower[i][col]

    k = 0
    while k < n:
        pivot = next((i for i in range(k, n) if schur[i][i]), None)
        if pivot is not None:
            swap(k, pivot, k)
            block = [[schur[k][k]]]
            size = 1
            for i in range(k + 1, n):
                lower[i][k] = schur[i][k] / block[0][0]
        else:
            pair = next(((i, j) for i in range(k, n) for j in range(i + 1, n)
                         if schur[i][j]), None)
            if pair is None:
                block, size = [[Fraction(0)]], 1
            else:
                swap(k, pair[0], k)
                swap(k + 1, pair[1], k)
                off = schur[k][k + 1]
                block, size = [[Fraction(0), off], [off, Fraction(0)]], 2
                for i in range(k + 2, n):
                    lower[i][k] = schur[i][k + 1] / off
                    lower[i][k + 1] = schur[i][k] / off
        for i in range(k + size, n):
            for j in range(i, n):
                correction = sum(lower[i][k + a] * schur[k + a][j]
                                 for a in range(size))
                schur[i][j] -= correction
                schur[j][i] = schur[i][j]
        blocks.append({"start": k, "size": size,
                       "D": [[_q_text(v) for v in row] for row in block]})
        local_counts = _inertia_of_block(block)
        counts = [x + y for x, y in zip(counts, local_counts)]
        k += size
    return {"permutation": permutation,
            "L": [[_q_text(v) for v in row] for row in lower],
            "blocks": blocks, "inertia": _inertia_dict(counts)}


def _matrix_payload(raw, n, name):
    if type(raw) not in (list, tuple) or len(raw) != n:
        raise InvalidInput(f"{name} dimension mismatch")
    if any(type(row) not in (list, tuple) or len(row) != n for row in raw):
        raise InvalidInput(f"{name} must be square")
    return [[_q(v) for v in row] for row in raw]


def _verify_congruence(matrix, witness):
    """Verifier: reconstruct PLDL^T exactly; does not rerun elimination."""
    n = len(matrix)
    if type(witness) is not dict or set(witness) != {"permutation", "L", "blocks", "inertia"}:
        raise InvalidInput("wrong congruence witness fields")
    permutation = witness["permutation"]
    if (type(permutation) is not list or len(permutation) != n
            or any(type(v) is not int for v in permutation)
            or sorted(permutation) != list(range(n))):
        raise InvalidInput("P must be a genuine permutation")
    lower = _matrix_payload(witness["L"], n, "L")
    if any(lower[i][j] != int(i == j) for i in range(n) for j in range(i, n)):
        raise InvalidInput("L must be unit lower triangular")
    raw_blocks = witness["blocks"]
    if type(raw_blocks) is not list or not 1 <= len(raw_blocks) <= n:
        raise InvalidInput("invalid block list")
    blocks = []
    counts = [0, 0, 0]
    cursor = 0
    for raw in raw_blocks:
        if type(raw) is not dict or set(raw) != {"start", "size", "D"}:
            raise InvalidInput("wrong D-block fields")
        start = _nonnegative_int(raw["start"], "block start")
        size = _nonnegative_int(raw["size"], "block size")
        if start != cursor or size not in (1, 2) or start + size > n:
            raise InvalidInput("D blocks must cover all indices contiguously")
        block = _matrix_payload(raw["D"], size, "D block")
        if size == 2 and block[0][1] != block[1][0]:
            raise InvalidInput("D block must be symmetric")
        blocks.append((start, size, block))
        local_counts = _inertia_of_block(block)
        counts = [x + y for x, y in zip(counts, local_counts)]
        cursor += size
    if cursor != n:
        raise InvalidInput("D does not cover the full matrix")
    reported = witness["inertia"]
    if type(reported) is not dict or set(reported) != {"negative", "zero", "positive"}:
        raise InvalidInput("wrong inertia fields")
    for key, value in reported.items():
        _nonnegative_int(value, key)
    if reported != _inertia_dict(counts):
        raise InvalidInput("reported D-block signs do not match exact signs")
    # Independent multiplication by blocks avoids constructing any inverse.
    # Unit lower triangular L and permutation P are both provably invertible.
    for i in range(n):
        for j in range(i, n):
            reconstructed = Fraction(0)
            for start, size, block in blocks:
                for a in range(size):
                    for b in range(size):
                        reconstructed += lower[i][start + a] * block[a][b] * lower[j][start + b]
            if reconstructed != matrix[permutation[i]][permutation[j]]:
                raise InvalidInput("exact P/L/D congruence identity failed")
    return _inertia_dict(counts)


def certify_interval_inertia(bounds, labels, *, max_dimension=64):
    """Construct then independently verify a negative-inertia family certificate.

    Invalid input raises InvalidInput; explicit size exhaustion raises
    ComputationBudgetExceeded. UNDETERMINED is mathematical inconclusiveness,
    never a synonym for either malformed input or resource exhaustion.
    """
    midpoint, delta, digest = _input(bounds, labels, max_dimension)
    minus = _congruence(_shift(midpoint, -delta))
    plus = _congruence(_shift(midpoint, delta))
    q_minus, q_plus = minus["inertia"]["negative"], plus["inertia"]["negative"]
    status = "CERTIFIED" if q_minus == q_plus else "UNDETERMINED"
    certificate = {"schema": SCHEMA, "dimension": len(midpoint),
                   "input_sha256": digest, "delta": _q_text(delta),
                   "minus": minus, "plus": plus, "status": status,
                   "negative_count": q_minus if status == "CERTIFIED" else None}
    result = verify_interval_inertia(bounds, labels, certificate, max_dimension=max_dimension)
    if result["status"] == "INVALID_CERTIFICATE":
        raise ArithmeticError("generated certificate failed independent verification: " + result["reason"])
    if not result["verification_complete"]:
        raise ComputationBudgetExceeded(result["reason"])
    return certificate


def verify_interval_inertia(bounds, labels, certificate, *, max_dimension=64):
    """Verify original-input binding, endpoint congruences and inertia conclusion.

    The verifier checks an explicit witness instead of trusting any status or
    rerunning the producing elimination. It makes no Weil-object claim.
    """
    try:
        midpoint, delta, digest = _input(bounds, labels, max_dimension)
        fields = {"schema", "dimension", "input_sha256", "delta", "minus", "plus",
                  "status", "negative_count"}
        if type(certificate) is not dict or set(certificate) != fields:
            raise InvalidInput("wrong certificate fields")
        if certificate["schema"] != SCHEMA:
            raise InvalidInput("unknown certificate schema")
        if type(certificate["dimension"]) is not int or certificate["dimension"] != len(midpoint):
            raise InvalidInput("certificate dimension mismatch")
        if certificate["input_sha256"] != digest:
            raise InvalidInput("certificate is not bound to these bounds and labels")
        if _q(certificate["delta"]) != delta:
            raise InvalidInput("delta is not the exact radius maximum row sum")
        minus = _verify_congruence(_shift(midpoint, -delta), certificate["minus"])
        plus = _verify_congruence(_shift(midpoint, delta), certificate["plus"])
        lower, upper = plus["negative"], minus["negative"]
        if lower > upper:
            raise InvalidInput("endpoint inertia contradicts Loewner ordering")
        expected_status = "CERTIFIED" if lower == upper else "UNDETERMINED"
        expected_count = lower if lower == upper else None
        if certificate["status"] != expected_status:
            raise InvalidInput("reported status contradicts verified endpoint inertias")
        reported_count = certificate["negative_count"]
        if expected_count is not None:
            _nonnegative_int(reported_count, "negative_count")
        if reported_count != expected_count:
            raise InvalidInput("reported negative count contradicts verified endpoint inertias")
        return {"status": expected_status, "negative_count": expected_count,
                "negative_count_bounds": [lower, upper], "reason": "verified exact interval-family witness",
                "scope": SCOPE, "verification_complete": True}
    except ComputationBudgetExceeded as error:
        return {"status": "UNDETERMINED", "negative_count": None,
                "negative_count_bounds": None, "reason": "verification budget incomplete: " + str(error),
                "scope": SCOPE, "verification_complete": False}
    except (ValueError, TypeError, KeyError, IndexError, OverflowError, RecursionError) as error:
        return {"status": "INVALID_CERTIFICATE", "negative_count": None,
                "negative_count_bounds": None, "reason": str(error), "scope": SCOPE,
                "verification_complete": False}


# Short aliases agreed with the independent producer.
certify = certify_interval_inertia
verify = verify_interval_inertia
