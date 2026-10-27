#!/usr/bin/env python3
"""R5: exact rational parametric N=3 hull separation certificates (author check)."""
from fractions import Fraction as F
from itertools import product

ONE = F(1)
HALF = F(1, 2)
H = ('A', 'B')
Z = ('C', 'L', 'H')


def model(c, delta, eps, pa, pb):
    c, delta, eps, pa, pb = map(F, (c, delta, eps, pa, pb))
    assert 0 < c < 1 and 0 < delta < 1 and 0 < eps < 1
    assert 0 < pb < pa < HALF
    r2 = {'C': ONE, 'L': ONE - delta, 'H': ONE + delta}
    q2 = {'C': c, 'L': (1 - c) / 2, 'H': (1 - c) / 2}
    y3 = (ONE - eps, ONE, ONE + eps)
    kh = {'A': (pa, ONE - 2*pa, pa), 'B': (pb, ONE - 2*pb, pb)}
    assert sum(q2.values()) == ONE
    assert sum(q2[z]*r2[z] for z in Z) == ONE
    leaves = []
    for h in H:
        for z in Z:
            children = list(zip(y3, kh[h])) if z == 'C' else [(r2[z], ONE)]
            for y, k in children:
                q = HALF*q2[z]*k
                p = y*q
                leaves.append((h,z,y,q,p))
    assert len(leaves) == 10 and min(min(q,p) for _,_,_,q,p in leaves) > 0
    assert sum(q for _,_,_,q,p in leaves) == sum(p for _,_,_,q,p in leaves) == ONE
    return leaves, r2, c, delta, eps, pa, pb


def observer(leaves, r2, early, late):
    op = [F(0) for _ in range(4)]
    for h,z,y,q,p in leaves:
        if not early(h): tau,r = 1, ONE
        elif not late(h,z): tau,r = 2, r2[z]
        else: tau,r = 3, y
        if r < ONE: op[0] += p
        else: op[1] += q
        op[2] += tau*p
        op[3] += tau*q
    return tuple(op)


def exhaustive(leaves, r2, s):
    full_min = (None,None)
    lr_min = (None,None)
    nfull = nlr = 0
    for bits in product((False, True), repeat=8):
        early = dict(zip(H,bits[:2]))
        late = dict(zip(product(H,Z),bits[2:]))
        o = observer(leaves,r2,lambda h:early[h],lambda h,z:late[h,z])
        value = o[0]+o[1]+s*o[3]
        if full_min[0] is None or value < full_min[0]: full_min = (value,o)
        nfull += 1
    for bits in product((False,True),repeat=4):
        early = bits[0]
        late = dict(zip(Z,bits[1:]))
        o = observer(leaves,r2,lambda h:early,lambda h,z:late[z])
        value = o[0]+o[1]+s*o[3]
        if lr_min[0] is None or value < lr_min[0]: lr_min = (value,o)
        nlr += 1
    assert (nfull,nlr)==(256,16)
    return full_min,lr_min


def bellman(c, delta, eps, pa, pb, s):
    b = (1-c)*delta/2
    dA, dB = eps*pa, eps*pb
    dm = (dA+dB)/2
    h = lambda d: min(F(0),s-b+c*min(F(0),s-d))
    full = 1+s+(h(dA)+h(dB))/2
    lr = 1+s+h(dm)
    assert lr>=full
    return full,lr,b,dA,dB,dm


def rational_witness(c,delta,eps,pa,pb):
    b = (1-c)*delta/2
    dA, dB = eps*pa, eps*pb
    dm = (dA+dB)/2
    if b <= dB:
        # LR early-stop kink at dbar, while both hidden types differ.
        s = (b+c*dm)/(1+c)
        gap = c*(dA-dB)/4
        regime = 'EARLY_ACTION_CONFLICT'
    else:
        # Both hidden histories continue at time 1; conflict is at C.
        cap = min(b,dA)
        s = (dB+cap)/2
        gap = c*(cap-dB)/4
        regime = 'TERMINAL_COLLISION_CONFLICT'
    assert s>0 and gap>0
    vf,vl,*_ = bellman(c,delta,eps,pa,pb,s)
    assert vl-vf==gap, (regime,s,vl-vf,gap)
    return s, gap,regime,vf,vl


def main():
    examples = [
        ('HIGH_B', F(1,2),F(3,4),F(1,2),F(1,3),F(1,8), F(11,96),F(5,384)),
        ('LOW_B', F(1,2),F(1,8),F(1,2),F(1,3),F(1,8), F(17,288),F(5,384)),
    ]
    for label,c,delta,eps,pa,pb,exp_s,exp_gap in examples:
        leaves,r2,*_ = model(c,delta,eps,pa,pb)
        s,gap,regime,vf,vl = rational_witness(c,delta,eps,pa,pb)
        assert (s,gap)==(exp_s,exp_gap)
        f,l = exhaustive(leaves,r2,s)
        assert (f[0],l[0]) == (vf,vl)
        assert l[0]-f[0] == gap
        print(f'{label}: b={(1-c)*delta/2} dA={eps*pa} dB={eps*pb} s={s} regime={regime}')
        print(f'{label}: FULL={vf} LR={vl} GAP={gap} ENUM=(256,16)')
        print(f'{label}: FULL_WITNESS_OBSERVER={f[1]} LR_WITNESS_OBSERVER={l[1]}')
    checks = 0
    for c,delta,eps,pa,pb in product(
        (F(1,3),F(1,2),F(2,3)),
        (F(1,8),F(3,8),F(3,4)),
        (F(1,3),F(1,2),F(2,3)),
        (F(1,3),F(2,5)),
        (F(1,8),F(1,6))
    ):
        model(c,delta,eps,pa,pb)
        rational_witness(c,delta,eps,pa,pb)
        checks += 1
    assert checks==108
    print('EXACT_RATIONAL_FAMILY_GRID=',checks,'(algebraic witness and 10 positive P/Q leaves each)')
    print('THEOREM_UNIVERSALITY=deductive piecewise Jensen proof, not inferred from grid')
    print('ALL EXACT CHECKS PASSED')


if __name__ == '__main__': main()
