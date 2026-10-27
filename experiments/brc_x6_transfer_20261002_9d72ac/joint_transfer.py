#!/usr/bin/env python3
"""Exact X6 cross-axis dependence probe, reusing the existing degree-two BRC tool.

Six signed coordinates are native raw Cell coordinates at one fixed anchor.
The chosen conditional routing F(z)=z+z[3]*e1 is one signed native step on
this invariant support (z[3] is always +/-1). It is not a force law, a new
primitive diagonal direction, or a derivation of the P000 dynamics.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
from enterprise_math.brc_transport import (  # noqa: E402
    Affine, EffectHistogram, MomentState, eye, ma, point_moment, sm,
)

OUT = Path(__file__).resolve().parent


def initial(kind):
    points = [x for x in product((-1, 1), repeat=6)
              if kind == "independent" or x[3] == (1 if kind == "aligned" else -1) * x[0]]
    return {x: Q(1, len(points)) for x in points}


def projection(law, axes):
    result = defaultdict(Q)
    for x, w in law.items():
        result[tuple(x[i] for i in axes)] += w
    return dict(result)


def tv(a, b):
    return sum((abs(a.get(x, 0) - b.get(x, 0)) for x in a.keys() | b.keys()), Q()) / 2


def moment(law):
    result = sm(0, eye(7))
    for x, w in law.items():
        result = ma(result, sm(w, point_moment(x)))
    return MomentState.from_matrix(result)


def gamma(law, axis):
    mean = sum((w*x[axis] for x,w in law.items()), Q())
    variance = sum((w*(x[axis]-mean)**2 for x,w in law.items()), Q())
    if not variance:
        return None
    m4 = sum((w*(x[axis]-mean)**4 for x,w in law.items()), Q())
    return str(m4 / variance**2 - 3)


def run():
    a = [list(row) for row in eye(6)]
    a[0][3] = Q(1)
    action = Affine(tuple(tuple(row) for row in a), (Q(),)*6)
    packet = EffectHistogram.from_terms(6, [(1, action, 1)])
    laws = {kind: initial(kind) for kind in ("aligned", "opposed", "independent")}
    original = {kind: dict(law) for kind,law in laws.items()}
    moments = {kind: moment(law) for kind,law in laws.items()}
    assert len(moments["aligned"].upper) == 28
    assert projection(laws["aligned"], (0,1,2)) == projection(laws["opposed"], (0,1,2))
    assert all(projection(laws["aligned"], (i,)) == projection(laws["opposed"], (i,)) for i in range(6))
    rows = []
    for n in range(65):
        for kind, law in laws.items():
            exact = moment(law)
            assert exact == moments[kind], (kind, n, "BRC-vs-full-law mismatch")
            matrix = exact.to_matrix()
            assert all(matrix[i][6] == 0 for i in range(6))
            expected = {"aligned": (n+1)**2, "opposed": (n-1)**2, "independent": 1+n*n}[kind]
            assert matrix[0][0] == expected
            rows.append({"kind":kind, "n":n,
                         "covariance_upper_21":[str(matrix[i][j]) for i in range(6) for j in range(i,6)],
                         "moment_upper_28":[str(v) for v in exact.upper],
                         "variance_x1":str(matrix[0][0]), "covariance_x1_x4":str(matrix[0][3]),
                         "gamma4_x1":gamma(law,0),
                         "initial_decorrelation_variance":str(1+n*n),
                         "drop_covariance_every_step_variance":str(1+n)})
        if n == 1:
            assert tv(projection(laws["aligned"], (0,1,2)), projection(laws["opposed"], (0,1,2))) == 1
        assert tv(laws["aligned"], laws["opposed"]) == 1
        if n < 64:
            for kind, law in laws.items():
                next_law = defaultdict(Q)
                for x,w in law.items():
                    y = tuple(int(v) for v in action.apply(x))
                    assert sum(abs(u-v) for u,v in zip(x,y)) == 1
                    next_law[y] += w
                laws[kind] = dict(next_law)
                moments[kind] = moments[kind].then(packet)
    result = {
        "native_spatial_dimensions":6, "time_type":"separate discrete routing tick",
        "coordinate_type":"signed raw chart at a fixed Cell anchor; not final Cell address output",
        "operation":"F(z)=z+z4*e1; z4 in {-1,+1} on the invariant support",
        "scope":"conditional state-indexed native-step model, not an established physical coupling law",
        "reuse":"existing T0_BRC Affine/EffectHistogram/MomentState; exact degree <=2 only",
        "future_scope":"repeated F and declared spatial/moment observers; no hidden branch-history access",
        "provenance":"initial law stored atomwise; F deterministic and invertible, so x0=F^(-n)(xn) reconstructs the full ordered path",
        "initial_laws":{kind:[{"raw_x6":x,"probability":str(w)} for x,w in law.items()] for kind,law in original.items()},
        "n_range":[0,64], "rows":rows,
        "checks":{"exact_BRC_vs_full_distribution_rows":len(rows),
                  "all_six_initial_marginals_equal":True,
                  "initial_axes123_joint_projection_equal":True,
                  "after_one_tick_axes123_TV":"1",
                  "full_spatial_law_TV_aligned_vs_opposed_all_ticks":"1",
                  "every_executed_step_native_unit":True},
        "conclusion":"Initial retained projection does not determine future projected law. Cross-covariance is necessary for this degree-two future; 28 moments are not claimed sufficient for arbitrary observers."
    }
    target = OUT / "joint_results.json"
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps(result["checks"], ensure_ascii=False))


if __name__ == "__main__":
    run()
