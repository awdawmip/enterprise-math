#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import combinations, product

def tv(z): return sum(abs(x) for x in z)/2
def dot(x,y): return sum((a*b for a,b in zip(x,y)),F(0))
def circuit(Y,i,j,k):
    z=[F(0)]*len(Y); d=Y[k]-Y[i]
    z[i]=(Y[k]-Y[j])/d; z[j]=F(-1); z[k]=(Y[j]-Y[i])/d
    assert sum(z)==0 and dot(z,Y)==0 and tv(z)==1
    return tuple(z)
def certificate(Y,v):
    assert len(Y)==len(v) and all(x<y for x,y in zip(Y,Y[1:]))
    triples=[(i,j,k,circuit(Y,i,j,k)) for i,j,k in combinations(range(len(Y)),3)]
    R=max([F(0)]+[abs(dot(z,v)) for _,_,_,z in triples])
    lo=[];hi=[]
    for i,j in combinations(range(len(Y)),2):
        d=Y[j]-Y[i];s=(v[j]-v[i])/d;lo.append(s-R/d);hi.append(s+R/d)
    B=max(lo);assert B<=min(hi)
    A=min(v[i]-B*Y[i] for i in range(len(Y)))
    resid=[v[i]-A-B*Y[i] for i in range(len(Y))]
    assert min(resid)==0 and max(resid)==R
    winner=next(((i+1,j+1,k+1,dot(z,v)) for i,j,k,z in triples
                  if abs(dot(z,v))==R),None)
    return R,A,B,winner
def observer(cont):
    Y=(F(1,2),F(3,4),F(5,4),F(3,2))
    K=((F(1,8),F(3,8),F(3,8),F(1,8)),(F(3,8),F(1,8),F(1,8),F(3,8)))
    eP=eQ=TP=TQ=F(0)
    for h in range(2):
        c=cont[h];eQ+=F(1,2)*(1-c);TP+=F(1,2)*(1-c);TQ+=F(1,2)*(1-c)
        for j,y in enumerate(Y):
            q=F(1,2)*c*K[h][j];p=y*q
            if j in (0,2): eP+=p
            else: eQ+=q
            TP+=2*p;TQ+=2*q
    return eP,eQ,TP,TQ
def main():
    Y=[F(1,2),F(3,4),F(5,4),F(3,2)]
    Ka=[F(1,8),F(3,8),F(3,8),F(1,8)]
    Kb=[F(3,8),F(1,8),F(1,8),F(3,8)]
    assert sum(Ka)==sum(Kb)==dot(Ka,Y)==dot(Kb,Y)==1 and min(Ka+Kb)>0
    cells=[]
    for h in range(2):
        for j in range(4):
            x=[0]*6;x[h]=1;x[j+2]=1;cells.append(tuple(x))
    assert len(set(cells))==8
    Q=[F(1,2)*K[j] for K in (Ka,Kb) for j in range(4)]
    P=[Q[i]*Y[i%4] for i in range(8)]
    assert sum(Q)==sum(P)==1 and min(P+Q)>0
    print('X6_EMBEDDED_8_LEAVES: 8 distinct cells; positive normalized P and Q')
    Va=[Y[j] if j in (0,2) else F(0) for j in range(4)]
    Vb=[F(0) if j in (0,2) else F(1) for j in range(4)]
    forms=[]
    for i,j,k in combinations(range(4),3):
        z=circuit(Y,i,j,k);forms.append(((i+1,j+1,k+1),dot(z,Va),dot(z,Vb)))
    assert forms==[((1,2,3),F(3,4),F(-1)),((1,2,4),F(3,8),F(-3,4)),
                   ((1,3,4),F(-9,8),F(3,4)),((2,3,4),F(-5,4),F(1))]
    print('4POINT_GLOBAL_SIGNED_FORMS:',forms)
    V=[Va[i]+Vb[i] for i in range(4)]
    R,A,B,w=certificate(Y,V)
    assert (R,A,B)==(F(3,8),F(1,4),F(1,2))
    print('4POINT_PRIMAL_DUAL:',R,A,B,w)
    OF=observer((F(3,4),F(1,4))); OB=observer((F(1,2),F(1,2)))
    D=tuple(x-y for x,y in zip(OF,OB))
    assert OF==(F(31,128),F(3,4),F(3,2),F(3,2))
    assert OB==(F(7,32),F(3,4),F(3,2),F(3,2))
    assert D==(F(3,128),F(0),F(0),F(0))
    DK=[(F(3,4)*Ka[j]+F(1,4)*Kb[j])-(Ka[j]+Kb[j])/2 for j in range(4)]
    assert DK==[-F(1,16),F(1,16),F(1,16),-F(1,16)]
    assert sum(DK)==dot(DK,Y)==0 and tv(DK)==F(1,8)
    assert F(1,2)*dot(DK,V)==F(1,2)*tv(DK)*R==F(3,128)
    z124=circuit(Y,0,1,3);z134=circuit(Y,0,2,3)
    assert tuple(x/tv(DK) for x in DK)==tuple(-(x+y)/2 for x,y in zip(z124,z134))
    print('8LEAF_FULL_O:',OF)
    print('8LEAF_LR_O:',OB)
    print('8LEAF_DIFFERENCE:',D)
    print('8LEAF_TV_CURVATURE_EQUALITY:',F(3,128),'=',F(3,128))
    print('DUAL_FACE: DK/TV=-(z124+z134)/2')
    n=0
    for aa,bb,uu,vv in product(range(-2,3),repeat=4):
        a,b,u,v=map(F,(aa,bb,uu,vv))
        v4=[a*Va[i]+b*Vb[i]+2*u*Y[i]+2*v for i in range(4)]
        r,*_=certificate(Y,v4)
        assert r==max(abs(ca*a+cb*b) for _,ca,cb in forms)
        n+=1
    assert n==625
    print('FOUR_POINT_SIGNED_GRID:',n,'exact certificates PASS')
    Y5=list(map(F,[F(1,5),F(2,5),F(4,5),F(6,5),F(7,5)]))
    V5=list(map(F,[0,1,-1,2,-2]))
    R5,A5,B5,w5=certificate(Y5,V5)
    assert R5==F(11,3)
    print('FIVE_POINT_CERTIFICATE:',R5,A5,B5,w5)
    Y3=[F(1,2),F(1),F(3,2)]
    n=0
    for aa,bb,uu,vv in product(range(-2,3),repeat=4):
        a,b,u,v=map(F,(aa,bb,uu,vv))
        vals=[a*Y3[0]+3*u*Y3[0]+3*v,b+3*u*Y3[1]+3*v,b+3*u*Y3[2]+3*v]
        r,*_=certificate(Y3,vals)
        assert r==abs(a-2*b)/4
        assert abs(F(7,1024)*(a-2*b))==F(1,2)*F(11,16)*F(7,88)*r
        n+=1
    assert n==625
    print('THREE_POINT_SIGNED_GRID:',n,'exact certificates PASS')
    print('ALL EXACT CHECKS PASSED')
if __name__=='__main__':main()
