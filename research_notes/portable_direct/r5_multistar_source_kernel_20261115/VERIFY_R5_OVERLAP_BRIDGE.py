#!/usr/bin/env python3
"""Exact finite sharpness certificate: two overlapping stars, 10 vs 12."""
O = [frozenset(int(x) for x in s) for s in ('0125','0135','0235','0245','0246')]
A = [(frozenset(int(x) for x in s),b) for s,b in
     [('1235',1),('1245',1),('1246',1),('1345',0),('1346',0)]]
Y0={1,2,4}; Y1={11,13,14}; Y=Y0|Y1; X=Y|{5,10}
assert len(X)==8 and len(Y)==6

def rho(C,t,y,o):
    j,s,u=o
    return len(C-O[j])+(s!=t)+(u^y).bit_count()

def covered(o,types):
    return {(s,t,y) for s,t in types for y in Y
            if rho(frozenset(int(x) for x in s),t,y,o)<=2}

old=[(j,b,u) for u in X for j in range(5) for b in (0,1)]
critical=[('1245',1),('1246',1),('1345',0),('1346',0)]
all_targets=[(s,t,y) for s,t in [('1235',1)]+critical for y in Y]
E=[('1346',0,y) for y in Y]
for _,_,y in E:
    witnesses=[o for o in old if ('1346',0,y) in covered(o,[('1346',0)])]
    assert set(witnesses)=={(1,0,y),(4,0,y)}

for o in old:
    mask=covered(o,critical)
    if o in {(j,0,y) for y in Y for j in (1,4)}:
        assert len(mask)<=2
    else:
        assert len(mask)<=3
# Six compulsory baselines reach at most two critical targets each;
# any other three resources reach at most three each: 21<24.
assert 6*2+3*3 < len(Y)*len(critical)

witness=[(1,0,y) for y in sorted(Y)]+[
    (0,1,5),(4,1,5),(0,1,10),(4,1,10)]
assert len(witness)==10
assert all((s,t,y) in set().union(*(covered(o,[(s,t)]) for o in witness))
           for s,t,y in all_targets)
assert min((a^b).bit_count() for a in Y0 for b in Y1)==2
assert all(not ((a^b).bit_count()<2)
           for a in Y for b in Y if a!=b)
assert 0 not in X and 15 not in X
print('Y0:', sorted(Y0),'Y1:',sorted(Y1),'X:',sorted(X))
print('distance between target groups = 2; both star centers absent')
print('forced baselines=6, critical targets=24, max coverage with 9 resources=21')
print('verified constructive library:',witness)
print('EXACT kappa_a(X,Y;2)=10, vs separate-star 6+6=12')
print('PASS_R5_OVERLAPPING_STAR_BRIDGE_SHARPNESS')
