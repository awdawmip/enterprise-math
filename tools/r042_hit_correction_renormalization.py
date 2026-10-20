from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

TOOLS = Path(__file__).resolve().parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from r042_polygonal_branch_limit import (
    discriminant_z,
    exact_children,
    fundamental_pell_unit,
    is_exact_hit,
    pell_matrix_period_mod,
    predecessor,
)

Quad = Tuple[int, int]  # A + B*sqrt(r)


@dataclass(frozen=True)
class PellCoordinate:
    seed_hit: int
    unit_rank: int
    y: int
    z: int


def quad_mul(r: int, x: Quad, y: Quad) -> Quad:
    a, b = x
    c, d = y
    return a * c + r * b * d, a * d + b * c


def quad_pow(r: int, x: Quad, n: int) -> Quad:
    if n < 0:
        raise ValueError("n must be nonnegative")
    out = (1, 0)
    base = x
    while n:
        if n & 1:
            out = quad_mul(r, out, base)
        base = quad_mul(r, base, base)
        n >>= 1
    return out


def quad_norm(r: int, x: Quad) -> int:
    a, b = x
    return a * a - r * b * b


def alpha_times(r: int, x: Quad) -> Quad:
    a, b = x
    return r * b, a


def alpha_power_times(r: int, x: Quad, d: int) -> Quad:
    if d < 0:
        raise ValueError("d must be nonnegative")
    out = x
    for _ in range(d):
        out = alpha_times(r, out)
    return out


def hit_pair(s: int, r: int, k: int) -> Quad:
    """Return (y,z) for an exact-hit parent k, encoded as y + z*sqrt(r)."""
    if not is_exact_hit(s, r, k):
        raise ValueError(f"k={k} is not an exact hit")
    child = exact_children(s, r, k).children[0]
    return discriminant_z(s, child), discriminant_z(s, k)


def pair_to_hit_index(s: int, r: int, pair: Quad) -> Optional[int]:
    """Decode a positive residue-compatible exact-hit pair back to its parent index."""
    y, z = pair
    a = s - 2
    c = s - 4
    m = 2 * a
    if y <= 0 or z <= 0:
        return None
    if (y + c) % m or (z + c) % m:
        return None
    k = (z + c) // m
    if k < 1 or discriminant_z(s, k) != z or not is_exact_hit(s, r, k):
        return None
    child = exact_children(s, r, k).children[0]
    if discriminant_z(s, child) != y:
        return None
    return k


def residue_pell_unit(s: int, r: int) -> Tuple[int, Quad]:
    """Least positive power of the fundamental Pell unit acting trivially mod 2a."""
    m = 2 * (s - 2)
    p = pell_matrix_period_mod(r, m)
    unit = quad_pow(r, fundamental_pell_unit(r), p)
    U, V = unit
    if quad_norm(r, unit) != 1:
        raise AssertionError("Pell unit norm failure")
    if (U - 1) % m or V % m or (r * V) % m:
        raise AssertionError("residue-unit matrix is not identity modulo 2a")
    return p, unit


def apply_unit(r: int, pair: Quad, unit: Quad) -> Quad:
    return quad_mul(r, unit, pair)


def inverse_unit(r: int, pair: Quad, unit: Quad) -> Quad:
    """Multiply by unit^{-1}=U-V*sqrt(r), valid for norm-one unit."""
    U, V = unit
    y, z = pair
    return U * y - r * V * z, U * z - V * y


def pell_coordinate(s: int, r: int, k: int) -> PellCoordinate:
    """Reduce an ambient positive exact hit by the residue-preserving Pell unit.

    The reduction stops exactly when one further inverse-unit step is no longer a
    positive exact hit in the k>=1 polygonal endpoint domain.
    """
    pair = hit_pair(s, r, k)
    _, unit = residue_pell_unit(s, r)
    rank = 0
    seed = k
    while True:
        prev_pair = inverse_unit(r, pair, unit)
        prev = pair_to_hit_index(s, r, prev_pair)
        if prev is None:
            break
        pair = prev_pair
        seed = prev
        rank += 1
    return PellCoordinate(seed, rank, pair[0], pair[1])


