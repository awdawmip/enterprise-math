#!/usr/bin/env python3
"""X6 R155: exact rational, full-Port-10 polygon certificate for cusp germs.

Conditional static centered-three-axis six-pair joint BRC observer only;
no native physical time/residual claim. Standard-library Fraction arithmetic.
"""
from fractions import Fraction as Q
from itertools import product

U=(4,-4,1); V=(6,-1,0)
A=(1,0,0); C=(5,-4,1); K=(5,-1,0); H=(9,-5,1)
P=(1,3,-1); R=(7,-1,0)
X=(3,-4,1)
FAMILY={U,V,A,C,K,H,P,R}
ENTER4={A,C,K,H}
BANDS=((Q(0),Q(20)),(Q(20),Q(304,3)))
SLAB=Q(1)


def population():
    out={}
    for v in product(range(-10,11),repeat=3):
        if v==(0,0,0): continue
        if max(sum(max(z,0) for z in v),sum(max(-z,0) for z in v))>10: continue
        if next(z for z in v if z)!=abs(next(z for z in v if z)): continue
        x,y,z=v
        h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)
        out[v]=tuple(abs(h[j]-h[i]) for i,j in
                     ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3)))
    assert len(out)==1935
    return out

G=population()
assert set(FAMILY)<=set(G)

def e(B):
    B=Q(B)
    return Q(3,136+B) if B<=20 else Q(1,52)

def T(B):
    B=Q(B)
    return (B+544)/3 if B<=20 else 208-B

def values(v,B,delta):
    B=Q(B); delta=Q(delta)
    D=T(B)+delta
    capacities=(136+B,Q(312),136+D,B+176,B+D,D+176)
    return tuple(Q(g,c) for g,c in zip(G[v],capacities))

def score(v,B,delta):
    return max(values(v,B,delta))


def fixed_channel_certificates():
    """Each comparison becomes affine after multiplying by 136+B or 52.

    At every band B is affine and D=T(B)+delta is affine, so
    a gap inequality holding at all parallelogram vertices holds
    throughout. Same for strict comparisons if strict at vertices.
    """
    summaries=[]
    for b0,b1 in BANDS:
        vertices=list(product((b0,b1),(-SLAB,SLAB)))
        assert min(T(b)+d for b,d in vertices)>0
        assert all(values(V,b,d)[0 if b1==20 else 1]==e(b) for b,d in vertices)
        for b,d in vertices:
            assert all(a<=e(b) for a in values(V,b,d))
        opt_hist=[0]*6
        outside_hist=[0]*6
        for v in G:
            if v!=V:
                js=[j for j in range(6) if all(
                    values(v,b,d)[j]>=e(b) for b,d in vertices)]
                assert js, ('missing fixed optimizer lower channel',b0,b1,v)
                opt_hist[js[0]]+=1
            if v not in FAMILY:
                if b0==20 and v==X:
                    assert all(values(X,b,d)[1]==Q(3,104) for b,d in vertices)
                    continue   # Equality always excludes X from strict near set.
                js=[j for j in range(6) if all(
                    values(v,b,d)[j]>Q(3,2)*e(b) for b,d in vertices)]
                assert js, ('missing fixed outsider strict channel',b0,b1,v)
                outside_hist[js[0]]+=1
        assert sum(opt_hist)==1934
        assert sum(outside_hist)==1927-(1 if b0==20 else 0)
        for v in (U,V):
            assert all(all(r<Q(3,2)*e(b) for r in values(v,b,d))
                       for b,d in vertices)
        assert all(G[v][4]==6 for v in ENTER4|{P,R})
        assert all(values(A,b,0)[4]==Q(3,2)*e(b) for b in (b0,b1))
        assert all(values(v,b,0)[4]==Q(3,2)*e(b)
                   for v in ENTER4|{P,R} for b in (b0,b1))
        summaries.append((str(b0),str(b1),opt_hist,outside_hist))
    return summaries


def right_germ(v,B):
    """Exact local right-hand truth, not a finite delta assertion.

    On the T-wall the fifth channel equals the threshold for six
    potential entrants, and its derivative with delta is negative.
    An equality in a D-dependent channel (2 or 5) likewise resolves
    strictly to 'in'; equality in a D-independent channel blocks it.
    """
    assert v in ENTER4|{P,R}
    threshold=Q(3,2)*e(B)
    for j,ratio in enumerate(values(v,B,Q(0))):
        if j==4: continue
        if ratio>threshold: return False
        if ratio==threshold and j not in (2,5): return False
    return True


def expected_germ(B):
    out={U,V,*ENTER4}
    if B<=Q(224,19):out.add(P)
    if B<=8:out.add(R)
    return out


