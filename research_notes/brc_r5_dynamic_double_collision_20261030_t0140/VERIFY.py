#!/usr/bin/env python3
"""R5 exact P/Q stopping check. Auxiliary finite model, not native BRC arithmetic."""
from fractions import Fraction as F
from itertools import product

P={'A':F(1,3),'B':F(2,3)}; Q={'A':F(2,3),'B':F(1,3)}
Y={'A':(F(1,2),F(1,4)),'B':(F(1,4),F(1,2))}
Z={('A',1):(F(1,2),F(1,4)),('B',1):(F(2,3),F(1,3)),
   ('A',0):(F(1,2),F(2,5)),('B',0):(F(1,2),F(3,5))}
q2={('A',1):F(3,10),('B',1):F(7,10),('A',0):F(2,5),('B',0):F(3,5)}
q3={('A',1,1):F(1,5),('A',1,0):F(3,5),('B',1,1):F(4,5),
    ('B',1,0):F(2,5),('A',0,1):F(2,5),('A',0,0):F(3,5),
    ('B',0,1):F(1,3),('B',0,0):F(2,3)}
def errors(s,y,z):
    return ((F(3,4),{('A',1):F(1,10),('B',1):F(9,10)}.get((s,y),F(1,2)),
             F(9,10) if (s,y)==('A',1) else F(1,10) if (s,y)==('B',1) else F(1,2),F(1,2)),
            (F(2,3),q2[s,y],q3[s,y,z],F(1,2)))
assert sum(P.values())==sum(Q.values())==1
assert all(0<v<1 for d in (P,Q) for v in d.values())
assert all(0<v<1 for table in (Y,Z) for pair in table.values() for v in pair)
leaves=[]
for s,y,z in product(('A','B'),(0,1),(0,1)):
    pY,qY=Y[s];pZ,qZ=Z[s,y]
    a=P[s];b=Q[s];r1=a/b
    a*=pY if y else 1-pY; b*=qY if y else 1-qY;r2=a/b
    a*=pZ if z else 1-pZ; b*=qZ if z else 1-qZ;r3=a/b
    ep,eq=errors(s,y,z)
    assert a>0 and b>0 and all(0<v<1 for v in ep+eq)
    leaves.append((s,y,z,a,b,(r1,r2,r3),ep,eq))
assert sum(h[3] for h in leaves)==sum(h[4] for h in leaves)==1
R={(s,y,z):r for s,y,z,_,_,r,_,_ in leaves}
assert R['A',1,0][1]==R['B',1,0][1]==1
assert R['A',1,1][2]==R['B',1,1][2]==2
assert R['A',0,0][1]==F(1,3) and R['B',0,0][1]==3
assert R['A',1,0][2]==F(2,3) and R['B',1,0][2]==F(1,2)
assert R['A',0,1][2]==F(5,12) and R['A',0,0][2]==F(5,18)
assert R['B',0,1][2]==F(5,2) and R['B',0,0][2]==F(15,4)

def key(h,t,kind):
    s,y,z,_,_,r,_,_=h
    if kind=='FULL': return (t,s) if t==1 else ((t,s,y) if t==2 else (t,s,y,z))
    if kind=='TAG3' and t==3 and r[2]==2: return (t,r[2],s)
    return (t,r[t-1])

def observe(bits,idx,kind):
    out=[F(0)]*4
    for h in leaves:
        s,y,z,p,q,r,ep,eq=h
        t=next((j for j in (1,2,3) if bits[idx[key(h,j,kind)]]),4)
        out[0]+=p*ep[t-1];out[1]+=q*eq[t-1]
        out[2]+=p*t;out[3]+=q*t
    return tuple(out)

mins={}
for kind,n,target in [('LR',12,F(7,15)),('TAG3',13,F(13,30)),('FULL',14,F(11,30))]:
    ks=sorted({key(h,t,kind) for h in leaves for t in (1,2,3)},key=str)
    assert len(ks)==n
    idx={k:i for i,k in enumerate(ks)}
    best=None;count=0;bestobs=None
    for bits in product((0,1),repeat=n):
        obs=observe(bits,idx,kind)
        if best is None or obs[0]<best:best=obs[0];count=1;bestobs=obs
        elif obs[0]==best:count+=1
    assert best==target,(kind,best,target)
    mins[kind]=best
    print(kind,'keys',n,'exact_corners',2**n,'minimum_eP',best,
          'argmin_count',count,'first_argmin_O',bestobs)

# Explicit FULL witness: stop at t2 on A1, at t3 on B1, else forced t4.
O=[F(0)]*4
for s,y,z,p,q,r,ep,eq in leaves:
    t=2 if (s,y)==('A',1) else 3 if (s,y)==('B',1) else 4
    O[0]+=p*ep[t-1];O[1]+=q*eq[t-1];O[2]+=p*t;O[3]+=q*t
assert tuple(O)==(F(11,30),F(17,36),F(7,2),F(7,2))
assert mins['LR']-mins['FULL']==F(1,10)
assert mins['LR']-mins['TAG3']==F(1,30)
assert mins['TAG3']-mins['FULL']==F(1,15)
print('witness_FULL_O',tuple(O))
print('collision_time2_LR',R['A',1,0][1],R['B',1,0][1],
      'collision_time3_LR',R['A',1,1][2],R['B',1,1][2])
print('support_gap',mins['LR']-mins['FULL'],'stage2_loss',mins['TAG3']-mins['FULL'],
      'stage3_loss',mins['LR']-mins['TAG3'])
print('PASS_EXACT_R5_DYNAMIC_DOUBLE_COLLISION_TWO_STAGE_OBSTRUCTION')
