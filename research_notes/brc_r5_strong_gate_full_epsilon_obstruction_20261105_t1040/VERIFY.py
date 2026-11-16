"""Exact R5 strong-second-gate certificate, standard Python fractions only."""
from fractions import Fraction as F
from itertools import product
R=(F(1,2),F(1),F(3,2)); S=(F(1,4),F(1,2),F(1),F(3,2),F(7,4))
K=((F(1,4),F(1,2),F(1,4)),(F(3,8),F(1,4),F(3,8)))
V=((F(11,15),)+(F(1,15),)*4,(F(1,5),)*5,(F(1,15),)*4+(F(11,15),))

def model(e):
    assert 0<e<=1
    M=tuple(tuple((1-e)*(r==s)+e*v for s,v in zip(S,row)) for r,row in zip(R,V))
    for r,row in zip(R,M):
        assert min(row)>0 and sum(row)==1 and sum(s*q for s,q in zip(S,row))==r
        assert sum(s*q/r for s,q in zip(S,row))==1
    for row in K:
        assert sum(row)==sum(r*q for r,q in zip(R,row))==1 and min(row)>0
    return M

def bellman(e,k,u,v):
    M=model(e); C=lambda r:-min(r,k); c=lambda r:u*r+v
    B=tuple(sum(q*C(s) for q,s in zip(row,S))-C(r) for r,row in zip(R,M))
    A=tuple(sum(q*C(r) for q,r in zip(row,R))-C(F(1)) for row in K)
    G=tuple(aa-c(F(1))+sum(q*max(F(0),bb-c(r)) for q,bb,r in zip(row,B,R)) for aa,row in zip(A,K))
    base=C(F(1))-c(F(1))
    full=base+(max(0,G[0])+max(0,G[1]))/2
    lr=base+max(F(0),(G[0]+G[1])/2)
    return full,lr,G,B

def lr_enum(e,n):
    M=model(e); best=None; count=0
    for a in 'PQC':
      for middle in product('PQC',repeat=3):
       for last in product('PQ',repeat=5):
        out=[F(0)]*4
        def add(q,r,t,label):
            if label=='Q':out[0]+=q*r
            else:out[1]+=q
            out[2]+=q*r*t;out[3]+=q*t
        for source in (0,1):
          if a!='C':add(F(1,2),F(1),1,a);continue
          for j,r in enumerate(R):
            q=K[source][j]/2
            if middle[j]!='C':add(q,r,2,middle[j])
            else:
              for s,m,label in zip(S,M[j],last):add(q*m,s,3,label)
        score=sum(x*y for x,y in zip(out,n));count+=1
        if best is None or score>best:best=score
    assert count==2592
    return best,count

n=(-F(1),-F(1,2),-F(3,4),F(5,8))
for e in (F(5,8),F(3,4),F(9,11),F(1)):
    full,lr,G,B=bellman(e,F(1,2),F(3,4),-F(5,8))
    assert B==(11*e/60,e/20,e/60)
    assert G==(-F(1,16)+11*e/240,-F(1,32)+11*e/160)
    pred=(-F(1,64)+11*e/320) if e<=F(9,11) else (F(1,32)-11*e/480)
    assert full-lr==pred>0
    exact,count=lr_enum(e,n);assert exact==lr
    W=(11*e/320,F(1)-11*e/80,F(51,32),F(27,16))
    assert sum(x*y for x,y in zip(W,n))==full
    distance=(full-lr)/sum(abs(x) for x in n)
    print('strong',str(e),'FULL',full,'LR',lr,'gap',full-lr,'W',W,'dist_inf>=',distance,'count',count)
old=(-F(1),-F(1),-F(5,32),F(0))
for e in (F(1,16),F(5,8)):
    full,lr,G,B=bellman(e,F(1),F(5,32),F(0))
    assert all(b<=F(5,32)*r for b,r in zip(B,R))
    assert full-lr==F(1,64)
    exact,count=lr_enum(e,old);assert exact==lr
    print('weak',str(e),'FULL',full,'LR',lr,'gap',full-lr,'count',count)
print('PASS_EXACT_R5_STRONG_GATE_FULL_EPSILON_OBSTRUCTION')
