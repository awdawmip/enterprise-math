"""Exact dual identities and witnesses: N4 BU bit phase; standard library only."""
from fractions import Fraction as F
from random import Random
from json import dumps
Z,O=F(0),F(1)
def calc(z,A,B,c,u,v):
    U,V=A*u,B*v
    s=(A-1+B-F(1,20))/2
    t=(A-1+3*(B-F(1,20)))/4
    H=B*c/4
    rq=z/6-A*c/6-U/3-V/4
    rp=z/6-A*c/6-U/12-V/2
    dq=(s,H-s-rq,rq,-H)
    dp=(t,H-t-rp,rp,-H)
    e=max(sum(map(abs,dq))/2,sum(map(abs,dp))/2)
    return e,s,t,H,rq,rp,dq,dp,U,V
def witness(z):
    if z<=F(7,40): c,u,v=Z,2*z/7,40*z/7
    else: c,u,v=(40*z-7)/44,(40*z+37)/880,O
    return c,u,v
def check(z,A,B,c,u,v):
    e,s,t,H,rq,rp,dq,dp,U,V=calc(z,A,B,c,u,v)
    assert Z<=c<=O and Z<=u<=O and Z<=v<=O
    assert e>=c/80
    target=max(Z,(40*z-7)/3520)
    if z>F(7,40) and c<(40*z-7)/44:
        if c<=F(3,7):
            al=(c+4)/(23-2*c)
            be=(3-7*c)/(23-2*c)
            ga=2*(1+4*c-c*c)/(23-2*c)
            de=2*(c*c-2*c+7)/(23-2*c)
            assert min(al,be,ga,de)>=Z and al+be+ga+de==O
            lhs=al*dq[1]+be*(H-s)+ga*dp[2]+de*(t+rp)+7*al*(V-B)/4
            rhs=(al*(40*z-7-44*c)+c)/80
            assert lhs==rhs and e>=rhs>=target
        else:
            ws=(7*(1-c)/20,(7*c-3)/20,(3*c+1)/10,(7-3*c)/10)
            assert min(ws)>=Z and sum(ws,Z)==O
            lhs=ws[0]*dq[1]+ws[1]*(H-rq)+ws[2]*rp+ws[3]*(t+rp)+F(7,20)*(V-B)
            assert lhs==(40*z-7-39*c)/400 and e>=lhs>=target
    else: assert e>=target
    return e
rng=Random(2026102902)
zs=sorted(set([F(k,40) for k in range(41)]+[F(7,40)-F(1,1000),F(7,40)+F(1,1000)]))
for z in zs:
    c,u,v=witness(z)
    assert check(z,O,F(1,20),c,u,v)==max(Z,(40*z-7)/3520)
    for _ in range(300):
        vals=[F(rng.randrange(101),100) for i in range(5)]
        check(z,*vals)
print(dumps({'status':'PASS_EXACT_BU_BIT_PHASE_RELEASE',
    'formula':'d2(z)=d23(z)=max(0,(40*z-7)/3520)',
    'z_cases':len(zs),'rational_competitor_cases':len(zs)*300,
    'low_c_dual':'IDENTITY_PASS','high_c_dual':'IDENTITY_PASS',
    'real_interval_proof':'PROOF.md','native_X6_bridge':'NOT_ESTABLISHED',
    'acceptance':'AUTHOR_SIDE_UNREVIEWED'},indent=2,sort_keys=True))
