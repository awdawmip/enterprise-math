#!/usr/bin/env python3
"""Exact task-local checker for the P000 P11 genuine-doubleton Diophantine normal form.

Standard-library only.  Symbolic proofs are stated in the Return; this checker
verifies the canonical rank-one coordinates, the frozen examples, the exact
root-box regression declared at |root| <= 20, and the genus-one obstruction
certificate by exact rational polynomial arithmetic.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import reduce
from itertools import combinations
from math import gcd, isqrt

R = 20
C1_EDGES = ((0,0),(0,1),(1,0),(1,2),(2,1),(2,2))
C2_EDGES = ((0,1),(0,2),(1,0),(1,2),(2,0),(2,1))


def pairable(h, t):
    d2 = h*h - 4*t
    if d2 < 0:
        return False
    d = isqrt(d2)
    return d*d == d2 and (d-h) % 2 == 0


def root_pair(h, t):
    assert pairable(h, t)
    d = isqrt(h*h - 4*t)
    a = (h-d)//2
    b = (h+d)//2
    assert a <= b and a+b == h and a*b == t
    return a, b


def build_root_box(R):
    ht = {}
    h2t = defaultdict(set)
    t2pairs = defaultdict(list)
    for a in range(-R, R+1):
        for b in range(a, R+1):
            h, t = a+b, a*b
            assert (h,t) not in ht or ht[(h,t)] == (a,b)
            ht[(h,t)] = (a,b)
            h2t[h].add(t)
            t2pairs[t].append((a,b))
    return ht, h2t, t2pairs


def enumerate_class(ht, h2t, cls):
    out = []
    for H in combinations(sorted(h2t), 3):
        h0,h1,h2 = H
        A, B = h1-h0, h2-h1
        if cls == "C1":
            S0 = h2t[h0] & h2t[h1]
            S1 = h2t[h0] & h2t[h2]
            S2 = h2t[h1] & h2t[h2]
            for t0 in S0:
                for t1 in S1:
                    if not t0 < t1:
                        continue
                    C = t1-t0
                    if (A*C) % B:
                        continue
                    D = (A*C)//B
                    t2 = t1+D
                    if t2 > t1 and t2 in S2:
                        out.append((H,(t0,t1,t2)))
        else:
            S0 = h2t[h1] & h2t[h2]
            S1 = h2t[h0] & h2t[h2]
            S2 = h2t[h0] & h2t[h1]
            for t0 in S0:
                for t1 in S1:
                    if not t0 < t1:
                        continue
                    C = t1-t0
                    if (B*C) % A:
                        continue
                    D = (B*C)//A
                    t2 = t1+D
                    if t2 > t1 and t2 in S2:
                        out.append((H,(t0,t1,t2)))
    return out


def edge_set(cls):
    return C1_EDGES if cls == "C1" else C2_EDGES


def root_gcd(cls, H, T, ht):
    vals = []
    for i,j in edge_set(cls):
        vals.extend(ht[(H[i],T[j])])
    return reduce(gcd, (abs(x) for x in vals), 0)


def sign_pattern(xs):
    return ''.join('-' if x < 0 else '0' if x == 0 else '+' for x in xs)


def primitive_row(row):
    a,b = row
    d = gcd(abs(a),abs(b))
    assert d > 0
    p,q = a//d, b//d
    if p < 0 or (p == 0 and q < 0):
        p,q = -p,-q
    assert gcd(abs(p),abs(q)) == 1
    return p,q


def transition_factor(top, bottom):
    """Canonical rank-one factor of equal-product sorted root pairs.

    For top=(a,b), bottom=(c,d), form M=[[a,c],[d,b]].
    det M=ab-cd=0.  Return primitive (p,q) and (u,v) with
    M=[[u*p,u*q],[v*p,v*q]], primitive row sign normalized.
    """
    a,b = top
    c,d = bottom
    assert a <= b and c <= d and a*b == c*d
    M0 = (a,c)
    M1 = (d,b)
    assert M0 != (0,0) or M1 != (0,0)
    p,q = primitive_row(M0 if M0 != (0,0) else M1)

    def coefficient(row):
        r,s = row
        if p != 0:
            assert r % p == 0
            k = r//p
            assert s == k*q
            return k
        assert q == 1
        assert r == 0
        return s

    u = coefficient(M0)
    v = coefficient(M1)
    assert (u*p,u*q) == M0
    assert (v*p,v*q) == M1
    return p,q,u,v


def c1_columns(H,T,ht):
    return (
        (ht[(H[0],T[0])], ht[(H[1],T[0])]),
        (ht[(H[0],T[1])], ht[(H[2],T[1])]),
        (ht[(H[1],T[2])], ht[(H[2],T[2])]),
    )


def c1_normal_form(H,T,ht):
    pars = [transition_factor(*col) for col in c1_columns(H,T,ht)]
    (p0,q0,u0,v0),(p1,q1,u1,v1),(p2,q2,u2,v2) = pars
    # Exact row compatibility.
    assert u0*p0 + v0*q0 == u1*p1 + v1*q1 == H[0]
    assert u0*q0 + v0*p0 == u2*p2 + v2*q2 == H[1]
    assert u1*q1 + v1*p1 == u2*q2 + v2*p2 == H[2]
    # Exact products.
    assert (u0*v0*p0*q0, u1*v1*p1*q1, u2*v2*p2*q2) == T
    A = (q0-p0)*(u0-v0)
    B = (q2-p2)*(u2-v2)
    C = T[1]-T[0]
    D = T[2]-T[1]
    assert (A,B) == (H[1]-H[0],H[2]-H[1])
    assert (q1-p1)*(u1-v1) == A+B
    assert A > 0 and B > 0 and C > 0 and D > 0
    assert A*C == B*D
    m = reduce(gcd, (abs(z) for z in (u0,v0,u1,v1,u2,v2)), 0)
    assert m == root_gcd("C1",H,T,ht)
    return pars, m


def involution_c1_to_c2(H,T):
    return tuple(-h for h in reversed(H)), T


def poly_trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def poly_add(a,b):
    n=max(len(a),len(b)); out=[0]*n
    for i in range(n):
        out[i]=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
    return poly_trim(out)


def poly_mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return poly_trim(out)


def poly_scale(a,c):
    return poly_trim([c*x for x in a])


def poly_deriv(a):
    if len(a)<=1:
        return [0]
    return poly_trim([i*a[i] for i in range(1,len(a))])


def poly_divmod_q(a,b):
    a=poly_trim([Fraction(x) for x in a])
    b=poly_trim([Fraction(x) for x in b])
    assert b != [0]
    if len(a)<len(b):
        return [Fraction(0)],a
    q=[Fraction(0)]*(len(a)-len(b)+1)
    while a != [0] and len(a)>=len(b):
        k=len(a)-len(b)
        c=a[-1]/b[-1]
        q[k]+=c
        for j in range(len(b)):
            a[j+k]-=c*b[j]
        a=poly_trim(a)
    return poly_trim(q),poly_trim(a)


def poly_gcd_q(a,b):
    a=poly_trim([Fraction(x) for x in a])
    b=poly_trim([Fraction(x) for x in b])
    while b != [0]:
        _,r=poly_divmod_q(a,b)
        a,b=b,r
    if a == [0]:
        return [Fraction(0)]
    lead=a[-1]
    return poly_trim([x/lead for x in a])


def obstruction_cubic(u0,u1,u2):
    return (
        11220*u0**3 - 45405*u0*u0*u1 - 33552*u0*u0*u2
        + 49515*u0*u1*u1 + 55200*u0*u1*u2 - 96*u0*u2*u2
        - 16296*u1**3 - 22667*u1*u1*u2 + 163*u1*u2*u2
        + 120*u2**3
    )


def obstruction_v(u0,u1,u2):
    return (
        Fraction(-55*u0 + 45*u1 + 16*u2, 13),
        Fraction(-120*u0 + 97*u1 + 16*u2, 13),
        Fraction(-96*u0 + 75*u1 + 5*u2, 13),
    )


def obstruction_collision(u0,u1,u2):
    # Skeleton ((5,-1),(4,-1),(5,3)).  Row equations solved by obstruction_v.
    v0,v1,v2=obstruction_v(u0,u1,u2)
    p0,q0=5,-1; p1,q1=4,-1; p2,q2=5,3
    A=(q0-p0)*(Fraction(u0)-v0)
    B=(q2-p2)*(Fraction(u2)-v2)
    t0=Fraction(u0)*v0*p0*q0
    t1=Fraction(u1)*v1*p1*q1
    t2=Fraction(u2)*v2*p2*q2
    return A*(t1-t0)-B*(t2-t1)


def main():
    ht,h2t,t2pairs=build_root_box(R)
    assert len(ht) == (2*R+1)*(2*R+2)//2 == 861

    # Rank-one factor lemma regression over every equal-product root-pair transition.
    factor_checks=0
    for pairs in t2pairs.values():
        for top in pairs:
            for bottom in pairs:
                if sum(top)==sum(bottom):
                    continue
                transition_factor(top,bottom)
                factor_checks += 1
    assert factor_checks > 0

    c1=enumerate_class(ht,h2t,"C1")
    c2=enumerate_class(ht,h2t,"C2")
    assert len(c1) == 83 and len(c2) == 83
    c1set,c2set=set(c1),set(c2)
    assert all(involution_c1_to_c2(H,T) in c2set for H,T in c1)
    assert all(involution_c1_to_c2(H,T) in c1set for H,T in c2)

    gcd_counts=Counter()
    primitive=0
    zero_column=0
    primitive_zero=0
    t_signs=Counter()
    h_signs=Counter()
    ap_c1=[]
    for H,T in c1:
        pars,m=c1_normal_form(H,T,ht)
        gcd_counts[m]+=1
        primitive += (m==1)
        zero_column += (0 in T)
        primitive_zero += (m==1 and 0 in T)
        t_signs[sign_pattern(T)] += 1
        h_signs[sign_pattern(H)] += 1
        if H[1]-H[0] == H[2]-H[1] and T[1]-T[0] == T[2]-T[1]:
            ap_c1.append((H,T))
        # Primitive quotient is exact and remains a genuine C1 solution.
        assert all(h % m == 0 for h in H)
        assert all(t % (m*m) == 0 for t in T)
        H0=tuple(h//m for h in H)
        T0=tuple(t//(m*m) for t in T)
        assert all(pairable(H0[i],T0[j]) for i,j in C1_EDGES)
        A0,B0=H0[1]-H0[0],H0[2]-H0[1]
        C0,D0=T0[1]-T0[0],T0[2]-T0[1]
        assert A0*C0 == B0*D0

    assert gcd_counts == Counter({1:78,2:4,3:1})
    assert primitive == 78
    assert zero_column == 66 and primitive_zero == 61
    assert t_signs == Counter({'--0':32,'-0+':22,'0++':12,'--+':8,'---':7,'+++':2})
    assert h_signs == Counter({'--+':33,'-++':26,'+++':19,'---':4,'0++':1})
    assert ap_c1 == [
        ((-7,-4,-1),(-60,-30,0)),
        ((-7,2,11),(-120,-60,0)),
        ((-3,3,9),(-130,-70,-10)),
    ]
    # No simultaneous genuine C1+C2 point in the declared box; regression only.
    assert len(c1set & c2set) == 0

    # Retained B=6 C1 witness and a primitive non-scaling counterexample at height 9.
    b6=((-1,1,4),(-30,-12,0))
    assert b6 in c1set and root_gcd("C1",*b6,ht)==1
    counter=((-7,-3,2),(-18,-8,0))
    assert counter in c1set and root_gcd("C1",*counter,ht)==1
    assert max(abs(r) for i,j in C1_EDGES for r in ht[(counter[0][i],counter[1][j])]) == 9
    assert counter != b6

    # Canonical nonzero obstruction witness and its rank-one skeleton.
    H=(-7,11,13); T=(10,12,30)
    assert (H,T) in c1set and 0 not in T and root_gcd("C1",H,T,ht)==1
    pars,m=c1_normal_form(H,T,ht)
    assert pars == [(5,-1,-1,2),(4,-1,-1,3),(5,3,1,2)]
    assert m == 1
    assert obstruction_v(-1,-1,1) == (Fraction(2),Fraction(3),Fraction(2))
    assert obstruction_cubic(-1,-1,1) == 0

    # Exact algebraic identity on the skeleton: collision = 10/169 * cubic.
    # Degree is three, so a dense small integer grid is a deterministic identity regression.
    identity_checks=0
    for u0 in range(-2,3):
        for u1 in range(-2,3):
            for u2 in range(-2,3):
                lhs=obstruction_collision(u0,u1,u2)
                rhs=Fraction(10*obstruction_cubic(u0,u1,u2),169)
                assert lhs == rhs
                identity_checks += 1
    assert identity_checks == 125

    # Line pencil through projective point (1:1:-1) on the cubic.
    # After y=-1+s(x-1), the residual quadratic in x has A(s),B(s),C(s):
    A=[-16296,-22667,163,120]
    B=[55886,54874,-619,-240]
    C=[-44556,-33000,456,120]
    disc=poly_add(poly_mul(B,B),poly_scale(poly_mul(A,C),-4))
    expected=[218906692,-57498680,8699424,-2689724,466489]
    assert disc == expected
    # Squarefree quartic => smooth genus-one double cover after projective completion.
    gd=poly_gcd_q(disc,poly_deriv(disc))
    assert gd == [Fraction(1)]
    assert len(disc)-1 == 4 and disc[-1] == 466489

    print(
        "PASS P000_P11_GENUINE_DOUBLETON_DIOPHANTINE_NORMAL_FORM "
        f"root_box_R={R} unordered_root_pairs={len(ht)} "
        f"factor_checks={factor_checks} C1={len(c1)} C2={len(c2)} "
        f"primitive_C1={primitive} gcd_profile=1:78,2:4,3:1 "
        f"zero_column_C1={zero_column} primitive_zero_C1={primitive_zero} "
        f"AP_C1={len(ap_c1)} simultaneous_genuine_box=0 "
        "counterexample_height=9 obstruction_skeleton=(5,-1)|(4,-1)|(5,3) "
        f"cubic_identity_checks={identity_checks} quartic_degree=4 quartic_squarefree=1"
    )


if __name__ == '__main__':
    main()
