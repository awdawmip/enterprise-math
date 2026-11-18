"""Exact finite-state certificates. Python 3 standard library."""
from fractions import Fraction as Q
from itertools import product
from functools import reduce
from math import gcd


def endpoints(M, T):
    r = min(T, M-2)
    l = min(max(0, T-1), M-2-r)
    return list(range(l)) + list(range(M-r+1, M+1)), l


def observables(M, T):
    points, _ = endpoints(M, T)
    return [[x**k for x in range(M+1)] for k in range(3)] + [
        [int(x == j) for x in range(M+1)] for j in points]


def lift(v, a, M):
    if a == 'A':
        return v[1:] + v[-1:]
    if a == 'R':
        return v[::-1]
    # Scale by M to keep integer rows. Rational row span is unchanged.
    return [x*v[min(M, x+1)] + (M-x)*v[M-x] for x in range(M+1)]


def primitive(v):
    d = reduce(gcd, v, 0)
    return [x//d for x in v] if d else v


def add_row(echelon, v):
    for j, pivot in sorted(echelon.items()):
        if v[j]:
            v = primitive([pivot[j]*a - v[j]*b for a, b in zip(v, pivot)])
    j = next((j for j, a in enumerate(v) if a), None)
    if j is not None:
        echelon[j] = primitive(v)


def rank_words(M, letters, maxT):
    layer = observables(M, 0)
    echelon = {}
    for T in range(maxT+1):
        _, l = endpoints(M,T)
        r = min(T, M-2)
        for f in layer:
            # Third differences vanish on the entire untracked central interval.
            assert all(f[i+3]-3*f[i+2]+3*f[i+1]-f[i] == 0
                       for i in range(l, M-r-2))
            if len(echelon) < M+1:
                add_row(echelon, f)
        assert len(echelon) == len(observables(M,T))
        if T < maxT:
            layer = [lift(v,a,M) for v in layer for a in letters]


def dot(v, w):
    return sum(a*b for a, b in zip(v, w))


def witnesses(M,T):
    base = observables(M,T)
    pts, l = endpoints(M,T)
    anchors = [l,l+1,l+2]
    # Coefficients of each Lagrange cardinal polynomial (low to high).
    polys = []
    for j in anchors:
        a,b = [i for i in anchors if i != j]
        den = (j-a)*(j-b)
        polys.append([Q(a*b,den), Q(-a-b,den), Q(1,den)])
    for j in range(len(base)):
        v = [Q(0) for _ in range(M+1)]
        if j < 3:
            for a,p in zip(anchors,polys):
                v[a] = p[j]
            readout = base[j]
        else:
            pos = pts[j-3]
            v[pos] = 1
            for a,p in zip(anchors,polys):
                v[a] = -(p[0]+p[1]*pos+p[2]*pos*pos)
            if pos < l:
                readout = [min(M, M-x+pos+1) for x in range(M+1)]
                assert pos+2 <= T  # R, then A^(pos+1)
            else:
                readout = [min(M, x+M-pos+1) for x in range(M+1)]
                assert M-pos+1 <= T
        assert [dot(v, f) for f in base] == [int(i==j) for i in range(len(base))]
        plus,minus = [max(0,x) for x in v], [max(0,-x) for x in v]
        assert dot(plus,readout) != dot(minus,readout)
        if j:
            assert sum(plus) == sum(minus) > 0
        else:
            assert sum(plus)-sum(minus) == 1


def arbitrary_guards():
    cases = 0
    # Enumerate probabilities at all interior states. Endpoint p(M) is free.
    for M in range(2,6):
        bas = observables(M,1)
        for p in product([Q(0),Q(1,2),Q(1)], repeat=M):
            u = [p[x]*(2*x+1-M) for x in range(M)]
            fits = all(u[i+3]-3*u[i+2]+3*u[i+1]-u[i]==0 for i in range(M-3))
            slots = {}
            for f in bas:
                add_row(slots, f)
            for k in [1,2]:
                a = list(p)+[Q(1,2)]
                f = [v*min(M,x+1)**k + (1-v)*(M-x)**k for x,v in enumerate(a)]
                add_row(slots, [int(2*v) for v in f])
            assert len(slots) == len(bas) + (not fits)
            cases += 1
    return cases


def update_check(M,T):
    points, left = endpoints(M,T)
    dest_points, _ = endpoints(M,T-1)
    atoms = [Q((x+3)*(x+1),7*M) for x in range(M+1)]
    m = [dot(atoms,f) for f in observables(M,T)[:3]]
    histogram = {x:atoms[x] for x in points}
    if len(points) == M-2:
        center = range(left,left+3)
        rem = [m[k]-sum(w*x**k for x,w in histogram.items()) for k in range(3)]
        for a in center:
            j,k = [x for x in center if x != a]
            histogram[a] = (rem[2]-(j+k)*rem[1]+j*k*rem[0])/((a-j)*(a-k))
    for intercept,slope in [(1,0),(0,0),(0,Q(1,M))]:
        def weight(x):
            return intercept+slope*x
        c = [(1-M)*intercept,2*intercept+(1-M)*slope,2*slope]
        qM = sum(v*M**k for k,v in enumerate(c))
        mean,second = M*m[0]-m[1]+dot(m,c), M*M*m[0]-2*M*m[1]+m[2]+(M+1)*dot(m,c)
        mean += (weight(M)*M-qM)*histogram[M]
        second += (weight(M)*M*M-(M+1)*qM)*histogram[M]
        compressed = [m[0],mean,second]
        for j in dest_points:
            src = [j-1] if j else []
            if j == M:
                src.append(M)
            compressed.append(sum(weight(x)*histogram[x] for x in src) +
                              (1-weight(M-j))*histogram[M-j])
        direct = [Q(0) for x in range(M+1)]
        for x,w in enumerate(atoms):
            direct[min(x+1,M)] += weight(x)*w
            direct[M-x] += (1-weight(x))*w
        assert compressed == [dot(direct,f) for f in observables(M,T-1)]


def run():
    checks = 0
    for M in range(2,17):
        for letters in ["AR","ARB"]:
            rank_words(M,letters,6)
        for T in range(7):
            witnesses(M,T)
            if T:
                update_check(M,T)
            checks += len(observables(M,T))
    M = 4
    p = [Q(x*x, M*M) for x in range(M+1)]
    diff = [-1,3,-3,1,0]
    g = [p[x]*min(x+1,M)+(1-p[x])*(M-x) for x in range(M+1)]
    assert all(dot(diff,f)==0 for f in observables(M,1)) and dot(diff,g)==Q(3,4)
    print("210 exact word-span ranks, "+str(checks)+" exact one-coordinate deletion certificates")
    print("270 compressed updates agree with forward full histograms")
    print(arbitrary_guards(), "exact one-step arbitrary-guard checks")
    print("M=4 nonlinear guard: normalized mean gap =", dot(diff,g)/4)


if __name__ == '__main__':
    run()
