"""R146: exact three-witness Port-10 six-gap BRC optimizer, B>=136, D>=528.
This is arithmetic *within* the R121/R122 fixed conditional BRC observer,
not a native physical time-evolution computation.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import product

P=10
A=[a for a in product(range(-P,P+1),repeat=3)
   if a!=(0,0,0)
   and max(sum(max(v,0) for v in a),sum(max(-v,0) for v in a))<=P
   and next(v for v in a if v != 0)>0]

def gaps(a):
    x,y,z=a
    h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)
    return tuple(abs(h[j]-h[i]) for i in range(4) for j in range(i+1,4))

G={a:gaps(a) for a in A}
b=(4,-1,0)
c=(6,-4,1)
a0=(9,-5,1)

def F(a,B,D):
    ss=(136+B,312,136+D,B+176,B+D,176+D)
    return max(Q(g,s) for g,s in zip(G[a],ss))

def exact_formula(B,D):
    fb=max(Q(1,136+B),Q(11,136+D),Q(12,B+D))
    fc=Q(12,136+D)
    return min(Q(1,104),fb,fc)

def brute(B,D):
    return min(F(a,B,D) for a in A)

def main():
    assert len(A)==len(G)==1935
    assert G[b]==(1,0,11,1,12,11)
    assert G[c]==(0,0,12,0,12,12)
    assert G[a0]==(0,3,6,3,6,3)
    zero=[a for a in A if G[a][1]==0]
    assert len(zero)==15 and set((b,c))<=set(zero)
    high=[a for a in A if G[a][1]!=0]
    assert len(high)==1920 and all(G[a][1]>=3 and G[a][1]%3==0 for a in high)
    rest=[a for a in zero if a not in (b,c)]
    assert len(rest)==13
    assert all(all(x>=y for x,y in zip(G[a],G[b])) for a in rest)
    assert all(all(x>=y for x,y in zip(G[a],G[c])) for a in rest)
    assert all(G[a][2]>=22 for a in rest)
    # Exact all-population crosschecks incl. walls, both sides, and a large B,D regime.
    samples=0
    for B in map(Q,[136,137,150,200,240,241,500,1000000]):
        E=max(Q(1008),Q(1248)-B)
        switch=12*B+1496
        Ds={Q(528),E,(Q(528)+E)/2,E+Q(1,100),E+1,
            Q(1112),switch-Q(1,100),switch,switch+Q(1,100),
            Q(10000),Q(1000000)}
        for D in sorted(Ds):
            if D<Q(528): continue
            got=brute(B,D)
            assert got==exact_formula(B,D),(B,D,got,exact_formula(B,D))
            if D>E:
                assert got<Q(1,104)
                winners=[a for a in A if F(a,B,D)==got]
                assert set(winners)<={b,c},(B,D,winners)
            samples+=1
    print('R146 EXACT THREE-WITNESS GLOBAL PORT-10 OPTIMIZER PASS')
    print('population',len(A),'fixed_lower_bound_directions',len(high),
          'zero_pair_directions',len(zero),'dominated_zero_pair',len(rest))
    print('optimizer_candidate_witnesses',a0,b,c)
    print('exact_fraction_full_population_crosschecks',samples)
    print('switch_for_B_gt_136','D=12 B + 1496; below b, tie at wall, above c')

if __name__=='__main__':
    main()
