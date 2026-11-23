#!/usr/bin/env python3
"""R154 exact affine-vertex certificate around the fourfold BRC entry wall."""
from fractions import Fraction as Q
from itertools import product

U,V=(4,-4,1),(6,-1,0)
EXTRA=((1,0,0),(5,-4,1),(5,-1,0),(9,-5,1))
W={U,V,*EXTRA}
RECTANGLES=((Q(19),Q(20)),(Q(20),Q(21)))
DLO,DHI=Q(187),Q(189)


def population():
    out={}
    for v in product(range(-10,11),repeat=3):
        if v==(0,0,0):continue
        if max(sum(max(n,0) for n in v),sum(max(-n,0) for n in v))>10:continue
        if next(n for n in v if n)<0:continue
        x,y,z=v
        h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)
        out[v]=tuple(abs(h[j]-h[i]) for i,j in
                     ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3),(2,3)))
    assert len(out)==1935
    return out


def caps(B,D):
    return (136+B,Q(312),136+D,B+176,B+D,D+176)


def target(B):
    return max(Q(3,136+B),Q(1,52))


def comp(g,j,B,D,lam,strict=False):
    # Sign is affine in B,D after positive denominators are cleared,
    # separately on B<=20 (eta=3/(136+B)) and B>=20 (eta=1/52).
    lhs=Q(g,caps(B,D)[j])
    rhs=lam*target(B)
    return lhs < rhs if strict else lhs >= rhs


def main():
    pop=population()
    outside_counts=[]
    for b0,b1 in RECTANGLES:
        corners=list(product((b0,b1),(DLO,DHI)))
        # V is an exact optimizer witness: its score is target throughout,
        # since the two active ratios are 3/(136+B) and 6/312.
        assert all(max(Q(g,c) for g,c in zip(pop[V],caps(B,D)))==target(B)
                   for B,D in corners)
        # No vector can beat V: one fixed gap term per vector works at
        # all four corners, hence everywhere on the rectangle.
        lower_witness={}
        outside_near_witness={}
        histogram=[0]*6
        for v,gaps in pop.items():
            if v!=V:
                js=[j for j,g in enumerate(gaps) if all(
                    comp(g,j,B,D,Q(1)) for B,D in corners)]
                assert js, ('optimizer-lower-bound',b0,b1,v)
                lower_witness[v]=js[0]
            if v not in W:
                js=[j for j,g in enumerate(gaps) if all(
                    comp(g,j,B,D,Q(3,2)) for B,D in corners)]
                assert js, ('outsider-exclusion',b0,b1,v)
                outside_near_witness[v]=js[0]
                histogram[js[0]]+=1
        assert len(outside_near_witness)==1929
        # U and V are strictly near everywhere. For the four candidates
        # in EXTRA all but the fifth pair are strictly below threshold;
        # the fifth pair is identically 6/(B+D), giving one exact wall.
        for v in (U,V):
            assert all(comp(g,j,B,D,Q(3,2),strict=True)
                       for j,g in enumerate(pop[v]) for B,D in corners)
        for v in EXTRA:
            assert pop[v][4]==6
            assert all(comp(g,j,B,D,Q(3,2),strict=True)
                       for j,g in enumerate(pop[v]) if j!=4
                       for B,D in corners)
        outside_counts.append(histogram)
        # Spot check strict equalities as independent full-population replay.
        for B,D in corners+[(Q(20),Q(188)),(Q(19),Q(563,3)),
                            (Q(21),Q(187)),(Q(20),Q(189))]:
            if not (b0<=B<=b1 and DLO<=D<=DHI):continue
            ss={v:max(Q(g,c) for g,c in zip(vec,caps(B,D)))
                for v,vec in pop.items()}
            eta=min(ss.values())
            assert eta==target(B)
            expected={U,V}
            wall=(B+544)/3 if B<=20 else 208-B
            if D>wall: expected.update(EXTRA)
            actual={v for v,f in ss.items() if 2*f<3*eta}
            assert actual==expected, ('full-population',B,D)
    print('R154 EXACT TWO-PARAMETER CUSP CERTIFICATE PASS')
    print('complete_directions',len(pop),'outsider_fixed_gap_certificates',1929*2)
    print('witness_histograms_by_B_rectangle',outside_counts)
    print('entry walls: D=(B+544)/3 for 19<=B<=20; D=208-B for 20<=B<=21')


if __name__=='__main__':
    main()
