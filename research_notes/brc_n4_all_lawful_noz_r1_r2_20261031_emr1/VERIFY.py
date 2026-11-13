#!/usr/bin/env python3
"""Exact finite BRC N=4 no-Z all-policy lower witness and universal decoders.

No external dependencies. Fraction rational arithmetic. Exhaustive check covers a
specified 1,728-policy deterministic S23 subfamily (not all randomized or T4
policies); universal theorems are analytic via total-variation contraction.
"""
from fractions import Fraction as F
from itertools import product

S = ("AU", "AV", "BU", "BV")
B = ("Q", "P")
PREPS = tuple((s, b) for s in S for b in B)
RAW = {
    "Q": {"AU": (10, 10), "AV": (20, 20), "BU": (15, 15), "BV": (15, 15)},
    "P": {"AU": (9, 11), "AV": (5, 5), "BU": (3, 27), "BV": (30, 30)},
}


def source_law(s, b):
    a, c = RAW[b][s]
    return {(s, 0): F(a, a + c), (s, 1): F(c, a + c)}


def add_scaled(dst, law, weight):
    for atom, mass in law.items():
        dst[atom] = dst.get(atom, F(0)) + weight * mass


def tv(p, q):
    return sum((abs(p.get(k, F(0)) - q.get(k, F(0))) for k in p.keys() | q.keys()), F(0)) / 2


def push(law, strategy):
    out = {}
    for (s, j), mass in law.items():
        stop2 = strategy[0]["AB" if s in ("AU", "BU") else s]
        if stop2 != "C":
            atom = (2, stop2)
        else:
            atom = (3, strategy[1]["AV" if s == "AV" else "BV" if s == "BV" else s + str(j)])
        out[atom] = out.get(atom, F(0)) + mass
    return out


def pack_lower(k, g=4):
    return F(g-k, g)


def main():
    for b in B:
        leaf = [RAW[b][s][j] for s in S for j in (0, 1) for _ in (0, 1)]
        assert len(leaf) == 16 and min(leaf) > 0 and sum(leaf) == 240
    assert len(PREPS) == 8
    assert all(sum(source_law(s,b).values(), F(0)) == 1 for s,b in PREPS)

    # Two universal reference laws for deterministic L/R encoding.
    FL, FR = {}, {}
    add_scaled(FL, source_law("AU", "Q"), F(1,4))
    add_scaled(FL, source_law("AU", "P"), F(1,4))
    add_scaled(FL, source_law("AV", "Q"), F(1,2))
    FR[("BU",0)] = F(1,10)
    FR[("BU",1)] = F(2,5)
    add_scaled(FR, source_law("BV", "Q"), F(1,2))
    F1 = {}
    add_scaled(F1, FL, F(1,2))
    add_scaled(F1, FR, F(1,2))
    assert sum(FL.values(),F(0)) == sum(FR.values(),F(0)) == sum(F1.values(),F(0)) == 1
    for s,b in PREPS:
        law=source_law(s,b)
        group = FL if s in ("AU", "AV") else FR
        assert tv(law,group) == F(1,2), (s,b,"two-code")
        assert tv(law,F1) == F(3,4), (s,b,"one-code")
    print("SOURCE_LEAVES: P=16/240 Q=16/240, positive and normalized; prepared states=8")
    print("FULL_FUTURE_TV: R1=3/4 each input; R2=1/2 each input")
    print("FL:", sorted((str(k),str(v)) for k,v in FL.items()))
    print("FR:", sorted((str(k),str(v)) for k,v in FR.items()))

    # Hdagger: stage-2 AV->P, BV->Q; AU/BU continue;
    # time-3 AU->P, BU->Q. Equal-LR classes get equal decisions.
    hd = ({"AB":"C", "AV":"P", "BV":"Q"},
          {"AU0":"P", "AU1":"P", "BU0":"Q", "BU1":"Q", "AV":"P", "BV":"Q"})
    prototypes={s:push(source_law(s,"Q"),hd) for s in S}
    assert prototypes == {"AU":{(3,"P"):F(1)},"AV":{(2,"P"):F(1)},
                          "BU":{(3,"Q"):F(1)},"BV":{(2,"Q"):F(1)}}
    assert all(push(source_law(s,b),hd) == prototypes[s] for s,b in PREPS)
    assert len({next(iter(x)) for x in prototypes.values()})==4
    assert pack_lower(1)==F(3,4) and pack_lower(2)==F(1,2)
    print("LAWFUL_H_DAGGER: AU=(3,P), AV=(2,P), BU=(3,Q), BV=(2,Q)")
    print("DISJOINT_PACKING: R1>=3/4; R2>=1/2")

    # Exhaustive deterministic policy subfamily: at T2, one common AU/BU
    # action, independent AV and BV actions, each in C/P/Q. At T3, six
    # contemporaneous likelihood-ratio classes independently P/Q.
    classes=("AU0","AU1","AV","BU0","BU1","BV")
    n=0
    max1=max2=F(0)
    worst=None
    for a_ab,a_av,a_bv in product(("C","P","Q"),repeat=3):
        stage2={"AB":a_ab,"AV":a_av,"BV":a_bv}
        for picks in product(("P","Q"),repeat=6):
            h=(stage2,dict(zip(classes,picks)))
            d1=push(F1,h)
            dl,dr=push(FL,h),push(FR,h)
            for s,b in PREPS:
                t=push(source_law(s,b),h)
                e1=tv(t,d1)
                e2=tv(t,dl if s in ("AU","AV") else dr)
                assert e1<=F(3,4) and e2<=F(1,2), (h,s,b,e1,e2)
                if e1>max1:max1=e1
                if e2>max2:max2=e2
            n+=1
    assert n==27*64 and max1==F(3,4) and max2==F(1,2)
    print("AUDIT: 27 T2 kernels x 64 T3 ratio maps =",n,"lawful deterministic subfamily")
    print("FULL_PUBLIC_OUTPUT_EXACT_COMPARISONS:",n*len(PREPS)*2)
    print("AUDIT_MAX: R1=",max1,"R2=",max2)
    print("THEOREM: all S23 and S2, no-Z (T,Decision), R1=3/4 R2=1/2")
    print("SCOPE: complete randomized/adaptive/T4 universal claims follow analytically by TV data processing, not enumeration")
    print("PASS_BRC_N4_ALL_LAWFUL_NOZ_R1_R2_EXACT_20261031")

if __name__ == '__main__': main()