def boundary_germ_proof():
    # For all 0<B<=20, A,C,K,H have uniformly strictly subthreshold
    # nonfifth channels at the ends of the affine B strip.
    for v in ENTER4:
        assert all(values(v,B,0)[j]<Q(3,2)*e(B)
                   for B in (Q(0),Q(20)) for j in range(6) if j!=4)
    # For 20<=B<=304/3, these channels are <= and only A's third
    # channel touches the threshold at the rightmost boundary.
    for v in ENTER4:
        for B in (Q(20),Q(304,3)):
            for j in range(6):
                if j!=4:assert values(v,B,0)[j]<=Q(3,2)*e(B), (v,B,j)
    assert values(A,Q(304,3),0)[2]==Q(3,104)
    for v in ENTER4-{A}:
        assert all(values(v,Q(304,3),0)[j]<Q(3,104)
                   for j in range(6) if j!=4)

    # P and R each have the permanently blocking second channel
    # for B>=20. Below 20 the exact change thresholds are
    # P sixth: B=224/19; R third: B=8. Equalities in those
    # D-dependent channels become strict immediately to the right.
    assert G[P]==(4,9,2,5,6,11)
    assert G[R]==(4,9,10,5,6,1)
    assert all(values(v,Q(20),0)[1]==Q(3,104) for v in (P,R))
    assert values(P,Q(224,19),0)[5]==Q(3,2)*e(Q(224,19))
    assert values(R,Q(8),0)[2]==Q(3,2)*e(Q(8))
    assert all(values(P,B,0)[5]<Q(3,2)*e(B) for B in (Q(0),Q(8)))
    assert values(P,Q(20),0)[5]>Q(3,2)*e(Q(20))
    assert values(R,Q(0),0)[2]<Q(3,2)*e(Q(0))
    assert values(R,Q(20),0)[2]>Q(3,2)*e(Q(20))
    # Other nonfifth components stay safely below at required subdomains.
    for v in (P,R):
        hi=Q(224,19) if v==P else Q(8)
        exempt=5 if v==P else 2
        for B in (Q(0),hi):
            assert all(values(v,B,0)[j]<Q(3,2)*e(B)
                       for j in range(6) if j not in (4,exempt))

    # The formula for the immediate right germ is now a finite
    # affine sign argument in B on the displayed exact threshold bands.
    pieces=[(Q(1,100),8),(8,Q(224,19)),(Q(224,19),Q(20)),
            (Q(20),Q(304,3))]
    for lo,hi in pieces:
        for B in (lo,(lo+hi)/2,hi):
            if B<=0:continue
            got={U,V}|{v for v in ENTER4|{P,R} if right_germ(v,B)}
            assert got==expected_germ(B),('wrong right germ',B,got,expected_germ(B))
    # Distinct sharp contact multiplicity counts on right.
    assert len(expected_germ(Q(4)))==8
    assert len(expected_germ(Q(10)))==7
    assert len(expected_germ(Q(20)))==6
    assert len(expected_germ(Q(304,3)))==6
    # At B>304/3 A's third channel exceeds the threshold at the wall;
    # the 4-direction synchronized entry thus fails beyond the endpoint.
    B=Q(102)
    assert values(A,B,Q(0))[2]>Q(3,2)*e(B)
    assert right_germ(A,B) is False
    # full-population exact samples around all sharp B endpoints.
    examples=[]
    Bs=(Q(1),Q(8),Q(9),Q(224,19),Q(12),Q(20),Q(21),Q(80),Q(304,3),Q(102))
    for B in Bs:
        for d in (-Q(1,10000),Q(0),Q(1,10000)):
            D=T(B)+d
            if D<=0: continue
            ss={v:score(v,B,d) for v in G}
            optimum=min(ss.values())
            assert optimum==e(B)
            observed={v for v,f in ss.items() if 2*f<3*optimum}
            if B<=Q(304,3):
                if d<=0:assert observed=={U,V}, (B,d,observed)
                else:assert observed==expected_germ(B), (B,d,observed,expected_germ(B))
            if B==102 and d==Q(1,10000):
                assert A not in observed
            examples.append((str(B),str(d),len(observed)))
    return examples


def main():
    summary=fixed_channel_certificates()
    examples=boundary_germ_proof()
    print('R155 EXACT PORT-10 CUSP MULTIPLICITY / TWO-PARAMETER SLAB PASS')
    print('direction_count',len(G),'family_size',len(FAMILY),'full_rational_samples',len(examples))
    print('band_certificates',summary)
    print('T: (B+544)/3 on 0<B<=20; 208-B on 20<=B<=304/3')
    print('right-germ counts: 8 for B<=8, 7 for 8<B<=224/19, 6 for 224/19<B<=304/3')
    print('sharp loss of A just beyond 304/3 at B=102')

if __name__=='__main__':main()
