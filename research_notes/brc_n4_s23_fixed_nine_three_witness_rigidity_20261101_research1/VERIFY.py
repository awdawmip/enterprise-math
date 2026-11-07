#!/usr/bin/env python3
"""Exact three-policy obstruction for a fixed nine-kernel BRC/S23 decoder bank.
All input masses and TV distances use Fraction; no sampling or float comparison.
"""
from fractions import Fraction as F

M20 = ((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
       (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
GROUP = (0,0,1,2,2,3)
A_SLOT = (0,0,0,1,1,1)
B_SLOT = (0,0,1,0,0,2)
NINE = ("34 24 34 24", "34 23 34 34", "34 34 34 23",
        "24 24 12 12", "12 12 24 34", "12 13 23 24",
        "23 34 12 13", "24 34 12 14", "13 12 13 13")


def prepared(aA,aB,bU,bAV,bBV, cs):
    abc = (aA,aB),(bU,bAV,bBV)
    six=[]
    for x in range(6):
        a=abc[0][A_SLOT[x]]
        b=abc[1][B_SLOT[x]]
        c=cs[x]
        six.append((a,(1-a)*b,(1-a)*(1-b)*c,(1-a)*(1-b)*(1-c)))
    return tuple(tuple(sum(F(M20[i][x],20)*six[x][t] for x in range(6))
                       for t in range(4)) for i in range(6))


def pair_decoder(pairs):
    rows=[]
    for pair in pairs.split():
        row=[F(0)]*4
        row[int(pair[0])-1]+=F(1,2)
        row[int(pair[1])-1]+=F(1,2)
        rows.append(tuple(row))
    return tuple(rows)


def tv(u,v):
    return sum((abs(x-y) for x,y in zip(u,v)),F(0))/2


def risk(p, d):
    return max(tv(p[i], d[GROUP[i]]) for i in range(6))

W=prepared(F(1),F(0),F(0),F(0),F(1),(F(0),)*6)
H=prepared(F(1,3),F(1),F(0),F(0),F(0),
           (F(1),F(0),F(1),F(0),F(0),F(0)))
J=prepared(F(1),F(1,3),F(0),F(0),F(0),
           (F(0),F(0),F(0),F(0),F(1),F(0)))
P=(('W',W),('H',H),('J',J))

# Four group rows: AU, AV, BU, BV. One tenth decoder, fixed across policies.
Dstar=((F(1,2),F(0),F(1,4),F(1,4)),
       (F(1,2),F(0),F(1,2),F(0)),
       (F(4,9),F(0),F(1,9),F(4,9)),
       (F(4,9),F(4,9),F(0),F(1,9)))
assert all(sum(row)==1 and all(x>=0 for x in row) for row in Dstar)
assert W==( (F(1),F(0),F(0),F(0)),)*3 + ((F(0),F(0),F(0),F(1)),)*2 + ((F(0),F(1),F(0),F(0)),)
assert H[5]==(F(1),F(0),F(0),F(0))
assert J[5]==(F(1,3),F(0),F(0),F(2,3))

expected_min9={'W':F(1),'H':F(2,3),'J':F(2,3)}
for name,p in P:
    old=tuple(risk(p,pair_decoder(spec)) for spec in NINE)
    assert min(old)==expected_min9[name], (name,old)
    new=risk(p,Dstar)
    assert new<=F(5,9), (name,new)
    print(f'{name}: fixed9={[str(x) for x in old]} min9={min(old)} tenth={new}')
    print(f'  row_TV={[str(tv(p[i],Dstar[GROUP[i]])) for i in range(6)]}')

# Analytic lower certificate for arbitrary tenth BV row q=(q1,q2,q3,q4):
# any radius r covering W/H/J must have:
# 1-r <= q1, 1-r <= q2, q4 <= 1-q1-q2 <= 2r-1;
# r >= TV((1/3,0,0,2/3),q) >= 2/3-q4 >= 5/3-2r;
# thus 3r >= 5/3, r >= 5/9.
# At r=5/9, BV q=(4/9,4/9,0,1/9) saturates the three inequalities.
q=Dstar[3]
assert tv(W[5],q)==tv(H[5],q)==tv(J[5],q)==F(5,9)
assert max(risk(p,Dstar) for _,p in P)==F(5,9)
print('PASS_BRC_N4_S23_FIXED_NINE_THREE_WITNESS_5_9_20261101')
print('exact finite theorem: min over arbitrary tenth stochastic decoder of max_W,H,J min_10-label loss = 5/9')
