"""Exact asymmetric K3 clock-face separation checks; standard-library rationals only."""
from fractions import Fraction as F
from itertools import product

C = (F(1,8), F(1,6), F(1,16), F(3,32))
UP_FULL = ((0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,1,0))
UP_LR = ((0,0,0),(0,1,1),(1,0,0),(1,1,0))
STAGES = ((0,0,0),(1,0,0),(1,1,0),(1,1,1))
CHECKS=0

def check(a,b):
    global CHECKS
    CHECKS += 1
    assert a==b, (CHECKS,a,b)

def obs(up,js,p,q,r,v):
    x,y,i=up
    c=(C[0],F(1-x,6),F(y,16),F(3*i,32))
    d=F(y,16)+F(3*i,32)
    M=tuple(c[s]*STAGES[js[s]][0] for s in range(4))
    S=tuple(F(2,3)*M[s]*STAGES[js[s]][1] for s in range(4))
    U=tuple(S[s]*STAGES[js[s]][2] for s in range(4))
    return (F(107,128)-F(21*x,128)+d/4-sum(S)/2+sum((p[s]*S[s]/8 for s in range(4)),F(0)),
            F(13,64)+F(3*x,64)-d/2+sum(S)/8+sum((q[s]*S[s]/32 for s in range(4)),F(0)),
            F(3)+sum(M)+F(3,2)*sum(S)+sum((r[s]*U[s] for s in range(4)),F(0)),
            F(3)+sum(M)/2+F(3,8)*sum(S)+sum((v[s]*U[s]/4 for s in range(4)),F(0)))

def dot(a,b):return sum((u*t for u,t in zip(a,b)),F(0))
def mu(r,v):return (9+2*v)/(8*(3+r))

def certify(r,v,p,q,m=F(1,3),primary=False):
    for data in (r,v,p,q):check(all(F(0)<t<F(1) for t in data),True)
    low=max(mu(r[s],v[s]) for s in (0,1))
    high=min(mu(r[s],v[s]) for s in (2,3))
    check(low < m < min(high,F(3,8)),True)
    A=tuple(2*m-F(3,4)+(4*m*r[s]-v[s])/6 for s in range(4))
    check(A[0]>0 and A[1]>0 and A[2]<0 and A[3]<0,True)
    check(m-F(1,2)<0 and 2*m-F(3,4)<0,True)
    n0=(F(0),F(0),m,-F(1))
    full=[obs(up,js,p,q,r,v) for up in UP_FULL for js in product(range(4),repeat=4)]
    lr=[obs(up,(j,)*4,p,q,r,v) for up in UP_LR for j in range(4)]
    check((len(full),len(lr)),(1536,16))
    W=obs((0,1,1),(3,3,0,0),p,q,r,v)
    H=obs((0,0,0),(3,3,3,3),p,q,r,v)
    check(tuple(W[s]-H[s] for s in range(4)),(F(5,128),-F(5,64),F(0),F(0)))
    f0=max(dot(n0,t) for t in full)
    l0=max(dot(n0,t) for t in lr)
    check((f0,l0,dot(n0,W),dot(n0,H)),(dot(n0,H),)*4)
    check(sum(dot(n0,z)==l0 for z in lr),1)
    g=min(C[1]*A[1],-C[2]*A[2]-C[3]*A[3])
    check(min(l0-dot(n0,z) for z in lr if z!=H),g)
    check(g>0,True)
    eps=g/2
    n=(eps,F(0),m,-F(1))
    check(all(0<z[0]<1 for z in lr),True)
    check(max(abs(z[0]-H[0]) for z in lr)<1,True)
    check(max(dot(n,z) for z in lr),dot(n,H))
    check(sum(dot(n,z)==dot(n,H) for z in lr),1)
    gap=dot(n,W)-dot(n,H)
    check(gap,F(5,128)*eps)
    check(gap>0,True)
    check(max(dot(n,z) for z in full) >= dot(n,W),True)
    bound=gap/sum(map(abs,n))
    if primary:
        check(g,F(1,360))
        check(eps,F(1,720))
        check(A,(F(1,36),F(1,60),-F(1,18),-F(1,20)))
        check(W,(F(455,576),F(39,256),F(671,180),F(13981,4320)))
        check(H,(F(865,1152),F(59,256),F(671,180),F(13981,4320)))
        check(gap,F(1,18432))
        check(bound,F(5,123008))
        check(max(dot(n,z) for z in full),dot(n,W))
        print('PRIMARY', 'mu',tuple(mu(r[s],v[s]) for s in range(4)),'stages',A)
        print('PRIMARY_W',W)
        print('PRIMARY_H',H)
        print('PRIMARY_NORMAL',n,'hFULL',max(dot(n,z) for z in full),'hLR',max(dot(n,z) for z in lr))
    print('CASE', 'r',r,'v',v,'p',p,'q',q,'LR_clock_gap',g,'eps',eps,'signed_gap',gap,'dist_inf_lower',bound)

r=(F(4,5),F(7,10),F(1,5),F(3,10))
v=(F(2,5),F(1,3),F(1,10),F(1,5))
certify(r,v,(F(1,2),)*4,(F(1,2),)*4,primary=True)
certify(r,v,(F(1,4),F(1,2),F(3,4),F(1,3)),(F(3,4),F(1,3),F(1,4),F(1,2)))
rd=tuple(r[s]+(F(1,100) if s%2==0 else -F(1,100)) for s in range(4))
vd=tuple(v[s]+(-F(1,100) if s%2==0 else F(1,100)) for s in range(4))
certify(rd,vd,(F(2,3),F(1,5),F(4,5),F(3,7)),(F(3,5),F(2,3),F(1,5),F(4,7)))
print('ASSERTIONS',CHECKS)
print('PASS_EXACT_R5_K3_ASYMMETRIC_CLOCK_FACE_FIBER')
