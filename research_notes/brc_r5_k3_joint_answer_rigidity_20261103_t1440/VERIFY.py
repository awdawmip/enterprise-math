from fractions import Fraction as F
from itertools import product

c=(F(1,8),F(1,6),F(1,16),F(3,32))
alpha=(F(1,2),F(2,3),F(1,2),F(3,4))
flat=(F(1,2),)*4
patterns=(
 (F(1,4),F(1,2),F(3,4),F(1,2)),
 (F(1,16),F(3,4),F(15,16),F(1,8)),
 (F(3,4),F(1,4),F(1,8),F(7,8)),
 flat
)

def observe(x,y,i,gate,p,q):
    w=(F(1,4),(1-x)/4,y/8,i/8)
    d=y/16+3*i/32
    M=[w[s]*alpha[s] if gate[s]>=1 else F(0) for s in range(4)]
    S=[F(2,3)*M[s] if gate[s]>=2 else F(0) for s in range(4)]
    U=[S[s] if gate[s]>=3 else F(0) for s in range(4)]
    return (F(107,128)-21*x/128+d/4-sum(S)/2+sum(p[s]*U[s] for s in range(4))/8,
            F(13,64)+3*x/64-d/2+sum(S)/8+sum(q[s]*U[s] for s in range(4))/32,
            F(3)+sum(M)+3*sum(S)/2+F(3,4)*sum(U),
            F(3)+sum(M)/2+3*sum(S)/8+F(3,16)*sum(U))

def brute(n,p,q,full):
    if full:
        upstream=((F(0),F(0)),(F(0),F(1)),(F(1),F(0)))
        points=((x,F(y),i,g) for x,i in upstream for y in (0,1) for g in product(range(4),repeat=4))
    else:
        points=((F(x),F(y),F((1-x)*y),(j,)*4) for x,y,j in product((0,1),(0,1),range(4)))
    return max(sum(n[k]*w[k] for k in range(4)) for x,y,i,g in points for w in [observe(x,y,i,g,p,q)])

def normals(tau):
    return ((F(8),F(0),-(4+8*tau)/9,(80+16*tau)/9),
            (F(0),F(-32),(8*tau-4)/9,(80-16*tau)/9))

def gaps(a,tau):
    P=sum(c[s]*max(a[s]-tau,F(0)) for s in range(4))
    N=sum(c[s]*max(tau-a[s],F(0)) for s in range(4))
    return F(2,3)*min(P,N)

count=0
for tau in (F(1,4), F(1,2), F(3,4)):
    np,nq=normals(tau)
    assert np[2]+np[3]/2==4 and nq[2]+nq[3]/2==4; count+=1
    for p in patterns:
        for q in patterns:
            for name,n,a in (('P',np,p),('Q',nq,q)):
                hF=brute(n,p,q,True); hLR=brute(n,p,q,False)
                assert hF-hLR==gaps(a,tau), (name,tau,p,q,hF,hLR)
                count+=1
# 3 thresholds x 4 P vectors x 4 Q vectors x 2 isolators =96 full exact support tests.
tau=F(1,2)
p=(F(1,4),F(1,2),F(3,4),F(1,2))
q=(F(3,4),F(1,2),F(1,4),F(1,2))
np,nq=normals(tau)
witness=observe(F(0),F(1),F(1),(1,1,3,1),p,q)
for name,n,a in [('P',np,p),('Q',nq,q)]:
    hF=brute(n,p,q,True); hLR=brute(n,p,q,False)
    assert sum(n[k]*witness[k] for k in range(4))==hF; count+=1
    assert gaps(a,tau)==F(1,96); count+=1
    print(name,'normal=',n,'hFULL=',hF,'hLR=',hLR,'witness=',witness,'Linf>=',(hF-hLR)/sum(map(abs,n)))
# Whole-source constant p,q: finite exact policy aggregation test on non-vertices.
p=flat;q=(F(3,5),)*4
for t in range(40):
    x=F(t%7,12); i=F((t*3)%8,13); y=F((t*11)%13,17)
    if x+i>1: i=1-x
    zz=[F(((t+7*s)%11),12) for s in range(4)]
    tt=[F(((t+3*s)%9),10) for s in range(4)]
    uu=[F(((t+5*s)%7),8) for s in range(4)]
    wa=(F(1,4),(1-x)/4,y/8,i/8)
    ms=[wa[s]*alpha[s]*zz[s] for s in range(4)]
    ss=[F(2,3)*ms[s]*tt[s] for s in range(4)]
    us=[ss[s]*uu[s] for s in range(4)]
    d=y/16+3*i/32
    yr=32*d/(5-3*x)
    assert 0<=yr<=1; count+=1
    newmass=(F(1,8)+(1-x)/6+yr/16+3*(1-x)*yr/32)
    z=sum(ms)/newmass
    tr=F(3,2)*sum(ss)/sum(ms) if sum(ms) else F(0)
    ur=sum(us)/sum(ss) if sum(ss) else F(0)
    assert all(0<=a<=1 for a in (z,tr,ur)); count+=1
    def from_totals(x,d,M,S,U):
        return (F(107,128)-21*x/128+d/4-S/2+p[0]*U/8,
                F(13,64)+3*x/64-d/2+S/8+q[0]*U/32,
                F(3)+M+3*S/2+F(3,4)*U,
                F(3)+M/2+3*S/8+F(3,16)*U)
    lhs=from_totals(x,d,sum(ms),sum(ss),sum(us))
    mr=newmass*z; sr=F(2,3)*mr*tr; u=sr*ur
    rhs=from_totals(x,yr*(5-3*x)/32,mr,sr,u)
    assert lhs==rhs; count+=1
print('PASS_EXACT_R5_K3_JOINT_ANSWER_SOURCE_RIGIDITY',count,'exact assertions; 96 paired full(1536)/LR(16) support comparisons, 40 nonbinary aggregations')