def unit_translate_hit(s: int, r: int, seed_hit: int, n: int) -> int:
    coord = pell_coordinate(s, r, seed_hit)
    if coord.unit_rank != 0 or coord.seed_hit != seed_hit:
        raise ValueError("seed_hit must be Pell-unit reduced")
    _, unit = residue_pell_unit(s, r)
    pair = apply_unit(r, hit_pair(s, r, seed_hit), quad_pow(r, unit, n))
    out = pair_to_hit_index(s, r, pair)
    if out is None:
        raise AssertionError("residue-compatible unit translate did not decode as exact hit")
    return out


def correction_digit(s: int, r: int, k0: int, k1: int, k2: int) -> int:
    """q_t in z_{t+2}=r*z_t+q_t for one exact legal length-two branch segment."""
    if k1 not in exact_children(s, r, k0).children:
        raise ValueError("k0->k1 is not legal")
    if k2 not in exact_children(s, r, k1).children:
        raise ValueError("k1->k2 is not legal")
    return discriminant_z(s, k2) - r * discriminant_z(s, k0)


def correction_residue(s: int, r: int) -> int:
    m = 2 * (s - 2)
    c = s - 4
    return ((r - 1) * c) % m


def coarse_integer_q_bound(s: int, r: int) -> int:
    """Certified strict outer bound |q_t| < returned integer.

    It avoids floating point. For z>=s,
      alpha*z-W(z) < B/s, |z_child-W(z)|<m, alpha=sqrt(r)<r,
    hence |q_t| < (r+1)*(m+B/s). Replacing B/s by ceil(B/s)
    gives this convenient integer outer bound.
    """
    m = 2 * (s - 2)
    c = s - 4
    B = (r - 1) * c * c
    ceil_B_over_s = (B + s - 1) // s
    return (r + 1) * (m + ceil_B_over_s)


def q_in_certified_outer_alphabet(s: int, r: int, q: int) -> bool:
    m = 2 * (s - 2)
    return abs(q) < coarse_integer_q_bound(s, r) and q % m == correction_residue(s, r)


def transition_pair(s: int, k0: int, k1: int) -> Quad:
    return discriminant_z(s, k1), discriminant_z(s, k0)


def transition_norm(s: int, r: int, k0: int, k1: int) -> int:
    return quad_norm(r, transition_pair(s, k0, k1))


def correction_block(s: int, r: int, hit_path: Sequence[int]) -> Dict[str, object]:
    """Exact hit-to-hit correction cocycle certificate.

    hit_path=[k_t,...,k_{t+d}] must be a legal branch segment whose two endpoints
    are exact hits. The exact successor of the terminal hit is appended
    automatically so that q_{t+d-1} is certified.
    """
    if len(hit_path) < 2:
        raise ValueError("need two hit endpoints")
    if not is_exact_hit(s, r, hit_path[0]) or not is_exact_hit(s, r, hit_path[-1]):
        raise ValueError("path endpoints must be exact hits")
    for u, v in zip(hit_path, hit_path[1:]):
        if v not in exact_children(s, r, u).children:
            raise ValueError(f"illegal edge {u}->{v}")

    terminal_successor = exact_children(s, r, hit_path[-1]).children[0]
    ext = list(hit_path) + [terminal_successor]
    qs = [correction_digit(s, r, ext[i], ext[i + 1], ext[i + 2])
          for i in range(len(hit_path) - 1)]
    if not all(q_in_certified_outer_alphabet(s, r, q) for q in qs):
        raise AssertionError("legal correction digit escaped certified finite outer alphabet")

    # P=sum alpha^(d-1-j) q_j, accumulated by P <- alpha*P+q.
    P: Quad = (0, 0)
    for q in qs:
        A, Bc = alpha_times(r, P)
        P = (A + q, Bc)

    d = len(hit_path) - 1
    xi0 = hit_pair(s, r, hit_path[0])
    xi1 = hit_pair(s, r, hit_path[-1])
    scaled = alpha_power_times(r, xi0, d)
    direct = (xi1[0] - scaled[0], xi1[1] - scaled[1])
    if P != direct:
        raise AssertionError((P, direct))
    if P == (0, 0):
        raise AssertionError("nonzero hit-to-hit correction required by norm mismatch")

    return {
        "gap_steps": d,
        "q_digits": qs,
        "P": P,
        "P_norm": quad_norm(r, P),
        "source_xi": xi0,
        "target_xi": xi1,
        "source_norm": quad_norm(r, xi0),
        "target_norm": quad_norm(r, xi1),
    }


