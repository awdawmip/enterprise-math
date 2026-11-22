"""Exact BRC signed/Z2 calculation for PREFIX-1013, frozen P000 V5/Stage46 candidate."""
from collections import defaultdict
from fractions import Fraction

Z=(0,)*6
E1=(1,0,0,0,0,0)
e2=(0,1,0,0,0,0)
e3=(0,3,0,0,0,0)
D=[tuple((1 if j<6 else -1) if i==j%6 else 0 for i in range(6)) for j in range(12)]
neg=lambda d:tuple(-x for x in d)
add=lambda a,b:tuple(x+y for x,y in zip(a,b))

def evolve(v,one_negative=False):
    w=defaultdict(int)
    for (x,h,k),amp in v.items():
        for d in D:
            q=k+(sum(d)<0)
            if one_negative and q>1:continue
            y=add(x,d)
            if (x==Z and y==E1) or (x==E1 and y==Z):continue
            w[y,neg(d),q]+=amp*(1-6*(h==d))
    return {k:v for k,v in w.items() if v}

def defect(v):
    return sum(amp*(1-6*(h==E1)) for (x,h,k),amp in v.items() if x==Z)+sum(amp*(1-6*(h==neg(E1))) for (x,h,k),amp in v.items() if x==E1)

A={(e2,neg(E1),0):1}
B={(e3,neg(E1),0):1}
assert (sum(A.values()),defect(A))==(1,0)==(sum(B.values()),defect(B))
A1=evolve(A); B1=evolve(B)
assert (sum(A1.values()),sum(B1.values()))==(6,6)
assert (defect(A1),defect(B1))==(1,0)
A2=evolve(A1);B2=evolve(B1)
assert (sum(A2.values()),sum(B2.values()))==(35,36)
assert (sum(x*x for x in A2.values()),sum(x*x for x in B2.values()))==(1295,1296)
assert (sum(v for (x,h,k),v in A2.items() if k==1),sum(v for (x,h,k),v in B2.items() if k==1))==(-1,0)
assert (sum(v*v for (x,h,k),v in A2.items() if k==1),sum(v*v for (x,h,k),v in B2.items() if k==1))==(1079,1080)

# Z2 phase-cover independently checks signed recursion in each Cell-port fibre.
def phase(n):
    q={(Z,neg(E1),0,0):1}
    for _ in range(n):
        nx=defaultdict(int)
        for (x,h,k,phi),amp in q.items():
            for d in D:
                j=k+(sum(d)<0)
                if j>1:continue
                y=add(x,d)
                if (x==Z and y==E1) or (x==E1 and y==Z):continue
                match=h==d
                nx[y,neg(d),j,phi^int(match)]+=amp*(5 if match else 1)
        q=nx
    out=defaultdict(int)
    for (x,h,k,phi),amp in q.items():
        if k==1:out[x,h]+=(-amp if phi else amp)
    return {k:v for k,v in out.items() if v}

for n in (5,6,7,8):
    a={(Z,neg(E1),0):1}
    for _ in range(n):a=evolve(a,True)
    fibres={(x,h):v for (x,h,k),v in a.items() if k==1 and v}
    assert fibres==phase(n)
    pos=[sum(v for (x,h),v in fibres.items() if h==neg(D[i])) for i in range(6)]
    negm=[sum(v for (x,h),v in fibres.items() if h==D[i]) for i in range(6)]
    assert pos==[25*6**(n-4)]*6 and negm==[0]*6
    assert Fraction(sum(pos),6**n)==Fraction(25,216)
    if n==5:assert Fraction(sum(v*v for v in fibres.values()),36**n)==Fraction(5285,419904)
    print(n, 'signed_port_+',pos[0], 'signed_port_-',negm[0], 'joint_fibres',len(fibres))
print('PASS: two-step observer obstruction and n=5..8 typed BRC/Z2 checks')


# Fixed-source counterexample: equal signed port margins, unequal port-resolved Gram masses.
v={(Z,neg(E1),0):1}
for _ in range(5):v=evolve(v,True)
qpos=[sum(amp*amp for (x,h,k),amp in v.items() if k==1 and h==neg(D[j])) for j in range(6)]
qneg=[sum(amp*amp for (x,h,k),amp in v.items() if k==1 and h==D[j]) for j in range(6)]
assert qpos==[135110]+[109490]*5
assert qneg==[16560]+[12384]*5
assert Fraction(sum(qpos)+sum(qneg),36**5)==Fraction(5285,419904)
print('n=5 Gram per positive-last port:',qpos,'per negative-last port:',qneg)
