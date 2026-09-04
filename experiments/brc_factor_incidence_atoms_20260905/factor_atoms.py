"""Reference-grade BRC common valuation atoms; exact rational coefficients only.

No irreducible factorization, root approximation, or subset enumeration occurs
in compile_atoms. A backend is explicitly selected before use. The repository
backend reuses its existing polynomial/Sturm kernel; the pinned backend is a
standalone transcription of the same pure source functions, not package CI.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from importlib import import_module
from typing import Iterable

Q = Fraction
Poly = tuple[Q, ...]
ONE: Poly = (Q(1),)
ZERO: Poly = (Q(0),)
K = None
BACKEND = "UNSELECTED"

def select_backend(name: str) -> None:
    global K, BACKEND
    if name == "repository":
        K = import_module("enterprise_math.brc_critical_degeneracy")
        BACKEND = "REPOSITORY_PACKAGE"
    elif name == "pinned":
        K = import_module("pinned_polynomial_kernel")
        BACKEND = "PINNED_PURE_FUNCTION_TRANSCRIPTION"
    else:
        raise ValueError("backend must be repository or pinned")

def checked_poly(values: Iterable[int | Q]) -> Poly:
    if K is None:
        raise RuntimeError("select_backend('pinned' or 'repository') first")
    raw = tuple(values)
    if not raw:
        raise ValueError("empty polynomial coefficient sequence")
    if any(isinstance(x, bool) or not isinstance(x, (int, Q)) for x in raw):
        raise TypeError("coefficients must be integers or Fractions, not floats/bools")
    out = K._trim(tuple(Q(x) for x in raw))
    if out == ZERO:
        raise ValueError("zero polynomial has no finite root-support certificate")
    return out

def ppow(poly: Poly, exponent: int) -> Poly:
    if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 0:
        raise ValueError("exponent must be a nonnegative integer")
    out = ONE
    base = poly
    while exponent:
        if exponent & 1:
            out = K._p_mul(out, base)
        exponent //= 2
        if exponent:
            base = K._p_mul(base, base)
    return out

@dataclass(frozen=True)
class Atom:
    profile: tuple[int, ...]
    polynomial: Poly

@dataclass(frozen=True)
class Certificate:
    scalars: tuple[Q, ...]
    atoms: tuple[Atom, ...]
    total_input_degree: int
    squarefree_layers: int
    refinement_gcd_calls: int

def squarefree_layers(poly: Poly) -> tuple[tuple[int, Poly], ...]:
    """Characteristic-zero squarefree layers, using only gcd/exact division."""
    f = K._p_monic(poly)
    if len(f) <= 1:
        return ()
    c = K._p_gcd(f, K._p_derivative(f))
    w = K._p_div_exact(f, c)
    exponent = 1
    layers = []
    while w != ONE:
        y = K._p_gcd(w, c)
        z = K._p_div_exact(w, y)
        if z != ONE:
            layers.append((exponent, z))
        w = y
        c = K._p_div_exact(c, y)
        exponent += 1
    if c != ONE:
        raise AssertionError("characteristic-zero squarefree decomposition failed")
    return tuple(layers)

def compile_atoms(factors: Iterable[Iterable[int | Q]]) -> Certificate:
    factors = tuple(checked_poly(f) for f in factors)
    n = len(factors)
    atoms: list[Atom] = []
    calls = layer_count = 0
    for index, f in enumerate(factors):
        for exponent, layer in squarefree_layers(f):
            layer_count += 1
            residual = layer
            refined = []
            for atom in atoms:
                calls += 1
                common = K._p_gcd(atom.polynomial, residual)
                outside = K._p_div_exact(atom.polynomial, common)
                if outside != ONE:
                    refined.append(Atom(atom.profile, outside))
                if common != ONE:
                    if atom.profile[index] != 0:
                        raise AssertionError("distinct squarefree layers overlapped")
                    profile = list(atom.profile)
                    profile[index] = exponent
                    refined.append(Atom(tuple(profile), common))
                    residual = K._p_div_exact(residual, common)
            if residual != ONE:
                profile = [0] * n
                profile[index] = exponent
                refined.append(Atom(tuple(profile), residual))
            grouped: dict[tuple[int, ...], Poly] = {}
            for atom in refined:
                grouped[atom.profile] = K._p_mul(grouped.get(atom.profile, ONE), atom.polynomial)
            atoms = [Atom(v, g) for v, g in sorted(grouped.items())]
    return Certificate(
        tuple(f[-1] for f in factors), tuple(atoms),
        sum(len(f) - 1 for f in factors), layer_count, calls,
    )

def verify_certificate(factors: Iterable[Iterable[int | Q]], cert: Certificate) -> bool:
    """Independent structural verification; no trust in the compiler counters."""
    factors = tuple(checked_poly(f) for f in factors)
    n = len(factors)
    if len(cert.scalars) != n or any(c == 0 for c in cert.scalars):
        return False
    seen = set()
    for j, atom in enumerate(cert.atoms):
        v, g = atom.profile, atom.polynomial
        if len(v) != n or any(isinstance(a, bool) or not isinstance(a, int) or a < 0 for a in v):
            return False
        if not any(v) or v in seen:
            return False
        seen.add(v)
        if len(g) <= 1 or g[-1] != 1 or K._trim(g) != g:
            return False
        if K._p_gcd(g, K._p_derivative(g)) != ONE:
            return False
        if any(K._p_gcd(g, previous.polynomial) != ONE for previous in cert.atoms[:j]):
            return False
    for i, factor in enumerate(factors):
        recovered = (cert.scalars[i],)
        for atom in cert.atoms:
            recovered = K._p_mul(recovered, ppow(atom.polynomial, atom.profile[i]))
        if recovered != factor:
            return False
    return True

def root_count(poly: Poly, left: int | Q, right: int | Q) -> int:
    """Existing endpoint deflation plus squarefree Sturm open-interval law."""
    for endpoint in (left, right):
        if isinstance(endpoint, bool) or not isinstance(endpoint, (int, Q)):
            raise TypeError("endpoints must be exact rational numbers")
    left, right = Q(left), Q(right)
    if not left < right:
        raise ValueError("left endpoint must be below right endpoint")
    out = checked_poly(poly)
    for endpoint in (left, right):
        linear = (-endpoint, Q(1))
        while len(out) > 1 and K._p_eval(out, endpoint) == 0:
            out = K._p_div_exact(out, linear)
    if len(out) <= 1:
        return 0
    g = K._p_gcd(out, K._p_derivative(out))
    out = K._p_div_exact(out, g)
    return K._root_count(K._sturm_sequence(out), left, right)

def atom_counts(cert: Certificate, left: int | Q, right: int | Q) -> tuple[int, ...]:
    # Validate the interval even when the certificate has no atoms.
    root_count(ONE, left, right)
    return tuple(root_count(a.polynomial, left, right) for a in cert.atoms)

def observe(cert: Certificate, counts: tuple[int, ...], weights: Iterable[int]) -> tuple[bool, int, int]:
    w = tuple(weights)
    if len(w) != len(cert.scalars) or len(counts) != len(cert.atoms):
        raise ValueError("observer dimensions do not match certificate")
    if any(isinstance(x, bool) or not isinstance(x, int) or x < 0 for x in w + counts):
        raise ValueError("weights and certified counts must be nonnegative integers")
    distinct = multiplicity = 0
    for atom, count in zip(cert.atoms, counts):
        exponent = sum(a * b for a, b in zip(atom.profile, w))
        if exponent:
            distinct += count
            multiplicity += exponent * count
    return distinct == 0, distinct, multiplicity

def support_histogram(cert: Certificate, counts: tuple[int, ...]) -> dict[int, int]:
    if len(counts) != len(cert.atoms):
        raise ValueError("count dimension mismatch")
    out: dict[int, int] = {}
    for atom, count in zip(cert.atoms, counts):
        if count:
            mask = sum(1 << i for i, a in enumerate(atom.profile) if a)
            out[mask] = out.get(mask, 0) + count
    return out

def failing_factors(cert: Certificate, counts: tuple[int, ...]) -> tuple[int, ...]:
    if len(counts) != len(cert.atoms):
        raise ValueError("count dimension mismatch")
    return tuple(i for i in range(len(cert.scalars))
                 if any(c > 0 and a.profile[i] > 0 for a, c in zip(cert.atoms, counts)))


def minimal_count_signature(cert: Certificate, counts: tuple[int, ...]):
    """Minimal joint distinct/multiplicity signature for fixed-I monomial queries.

    The support histogram is necessary for all activation subsets; the vector
    of per-factor multiplicity counts is necessary for all nonnegative weights.
    Full valuation-atom counts can be strictly more information than this.
    """
    if len(counts) != len(cert.atoms):
        raise ValueError("count dimension mismatch")
    support = tuple(sorted(support_histogram(cert, counts).items()))
    multiplicities = tuple(sum(a.profile[i] * c for a, c in zip(cert.atoms, counts))
                           for i in range(len(cert.scalars)))
    return support, multiplicities


def monomial_pushforward(cert: Certificate, columns, counts=None):
    """Compile H_j=product_i F_i**columns[j][i], with NO gcd or root count.

    Optional certified interval counts are pushed forward by addition. Polynomial
    blocks with identical nonzero transformed profiles merge. Zero profiles drop.
    Algebraic scalar units are retained; negative exponents/additive polynomial
    operations are outside this exact input contract.
    """
    columns = tuple(tuple(column) for column in columns)
    n = len(cert.scalars)
    if any(len(column) != n for column in columns):
        raise ValueError("column length must match source factor count")
    if any(isinstance(x, bool) or not isinstance(x, int) or x < 0
           for column in columns for x in column):
        raise ValueError("monomial exponents must be nonnegative integers")
    if counts is not None:
        counts = tuple(counts)
        if len(counts) != len(cert.atoms) or any(isinstance(x, bool) or not isinstance(x,int) or x < 0 for x in counts):
            raise ValueError("invalid certified atom counts")
    scalars = []
    for column in columns:
        scalar = Q(1)
        for c,e in zip(cert.scalars,column):
            scalar *= c ** e
        scalars.append(scalar)
    grouped = {}
    merged_counts = {}
    for j, atom in enumerate(cert.atoms):
        v = tuple(sum(e * a for e,a in zip(column,atom.profile)) for column in columns)
        if not any(v):
            continue
        grouped[v] = K._p_mul(grouped.get(v,ONE),atom.polynomial)
        if counts is not None:
            merged_counts[v] = merged_counts.get(v,0) + counts[j]
    atoms = tuple(Atom(v,g) for v,g in sorted(grouped.items()))
    total_degree = sum(sum(a.profile) * (len(a.polynomial)-1) for a in atoms)
    result = Certificate(tuple(scalars),atoms,total_degree,0,0)
    transported = None if counts is None else tuple(merged_counts[a.profile] for a in atoms)
    return result,transported
