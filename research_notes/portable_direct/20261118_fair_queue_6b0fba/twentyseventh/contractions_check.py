"""Exact external Fourier-observer audit in Q(i). Run with Python 3.10+."""
import argparse
import ast
import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path


class G:
    """Rational real and imaginary components, with no floating conversion."""
    __slots__ = ("r", "i")

    def __init__(self, r=0, i=0):
        self.r, self.i = F(r), F(i)

    @staticmethod
    def cast(x):
        return x if isinstance(x, G) else G(x)

    def __add__(self, x):
        x = self.cast(x)
        return G(self.r + x.r, self.i + x.i)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.r, -self.i)

    def __sub__(self, x):
        return self + (-self.cast(x))

    def __rsub__(self, x):
        return x + (-self)

    def __mul__(self, x):
        if isinstance(x, tuple):
            return NotImplemented
        x = self.cast(x)
        return G(self.r*x.r-self.i*x.i, self.r*x.i+self.i*x.r)

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = self.cast(x)
        z = self * x.bar()
        d = x.r*x.r+x.i*x.i
        return G(z.r/d, z.i/d)

    def __rtruediv__(self, x):
        return self.cast(x) / self

    def __bool__(self):
        return bool(self.r or self.i)

    def __eq__(self, x):
        x = self.cast(x)
        return self.r == x.r and self.i == x.i

    def bar(self):
        return G(self.r, -self.i)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def raw_vortex(spectrum):
    result = {}
    branches = []
    for p, u in sorted(spectrum.items()):
        for q, v in sorted(spectrum.items()):
            k = tuple(x + y for x, y in zip(p, q))
            term = tuple(q[j] * dot(u, v) - v[j] * dot(q, u) for j in range(3))
            result[k] = tuple(a + b for a, b in zip(result.get(k, (0, 0, 0)), term))
            branches.append({"p": p, "q": q, "k": k, "raw_i_numerator_over_4": term})
    return {k: v for k, v in result.items() if any(v)}, branches


HASH = "218cd4a23ecf427e5cc5676da6d3a3909fbb1d9991784af3d87c55d044aea144"
I = G(0, 1)
O = (G(), G(), G())
E1, E2 = (1, 0, 0), (0, 1, 0)
NAMES = "ABSTXYZW"
REPS = ("ABSXW", "ABTXY", "ASTXW", "ASXYZ", "ATXYZ", "STXYZW")


def bar(x):
    return tuple(bar(v) for v in x) if isinstance(x, tuple) else G.cast(x).bar()


def scale(v, t):
    return tuple(x*t for x in v)


def plus(*vs):
    return tuple(map(sum, zip(*vs)))


def cross(x, y):
    return tuple(x[(i+1)%3]*y[(i+2)%3]-x[(i+2)%3]*y[(i+1)%3] for i in range(3))


def geom(k, l):
    U, V, s = dot(k, k), dot(l, l), dot(k, l)
    d = U*V-s*s
    assert d
    return U, V, d, cross(k, l), scale(plus(scale(l, U), scale(k, -s)), F(1,d)), scale(plus(scale(k, V), scale(l, -s)), F(1,d))


def data(k, l, coords):
    U, V, d, n, u, v = geom(k, l)
    al, a, be, b = map(G.cast, coords)
    return plus(scale(u, al), scale(n, a)), plus(scale(v, be), scale(n, b))


def fields(k, l, a, b):
    assert not dot(k, a) and not dot(l, b)
    al, be = dot(l, a), dot(k, b)
    return dict(zip(NAMES, (dot(a,a), dot(b,b), dot(a,b), dot(a,bar(b)), scale(b,al), scale(a,be), scale(bar(b),al), scale(a,bar(be)))))


def signed(k, l, f):
    modes = (scale(k,2), scale(l,2), plus(k,l), plus(k,scale(l,-1)))
    vals = (scale(k,f["A"]), scale(l,f["B"]),
            plus(scale(modes[2],f["S"]),scale(f["X"],-1),scale(f["Y"],-1)),
            plus(scale(modes[3],f["T"]),f["Z"],scale(f["W"],-1)))
    pos = {m:v for m,v in zip(modes,vals) if any(v)}
    return pos | {scale(m,-1):scale(bar(v),-1) for m,v in pos.items()}


