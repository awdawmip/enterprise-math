from fractions import Fraction as F
from itertools import product
raw={'Q':[(10,10),(20,20),(15,15),(15,15)],'P':[(9,11),(5,5),(3,27),(30,30)]}
for rows in raw.values():
    leaves=[n for pair in rows for n in pair for _ in range(2)]
    assert len(leaves)==16 and min(leaves)>0 and sum(leaves)==240
M=[[F(x,20) for x in row] for row in ((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),(0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))]
assert all(sum(r)==1 for r in M)
assert len(set([F(9,10),F(11,10),F(1,4),F(1,5),F(9,5),F(2)]))==6
norm=lambda v: sum((abs(x) for x in v),F(0))
channel=lambda v: [sum((v[i]*M[i][j] for i in range(6)),F(0)) for j in range(6)]
count=0
for a,b,c,d in product(range(-3,4),repeat=4):
    w=[F(x) for x in (a,a,b,c,d,-2*a-b-c-d)]
    if norm(w):
        assert 5*norm(channel(w))>=2*norm(w)
        count+=1
assert 5*norm(channel([F(i) for i in (0,0,0,1,-1,0)]))==4
A=[(11,-10,0,0,0,0),(-9,10,0,0,0,0),(0,0,1,0,0,0),(0,0,0,F(9,4),F(-5,4),0),(0,0,0,F(-1,4),F(5,4),0),(0,0,0,0,0,1)]
for j in range(6):
    assert channel([F(v) for v in A[j]])==[F(i==j) for i in range(6)]
diam=max(norm([F(A[i][t])-F(A[j][t]) for t in range(6)]) for i in range(6) for j in range(i))
assert diam==40 and 20*norm(channel([F(i) for i in (1,-1,0,0,0,0)]))==2
E4=(0,0,1,2,2,3); E5=(0,0,1,2,3,4)
R4=[(F(19,40),F(21,40),0,0,0,0),(0,0,1,0,0,0),(0,0,0,F(3,10),F(7,10),0),(0,0,0,0,0,1)]
R5=[R4[0],R4[1],(0,0,0,F(1,2),F(1,2),0),(0,0,0,F(1,10),F(9,10),0),R4[3]]
for R in (R4,R5): assert all(sum(row)==1 for row in R)
assert [norm([M[i][j]-R4[E4[i]][j] for j in range(6)])/2 for i in range(6)]==[F(1,40),F(1,40),F(0),F(1,5),F(1,5),F(0)]
assert [norm([M[i][j]-R5[E5[i]][j] for j in range(6)])/2 for i in range(6)]==[F(1,40),F(1,40),F(0),F(0),F(0),F(0)]
maxima=[F(0),F(0),F(0)]
for mask in range(64):
    bits=[(mask>>j)&1 for j in range(6)]
    for i in range(6):
        prob=lambda row:sum((F(row[j])*bits[j] for j in range(6)),F(0))
        p=prob(M[i]); q4=prob(R4[E4[i]]); q5=prob(R5[E5[i]])
        maxima=[max(a,b) for a,b in zip(maxima,[abs(p-F(1,2)),abs(p-q4),abs(p-q5)])]
assert maxima==[F(1,2),F(1,5),F(1,40)]
print('CHECK_16_POSITIVE_LEAVES_PER_LAW=PASS')
print('CHECK_6_LR_CLASSES_AND_CONDITIONAL_ROWS=PASS')
print(f'CHECK_R4_HYPERPLANE_GRID={count} PASS')
print('CHECK_R5_INVERSE_15_COLUMN_PAIRS_DIAMETER=40 PASS')
print('CHECK_64_POLICIES_X6_PREPARATIONS=384 PASS')
print(f'CERTIFIED_CONSTRUCTIVE_DECISION_RADII={maxima}')
print('PASS_BRC_N4_DECISION_OBSERVER_SANDWICH_20261031')
