"""Reproduce finite k=3..8 optimal slack-source dictionary sizes.
Requires scipy >= 1.9 with HiGHS MIP backend and numpy.
Run: python VERIFY_R5_SLACK_STATIC_MILP.py
This is solver-checked finite evidence; universal claims use the human proofs.
"""
import json
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import coo_matrix


def q(u, k):
    return sum(((u >> i) & 1) * ((u >> ((i + 1) % k)) & 1) for i in range(k))


def solve(k, s):
    n = 1 << k
    values = [q(u, k) for u in range(n)]
    rows, cols = [], []
    for v in range(n):
        for u in range(n):
            if (u & v) == u and values[v] - values[u] <= s:
                rows.append(u)
                cols.append(v)
    A = coo_matrix((np.ones(len(rows), dtype=float), (rows, cols)),
                   shape=(n, n)).tocsr()
    result = milp(c=np.ones(n), integrality=np.ones(n),
                  bounds=Bounds(np.zeros(n), np.ones(n)),
                  constraints=LinearConstraint(A, np.ones(n), np.inf),
                  options={"mip_rel_gap": 0.0, "time_limit": 90.0})
    assert result.status == 0 and result.x is not None, (k, s, result.message)
    chosen = [v for v in range(n) if result.x[v] > 0.5]
    assert abs(result.fun - len(chosen)) < 1e-7
    assert result.mip_gap < 1e-8
    for u in range(n):
        assert any((u & v) == u and values[v] - values[u] <= s
                   for v in chosen)
    return {"slack": s, "minimum": len(chosen),
            "mip_gap": float(result.mip_gap), "termination": "optimal",
            "witness_centers": chosen}


def main():
    cases = {str(k): [solve(k, s) for s in range(k + 1)]
             for k in range(3, 9)}
    for k in range(3, 9):
        assert cases[str(k)][k-1]["minimum"] == 3
        assert cases[str(k)][k-2]["minimum"] == 4
        assert cases[str(k)][k]["minimum"] == 1
    print(json.dumps({"status": "PASS_R5_SLACK_STATIC_MILP",
                      "model": "canonical source centers and cycle q, integer set cover",
                      "k_range": [3, 8], "solver": "SciPy milp / HiGHS",
                      "cases": cases}, indent=2))


if __name__ == "__main__":
    main()
