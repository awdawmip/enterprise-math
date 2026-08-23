"""Exact finite algebraic Morse cancellation for Enterprise Math.

This module deliberately accepts only finite *graded chain complexes* with an
explicit boundary operator.  A graph is used only as a derived obstruction
checker for closed gradient paths; arbitrary graph-node deletion is out of
scope.

Supported coefficient domains:
- Z: elementary cancellation only across incidence units +1/-1.
- Q: any non-zero incidence coefficient is cancellable, with a field-only
  marker when the pivot is not an integral unit.

The reduction returns an exact strong-deformation-retract certificate
(P, I, H) with

    P I = id_M,
    I P = id_C - d H - H d,

and chain-map identities.  All arithmetic uses fractions.Fraction.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, Iterable, List, Mapping, MutableMapping, Optional, Sequence, Tuple

Coeff = Fraction
Vector = Dict[str, Coeff]
LinearMap = Dict[str, Vector]


class MorseError(ValueError):
    """Base class for exact Morse-reduction failures."""


class ChainComplexError(MorseError):
    pass


class MatchingError(MorseError):
    pass


class CyclicMatchingError(MatchingError):
    def __init__(self, cycle: Sequence[str]):
        self.cycle = tuple(cycle)
        super().__init__("closed gradient path: " + " -> ".join(self.cycle))


class NonUnitIncidenceError(MatchingError):
    pass


class CertificateError(MorseError):
    pass


def _q(value) -> Coeff:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value, 1)
    if isinstance(value, str):
        return Fraction(value)
    if isinstance(value, (tuple, list)) and len(value) == 2:
        return Fraction(int(value[0]), int(value[1]))
    raise TypeError(f"unsupported exact coefficient {value!r}")


def _clean(v: Mapping[str, Coeff]) -> Vector:
    return {k: _q(c) for k, c in v.items() if _q(c) != 0}


def _vadd(*vectors: Mapping[str, Coeff]) -> Vector:
    out: Vector = {}
    for v in vectors:
        for k, c in v.items():
            out[k] = out.get(k, Fraction(0)) + _q(c)
            if out[k] == 0:
                del out[k]
    return out


def _vscale(v: Mapping[str, Coeff], scalar: Coeff) -> Vector:
    scalar = _q(scalar)
    if scalar == 0:
        return {}
    return _clean({k: scalar * _q(c) for k, c in v.items()})


def _basis_vector(name: str, coefficient: Coeff = Fraction(1)) -> Vector:
    coefficient = _q(coefficient)
    return {} if coefficient == 0 else {name: coefficient}


def apply_linear_map(linear_map: Mapping[str, Mapping[str, Coeff]], vector: Mapping[str, Coeff]) -> Vector:
    out: Vector = {}
    for source, c in vector.items():
        if source not in linear_map:
            raise CertificateError(f"linear map missing source generator {source!r}")
        out = _vadd(out, _vscale(linear_map[source], _q(c)))
    return out


def compose_linear_maps(second: Mapping[str, Mapping[str, Coeff]], first: Mapping[str, Mapping[str, Coeff]]) -> LinearMap:
    """Return second o first."""
    return {s: apply_linear_map(second, v) for s, v in first.items()}


def add_linear_maps(*maps: Mapping[str, Mapping[str, Coeff]]) -> LinearMap:
    if not maps:
        return {}
    keys = set(maps[0])
    if any(set(m) != keys for m in maps[1:]):
        raise CertificateError("linear-map source domains differ")
    return {s: _vadd(*(m[s] for m in maps)) for s in sorted(keys)}


def identity_map(generators: Iterable[str]) -> LinearMap:
    return {g: {g: Fraction(1)} for g in generators}


def _map_equal(left: Mapping[str, Mapping[str, Coeff]], right: Mapping[str, Mapping[str, Coeff]]) -> bool:
    if set(left) != set(right):
        return False
    return all(_clean(left[k]) == _clean(right[k]) for k in left)


def _coeff_json(c: Coeff):
    c = _q(c)
    return c.numerator if c.denominator == 1 else f"{c.numerator}/{c.denominator}"


def _vector_json(v: Mapping[str, Coeff]):
    return {k: _coeff_json(v[k]) for k in sorted(v) if _q(v[k]) != 0}


def _map_json(m: Mapping[str, Mapping[str, Coeff]]):
    return {k: _vector_json(m[k]) for k in sorted(m)}


@dataclass(frozen=True)
class MatchingPair:
    lower: str
    upper: str

    @classmethod
    def from_obj(cls, obj) -> "MatchingPair":
        if isinstance(obj, cls):
            return obj
        if isinstance(obj, Mapping):
            return cls(lower=str(obj["lower"]), upper=str(obj["upper"]))
        if isinstance(obj, (tuple, list)) and len(obj) == 2:
            return cls(lower=str(obj[0]), upper=str(obj[1]))
        raise MatchingError(f"invalid matching pair {obj!r}")

    def to_dict(self):
        return {"lower": self.lower, "upper": self.upper}


@dataclass(frozen=True)
class FiniteChainComplex:
    ring: str
    basis_by_degree: Mapping[int, Tuple[str, ...]]
    boundary: Mapping[str, Vector]

    def __post_init__(self):
        ring = str(self.ring).upper()
        if ring not in {"Z", "Q"}:
            raise ChainComplexError("supported rings are exactly Z and Q")
        object.__setattr__(self, "ring", ring)

        normalized_basis: Dict[int, Tuple[str, ...]] = {}
        seen = set()
        for raw_k, raw_basis in self.basis_by_degree.items():
            k = int(raw_k)
            basis = tuple(str(x) for x in raw_basis)
            if len(set(basis)) != len(basis):
                raise ChainComplexError(f"duplicate generator within degree {k}")
            overlap = seen.intersection(basis)
            if overlap:
                raise ChainComplexError(f"generator appears in multiple degrees: {sorted(overlap)!r}")
            seen.update(basis)
            normalized_basis[k] = basis
        object.__setattr__(self, "basis_by_degree", dict(sorted(normalized_basis.items())))

        normalized_boundary: Dict[str, Vector] = {}
        for g in seen:
            raw = self.boundary.get(g, {})
            if not isinstance(raw, Mapping):
                raise ChainComplexError(f"boundary[{g!r}] is not a mapping")
            v = {str(h): _q(c) for h, c in raw.items() if _q(c) != 0}
            if ring == "Z" and any(c.denominator != 1 for c in v.values()):
                raise ChainComplexError("Z complex contains a nonintegral coefficient")
            normalized_boundary[g] = v
        extra = set(self.boundary).difference(seen)
        if extra:
            raise ChainComplexError(f"boundary supplied for unknown generators: {sorted(extra)!r}")
        object.__setattr__(self, "boundary", normalized_boundary)
        self.validate()

    @classmethod
    def from_dict(cls, obj: Mapping) -> "FiniteChainComplex":
        required = {"ring", "basis_by_degree", "boundary"}
        if not isinstance(obj, Mapping) or not required.issubset(obj):
            raise ChainComplexError(
                "finite chain complex requires ring, basis_by_degree, and boundary; arbitrary graph payloads are not accepted"
            )
        basis = {int(k): tuple(v) for k, v in obj["basis_by_degree"].items()}
        return cls(ring=obj["ring"], basis_by_degree=basis, boundary=obj["boundary"])

    @property
    def generators(self) -> Tuple[str, ...]:
        return tuple(g for k in sorted(self.basis_by_degree) for g in self.basis_by_degree[k])

    @property
    def degree(self) -> Dict[str, int]:
        return {g: k for k, basis in self.basis_by_degree.items() for g in basis}

    def validate(self) -> None:
        deg = self.degree
        gens = set(deg)
        for upper in self.generators:
            for lower, coefficient in self.boundary[upper].items():
                if lower not in gens:
                    raise ChainComplexError(f"boundary of {upper!r} references unknown generator {lower!r}")
                if deg[lower] != deg[upper] - 1:
                    raise ChainComplexError(
                        f"boundary must lower degree by exactly one: {upper!r}({deg[upper]}) -> {lower!r}({deg[lower]})"
                    )
                if coefficient == 0:
                    raise ChainComplexError("zero coefficient survived normalization")
        for g in self.generators:
            d2 = self.d_vector(self.boundary[g])
            if d2:
                raise ChainComplexError(f"d^2 != 0 on {g!r}: {d2!r}")

    def d_vector(self, vector: Mapping[str, Coeff]) -> Vector:
        out: Vector = {}
        for g, c in vector.items():
            if g not in self.boundary:
                raise ChainComplexError(f"unknown generator in vector: {g!r}")
            out = _vadd(out, _vscale(self.boundary[g], c))
        return out

    def boundary_map(self) -> LinearMap:
        return {g: dict(self.boundary[g]) for g in self.generators}

    def to_dict(self):
        return {
            "ring": self.ring,
            "basis_by_degree": {str(k): list(v) for k, v in self.basis_by_degree.items()},
            "boundary": {g: _vector_json(self.boundary[g]) for g in self.generators},
        }


@dataclass(frozen=True)
class CancellationStep:
    lower: str
    upper: str
    pivot: Coeff
    field_only: bool
    before_count: int
    after_count: int

    def to_dict(self):
        return {
            "lower": self.lower,
            "upper": self.upper,
            "pivot": _coeff_json(self.pivot),
            "field_only": self.field_only,
            "before_count": self.before_count,
            "after_count": self.after_count,
        }


@dataclass(frozen=True)
class MorseReductionCertificate:
    source: FiniteChainComplex
    reduced: FiniteChainComplex
    matching: Tuple[MatchingPair, ...]
    cancellation_order: Tuple[MatchingPair, ...]
    critical_generators: Tuple[str, ...]
    projection: LinearMap
    lift: LinearMap
    homotopy: LinearMap
    steps: Tuple[CancellationStep, ...]
    field_only: bool

    def to_dict(self):
        return {
            "source": self.source.to_dict(),
            "reduced": self.reduced.to_dict(),
            "matching": [p.to_dict() for p in self.matching],
            "cancellation_order": [p.to_dict() for p in self.cancellation_order],
            "critical_generators": list(self.critical_generators),
            "projection": _map_json(self.projection),
            "lift": _map_json(self.lift),
            "homotopy": _map_json(self.homotopy),
            "steps": [s.to_dict() for s in self.steps],
            "field_only": self.field_only,
        }

    @classmethod
    def from_dict(cls, obj: Mapping) -> "MorseReductionCertificate":
        try:
            source = FiniteChainComplex.from_dict(obj["source"])
            reduced = FiniteChainComplex.from_dict(obj["reduced"])
            matching = tuple(MatchingPair.from_obj(x) for x in obj["matching"])
            order = tuple(MatchingPair.from_obj(x) for x in obj["cancellation_order"])
            projection = {str(k): _clean(v) for k, v in obj["projection"].items()}
            lift = {str(k): _clean(v) for k, v in obj["lift"].items()}
            homotopy = {str(k): _clean(v) for k, v in obj["homotopy"].items()}
            steps = tuple(
                CancellationStep(
                    lower=str(s["lower"]),
                    upper=str(s["upper"]),
                    pivot=_q(s["pivot"]),
                    field_only=bool(s["field_only"]),
                    before_count=int(s["before_count"]),
                    after_count=int(s["after_count"]),
                )
                for s in obj["steps"]
            )
            return cls(
                source=source,
                reduced=reduced,
                matching=matching,
                cancellation_order=order,
                critical_generators=tuple(str(x) for x in obj["critical_generators"]),
                projection=projection,
                lift=lift,
                homotopy=homotopy,
                steps=steps,
                field_only=bool(obj["field_only"]),
            )
        except (KeyError, TypeError, ValueError, ChainComplexError) as exc:
            raise CertificateError(f"malformed certificate: {exc}") from exc


def validate_matching(complex_: FiniteChainComplex, matching: Sequence[MatchingPair]) -> Tuple[MatchingPair, ...]:
    pairs = tuple(MatchingPair.from_obj(p) for p in matching)
    deg = complex_.degree
    used = set()
    for p in pairs:
        if p.lower not in deg or p.upper not in deg:
            raise MatchingError(f"unknown matched generator in {p!r}")
        if deg[p.upper] != deg[p.lower] + 1:
            raise MatchingError(f"matched pair is not adjacent-grade: {p!r}")
        pivot = complex_.boundary[p.upper].get(p.lower, Fraction(0))
        if pivot == 0:
            raise MatchingError(f"matched incidence is zero: {p!r}")
        if p.lower in used or p.upper in used:
            raise MatchingError(f"generator used in more than one matching pair: {p!r}")
        used.add(p.lower)
        used.add(p.upper)
        if complex_.ring == "Z" and pivot not in {Fraction(1), Fraction(-1)}:
            raise NonUnitIncidenceError(
                f"integer cancellation requires unit incidence +/-1; {p.upper}->{p.lower} has {pivot}"
            )
    cycle = closed_gradient_cycle(complex_, pairs)
    if cycle is not None:
        raise CyclicMatchingError(cycle)
    return pairs


def matching_dependency_graph(complex_: FiniteChainComplex, matching: Sequence[MatchingPair]) -> Dict[int, Tuple[int, ...]]:
    pairs = tuple(matching)
    lower_to_pair = {p.lower: i for i, p in enumerate(pairs)}
    graph: Dict[int, Tuple[int, ...]] = {}
    for i, p in enumerate(pairs):
        targets = []
        for lower, coefficient in complex_.boundary[p.upper].items():
            if coefficient == 0 or lower == p.lower:
                continue
            j = lower_to_pair.get(lower)
            if j is not None and j != i:
                targets.append(j)
        graph[i] = tuple(sorted(set(targets)))
    return graph


def closed_gradient_cycle(complex_: FiniteChainComplex, matching: Sequence[MatchingPair]) -> Optional[Tuple[str, ...]]:
    pairs = tuple(matching)
    graph = matching_dependency_graph(complex_, pairs)
    color = {i: 0 for i in range(len(pairs))}
    stack: List[int] = []
    position: Dict[int, int] = {}

    def dfs(i: int) -> Optional[Tuple[int, ...]]:
        color[i] = 1
        position[i] = len(stack)
        stack.append(i)
        for j in graph[i]:
            if color[j] == 0:
                found = dfs(j)
                if found is not None:
                    return found
            elif color[j] == 1:
                start = position[j]
                return tuple(stack[start:] + [j])
        stack.pop()
        position.pop(i, None)
        color[i] = 2
        return None

    for i in range(len(pairs)):
        if color[i] == 0:
            cycle = dfs(i)
            if cycle is not None:
                # Expand pair-cycle into an explicit V-path witness:
                # lower_i -> upper_i -> lower_j -> upper_j -> ... -> lower_i.
                witness: List[str] = []
                for index in cycle[:-1]:
                    witness.extend([pairs[index].lower, pairs[index].upper])
                witness.append(pairs[cycle[0]].lower)
                return tuple(witness)
    return None


def cancellation_order(complex_: FiniteChainComplex, matching: Sequence[MatchingPair]) -> Tuple[MatchingPair, ...]:
    pairs = tuple(matching)
    graph = {i: set(v) for i, v in matching_dependency_graph(complex_, pairs).items()}
    remaining = set(graph)
    order: List[int] = []
    while remaining:
        sinks = sorted(i for i in remaining if not (graph[i] & remaining))
        if not sinks:
            cycle = closed_gradient_cycle(complex_, pairs)
            raise CyclicMatchingError(cycle or ("<unknown-cycle>",))
        i = sinks[0]
        order.append(i)
        remaining.remove(i)
    return tuple(pairs[i] for i in order)


def _elementary_cancel(
    complex_: FiniteChainComplex, pair: MatchingPair
) -> Tuple[FiniteChainComplex, LinearMap, LinearMap, LinearMap, CancellationStep]:
    deg = complex_.degree
    a, b = pair.lower, pair.upper
    if a not in deg or b not in deg:
        raise MatchingError("matched pair is no longer present during cancellation")
    pivot = complex_.boundary[b].get(a, Fraction(0))
    if pivot == 0:
        raise MatchingError("matched pivot vanished during cancellation")
    if complex_.ring == "Z" and pivot not in {Fraction(1), Fraction(-1)}:
        raise NonUnitIncidenceError(f"nonunit pivot {pivot} encountered over Z")
    inverse = Fraction(1, 1) / pivot
    survivors = tuple(g for g in complex_.generators if g not in {a, b})
    survivor_set = set(survivors)

    # h(a)=u^-1 b, h(other)=0 on the current complex.
    h: LinearMap = {g: {} for g in complex_.generators}
    h[a] = {b: inverse}

    # p=q(Id-dh): p(a)=-u^-1*(d b - u a), p(b)=0, others=id.
    remainder = dict(complex_.boundary[b])
    remainder.pop(a, None)
    p: LinearMap = {}
    for g in complex_.generators:
        if g == a:
            p[g] = _vscale(remainder, -inverse)
        elif g == b:
            p[g] = {}
        else:
            p[g] = {g: Fraction(1)}

    # i=(Id-hd)j: i(x)=x-u^-1*[a](d x)b when degree(x)=degree(b).
    i_map: LinearMap = {}
    for g in survivors:
        correction = Fraction(0)
        if deg[g] == deg[b]:
            correction = complex_.boundary[g].get(a, Fraction(0)) * inverse
        i_map[g] = _vadd({g: Fraction(1)}, ({b: -correction} if correction else {}))

    new_basis = {
        k: tuple(g for g in basis if g in survivor_set)
        for k, basis in complex_.basis_by_degree.items()
        if any(g in survivor_set for g in basis)
    }
    new_boundary: Dict[str, Vector] = {}
    for g in survivors:
        new_boundary[g] = apply_linear_map(p, complex_.d_vector(i_map[g]))
    reduced = FiniteChainComplex(complex_.ring, new_basis, new_boundary)
    step = CancellationStep(
        lower=a,
        upper=b,
        pivot=pivot,
        field_only=(complex_.ring == "Q" and pivot not in {Fraction(1), Fraction(-1)}),
        before_count=len(complex_.generators),
        after_count=len(reduced.generators),
    )
    return reduced, p, i_map, h, step


def morse_reduce(complex_: FiniteChainComplex, matching: Sequence[MatchingPair]) -> MorseReductionCertificate:
    pairs = validate_matching(complex_, matching)
    order = cancellation_order(complex_, pairs)
    original = complex_
    current = complex_

    P: LinearMap = identity_map(original.generators)  # original -> current
    I: LinearMap = identity_map(original.generators)  # current -> original
    H: LinearMap = {g: {} for g in original.generators}  # original -> original[+1]
    steps: List[CancellationStep] = []

    for pair in order:
        reduced, p, i_map, h, step = _elementary_cancel(current, pair)
        # H_new = H_old + I_old h P_old
        ihp = compose_linear_maps(I, compose_linear_maps(h, P))
        H = add_linear_maps(H, ihp)
        P = compose_linear_maps(p, P)
        I = compose_linear_maps(I, i_map)
        current = reduced
        steps.append(step)

    matched = {x for p in pairs for x in (p.lower, p.upper)}
    critical = tuple(g for g in original.generators if g not in matched)
    cert = MorseReductionCertificate(
        source=original,
        reduced=current,
        matching=pairs,
        cancellation_order=order,
        critical_generators=critical,
        projection=P,
        lift=I,
        homotopy=H,
        steps=tuple(steps),
        field_only=any(s.field_only for s in steps),
    )
    verify_certificate(cert)
    return cert


def _verify_map_domains(cert: MorseReductionCertificate) -> None:
    source = set(cert.source.generators)
    reduced = set(cert.reduced.generators)
    if set(cert.projection) != source:
        raise CertificateError("projection source domain is not the source complex basis")
    if set(cert.homotopy) != source:
        raise CertificateError("homotopy source domain is not the source complex basis")
    if set(cert.lift) != reduced:
        raise CertificateError("lift source domain is not the reduced complex basis")
    for name, mapping, target in (
        ("projection", cert.projection, reduced),
        ("lift", cert.lift, source),
        ("homotopy", cert.homotopy, source),
    ):
        for s, v in mapping.items():
            bad = set(v).difference(target)
            if bad:
                raise CertificateError(f"{name}[{s!r}] references generators outside target basis: {sorted(bad)!r}")
            if cert.source.ring == "Z" and any(_q(c).denominator != 1 for c in v.values()):
                raise CertificateError(f"{name} contains nonintegral coefficient in Z certificate")


def verify_certificate(cert: MorseReductionCertificate) -> bool:
    cert.source.validate()
    cert.reduced.validate()
    pairs = validate_matching(cert.source, cert.matching)
    expected_order = cancellation_order(cert.source, pairs)
    if tuple(cert.cancellation_order) != expected_order:
        raise CertificateError("cancellation order is not the deterministic acyclic sink order")
    expected_critical = tuple(
        g for g in cert.source.generators if g not in {x for p in pairs for x in (p.lower, p.upper)}
    )
    if tuple(cert.critical_generators) != expected_critical:
        raise CertificateError("critical generator set/order is malformed")
    if tuple(cert.reduced.generators) != expected_critical:
        raise CertificateError("reduced basis is not exactly the critical-generator basis")
    if len(cert.steps) != len(pairs):
        raise CertificateError("cancellation trace length mismatch")
    if cert.field_only != any(s.field_only for s in cert.steps):
        raise CertificateError("field_only marker mismatch")
    _verify_map_domains(cert)

    dC = cert.source.boundary_map()
    dM = cert.reduced.boundary_map()

    # P d_C = d_M P and d_C I = I d_M.
    if not _map_equal(compose_linear_maps(cert.projection, dC), compose_linear_maps(dM, cert.projection)):
        raise CertificateError("projection is not a chain map")
    if not _map_equal(compose_linear_maps(dC, cert.lift), compose_linear_maps(cert.lift, dM)):
        raise CertificateError("lift is not a chain map")

    # P I = id_M.
    if not _map_equal(compose_linear_maps(cert.projection, cert.lift), identity_map(cert.reduced.generators)):
        raise CertificateError("projection/lift do not satisfy P I = id")

    # I P = id_C - dH - Hd  <=>  IP + dH + Hd = id_C.
    ip = compose_linear_maps(cert.lift, cert.projection)
    dh = compose_linear_maps(dC, cert.homotopy)
    hd = compose_linear_maps(cert.homotopy, dC)
    if not _map_equal(add_linear_maps(ip, dh, hd), identity_map(cert.source.generators)):
        raise CertificateError("chain-homotopy identity I P + dH + Hd = id failed")

    # Recompute reduction independently from the cancellation steps enough to
    # reject forged reduced boundaries/maps: replay exact elementary steps.
    current = cert.source
    P: LinearMap = identity_map(current.generators)
    I: LinearMap = identity_map(current.generators)
    H: LinearMap = {g: {} for g in current.generators}
    replay_steps: List[CancellationStep] = []
    for pair in expected_order:
        next_complex, p, i_map, h, step = _elementary_cancel(current, pair)
        H = add_linear_maps(H, compose_linear_maps(I, compose_linear_maps(h, P)))
        P = compose_linear_maps(p, P)
        I = compose_linear_maps(I, i_map)
        current = next_complex
        replay_steps.append(step)
    if current.to_dict() != cert.reduced.to_dict():
        raise CertificateError("reduced complex does not equal exact cancellation replay")
    if not _map_equal(P, cert.projection) or not _map_equal(I, cert.lift) or not _map_equal(H, cert.homotopy):
        raise CertificateError("certificate maps do not equal exact cancellation replay")
    if tuple(replay_steps) != tuple(cert.steps):
        raise CertificateError("cancellation trace does not equal exact replay")
    return True


def rank_one_integer_torsion_guard(coefficient: int) -> Mapping[str, object]:
    """Exact guard for Z --n--> Z, used to expose field information loss.

    For n != 0, H_0 = Z/nZ and H_1=0.  Tensoring with Q makes multiplication
    by n invertible, so rational homology vanishes and cannot certify integral
    acyclicity.  No floating rank is used.
    """
    n = int(coefficient)
    if n == 0:
        return {
            "coefficient": 0,
            "integral_h0": "Z",
            "integral_h1": "Z",
            "torsion_order": None,
            "rational_h0_dimension": 1,
            "rational_h1_dimension": 1,
        }
    return {
        "coefficient": n,
        "integral_h0": f"Z/{abs(n)}Z" if abs(n) != 1 else "0",
        "integral_h1": "0",
        "torsion_order": abs(n) if abs(n) != 1 else 1,
        "rational_h0_dimension": 0,
        "rational_h1_dimension": 0,
    }


def relabel_complex(complex_: FiniteChainComplex, renaming: Mapping[str, str]) -> FiniteChainComplex:
    if set(renaming) != set(complex_.generators) or len(set(renaming.values())) != len(renaming):
        raise ChainComplexError("renaming must be a bijection on all generators")
    basis = {k: tuple(renaming[g] for g in cells) for k, cells in complex_.basis_by_degree.items()}
    boundary = {
        renaming[g]: {renaming[h]: c for h, c in complex_.boundary[g].items()}
        for g in complex_.generators
    }
    return FiniteChainComplex(complex_.ring, basis, boundary)


def relabel_matching(matching: Sequence[MatchingPair], renaming: Mapping[str, str]) -> Tuple[MatchingPair, ...]:
    return tuple(MatchingPair(renaming[p.lower], renaming[p.upper]) for p in matching)


TOOL_CLASSIFICATION = {
    "semantic_domain": "finite free graded chain complexes over Z or Q with exact adjacent-degree boundary",
    "new_enterprise_capability": (
        "acyclic adjacent-grade matching plus exact unit/legal cancellation, critical-generator Morse boundary, "
        "and projection/lift/chain-homotopy certificate"
    ),
    "rejected_overlap": {
        "T2": "bounded incompatibility certificates do not perform chain cancellation",
        "T3": "signed incidence/cycle diagnostics may check acyclicity but do not yield invariant-preserving Morse reduction",
        "T6": "operation-safe quotient is stronger/different semantic preservation; homology equivalence is not operation safety",
        "T7": "symmetry/orbit reduction can accelerate matching search but is not cancellation",
        "T9": "gluing/holonomy obstruction is not chain-homotopy reduction",
        "alexander_descent": "threshold/Alexander specialization; no general acyclic-matching reduction engine",
    },
    "nonclaims": [
        "not new discrete Morse mathematics",
        "not arbitrary graph simplification",
        "not a canonical matching constructor",
        "not preservation of undeclared operation/observation semantics",
        "not an integral-homology proof by floating rank",
    ],
}
