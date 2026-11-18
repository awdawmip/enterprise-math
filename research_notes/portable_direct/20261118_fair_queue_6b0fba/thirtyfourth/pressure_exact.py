"""Exact rational finite witnesses for low-rank face drift in Dirichlet diffusion.

No packaged pilot inputs are loaded.  The small n=4 grid, face drift and loads
are independent finite test cases.  Only the stencil and regional QoI follow
the frozen pilot.  Fractions below denote exact signed observed errors.
"""
from fractions import Fraction as F
from itertools import product
import json


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), F(0))


def mv(A, x):
    return [dot(row, x) for row in A]


def solve(A, b):
    augmented = [list(map(F, row)) + [F(v)] for row, v in zip(A, b)]
    n = len(augmented)
    for i in range(n):
        pivot = next(j for j in range(i, n) if augmented[j][i])
        augmented[i], augmented[pivot] = augmented[pivot], augmented[i]
        a = augmented[i]
        normalization = a[i]
        a[:] = [val / normalization for val in a]
        for j, row in enumerate(augmented):
            if j != i and row[i]:
                alpha = row[i]
                row[:] = [v - alpha * w for v, w in zip(row, a)]
    return [row[-1] for row in augmented]


def stencil(n):
    h = F(1, n + 1)
    N = n * n
    A = [[F(0)] * N for _ in range(N)]
    gc = []
    for x, y in product(range(n), repeat=2):
        p = x * n + y
        A[p][p] = 4 / h**2
        for X, Y in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= X < n and 0 <= Y < n:
                A[p][X*n+Y] = -1 / h**2
        xp, yp = (x+1) * h, (y+1) * h
        if F(35,100) < yp < F(65,100):
            gc.append(int(F(15,100) < xp < F(35,100)) - int(F(65,100) < xp < F(85,100)))
        else:
            gc.append(0)
    return A, [F(z, gc.count(z)) if z else F(0) for z in gc]


def edge(N, i, j):
    v = [F(0)] * N
    v[i], v[j] = F(1), F(-1)
    return v


def add_drift(A, u, d):
    return [[v + sum(alpha * vec[i] * vec[j] for vec, alpha in zip(u, d))
             for j, v in enumerate(row)] for i, row in enumerate(A)]


def subtract(a, b):
    return [x-y for x,y in zip(a,b)]


def scenario(A, g, p0, u, d):
    b, z0 = mv(A, p0), solve(A, g)
    B = add_drift(A, u, d)
    p, z = solve(B, b), solve(B, g)
    r = subtract(b, mv(B, p0))
    dual_res = subtract(g, mv(B, z0))
    W = [solve(A, v) for v in u]
    H = [[dot(v, w) for w in W] for v in u]
    K = [[h + (1/d[i] if i == j else 0) for j,h in enumerate(row)] for i,row in enumerate(H)]
    q = [dot(v, p0) for v in u]
    t = [dot(v, z0) for v in u]
    mu = solve(K, q)
    err = dot(g, subtract(p, p0))
    assert err == dot(z, r) == -dot(t, mu)
    assert r == [-sum(a * v[j] * s for a, v, s in zip(d, u, q)) for j in range(len(g))]
    assert subtract(p0, p) == [sum(w[i]*a for w,a in zip(W,mu)) for i in range(len(g))]
    eta = dot(r,r) / dot(b,b)
    # The closed-form sharp all-load QoI norm is attained by b=+/-direction.
    lagrange = solve(K, t)
    direction = [sum(a*w[i] for a,w in zip(lagrange,W)) for i in range(len(g))]
    assert direction == subtract(z0, z)
    assert dot(direction,direction) == abs(dot(g, subtract(solve(B, direction), solve(A, direction))))
    return {"updates": [str(v) for v in d], "q": [str(v) for v in q], "H": [[str(x) for x in row] for row in H],
            "old_dual_estimate": str(dot(z0,r)), "qoi_error": str(err),
            "true_relative_residual_squared": str(eta), "current_dual_residual_squared": str(dot(dual_res,dual_res)),
            "qoi_all_unit_loads_max_squared": str(dot(direction,direction)), "passes_residual": eta<=F(1,10**6),
            "passes_qoi": abs(err)<=F(1,10**4)}


def main():
    n = 4
    A,g = stencil(n)
    assert [i for i,v in enumerate(g) if v] == [1,2,13,14]
    u = [edge(n*n, 1,5), edge(n*n, 2,6)]
    p0 = [F(2000)]*(n*n)
    p0[1] += 2
    p0[2] -= 1
    # h^-2 is 25. Set two interior face coefficients to 2 and 3.
    rank2 = scenario(A,g,p0,u,[F(25),F(50)])
    assert rank2["old_dual_estimate"] == "0" and rank2["passes_residual"] and not rank2["passes_qoi"]
    rank1 = scenario(A,g,p0,u[:1],[F(25)])
    h = F(rank1["H"][0][0])
    assert F(rank1["old_dual_estimate"])/(1+25*h) == F(rank1["qoi_error"])
    # Negative admissible update within coefficient interval [1,20].
    previous = add_drift(A,u[:1],[F(25)])
    negative = scenario(previous,g,p0,u[:1],[F(-25)])
    hh = F(negative["H"][0][0])
    assert 0 < 1-25*hh < 1
    assert F(negative["old_dual_estimate"])/(1-25*hh) == F(negative["qoi_error"])
    print(json.dumps({"model": "independent n=4 midpoint face drift, Dirichlet, frozen two-region mean functional",
                      "rank2_cancellation":rank2,"rank1_up":rank1,"rank1_down":negative},
                     sort_keys=True,indent=2))


if __name__ == "__main__":
    main()
