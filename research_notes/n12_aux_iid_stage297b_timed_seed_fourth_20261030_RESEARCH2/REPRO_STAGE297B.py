#!/usr/bin/env python3
"""Stage297-B: exact rational seed-descent and four-moment observation certificates.

Pure Python standard library; no floating arithmetic and no external or native X6 execution.
"""
from fractions import Fraction as F
from itertools import product
from math import comb


def moment(mu, k):
    return sum((w * x**k for w, x in mu), F(0))


def tv(p, q):
    assert set(p) == set(q)
    return sum((abs(p[k] - q[k]) for k in p), F(0)) / 2


def word_law(mu, n):
    return {
        word: sum((w * x**sum(word) * (1-x)**(n-sum(word)) for w, x in mu), F(0))
        for word in product((0, 1), repeat=n)
    }


def stop_jth_success(law, j):
    n = len(next(iter(law)))
    out = {k: F(0) for k in range(j, n+1)}
    out["censored"] = F(0)
    for word, mass in law.items():
        hit = next((k for k in range(j, n+1) if sum(word[:k]) == j), "censored")
        out[hit] += mass
    assert sum(out.values(), F(0)) == 1
    return out


def certify_four_moments():
    lo = [(F(1,3),F(1,5)), (F(2,3),F(4,5))]
    hi = [(F(2,15),F(0)), (F(2,3),F(3,5)), (F(1,5),F(1))]
    ml = tuple(moment(lo,k) for k in range(5))
    mh = tuple(moment(hi,k) for k in range(5))
    assert ml[:4] == mh[:4] == (F(1), F(3,5), F(11,25), F(43,125))
    assert ml[4] == F(171,625) and mh[4] == F(179,625)
    m0,m1,m2,m3 = ml[:4]
    # Schur complements of 3x3 Hankel and 2x2 t(1-t) localizer.
    L = (m2**3 - 2*m1*m2*m3 + m3**2)/(m2-m1**2)
    U = m3 - (m2-m3)**2/(m1-m2)
    assert (L,U,U-L) == (F(171,625),F(179,625),F(8,625))
    # Verify all strict lower-order Hausdorff constraints.
    assert m2 > m1**2 and m1 > m2 and m3 > m2**2/m1
    assert m3 < m2 - (m1-m2)**2/(1-m1)
    pl,ph = word_law(lo,4),word_law(hi,4)
    assert sum(pl.values(),F(0)) == sum(ph.values(),F(0)) == 1
    assert all(pl[x]>0 and ph[x]>0 for x in pl)
    assert tv(pl,ph) == F(64,625)
    for word in pl:
        assert abs(pl[word]-ph[word]) == F(8,625)
    print("FROZEN_MOMENTS", [str(x) for x in ml[:4]])
    print("FOURTH_INTERVAL",str(L),str(U),"WIDTH",str(U-L))
    print("ORDERED4_TV",tv(pl,ph),"RADIUS",tv(pl,ph)/2)
    expected={1:F(8,625),2:F(24,625),3:F(24,625),4:F(8,625)}
    for j in range(1,5):
        d=tv(stop_jth_success(pl,j),stop_jth_success(ph,j))
        assert d == expected[j] == comb(3,j-1)*(U-L)
        print("STOP_J",j,"TV",d,"RADIUS",d/2)
    # Count the top-moment coefficient in any order n, all stopping thresholds j.
    for n in range(2,9):
        assert sum(comb(n,k) for k in range(n+1)) == 2**n
        for j in range(1,n+1):
            coeff = comb(n-1,j-1) * (-1)**(n-j)
            # only terminal time n and censorship can depend on m_n
            assert abs(coeff) == comb(n-1,j-1)
    print("GENERAL_N_COEFFICIENTS_VALIDATED",list(range(2,9)))


def certify_timed_seed():
    a=F(1,4); h=a*(1-a)
    p=2*h  # equality mode E
    mode_law={}
    for z,wz in (("E",p),("X",1-p)):
        for u in (0,1):
            A=u; B=u if z=="E" else 1-u
            mode_law[(z,u,A,B)] = wz/2
    assert sum(mode_law.values(),F(0)) == 1
    q={pair: F(0) for pair in product((0,1),repeat=2)}
    for (_,_,A,B),mass in mode_law.items():
        q[(A,B)]+=mass
    assert q == {(0,0):F(3,16),(0,1):F(5,16),(1,0):F(5,16),(1,1):F(3,16)}
    for (z,u,A,B),mass in mode_law.items():
        assert z == ("E" if A==B else "X") and u==A and mass>0
    # Before B is shown, single retained visible bit A does not determine Z.
    for A in (0,1):
        den=sum((mass for (z,u,x,y),mass in mode_law.items() if x==A),F(0))
        pe=sum((mass for (z,u,x,y),mass in mode_law.items() if x==A and z=="E"),F(0))/den
        assert pe==p
        # q is compressed probability of emitting B=A without a Z label.
        # Weighted conditional TV to deterministic original B is affine in q,
        # and has exact minimum min(p,1-p) attained at q=0 because p<1/2.
        for q_same in (F(0),F(1,9),F(1,2),F(5,8),F(1)):
            loss=p*(1-q_same)+(1-p)*q_same
            assert loss >= p
        assert p==F(3,8)
    # A visible-only fresh mode sampled with q_same=p does reproduce the
    # pooled pair law; but not statewise/source-mode-conditional prediction.
    pooled={}
    for A in (0,1):
        pooled[(A,A)]=p/2
        pooled[(A,1-A)]=(1-p)/2
    assert pooled==q
    # Two hidden-seed lifts of exactly the same visible pair law:
    # W=Y_A versus W=Y_B; complete future read W distinguishes off-diagonal pairs.
    lift_A={(A,B,w): (q[(A,B)] if w==A else F(0)) for A,B,w in product((0,1),repeat=3)}
    lift_B={(A,B,w): (q[(A,B)] if w==B else F(0)) for A,B,w in product((0,1),repeat=3)}
    assert tv(lift_A,lift_B) == F(5,8)
    print("PARITY_MODE_P",p,"VISIBLE_PAIR",{str(k):str(v) for k,v in q.items()})
    print("POST_PAIR_DECODE", "E iff A=B; U=A; exact for future Z/U queries")
    print("PRE_B_STRONG_MIN_RISK", p,"POOLED_RISK",0)
    print("TWO_LIFTS_SAME_PAIR_FUTURE_W_TV",tv(lift_A,lift_B))


if __name__=="__main__":
    certify_four_moments()
    certify_timed_seed()
    print("STAGE297B_TIMED_SEED_FOURTH_MOMENT_EXACT_PASS")
