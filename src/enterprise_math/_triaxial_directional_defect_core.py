"""Independent triaxial directional-defect operators.

Phase-A implementation for
RS-TRIAXIAL-DIRECTIONAL-DEFECT-INDEPENDENT-TOOL-VERIFICATION.

The implementation uses the integer endpoint carrier Z^2 only as an implementation
carrier. Native trace identities are deliberately not quotiented by endpoint
coalescence.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Dict, List, Mapping, MutableMapping, Sequence, Tuple

Point = Tuple[int, int]
Triple = Tuple[int, int, int]
SparseField = Dict[Point, int]
Kernel = Dict[Point, int]


def canonical_decode_xy(r: int, s: int) -> Triple:
    m = min(r, s, 0)
    return (r - m, s - m, -m)


def carrier_xy(t: Triple) -> Point:
    a, b, c = t
    return (a - c, b - c)


def rho(t: Triple) -> Triple:
    a, b, c = t
    return (c, a, b)


def frame_width(seed: Triple) -> int:
    return max(seed) - min(seed)


def is_canonical_seed(seed: Triple) -> bool:
    return min(seed) == 0 and all(v >= 0 for v in seed) and frame_width(seed) > 0


def is_primitive_seed(seed: Triple) -> bool:
    if not is_canonical_seed(seed):
        return False
    x, y = carrier_xy(seed)
    return gcd(abs(x), abs(y)) == 1


def _add(p: Point, q: Point) -> Point:
    return (p[0] + q[0], p[1] + q[1])


def _neg(p: Point) -> Point:
    return (-p[0], -p[1])


@dataclass(frozen=True)
class Frame:
    seed: Triple
    directions: Tuple[Point, Point, Point]
    width: int
    primitive: bool


def declare_frame(seed: Triple) -> Frame:
    if not is_canonical_seed(seed):
        raise ValueError("seed must be nonzero, nonnegative, and min-zero")
    s1 = carrier_xy(seed)
    s2 = carrier_xy(rho(seed))
    s3 = carrier_xy(rho(rho(seed)))
    if _add(_add(s1, s2), s3) != (0, 0):
        raise AssertionError("endpoint carrier closure failed")
    if len({s1, s2, s3}) != 3:
        raise ValueError("degenerate frame")
    return Frame(seed, (s1, s2, s3), frame_width(seed), is_primitive_seed(seed))


def convolve_kernels(a: Mapping[Point, int], b: Mapping[Point, int]) -> Kernel:
    out: MutableMapping[Point, int] = {}
    for u, cu in a.items():
        for v, cv in b.items():
            w = _add(u, v)
            out[w] = out.get(w, 0) + cu * cv
            if out[w] == 0:
                del out[w]
    return dict(out)


def diff1_kernel(direction: Point) -> Kernel:
    return {direction: 1, (0, 0): -1}


def rhombus2_kernel(direction_i: Point, direction_j: Point) -> Kernel:
    return convolve_kernels(diff1_kernel(direction_i), diff1_kernel(direction_j))


def triple_defect_kernel(frame: Frame) -> Kernel:
    p: Kernel = {(0, 0): 1}
    for d in frame.directions:
        p = convolve_kernels(p, diff1_kernel(d))
    return p


def family_kernel(seeds: Sequence[Triple]) -> Kernel:
    p: Kernel = {(0, 0): 1}
    for seed in seeds:
        p = convolve_kernels(p, triple_defect_kernel(declare_frame(seed)))
    return p


def family_width(seeds: Sequence[Triple]) -> int:
    return sum(frame_width(seed) for seed in seeds)


def apply_kernel(field: Mapping[Point, int], kernel: Mapping[Point, int]) -> SparseField:
    out: MutableMapping[Point, int] = {}
    for x, value in field.items():
        if value == 0:
            continue
        for u, coeff in kernel.items():
            y = _add(x, u)
            out[y] = out.get(y, 0) + value * coeff
            if out[y] == 0:
                del out[y]
    return dict(out)


def diff1(field: Mapping[Point, int], direction: Point) -> SparseField:
    return apply_kernel(field, diff1_kernel(direction))


def rhombus2(field: Mapping[Point, int], direction_i: Point, direction_j: Point) -> SparseField:
    return apply_kernel(field, rhombus2_kernel(direction_i, direction_j))


def triple_defect(field: Mapping[Point, int], frame: Frame) -> SparseField:
    return apply_kernel(field, triple_defect_kernel(frame))


def adjoint_kernel(kernel: Mapping[Point, int]) -> Kernel:
    return {_neg(u): coeff for u, coeff in kernel.items()}


def directional_laplacian_kernel(direction: Point) -> Kernel:
    return convolve_kernels(adjoint_kernel(diff1_kernel(direction)), diff1_kernel(direction))


def gram_factor_kernel(frame: Frame) -> Kernel:
    g = triple_defect_kernel(frame)
    return convolve_kernels(adjoint_kernel(g), g)


def laplacian_product_kernel(frame: Frame) -> Kernel:
    p: Kernel = {(0, 0): 1}
    for d in frame.directions:
        p = convolve_kernels(p, directional_laplacian_kernel(d))
    return p


def eight_state_trace_cube(frame: Frame):
    out = []
    ds = frame.directions
    for bits in ((b1, b2, b3) for b1 in (0, 1) for b2 in (0, 1) for b3 in (0, 1)):
        k = sum(bits)
        endpoint = (0, 0)
        for bit, d in zip(bits, ds):
            if bit:
                endpoint = _add(endpoint, d)
        out.append((bits, endpoint, (-1) ** (3 - k)))
    return out


def six_point_endpoint_stencil(frame: Frame) -> Kernel:
    return triple_defect_kernel(frame)


def hex_box(radius: int) -> Tuple[Point, ...]:
    if radius < 0:
        return tuple()
    pts = []
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            if max(abs(x), abs(y), abs(x - y)) <= radius:
                pts.append((x, y))
    return tuple(sorted(pts))


def xray_line_key(point: Point, direction: Point) -> int:
    dx, dy = direction
    g = gcd(abs(dx), abs(dy))
    if g == 0:
        raise ValueError("zero direction")
    dx //= g
    dy //= g
    return -dy * point[0] + dx * point[1]


def xray_line_sums(field: Mapping[Point, int], direction: Point) -> Dict[int, int]:
    sums: MutableMapping[int, int] = {}
    for point, value in field.items():
        key = xray_line_key(point, direction)
        sums[key] = sums.get(key, 0) + value
    return dict(sums)


def xray_kernel_cert(seed_field: Mapping[Point, int], seeds: Sequence[Triple]) -> bool:
    ghost = apply_kernel(seed_field, family_kernel(seeds))
    for seed in seeds:
        for direction in declare_frame(seed).directions:
            if any(v != 0 for v in xray_line_sums(ghost, direction).values()):
                return False
    return True


def _canonical_undirected(direction: Point) -> Point:
    dx, dy = direction
    g = gcd(abs(dx), abs(dy))
    if g == 0:
        raise ValueError("zero direction")
    d = (dx // g, dy // g)
    return min(d, _neg(d))


def xray_matrix(seeds: Sequence[Triple], radius: int):
    points = hex_box(radius)
    index = {p: i for i, p in enumerate(points)}
    rows: List[List[int]] = []
    seen = set()
    for seed in seeds:
        frame = declare_frame(seed)
        if not frame.primitive:
            raise ValueError("tomography frame must be primitive")
        for direction in frame.directions:
            d = _canonical_undirected(direction)
            if d in seen:
                continue
            seen.add(d)
            groups: MutableMapping[int, List[int]] = {}
            for point, j in index.items():
                groups.setdefault(xray_line_key(point, d), []).append(j)
            for key in sorted(groups):
                row = [0] * len(points)
                for j in groups[key]:
                    row[j] = 1
                rows.append(row)
    return rows, points


def kernel_matrix(seeds: Sequence[Triple], radius: int):
    width = family_width(seeds)
    domain = hex_box(radius - width)
    codomain = hex_box(radius)
    row_index = {p: i for i, p in enumerate(codomain)}
    p = family_kernel(seeds)
    matrix = [[0] * len(domain) for _ in codomain]
    for j, x in enumerate(domain):
        for u, coeff in p.items():
            y = _add(x, u)
            if y not in row_index:
                raise AssertionError("family kernel escaped claimed hex-box erosion")
            matrix[row_index[y]][j] += coeff
    return matrix, domain, codomain


def rank_mod(matrix: Sequence[Sequence[int]], prime: int) -> int:
    a = [[v % prime for v in row] for row in matrix]
    if not a:
        return 0
    m, n, r = len(a), len(a[0]), 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, prime)
        a[r] = [(v * inv) % prime for v in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                factor = a[i][c]
                a[i] = [(a[i][j] - factor * a[r][j]) % prime for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def rank_q(matrix: Sequence[Sequence[int]]) -> int:
    a = [[Fraction(v) for v in row] for row in matrix]
    if not a:
        return 0
    m, n, r = len(a), len(a[0]), 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        pv = a[r][c]
        for j in range(c, n):
            a[r][j] /= pv
        for i in range(m):
            if i != r and a[i][c]:
                factor = a[i][c]
                for j in range(c, n):
                    a[i][j] -= factor * a[r][j]
        r += 1
        if r == m:
            break
    return r


def transpose(matrix):
    return [list(col) for col in zip(*matrix)] if matrix else []


def matmul(a, b):
    if not a or not b:
        return []
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def gram_matrix(seeds: Sequence[Triple], radius: int):
    a, domain, _ = kernel_matrix(seeds, radius)
    return matmul(transpose(a), a), domain


def exposed_vertex_sampling_matrix(seeds: Sequence[Triple], radius: int):
    kernel = family_kernel(seeds)
    weights = ((1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2), (1, 5), (5, 1), (-1, 2), (2, -1))
    exposed = q = None
    for candidate in weights:
        scores = {u: candidate[0] * u[0] + candidate[1] * u[1] for u in kernel}
        top = max(scores.values())
        maxima = [u for u, score in scores.items() if score == top]
        if len(maxima) == 1:
            exposed, q = maxima[0], candidate
            break
    if exposed is None or abs(kernel[exposed]) != 1:
        raise AssertionError("no unimodular exposed vertex")
    domain = list(hex_box(radius - family_width(seeds)))
    domain.sort(key=lambda x: (-(q[0] * x[0] + q[1] * x[1]), x))
    col_index = {x: j for j, x in enumerate(domain)}
    rows = []
    for x in domain:
        sample = _add(x, exposed)
        row = [0] * len(domain)
        for u, coeff in kernel.items():
            source = (sample[0] - u[0], sample[1] - u[1])
            j = col_index.get(source)
            if j is not None:
                row[j] += coeff
        rows.append(row)
    return rows, tuple(domain), exposed, q


def primitive_frame_census(width: int, oriented: bool = False):
    if width < 1:
        return tuple()
    if width == 1:
        return ((1, 0, 0), (1, 1, 0)) if oriented else ((1, 0, 0),)
    reps = []
    for k in range(1, width):
        if gcd(width, k) == 1:
            reps.append((width, k, 0))
            if oriented:
                reps.append((k, width, 0))
    return tuple(reps)


def euler_phi(n: int) -> int:
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1) if n >= 1 else 0


def frame_census_law(width: int):
    return (len(primitive_frame_census(width, False)), len(primitive_frame_census(width, True)))


def hive_bridge_values(field: Mapping[Point, int], frame: Frame):
    d1, d2, d3 = frame.directions
    h23 = rhombus2(field, d2, d3)
    h31 = rhombus2(field, d3, d1)
    h12 = rhombus2(field, d1, d2)
    return diff1(h23, d1), diff1(h31, d2), diff1(h12, d3), triple_defect(field, frame)


def y_delta_triangle_conductances(a: Fraction, b: Fraction, c: Fraction):
    total = a + b + c
    if total == 0:
        raise ZeroDivisionError("star total conductance is zero")
    return (a * b / total, b * c / total, c * a / total)


def y_delta_is_additive_counterexample() -> bool:
    p = (Fraction(1), Fraction(1), Fraction(1))
    q = (Fraction(1), Fraction(2), Fraction(3))
    fp = y_delta_triangle_conductances(*p)
    fq = y_delta_triangle_conductances(*q)
    r = tuple(p[i] + q[i] for i in range(3))
    fr = y_delta_triangle_conductances(*r)
    return fr != tuple(fp[i] + fq[i] for i in range(3))


def finite_support_left_inverse_possible(kernel: Mapping[Point, int]) -> bool:
    return len(kernel) == 1 and abs(next(iter(kernel.values()))) == 1
