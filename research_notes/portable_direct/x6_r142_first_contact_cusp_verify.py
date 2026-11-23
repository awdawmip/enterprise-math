"""R142 full Port-10 exact first-contact uniqueness and affine local cusp certificate."""
from fractions import Fraction as Q
from x6_r140_sharp_uniform_D_tube_verify import population, TARGET, CELLS, gaps, capacity, f
from x6_r141_sharp_lower_D_tube_verify import CELLS8, outsider_certificate, multiply

SPECIAL = (6,-1,0)
DIRECTIONS = population()
VERTICES = [(Q(B),Q(D)) for B in (19,21) for D in (447,449)]

def cap(j,B,D):
    base,slope=capacity(j,D)
    return base+slope*B

def nonnegative_every_vertex(g,j,K):
    return all(g[j]*(B+D) - K*cap(j,B,D)>=0 for B,D in VERTICES)

def main():
    assert len(DIRECTIONS)==1935
    assert SPECIAL not in TARGET
    opt=outside=inside=0
    a0=(1,0,0)
    assert all(all(g*(B+D)<=6*cap(j,B,D)
                   for j,g in enumerate(DIRECTIONS[a0])) for B,D in VERTICES)
    assert all(DIRECTIONS[a0][4]*(B+D)==6*cap(4,B,D) for B,D in VERTICES)
    for a,g in DIRECTIONS.items():
        assert any(nonnegative_every_vertex(g,j,6) for j in range(6)), ('opt',a)
        opt+=1
        if a in TARGET:
            assert all(g[j]*(B+D)<9*cap(j,B,D)
                       for j in range(6) for B,D in VERTICES), ('inside',a)
            inside+=1
        elif a!=SPECIAL:
            assert any(nonnegative_every_vertex(g,j,9) for j in range(6)), ('outside',a)
            outside+=1
    assert (opt,inside,outside)==(1935,4,1930)
    g=DIRECTIONS[SPECIAL]
    assert g==(3,6,3,3,0,3)
    for j in (2,3,4,5):
        assert all(52*g[j]<=cap(j,B,D) for B,D in VERTICES)
    assert all(cap(1,B,D)==312 for B,D in VERTICES)
    assert all(f(SPECIAL,B,D)==max(Q(3,136+B),Q(1,52)) for B,D in VERTICES)

    # Exact boundary lines, both side classifications, and strict equality.
    for B in [Q(39,2),Q(79,4),Q(20),Q(81,4),Q(41,2)]:
        edge=min(408+2*B,468-B)
        if Q(447)<=edge<=Q(449):
            eta=min(f(a,B,edge) for a in DIRECTIONS)
            assert eta==Q(6,B+edge)
            assert 2*f(SPECIAL,B,edge)==3*eta
    samples=0
    for B in [Q(19),Q(77,4),Q(39,2),Q(79,4),Q(20),Q(81,4),Q(41,2),Q(83,4),Q(21)]:
        for D in [Q(447),Q(895,2),Q(448),Q(897,2),Q(449)]:
            eta=min(f(a,B,D) for a in DIRECTIONS)
            near={a for a in DIRECTIONS if 2*f(a,B,D)<3*eta}
            expect=set(TARGET)
            if D<min(408+2*B,468-B):expect.add(SPECIAL)
            assert eta==Q(6,B+D) and near==expect,(B,D,eta,near^expect)
            samples+=1

    # Any outsider equality at D=448 must zero its nonnegative R141
    # polynomial. Nonnegative quadratic zeros occur only at endpoints
    # or their exact rational interior vertex.
    candidate_points=set()
    possible_pairs=set()
    checked=0
    for lo,hi,K,L0,L1,_ in CELLS8:
        m0,m1=(0,1) if hi is not None and hi<=136 else (136,0)
        for a,g in DIRECTIONS.items():
            if a in TARGET:continue
            j=outsider_certificate(g,lo,hi,K,L0,L1)
            assert j is not None
            s0,s1=capacity(j,500)
            L=multiply([2*g[j]*L0,2*g[j]*L1],[448+m0,m1])
            R=multiply([3*K*s0,3*K*s1],[500+m0,m1])
            p=[t-u for t,u in zip(L,R)]
            assert any(p),('identically_zero',a,lo)
            def val(v):return sum(t*v**k for k,t in enumerate(p))
            candidates={lo}
            if hi is not None:candidates.add(hi)
            if p[2]>0:
                vertex=-p[1]/(2*p[2])
                if lo<vertex and (hi is None or vertex<hi):candidates.add(vertex)
            for B in candidates:
                if B>0 and val(B)==0:
                    candidate_points.add(B)
                    possible_pairs.add((B,a))
            checked+=1
    assert checked==8*1931
    assert candidate_points=={Q(20)},candidate_points
    boundary_eta=min(f(v,Q(20),Q(448)) for v in DIRECTIONS)
    boundary_equal={a for a in DIRECTIONS if 2*f(a,Q(20),Q(448))==3*boundary_eta}
    assert boundary_equal=={SPECIAL},boundary_equal
    assert (Q(20),SPECIAL) in possible_pairs

    print('R142 UNIQUE FIRST CONTACT AND AFFINE LOCAL CUSP EXACT CERTIFICATE PASS')
    print('optimizer_lower',opt,'permanent_insiders',inside,'permanent_outsiders',outside)
    print('global_boundary_outsider_polynomials',checked,'possible_equal_B',sorted(candidate_points))
    print('actual_equality_B20_D448',sorted(boundary_equal),'raw_zero_candidates',len(possible_pairs))
    print('full_fraction_replays',samples,'local_box','19<=B<=21, 447<=D<=449')
    print('new_entrant',SPECIAL,'iff','D<min(408+2B,468-B)')

if __name__=='__main__':main()