def proj(m, v):
    sig = dot(m,v)/G(dot(m,m))
    return sig, plus(v,scale(m,-sig))


def recon(k, l, ea, eb, h):
    """Only k,l, energies and the named subobserver reach this function."""
    z = dict(h)
    if not ea or not eb:
        return dict(A=z["A"] if ea else G(), B=z["B"] if eb else G(), S=G(), T=G(), X=O, Y=O, Z=O, W=O)
    U,V,d,n,u,v = geom(k,l)
    x,y = z.get("X",O), z.get("Y",z.get("W",O))
    if "A" not in z and "B" not in z:
        X,Y,Z,W = (z[key] for key in "XYZW")
        z["A"] = (ea*dot(Y,W)/dot(Y,bar(Y)) if any(Y) else
                  (z["S"]*z["T"]+F(U,d)*dot(X,Z))/eb)
        z["B"] = (eb*dot(X,bar(Z))/dot(X,bar(X)) if any(X) else
                  (z["S"]*bar(z["T"])+F(V,d)*dot(Y,bar(W)))/ea)
        return z
    if any(x) and any(y):
        q = dot(k,x)
        if "Y" not in z:
            z["Y"] = scale(z["W"],q/dot(l,z["W"]))
        a0 = scale(z["Y"],1/q)
        size = ea/dot(a0,bar(a0))
        if "Z" in z:
            t = dot(k,z["Z"])/bar(q)
        elif "W" in z:
            t = dot(l,z["W"])/bar(q)
        elif z["A"]:
            t = z["A"]/(size*dot(a0,a0))
        elif z["B"]:
            t = dot(x,x)/(size*z["B"])
        else:
            t = z["T"]/dot(a0,bar(x))
        return dict(A=t*size*dot(a0,a0), B=dot(x,x)/(t*size),
                    S=dot(a0,x), T=t*dot(a0,bar(x)), X=x, Y=z["Y"],
                    Z=scale(bar(x),t), W=scale(z["Y"],t*bar(q)/q))
    if not any(x):
        ta = z["A"]/ea
        if "S" not in z:
            z["S"] = ta*bar(z["T"])
        z["T"] = ta*bar(z["S"])
        if "Y" not in z:
            z["Y"] = scale(bar(z["W"]),ta)
        z["W"] = scale(bar(z["Y"]),ta)
        yn, ab = dot(n,z["Y"])/d, z["S"]/d
        z["B"] = (F(V,d)*yn*yn+d*ab*ab)/(z["A"]/d)
        z["X"],z["Z"] = O,O
        return z
    xb = dot(n,x)/d
    if "B" in z:
        tb = z["B"]/eb
    elif "Z" in z:
        tb = xb/(dot(n,z["Z"])/d)
    elif z["T"]:
        tb = z["S"]/z["T"]
    else:
        tb = (xb/bar(xb))/(z["A"]/ea)
    if "S" not in z:
        z["S"] = tb*z["T"]
    z.update(B=tb*eb, T=z["S"]/tb, Z=scale(x,1/tb), Y=O, W=O)
    return z


def reindex(h, operation):
    if operation == "swap":
        names, conjugated = "BASTYXWZ", "TZW"
    else:
        names, conjugated = "ABTSZWXY", "B"
    return {new:bar(h[old]) if new in conjugated else h[old]
            for new,old in zip(NAMES,names) if old in h}


def consume(k,l,ea,eb,h):
    """Uniform consumer for any sufficient named menu on the given stratum."""
    for actions in [(),("swap",),("bar",),("swap","bar")]:
        g = dict(h)
        for op in actions:
            g = reindex(g,op)
        swapped = "swap" in actions
        aa,bb = (eb,ea) if swapped else (ea,eb)
        for rep in REPS:
            if not set(rep)<=g.keys() or ("A" not in rep and not aa*bb):
                continue
            if not aa and "B" not in rep and bb:
                continue
            result = recon(l if swapped else k,k if swapped else l,aa,bb,{s:g[s] for s in rep})
            for op in reversed(actions):
                result = reindex(result,op)
            return result
    raise ValueError("unsupported observation menu for this domain")


def masks(fields1, fields2):
    return frozenset(s for s in NAMES if fields1[s] != fields2[s])


