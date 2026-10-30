"""Exact 5-coordinate signed support obstruction for the 14-history R5 source tree."""
P=(120,240,60,60,180,60,30,30,30,30,90,90,20,40)
Q=(240,120,180,60,60,60,108,72,45,15,36,24,40,20)
T=(1,1,2,2,2,2,3,3,3,3,3,3,3,3)
PAR=(-1,-1,0,0,1,1,2,2,3,3,4,4,5,5)
KEY=(0,1,2,3,4,3,5,6,7,8,9,10,11,8)

def z(mask,lr):
    stopping=[(mask>>(KEY[i] if lr else i))&1 for i in range(14)]
    survival=[0]*14
    r=x=y=s=qA=0
    for i in range(14):
        survival[i]=1 if PAR[i]<0 else survival[PAR[i]]*(1-stopping[PAR[i]])
        if survival[i] and stopping[i]:
            x+=(4-T[i])*P[i]
            y+=(4-T[i])*Q[i]
            if i in (9,13):r+=Q[i]
            if i in (8,12):s+=P[i]
            if i==9:qA+=Q[i]
    return (r,x,y,s,qA)

def lin(v):
    r,x,y,s,qA=v
    return 17*r+x-y+s-50*qA

assert sum(P[:2])==sum(Q[:2])==360
assert all(P[i]>0 and Q[i]>0 for i in range(14))
LR=[z(m,True) for m in range(4096)]
FULL=[z(m,False) for m in range(16384)]
assert len(set(LR))==272 and len(set(FULL))==647
assert min(map(lin,LR))==-360
assert min(map(lin,FULL))==-720
assert z(516,False)==(15,150,375,0,15)
assert lin(z(516,False))==-720
assert min(map(lin,LR))-lin(z(516,False))==360
print('FIVE_COORD LR_polices=4096 FULL_policies=16384 LR_unique=272 FULL_unique=647')
print('EXACT_LR_BOUND 17*r+x-y+s-50*qA >= -360')
print('FULL_WITNESS mask=516 z=(15,150,375,0,15) value=-720 gap=360')
print('ALL_REAL_VALID via multiaffine Boolean-corner extremum, no persistent LR seed')
print('PASS_EXACT_R5_SOURCE_SPLIT_FIFTH_OBSERVER_NO_GO')
