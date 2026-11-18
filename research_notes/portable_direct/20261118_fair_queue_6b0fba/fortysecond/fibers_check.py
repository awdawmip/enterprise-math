#!/usr/bin/env python3
"""Finite-field P11 moment and congruence-ring lifts. Python standard library."""
from collections import Counter
from math import isqrt
import json


class Field:
    """Elements encoded by base-p digits, coefficients in ascending degree."""
    def __init__(self,p,degree=1):
        self.p = p
        self.degree = degree
        q = self.q = p**degree
        if degree == 1:
            self.add = [[(a+b)%p for b in range(p)] for a in range(p)]
            self.mul = [[(a*b)%p for b in range(p)] for a in range(p)]
        else:
            if degree == 2:
                nonsquare = next(d for d in range(2,p) if pow(d,(p-1)//2,p) == p-1)
                relation = [nonsquare,0]
            elif (p,degree) == (3,3):
                relation = [1,1,0]  # X^3=X+1; the cubic has no root over F_3.
            else:
                raise ValueError('unsupported verification field')
            digits = [[(a//p**i)%p for i in range(degree)] for a in range(q)]
            def encode(xs):
                return sum(v%p * p**i for i,v in enumerate(xs))
            def multiply(a,b):
                out = [0]*(2*degree-1)
                for i,x in enumerate(a):
                    for j,y in enumerate(b):
                        out[i+j] += x*y
                for k in range(2*degree-2,degree-1,-1):
                    for j,h in enumerate(relation):
                        out[k-degree+j] += h*out[k]
                return encode(out[:degree])
            self.add = [[encode([x+y for x,y in zip(a,b)]) for b in digits] for a in digits]
            self.mul = [[multiply(a,b) for b in digits] for a in digits]
        self.neg = [row.index(0) for row in self.add]
        self.inv = [None]+[row.index(1) for row in self.mul[1:]]
        self.sq = [self.mul[a][a] for a in range(q)]
        self.chi = [-1]*q
        for sq in self.sq:
            self.chi[sq] = 1
        self.chi[0] = 0


def verify_field(K):
    q,p = K.q,K.p
    add,mul,neg,sq,ch = K.add,K.mul,K.neg,K.sq,K.chi
    eps,e2,em2 = ch[neg[1]],ch[2],ch[neg[2]]
    cm = -sum(ch[mul[add[x][neg[1]]][add[sq[x]][neg[K.inv[2]]]]] for x in range(q))
    branch = -sum(ch[mul[x][add[1][neg[sq[x]]]]] for x in range(q))
    # Count actual projective primitive-parameter classes; s=1 because B is a unit.
    par = Counter()
    for r in range(q):
        A,B=add[sq[r]][neg[1]],add[r][r]
        if A and B and sq[A] != sq[B]:
            par[mul[B][K.inv[A]]] += 1
    traces = []
    weighted_all = 0
    for t in range(q):
        trace = -sum(ch[mul[mul[u][add[1][neg[u]]]][add[u][neg[sq[t]]]]] for u in range(q))
        weighted_all += ch[add[1][sq[t]]]*trace
        if t in (0,1,neg[1]):
            continue
        assert par[t] == 1 + ch[add[1][sq[t]]]
        P,Q = add[1][t],add[1][neg[t]]
        # Affine Z=1, then the disjoint infinity chart D=1.
        original_count = (1+eps)**2 + sum(
            (1+ch[add[sq[P]][neg[sq[d]]]])*(1+ch[add[sq[Q]][neg[sq[d]]]])
            for d in range(q))
        assert q+1-original_count == trace
        traces.append((t,trace))
    aop = sum(ch[mul[mul[mul[x][y]][mul[add[x][1]][add[y][1]]]][add[x][y]]]
              for x in range(q) for y in range(q))
    assert aop == e2*(cm*cm-q)
    assert weighted_all == -1-e2*cm*cm
    assert sum(t for _,t in traces) == -2*(1+eps)
    moment = sum(par[s]*a for s,a in traces)
    count = sum(par.values())
    assert count == q-5-2*e2
    assert moment == -4-2*eps-2*em2-e2*cm*cm
    strict = sum(par[s]*a for s,a in traces if add[1][sq[s]])
    assert strict == moment-(1+eps)*branch
    assert sum(par[s] for s,a in traces if add[1][sq[s]]) == count-(1+eps)
    if K.degree == 1:
        reps = [(x,isqrt((p-x*x)//2)) for x in range(1,isqrt(p)+1,2)
                if (p-x*x)%2 == 0 and 2*isqrt((p-x*x)//2)**2+x*x == p]
        assert (len(reps) == 1) if em2 == 1 else (not reps)
        assert cm*cm == (4*reps[0][0]**2 if reps else 0)
    return dict(p=p,degree=K.degree,projective_parameters=count,sum_traces=moment,
                sum_fibre_points=count*(q+1)-moment,cm_trace=cm,
                smooth_parameters_with_nonzero_hypotenuse=count-1-eps,
                trace_sum_with_nonzero_hypotenuse=strict)


def frobenius_power_sum(trace,norm,r):
    a,b = 2,trace
    for k in range(1,r):
        a,b = b,trace*b-norm*a
    return b


def ring_test(p,k,base):
    m = p**k
    roots = Counter(x*x%m for x in range(m))
    counts = Counter()
    par = 0
    for r in range(m):
        A,B = (r*r-1)%m,(2*r)%m
        if A*B*(A*A-B*B)%p == 0:
            continue
        t = B*pow(A,-1,m)%m
        P,Q = 1+t,1-t
        affine = sum(roots[(P*P-d*d)%m]*roots[(Q*Q-d*d)%m] for d in range(m))
        near_infinity = sum(roots[(P*P*z*z-1)%m]*roots[(Q*Q*z*z-1)%m] for z in range(0,m,p))
        counts[r%p] += affine+near_infinity
        par += 1
    assert par == base['projective_parameters']*p**(k-1)
    assert sum(counts.values()) == base['sum_fibre_points']*p**(2*k-2)
    if k>1:
        base_by_r = dict(ring_test(p,1,base)['counts_by_base_parameter'])
        assert {r:v for r,v in counts.items()} == {r:v*p**(2*k-2) for r,v in base_by_r.items()}
    return dict(p=p,k=k,parameters=par,point_parameter_pairs=sum(counts.values()),
                counts_by_base_parameter=sorted(counts.items()))


def main():
    primes = [p for p in range(3,252,2) if all(p%d for d in range(2,isqrt(p)+1))]
    rows = [verify_field(Field(p)) for p in primes]
    base = {row['p']:row for row in rows}
    for p,r in [(3,2),(3,3),(5,2),(7,2),(11,2),(13,2)]:
        row = verify_field(Field(p,r))
        c = base[p]['cm_trace']
        assert frobenius_power_sum(c,p,r) == row['cm_trace']
        char = lambda n: (1 if pow(n%p,(p-1)//2,p)==1 else -1)
        q = p**r
        pred_zeta = (q*q-4*q-1+2*char(-1)**r+2*char(-2)**r-2*char(2)**r
                     +char(2)**r*frobenius_power_sum(c*c-2*p,p*p,r))
        assert pred_zeta == row['sum_fibre_points']
        rows.append(row)
    finite_rings = [ring_test(p,k,base[p]) for p,k in
                    [(3,2),(5,2),(5,3),(7,2),(11,2),(13,2),(17,2)]]
    print(json.dumps(dict(prime_fields=len(primes),fields=rows,congruence_rings=finite_rings),
                     sort_keys=True,indent=2))


if __name__ == '__main__':
    main()
