from fractions import Fraction as F
R=[F(1,4),F(1,2),F(1),F(3,2),F(7,4)]
A=[F(x,1000) for x in (209,184,214,184,209)]
B=[F(x,1000) for x in (191,216,186,216,191)]
M=[[(r*F(99,100),F(1,2)),(r*F(101,100),F(1,2))] for r in R]
t=F(23,28); k=F(3,4); eps=F(1,100)
def eff(Q):
    return [(s,q*p) for j,(r,q) in enumerate(zip(R,Q)) for s,p in (M[j] if r<t else [(r,F(1))])]
def I(Q,k):return min(1,k)-sum(p*min(s,k) for s,p in eff(Q))
def L(Q):return 1+sum(q for q,r in zip(Q,R) if r<t)
for Q in [A,B]:
    assert sum(Q)==sum(q*r for q,r in zip(Q,R))==1
    assert all(q>0 for q in Q)
    assert (t-1)+sum(q*max(t-r,0) for q,r in zip(Q,R))==0
    assert sum(p for s,p in eff(Q))==sum(s*p for s,p in eff(Q))==1
for r,m in zip(R,M):
    assert all(s>0 and p>0 for s,p in m)
    assert sum(p for s,p in m)==1 and sum(s*p for s,p in m)==r
assert (I(A,k),I(B,k))==(F(301,2000),F(299,2000))
assert (L(A),L(B))==(F(1393,1000),F(1407,1000))
ta=-I(A,k)/L(A);tb=-I(B,k)/L(B)
assert (ta,tb)==(F(-43,398),F(-299,2814))
delta=(ta+tb)/2
assert delta==F(-60001,559986)
n=(-eps,-eps*k,F(-1),t+eps*delta)
a,b,c,d=n
def stop(r,time):return time*(c*r+d)+max(a*r,b)
def continuation(j):return sum(p*stop(s,3) for s,p in M[j])
def scores(Q):
    s=stop(F(1),1)
    v=sum(q*max(stop(r,2),continuation(j)) for j,(q,r) in enumerate(zip(Q,R)))
    return s,v
sa,ca=scores(A);sb,cb=scores(B)
assert sa==sb
assert ca-sa==F(1,80400) and cb-sb==F(-1,79600)
assert all((continuation(j)>stop(r,2))==(r<t) for j,r in enumerate(R))
hf=(max(sa,ca)+max(sb,cb))/2
hl=max(sa,(ca+cb)/2)
assert hf-hl==F(1,160800)
# Construct explicit FULL source A policy, source B STOP/P.
def eval_A():
    ep=eq=tp=tq=F(0)
    for j,(q,r) in enumerate(zip(A,R)):
        if r<t:
            for s,p in M[j]:
                z=q*p
                ep+=z*s;tp+=3*z*s;tq+=3*z
        else:
            eq+=q;tp+=2*q*r;tq+=2*q
    return ep,eq,tp,tq
wa=eval_A()
wb=(F(0),F(1),F(1),F(1))
w=tuple((x+y)/2 for x,y in zip(wa,wb))
assert w==(F(577,8000),F(1607,2000),F(12577,8000),F(3393,2000))
assert sum(x*y for x,y in zip(w,n))==hf
lower=(hf-hl)/sum(abs(x) for x in n)
assert lower==F(1393,411669698)
checks=0
for ki in range(1,75):
    kk=F(ki,40);ee=F(1,10000)
    for Q in (A,B):
        stop1=(t-1)-ee*min(1,kk);cv=F(0)
        for j,(q,r) in enumerate(zip(Q,R)):
            stop2=2*(t-r)-ee*min(r,kk)
            cont2=sum(p*(3*(t-s)-ee*min(s,kk)) for s,p in M[j])
            assert (cont2>stop2)==(r<t)
            cv+=q*max(stop2,cont2)
        assert cv-stop1==ee*I(Q,kk)
        checks+=1
print("PASS_EXACT_R5_TANGENT_BELLMAN_IDENTIFIABILITY")
print("theta_A",ta,"theta_B",tb,"delta",delta)
print("n",tuple(map(str,n)),"W",tuple(map(str,w)))
print("hFULL",hf,"hLR",hl,"gap",hf-hl,"dist_inf_lower",lower)
print("rational_Bellman_checks",checks)