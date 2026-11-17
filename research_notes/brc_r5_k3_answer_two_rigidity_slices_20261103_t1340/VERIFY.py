from fractions import Fraction as F
from itertools import product
c=(F(1,8),F(1,6),F(1,16),F(3,32)); r=F(3,4)
patterns=((F(1,4),F(1,2),F(3,4),F(1,2)),(F(1,16),F(3,4),F(15,16),F(1,8)),(F(3,4),F(1,4),F(1,8),F(7,8)),(F(1,2),)*4)
flat=(F(1,2),)*4

def O(x,y,i,g,p,q):
 w=(F(1,4),(1-x)/4,y/8,i/8); a=(F(1,2),F(2,3),F(1,2),F(3,4)); d=y/16+3*i/32
 M=[w[s]*a[s] if g[s]>=1 else F(0) for s in range(4)]
 S=[F(2,3)*M[s] if g[s]>=2 else F(0) for s in range(4)]
 U=[S[s] if g[s]>=3 else F(0) for s in range(4)]
 return (F(107,128)-21*x/128+d/4-sum(S)/2+sum(p[s]*U[s] for s in range(4))/8,
 F(13,64)+3*x/64-d/2+sum(S)/8+sum(q[s]*U[s] for s in range(4))/32,
 F(3)+sum(M)+3*sum(S)/2+r*sum(U),F(3)+sum(M)/2+3*sum(S)/8+r*sum(U)/4)

def support(n,p,q,full):
 ups=product(((F(0),F(0)),(F(0),F(1)),(F(1),F(0))),(0,1),product(range(4),repeat=4)) if full else (( (F(x),F((1-x)*y)),y,(j,)*4) for x,y,j in product((0,1),(0,1),range(4)))
 return max(sum(n[k]*w[k] for k in range(4)) for (x,i),y,g in ups for w in [O(x,F(y),i,g,p,q)])

count=0
for tau in (F(1,4),F(1,2),F(3,4)):
 np=(F(-8),F(64,9)*(tau-13),F(4),F(0)); nq=(F(16,7)*(5-tau),F(-32),F(4),F(0))
 for a in patterns:
  pm=sum(c[s]*max(tau-a[s],F(0)) for s in range(4)); pn=sum(c[s]*max(a[s]-tau,F(0)) for s in range(4)); gap=F(2,3)*min(pm,pn)
  for typ,p,q,n in [('P',a,flat,np),('Q',flat,a,nq)]:
   h1=support(n,p,q,True);h0=support(n,p,q,False)
   assert h1-h0==gap
   count+=1
   if tau==F(1,2) and a==patterns[0]:
    witness=O(F(0),F(1),F(1),tuple(3 if z<tau else 1 for z in a),p,q)
    assert sum(n[k]*witness[k] for k in range(4))==h1
    print(typ,'normal=',n,'hFULL=',h1,'hLR=',h0,'witness=',witness,'Linf>=',gap/sum(map(abs,n)))
    count+=1
print('PASS_EXACT_K3_ANSWER_TWO_SLICES',count,'assertions; 1536 FULL/16 LR corners per case')
