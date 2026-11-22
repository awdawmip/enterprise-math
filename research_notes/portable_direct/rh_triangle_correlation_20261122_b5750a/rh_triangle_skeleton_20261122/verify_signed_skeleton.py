#!/usr/bin/env python3
"""Exact-rational checks for signed skeleton and downward-only phase no-go.

No external libraries or cached road values are used. This checks the finite
algebra and scope examples; the accompanying proofs have universal quantifiers.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

OUT = Path(__file__).resolve().parent


def qstr(x):
    return str(x.numerator) + '/' + str(x.denominator)


def interp(n, u, v, a, b):
    return (F(v-n, v-u)*a + F(n-u, v-u)*b)


def positive(x):
    return max(F(0), x)


def main():
    gram_checks = convex_checks = positive_support_checks = 0
    # Unequal, short, and dyadic intervals; signed endpoints exercise both
    # root-crossing directions and endpoint-only support.
    intervals = [(2, 3), (3, 8), (8, 16), (9, 15), (19, 38), (30, 33)]
    endpoint_pairs = [(F(3), F(-2)), (F(-5), F(7)), (F(-3), F(-2)),
                      (F(0), F(4)), (F(5, 3), F(9, 7)), (F(0), F(0))]
    for u, v in intervals:
        for a, b in endpoint_pairs:
            for include_right in (False, True):
                ns = list(range(u, v + int(include_right)))
                h1 = sum((F(1, n) for n in ns), F(0))
                h2 = sum((F(1, n*n) for n in ns), F(0))
                h = v-u
                ll = (v*v*h2 - 2*v*h1 + len(ns))/h**2
                lr = ((u+v)*h1 - u*v*h2 - len(ns))/h**2
                rr = (u*u*h2 - 2*u*h1 + len(ns))/h**2
                direct = sum((interp(n, u, v, a, b)**2/n**2 for n in ns), F(0))
                assert direct == ll*a*a + 2*lr*a*b + rr*b*b
                assert min(ll, lr, rr, ll*rr-lr*lr) >= 0
                gram_checks += 1
                epos = sum((positive(interp(n, u, v, a, b))**2/n**2 for n in ns), F(0))
                omega_l, omega_r = (v*h2-h1)/h, (h1-u*h2)/h
                assert epos <= omega_l*positive(a)**2 + omega_r*positive(b)**2
                convex_checks += 1
                active = [n for n in ns if interp(n, u, v, a, b) > 0]
                z1 = sum((F(1,n) for n in active), F(0))
                z2 = sum((F(1,n*n) for n in active), F(0))
                alpha, beta = (v*a-u*b)/h, (b-a)/h
                assert epos == alpha*alpha*z2 + 2*alpha*beta*z1 + beta*beta*len(active)
                positive_support_checks += 1

    X, M = 8, F(3, 2)
    nodes = [X, 2*X, 4*X, 8*X]
    vals = [F(0), -M, -M/8, F(0)]
    q = {}
    for u,v,a,b in zip(nodes, nodes[1:], vals, vals[1:]):
        for n in range(u,v):
            assert n not in q
            q[n] = interp(n,u,v,a,b)
    q[nodes[-1]] = vals[-1]
    assert sorted(q) == list(range(X,8*X+1))
    assert all(z <= 0 for z in q.values())
    slopes = [(b-a)/F(v-u) for u,v,a,b in zip(nodes,nodes[1:],vals,vals[1:])]
    masses = [slopes[j-1]-slopes[j] for j in range(1,len(slopes))]
    assert masses == [-23*M/(16*X),13*M/(32*X)]
    green_peak = F((4*X-X)*(8*X-4*X), 8*X-X)*masses[1]
    assert green_peak == 39*M/56 > 0
    full = sum((positive(z)**2/n**2 for n,z in q.items()),F(0))
    interior = sum((positive(q[n])**2/n**2 for n in range(X+1,8*X)),F(0))
    assert full == interior + positive(vals[0])**2/X**2 + positive(vals[-1])**2/(8*X)**2

    # Nonzero true endpoints independently exercise the closed-window identity.
    u,v,a,b = 7,24,F(9,2),F(7,3)
    closed = sum((positive(interp(n,u,v,a,b))**2/n**2 for n in range(u,v+1)),F(0))
    inside = sum((positive(interp(n,u,v,a,b))**2/n**2 for n in range(u+1,v)),F(0))
    assert closed-inside == a*a/u**2+b*b/v**2

    no_go_checks = 0
    strict_count = 0
    for tnum in range(-12,13):
        for dnum in range(-12,1):
            t,d = F(tnum,3),F(dnum,5)
            val = positive(t+d)-d
            assert val == max(t,-d) >= positive(t)
            no_go_checks += 1
            strict_count += int(val > positive(t))
    # Positive kernels can overlap. Downward shifts stay non-improving in the
    # combined, signed reconstruction at every grid point, with arbitrary J.
    packets = [(2,5,13,F(2),F(-3)),(2,9,13,F(-1),F(-2)),
               (5,7,9,F(1,3),F(-1,7))]
    packet_checks=0
    for n in range(2,14):
        before=after=correction=F(0)
        for l,x,r,t,d in packets:
            T = F(0) if n<l or n>r else (F((n-l)*(r-x),r-l) if n<=x else F((x-l)*(r-n),r-l))
            before += positive(t)*T
            after += positive(t+d)*T
            correction += d*T
        for J in (F(-7),F(0),F(5,3)):
            assert positive(J+after-correction) >= positive(J+before)
            packet_checks += 1

    result = {'schema':'EM_SIGNED_SKELETON_EXACT_CHECK_V1','status':'PASS',
              'arithmetic':'fractions.Fraction; exact integers and rationals',
              'gram_checks':gram_checks,'convex_endpoint_checks':convex_checks,
              'positive_support_checks':positive_support_checks,
              'downward_no_go_scalar_checks':no_go_checks,
              'downward_no_go_strict_scalar_cases':strict_count,
              'overlapping_packet_reconstruction_checks':packet_checks,
              'skeleton_strict_loss_example':{'nodes':nodes,'values':[qstr(x) for x in vals],
                  'signed_masses':[qstr(x) for x in masses],
                  'true_positive_energy':qstr(full),'positive_mass_envelope_at_4X':qstr(green_peak)},
              'scope':'Finite exact checks support accompanying universal algebraic proofs; not actual arithmetic-road examples or independent review.'}
    result['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (OUT/'signed_skeleton_checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))


if __name__ == '__main__':
    main()
