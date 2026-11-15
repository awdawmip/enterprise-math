"""R178: exact positional path action, independent reference plus optional native BRC integration.

Scientific inputs: signed X6 primitive step alphabet and T_n finite transformation labels.
All tests use integers and fractions; native integration is attempted only when installed.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
import json
import random

AXES = tuple((axis, sign) for axis in range(6) for sign in (-1, 1))
RADIX = 13
DIRECTION_CODE = {s: i + 1 for i, s in enumerate(AXES)}
Q = Fraction


def add(u, v):
    return tuple(a + b for a, b in zip(u, v))


def scale(t, u):
    return tuple(t * a for a in u)


def step_vector(s):
    axis, sign = s
    return tuple(sign if i == axis else 0 for i in range(6))


def path_stats(path):
    d = (0,) * 6
    j = (0,) * 6
    h = 0
    for step in path:
        d = add(d, step_vector(step))
        j = add(j, d)
        h = RADIX * h + DIRECTION_CODE[step]
    return len(path), d, j, h


def concatenate_stats(p, q):
    m, d, j, h = path_stats(p)
    n, e, k, v = path_stats(q)
    return m + n, add(d, e), add(add(j, k), scale(n, d)), RADIX ** n * h + v


def transformations(n):
    return list(product(range(n), repeat=n))


def compose(f, g):
    # Chronological f*g = g o f
    return tuple(g[f[i]] for i in range(len(f)))


def simplex(f):
    n = len(f)
    def vertex(i):
        return tuple(int(i == k) for k in range(1, n))
    v0 = vertex(f[0])
    cols = [tuple(vertex(f[i])[r] - v0[r] for r in range(n - 1)) for i in range(1, n)]
    rows = tuple(tuple(cols[i][r] for i in range(n - 1)) for r in range(n - 1))
    return rows, v0


def affine_action(f, path):
    """Exact (n+12)-dimensional matrix and offset, with state (x[6],j[6],z[n-1],h)."""
    n = len(f)
    dim = n + 12
    m, d, j, h = path_stats(path)
    a = [[0] * dim for _ in range(dim)]
    for i in range(6):
        a[i][i] = 1
        a[6+i][6+i] = 1
        a[6+i][i] = m
    frows, foffset = simplex(f)
    for i in range(n-1):
        for k in range(n-1):
            a[12+i][12+k] = frows[i][k]
    a[-1][-1] = RADIX**m
    b = tuple(d) + tuple(j) + tuple(foffset) + (h,)
    return tuple(map(tuple, a)), b


def apply(action, x):
    a, b = action
    return tuple(sum(t * xj for t, xj in zip(row, x)) + bi for row, bi in zip(a,b))


def then(first, later):
    a,b=first
    c,d=later
    dim = len(b)
    out_a=tuple(tuple(sum(c[i][k]*a[k][j] for k in range(dim)) for j in range(dim)) for i in range(dim))
    out_b=tuple(sum(c[i][k]*b[k] for k in range(dim))+d[i] for i in range(dim))
    return out_a,out_b


def packet(terms):
    """Counter keyed by positive Fraction weight and complete affine action, with multiplicity."""
    c = Counter()
    for w, f, path, count in terms:
        assert Q(w)>0 and count>=0
        if count:
            c[(Q(w), affine_action(f,path))] += count
    return c


def packet_then(a,b):
    out=Counter()
    for (wa,fa),ca in a.items():
        for (wb,fb),cb in b.items():
            out[(wa*wb,then(fa,fb))]+=ca*cb
    return out


def execute():
    counts = {}
    first_collision = None
    for length in range(5):
        seen_code=set(); seen_moment={}; moment_collision=0
        total=0
        for p in product(AXES,repeat=length):
            total+=1
            m,d,j,h=path_stats(p)
            assert (m,h) not in seen_code
            seen_code.add((m,h))
            key=(d,j)
            if key in seen_moment:
                moment_collision+=1
                if first_collision is None:
                    first_collision=(seen_moment[key], p)
            else:
                seen_moment[key]=p
        counts[str(length)]={"path_count":total,"distinct_D_J":len(seen_moment),"moment_collision_excess":moment_collision,"distinct_positional_codes":len(seen_code)}
        if length<=3:
            assert moment_collision==0
    assert first_collision is not None and len(first_collision[0])==4
    p=(AXES[1], AXES[0], AXES[0], AXES[1])  # +e1,-e1,-e1,+e1
    q=(AXES[0], AXES[1], AXES[1], AXES[0])  # -e1,+e1,+e1,-e1
    assert path_stats(p)[:3]==path_stats(q)[:3]
    assert path_stats(p)[3]!=path_stats(q)[3]
    assert affine_action((0,1),p)!=affine_action((0,1),q)
    rng = random.Random(178)
    fs=transformations(3)
    action_pairs=0
    for _ in range(180):
        left=tuple(rng.choice(AXES) for _ in range(rng.randrange(5)))
        right=tuple(rng.choice(AXES) for _ in range(rng.randrange(5)))
        f=rng.choice(fs); g=rng.choice(fs)
        assert concatenate_stats(left,right)==path_stats(left+right)
        assert then(affine_action(f,left), affine_action(g,right)) == affine_action(compose(f,g),left+right)
        action_pairs+=1
    f=(1,0,2);g=(2,0,1)
    packet_cases=0
    for i in range(36):
        x=tuple(AXES[(i+k)%12] for k in range(i%3))
        y=tuple(AXES[(i+2*k+3)%12] for k in range((i+1)%4))
        w1=Q((i%4)+1, (i%3)+1)
        w2=Q((i%5)+1, (i%4)+1)
        a=packet([(w1,f,x,1+i%3),(w2,g,y,1)])
        b=packet([(w2,g,y,2),(w1,f,x,1)])
        actual=packet_then(a,b)
        direct=packet([(wa*wb,compose(fa,fb),pa+pb,ca*cb)
             for wa,fa,pa,ca in [(w1,f,x,1+i%3),(w2,g,y,1)]
             for wb,fb,pb,cb in [(w2,g,y,2),(w1,f,x,1)]])
        assert actual==direct
        packet_cases+=1
    native={"attempted":True,"imported":False,"passed":False,"error":None}
    try:
        from enterprise_math.brc_transport import Affine, EffectHistogram
        native["imported"]=True
        # Requires a repository environment; all entries and actions are exact Fractions.
        for n in (2,3):
            identity=tuple(range(n))
            smallpaths=[(),(AXES[0],),(AXES[1],AXES[0]),p,q]
            for path in smallpaths:
                aa,bb=affine_action(identity,path)
                native_a=Affine(aa,bb)
                assert native_a.apply((Q(0),)*len(bb))==tuple(Q(x) for x in bb)
            a=EffectHistogram.from_terms(n+12,[(Q(1,2),Affine(*affine_action(identity,p)),2)])
            b=EffectHistogram.from_terms(n+12,[(Q(3,5),Affine(*affine_action(identity,q)),3)])
            product_native=a.then(b)
            expected=Affine(*affine_action(identity,p+q))
            assert product_native.entries==((Q(3,10),expected,6),)
            assert a.alternatives(b).entries and len(a.alternatives(b).entries)==2
        native["passed"]=True
    except ModuleNotFoundError as exc:
        native["error"]="native package unavailable: "+str(exc)
    result={
        "schema":"R178_LOSSLESS_PATH_AFFINE_EXACT_VERIFICATION_V1",
        "radix":RADIX,"alphabet_size":12,"length_counts":counts,
        "first_moment_collision_length":4,
        "collision_witness":{"P":list(map(list,p)),"Q":list(map(list,q)),"shared_length_D_J":str(path_stats(p)[:3]),"P_code":path_stats(p)[3],"Q_code":path_stats(q)[3]},
        "random_matrix_composition_checks":action_pairs,"positive_packet_product_checks":packet_cases,
        "native_brc_integration":native,"exact_arithmetic":True,
        "conclusion":"REFERENCE_EXACT_PASS" if not native["passed"] else "NATIVE_EXACT_PASS"
    }
    return result


if __name__ == '__main__':
    result=execute()
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))