def fmt(seq):
    return "".join(x for x in NAMES if x in seq)


def orbit_names(rep):
    swap = str.maketrans("ABXYZW","BAYXWZ")
    conj = str.maketrans("STXYZW","TSZWXY")
    return {fmt(s) for s in (rep,rep.translate(swap),rep.translate(conj),rep.translate(swap).translate(conj))}


def transform(v, swap, conj):
    a,b,c,d = v
    if swap:
        a,b,c,d = c,d,a,b
    if conj:
        c,d = bar(c),bar(d)
    return a,b,c,d


def table(coords, raw, k=E1, l=E2):
    a,b = data(k,l,coords)
    e = dot(a,bar(a)),dot(b,bar(b))
    f = fields(k,l,a,b)
    spectrum = {k:a,l:b,scale(k,-1):bar(a),scale(l,-1):bar(b)}
    r,branches = raw(spectrum)
    assert len(branches)==16 and r==signed(k,l,f) and (0,0,0) not in r
    return e,f,r


def minimal(sets):
    answers = []
    for size in range(9):
        for names in itertools.combinations(NAMES,size):
            m = frozenset(names)
            if all(m & s for s in sets) and not any(t<=m for t in answers):
                answers.append(m)
    return sorted(map(fmt,answers))


def encode(q):
    if isinstance(q,(tuple,list)):
        return [encode(z) for z in q]
    z = G.cast(q)
    return [str(z.r),str(z.i)]