def reverse_transition(s: int, r: int, y: int, z: int) -> Optional[Dict[str, int]]:
    """Exact one-step reverse correction state for transition xi=y+sqrt(r)z.

    The parent endpoint is certified by the existing exact predecessor oracle.
    If it exists, q=y-r*x and x=(y-q)/r exactly.
    """
    a = s - 2
    c = s - 4
    m = 2 * a
    if (z + c) % m:
        return None
    k = (z + c) // m
    if k < 1:
        return None
    p = predecessor(s, r, k)
    if p is None:
        return None
    x = discriminant_z(s, p)
    q = y - r * x
    if (y - q) % r or (y - q) // r != x:
        raise AssertionError("reverse divisibility identity failed")
    if k not in exact_children(s, r, p).children:
        raise AssertionError("reverse predecessor is not dynamically accessible")
    return {"parent_index": p, "parent_z": x, "q": q}


def first_hit_ancestor(s: int, r: int, target_hit: int, max_depth: int = 100000) -> Optional[Dict[str, int]]:
    cur = target_hit
    for depth in range(1, max_depth + 1):
        cur = predecessor(s, r, cur)
        if cur is None:
            return None
        if is_exact_hit(s, r, cur):
            coord = pell_coordinate(s, r, cur)
            return {
                "depth": depth,
                "ancestor_hit": cur,
                "ancestor_seed": coord.seed_hit,
                "ancestor_unit_rank": coord.unit_rank,
            }
    raise RuntimeError("max_depth exhausted before predecessor chain terminated")


def bounded_unit_orbit_reachability(
    s: int,
    r: int,
    reduced_seeds: Iterable[int],
    n_max: int,
    max_depth: int = 100000,
) -> Dict[str, object]:
    """Bounded exact explorer; absence of findings is never a theorem."""
    reduced_seeds = tuple(reduced_seeds)
    findings: List[Dict[str, int]] = []
    max_checked_depth = 0
    for seed in reduced_seeds:
        coord = pell_coordinate(s, r, seed)
        if coord.seed_hit != seed or coord.unit_rank != 0:
            raise ValueError(f"{seed} is not a reduced seed")
        for n in range(n_max + 1):
            target = unit_translate_hit(s, r, seed, n)
            cur = target
            terminated = False
            for depth in range(1, max_depth + 1):
                cur = predecessor(s, r, cur)
                if cur is None:
                    max_checked_depth = max(max_checked_depth, depth - 1)
                    terminated = True
                    break
                if is_exact_hit(s, r, cur):
                    max_checked_depth = max(max_checked_depth, depth)
                    c = pell_coordinate(s, r, cur)
                    findings.append({
                        "target_seed": seed,
                        "target_unit_rank": n,
                        "target_hit": target,
                        "gap_steps": depth,
                        "ancestor_hit": cur,
                        "ancestor_seed": c.seed_hit,
                        "ancestor_unit_rank": c.unit_rank,
                    })
                    terminated = True
                    break
            if not terminated:
                raise RuntimeError("bounded explorer max_depth exhausted")
    return {
        "classification": "BOUNDED_EXHAUSTIVE_FOR_DECLARED_UNIT_TRANSLATES_ONLY",
        "s": s,
        "r": r,
        "reduced_seeds": list(reduced_seeds),
        "n_max": n_max,
        "max_checked_predecessor_depth": max_checked_depth,
        "findings": findings,
    }
