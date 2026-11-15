"""Exact F_p matrix-representation certificate checker for a finitely presented group.

A nonidentity image of a generator, after checking all relators, proves
that the presented group is nontrivial. An explicit rank-four word image
span certifies absolute irreducibility of the two-dimensional F_p image.

No conclusions about arbitrary 3-manifold groups or prime bounds are made.
"""
from __future__ import annotations

import json
from collections import deque
from dataclasses import dataclass
from math import isqrt

Matrix = tuple[int, int, int, int]
I: Matrix = (1, 0, 0, 1)


def is_prime(p: int) -> bool:
    if p < 2:
        return False
    for d in range(2, isqrt(p) + 1):
        if p % d == 0:
            return False
    return True


def multiply(a: Matrix, b: Matrix, p: int) -> Matrix:
    return (
        (a[0] * b[0] + a[1] * b[2]) % p,
        (a[0] * b[1] + a[1] * b[3]) % p,
        (a[2] * b[0] + a[3] * b[2]) % p,
        (a[2] * b[1] + a[3] * b[3]) % p,
    )


def inverse(a: Matrix, p: int) -> Matrix:
    if (a[0] * a[3] - a[1] * a[2]) % p != 1:
        raise ValueError("expected determinant-one image")
    return (a[3] % p, -a[1] % p, -a[2] % p, a[0] % p)


def word_image(word: list[int], matrices: list[Matrix], p: int) -> Matrix:
    out = I
    for item in word:
        if not 1 <= abs(item) <= len(matrices):
            raise ValueError("word refers to absent generator")
        image = matrices[abs(item) - 1]
        out = multiply(out, image if item > 0 else inverse(image, p), p)
    return out


def rank_mod_p(rows: list[Matrix], p: int) -> int:
    a = [list(row) for row in rows]
    rank = 0
    for c in range(4):
        pivot = next((j for j in range(rank, len(a)) if a[j][c] % p), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        scale = pow(a[rank][c], -1, p)
        a[rank] = [(x * scale) % p for x in a[rank]]
        for j in range(len(a)):
            if j != rank:
                factor = a[j][c]
                a[j] = [(x - factor * y) % p for x, y in zip(a[j], a[rank])]
        rank += 1
    return rank


def image_group_order(matrices: list[Matrix], p: int, limit: int = 200000) -> int:
    generators = matrices + [inverse(x, p) for x in matrices]
    seen = {I}
    queue = deque([I])
    while queue:
        g = queue.popleft()
        for h in generators:
            z = multiply(g, h, p)
            if z not in seen:
                if len(seen) >= limit:
                    raise ValueError("image group enumeration limit exceeded")
                seen.add(z)
                queue.append(z)
    return len(seen)


def check_certificate(cert: dict, enumerate_image: bool = False) -> dict:
    p = cert["p"]
    if not isinstance(p, int) or not is_prime(p):
        raise ValueError("p must be prime; this checker implements F_p, not arbitrary F_q")
    matrices = [tuple(int(x) % p for x in row) for row in cert["generator_matrices"]]
    if any(len(row) != 4 or (row[0] * row[3] - row[1] * row[2]) % p != 1 for row in matrices):
        raise ValueError("all generator images must lie in SL(2,F_p)")
    if any(word_image(w, matrices, p) != I for w in cert["relators"]):
        raise ValueError("a presentation relator is not satisfied")
    witness_words = cert.get("algebra_span_words", [])
    span_rank = rank_mod_p([word_image(w, matrices, p) for w in witness_words], p)
    nontrivial = any(row != I for row in matrices)
    result = {
        "p": p,
        "generator_count": len(matrices),
        "relators_verified": len(cert["relators"]),
        "nontrivial_finite_image": nontrivial,
        "algebra_span_rank": span_rank,
        "absolutely_irreducible_certified": span_rank == 4,
        "semantics": "finite-field homomorphism certificate; no manifold-recognition or general existence claim",
    }
    if enumerate_image:
        result["image_group_order"] = image_group_order(matrices, p)
    return result


POINCARE_HOMOLOGY_SPHERE = {
    "example": "binary icosahedral fundamental group: <s,t | s^3=t^5=(st)^2>",
    "p": 5,
    "generator_matrices": [[0, 1, 4, 1], [0, 4, 1, 3]],
    "relators": [[1, 1, 1, -2, -2, -2, -2, -2], [1, 2, 1, 2, -1, -1, -1]],
    "algebra_span_words": [[], [1], [2], [1, 2]],
}

THREE_SPHERE = {
    "example": "pi_1(S^3) = trivial, presentation < | >",
    "p": 5,
    "generator_matrices": [],
    "relators": [],
    "algebra_span_words": [[]],
}

CYCLIC_SANITY = {
    "example": "Z/3 (lens-space type sanity case; not an integral homology sphere)",
    "p": 7,
    "generator_matrices": [[2, 0, 0, 4]],
    "relators": [[1, 1, 1]],
    "algebra_span_words": [[], [1], [1, 1]],
}


def test_all() -> dict:
    a = check_certificate(POINCARE_HOMOLOGY_SPHERE, enumerate_image=True)
    b = check_certificate(THREE_SPHERE, enumerate_image=True)
    c = check_certificate(CYCLIC_SANITY, enumerate_image=True)
    assert a["image_group_order"] == 120 and a["absolutely_irreducible_certified"]
    assert a["nontrivial_finite_image"]
    assert b["image_group_order"] == 1 and not b["nontrivial_finite_image"]
    assert c["image_group_order"] == 3 and c["nontrivial_finite_image"]
    assert not c["absolutely_irreducible_certified"]
    bad = dict(POINCARE_HOMOLOGY_SPHERE, generator_matrices=[[1, 0, 0, 1], [0, 4, 1, 3]])
    try:
        check_certificate(bad)
    except ValueError:
        pass
    else:
        raise AssertionError("incorrect relator was accepted")
    try:
        check_certificate(dict(CYCLIC_SANITY, generator_matrices=[[2, 0, 0, 3]]))
    except ValueError:
        pass
    else:
        raise AssertionError("invalid determinant was accepted")
    return {"Poincare_homology_sphere": a, "S3": b, "cyclic_sanity": c, "rejected_invalid_relator": True, "rejected_invalid_determinant": True}


if __name__ == "__main__":
    print(json.dumps(test_all(), sort_keys=True, indent=2))