def main(raw):
    seeds = (
        ((0,1,0,1),(0,I,0,I)), ((1,0,0,1),(I,0,0,I)),
        ((1,I,0,1),(I,-1,0,I)), ((1,I,0,1),(I,1,0,I)),
        ((1,0,1,I),(I,0,I,-1)), ((0,1,0,1),(0,1,0,-1)),
        ((1,I,1,I),(I,-1,I,-1)), ((1,0,0,1),(1,0,0,-1)))
    witnessed = {}
    for pair in seeds:
        for sw,cj in itertools.product((False,True),repeat=2):
            uu,vv = (transform(v,sw,cj) for v in pair)
            if pair == seeds[6] and cj:
                uu,vv = (1,I,1,I),(I,-1,-I,1)
            e,f,r = table(uu,raw)
            e2,f2,r2 = table(vv,raw)
            assert e==e2 and r!=r2
            key = fmt(masks(f,f2))
            m = next(m for m in sorted(r.keys()|r2.keys()) if r.get(m,O)!=r2.get(m,O))
            witnessed[key] = dict(coords=[encode(uu),encode(vv)],frequency=m,raw_over_i=[encode(r.get(m,O)),encode(r2.get(m,O))])
    assert len(witnessed)==23
    full = {frozenset(s) for s in witnessed}
    active = minimal(full)
    assert set(active)==set.union(*(orbit_names(s) for s in REPS))
    assert len(active)==19
    half = minimal(full | {frozenset("A")})
    for sw in (False,True):
        e,f,r = table(transform((0,1,0,0),sw,False),raw)
        e2,f2,r2 = table(transform((0,I,0,0),sw,False),raw)
        assert e==e2 and r!=r2
        full.add(masks(f,f2))
    inclusive = minimal(full)
    assert set(inclusive)==orbit_names(REPS[0])|orbit_names(REPS[1])
    # Nonorthogonal unequal lengths and oblique components exercise reconstruction.
    cases = [E1+E2, (1,2,0,0,1,2), (2,-1,1,1,1,0)]
    patterns = list(itertools.product((0,1,I),repeat=4)) + [
        (1+I,1-I,2,2*I),(I,2,2+I,-1),(G(F(1,2),F(2,3)),G(-2,1),1-I,F(3,7))]
    tests = 0
    menu_tests = 0
    for waves in cases:
        k,l = waves[:3],waves[3:]
        for coords in patterns:
            e,f,r = table(coords,raw,k,l)
            for rep in REPS if all(e) else REPS[:2]:
                assert recon(k,l,*e,{s:f[s] for s in rep})==f, (k,l,coords,rep)
                tests += 1
            if coords in ((0,1,0,1),(1,I,0,1),(0,1,I,1),(1,I,1,I),(0,1,0,0),(0,0,0,1),(0,0,0,0)):
                for names in active if all(e) else inclusive:
                    assert consume(k,l,*e,{s:f[s] for s in names})==f,(coords,names)
                    menu_tests += 1
    quotient = {}
    for u,v in [((1,1,0,1),(-1,1,0,1)),((0,1,1,1),(0,1,-1,1)),((0,1,1,1),(0,1,1,-1))]:
        e,f,r = table(u,raw)
        e2,f2,r2 = table(v,raw)
        m = (1,1,0)
        assert e==e2 and any(cross(r[m],r2[m]))
        quotient[fmt(masks(f,f2))] = [encode(r[m]),encode(r2[m])]
    assert set(quotient)=={"XZ","YW","ST"}
    mixed = set()
    for sw,cj in itertools.product((False,True),repeat=2):
        left,right = [transform(v,sw,cj) for v in ((0,1,1,1),(0,I,I,-I))]
        e,f,r = table(left,raw)
        e2,f2,r2 = table(right,raw)
        assert e==e2 and any(cross(r[(1,1,0)],r2[(1,1,0)]))
        for names in itertools.product("ST","XZ","YW"):
            if all(f[s]==f2[s] for s in names):
                mixed.add(fmt(names))
    assert len(mixed)==6 and not {"SXY","TZW"} & mixed
    for sw in (False,True):
        u,v = (transform(t,sw,False) for t in [(1,1,0,0),(1,I,0,0)])
        e,f,r = table(u,raw)
        e2,f2,r2 = table(v,raw)
        assert e==e2 and bool(r)!=bool(r2)
        assert masks(f,f2)==frozenset("B" if sw else "A")
    proj_essential = []
    for s,row in witnessed.items():
        vector_diff = set(s) & set("XYZW")
        if len(vector_diff)!=1:
            continue
        def coords(v):
            return [G(F(x),F(y)) for x,y in v]
        rs = [table(coords(v),raw)[2] for v in row["coords"]]
        if any(proj(m,rs[0].get(m,O))[1]!=proj(m,rs[1].get(m,O))[1] for m in rs[0].keys()|rs[1].keys()):
            proj_essential.extend(vector_diff)
    assert set(proj_essential)==set("XYZW")
    first = []
    for u in [(0,F(1,2),0,F(1,2)),(F(1,2),0,0,F(1,2))]:
        e,f,r = table(u,raw)
        m = (1,1,0)
        sig,p = proj(m,r[m])
        first.append(dict(energy=encode(e),plus_raw_over_i=encode(r[m]),sigma_over_i=encode(sig),
                          projected_over_i=encode(p),projected_support_size=sum(any(proj(m,v)[1]) for m,v in r.items())))
    assert [z["projected_support_size"] for z in first]==[0,4]
    return dict(source_sha256=HASH,field_symbols={"A":"Jk","B":"Jl"},
                witness_coordinates="(alpha,a,beta,b) for A=alpha*u+a*n, B=beta*v+b*n; Gaussian codes [Re,Im]",
                source_baseline=first,exact_fiber_witnesses=witnessed,nonzero_minimal=active,
                full_minimal=inclusive,half_A_nonzero_minimal=half,full_consumer_symmetry_checks=menu_tests,nonzero_truth_positive_subsets=sum(any(t<=frozenset(x) for t in map(frozenset,active)) for n in range(9) for x in itertools.combinations(NAMES,n)),
                test_fields=len(cases)*len(patterns),representative_reconstructions=tests,translation_lower_bound=quotient,translation_mixed_three_rejected=sorted(mixed),
                projected_indispensable_within_XYZW=sorted(set(proj_essential)))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source",type=Path,help="pinned original check_polarization.py")
    args = ap.parse_args()
    raw = raw_vortex
    if args.source:
        data_bytes=args.source.read_bytes()
        assert hashlib.sha256(data_bytes).hexdigest()==HASH
        def extract(tree):
            return ast.Module([n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in {"dot","raw_vortex"}],[])
        src = extract(ast.parse(data_bytes))
        assert ast.dump(src)==ast.dump(extract(ast.parse(Path(__file__).read_bytes())))
        namespace = {}
        exec(compile(src,str(args.source),"exec"),namespace)
        raw = namespace["raw_vortex"]
    print(json.dumps(main(raw),indent=2,ensure_ascii=False))
