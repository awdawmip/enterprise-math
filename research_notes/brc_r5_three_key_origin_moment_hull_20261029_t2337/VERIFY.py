"""Exact Fraction verification for three-key source-moment hull."""
from fractions import Fraction as Q
from itertools import product, permutations

Z, O, H = Q(0), Q(1), Q(1, 2)

def F(k):
    x, y, z = k
    return (x, y, z, x*y*z)

def G(a,b):
    return tuple((p+q)/2 for p,q in zip(F(a),F(b)))

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)), Z)

def det4(M):
    ans=Z
    for p in permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        v=O if inv%2==0 else -O
        for i,j in enumerate(p): v*=M[i][j]
        ans+=v
    return ans

def feasible(v):
    x,y,z,t=v
    return all(Z<=a<=O for a in (x,y,z)) and Z<=t<=min(x,y,z) and t>=x+y+z-2

def check():
    bits=list(product((Z,O),repeat=3))
    lr=[F(b) for b in bits]
    full=[G(a,b) for a in bits for b in bits]
    assert len(lr)==8 and len(full)==64 and len(set(lr))==8
    assert set(lr).issubset(set(full))
    assert all(feasible(p) for p in lr+full)
    P={(s,z):H*(Q(2,3) if z else Q(1,3)) for s in ('A','B') for z in (0,1)}
    R={(s,z):H*(Q(1,3) if z else Q(2,3)) for s in ('A','B') for z in (0,1)}
    assert all(v>0 for v in list(P.values())+list(R.values()))
    assert sum(P.values())==sum(R.values())==O
    assert all(sum(P[s,z] for z in (0,1))==sum(R[s,z] for z in (0,1))==H for s in ('A','B'))
    for w in product((-Q(2),-O,Z,O,Q(2)),repeat=4):
        u=[dot(w,v) for v in lr]; v=[dot(w,a) for a in full]
        assert min(u)==min(v) and max(u)==max(v)
    C=G((Z,Z,Z),(O,O,O))
    assert C==(H,H,H,H)
    assert F((H,H,H))==(H,H,H,Q(1,8))
    assert C[3]-C[0]*C[1]*C[2]==Q(3,8)
    J=((H,Z,Z,H),(Z,H,Z,Z),(Z,Z,H,Z),(Q(1,32),Q(1,32),Q(1,32),Q(9,32)))
    assert det4(J)==Q(1,32)
    f=lambda d:(H+d)**3-(H-d)
    assert f(Q(1,6))<0<f(Q(3,16))
    print("P atoms:",[str(P[s,z]) for s in ('A','B') for z in (0,1)])
    print("Q atoms:",[str(R[s,z]) for s in ('A','B') for z in (0,1)])
    print("LR deterministic:",len(lr),"FULL source-deterministic:",len(full))
    print("Signed regression directions:",5**4)
    print("C:",tuple(map(str,C)),"R(C):",Q(3,8))
    print("Jacobian determinant:",Q(1,32),"distance root bracket:",Q(1,6),Q(3,16))
    print("PASS_EXACT_R5_THREE_KEY_SOURCE_MOMENT_HULL")

if __name__=="__main__":
    check()
