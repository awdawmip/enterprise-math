from fractions import Fraction as Q
from functools import cache
from math import comb, prod
import json

@cache
def F(k,n):
    return prod((Q(4*j+k,4*(j+k)) for j in range(1,n+1)), start=Q(1))

def rho_tau(k,n,s):
    rho=4*F(k,n)/F(k,s-1)
    factor=Q(28*(k-1+4*s)*prod(range(s+k,s+4*k)),
             (s+k-1)*prod(range(n+k+1,n+4*k+1)))
    return rho,rho*factor

def up(x,r): return prod((x+i for i in range(r)),start=Q(1))
def down(x,r): return prod((x-i for i in range(r)),start=Q(1))
def diff(fn,x,r): return sum(((-1)**(r-i)*comb(r,i)*fn(x+i) for i in range(r+1)),Q(0))

def terminal(w):
    amp=F(1,w)/F(1,2)
    t=Q(840,(w+2)*(w+3)*(w+4))
    return [amp*(t*a+b)/(1+amp*t*a) for a,b in [(Q(3,32),Q(15,32)),(Q(3,2),Q(15,8)),(Q(6),Q(3))]]

def block(k,n,s,z):
    r,t=rho_tau(k,n,s)
    return (r+t*z)/(1+t*z)

def inner(v,w): return [block(3,v,w,z) for z in terminal(w)]
def width(n,v,w):
    z=[block(5,n,v,t) for t in inner(v,w)]
    return max(z)/min(z)

def generic_euler(k,n,b,lo,hi,s):
    r,t=rho_tau(k,n,s)
    rb,tb=rho_tau(k,n+b,s)
    if lo==hi or r==1: return None
    u,v=(lo,hi) if r<1 else (hi,lo)
    a,beta=Q(3*k,4),Q(15*k,4)
    q=r/abs(1-r)
    eta=Q(b,n)
    if eta>1/(2*max(beta,a*q)): return None
    assert (1-r)*(1-rb)>0
    D=(1+t*v)*(r+t*u)
    P=(v-u)*t*(1-r)
    h=P/D
    hb=(v-u)*tb*(1-rb)/((1+tb*v)*(rb+tb*u))
    assert h>0 and hb>0
    E=-beta+a*r/(1-r)+beta*t*v/(1+t*v)+(a*r+beta*t*u)/(r+t*u)
    C1=a*(q+1)*(k+1)+3*beta*(4*k+1)
    A=beta+a*q
    B=a*beta*q
    K=a+2*beta
    L=a*beta+beta*beta
    C2=(a*(a+1)*(q+1)+3*beta*(beta+1))/2+4*(B+L+(A+K)*(K+L/(2*beta)))
    actual=abs(Q(n,b)*(hb/h-1)-E)
    bound=(C1+C2*b)/n
    assert actual<=bound,(k,n,b,s,lo,hi,actual,bound)
    return actual/bound

def main():
    checks={"n_jet":0,"s_jet":0,"newton_remainder":0,"physical_euler":0,"auxiliary_euler":0}
    for k in (1,3,5):
        a,beta=Q(3*k,4),Q(15*k,4)
        for n in range(2,20):
            for s in range(2,n+1):
                rho,tau=rho_tau(k,n,s)
                for r in range(5):
                    assert diff(lambda N:rho_tau(k,N,s)[0],n,r)==(-1)**r*up(a,r)/up(Q(n+k+1),r)*rho
                    assert diff(lambda N:rho_tau(k,N,s)[1],n,r)==(-1)**r*up(beta,r)/up(Q(n+4*k+1),r)*tau
                    checks["n_jet"]+=2
                    if s+r<=n+1:
                        assert diff(lambda S:rho_tau(k,n,S)[0],s,r)==down(a,r)/up(Q(s)+Q(k,4),r)*rho
                        us=lambda S:Q(4*S+k-1,S+k-1)
                        assert diff(lambda S:rho_tau(k,n,S)[1]/us(S),s,r)==down(beta,r)/up(Q(s)+Q(k,4),r)*tau/us(s)
                        checks["s_jet"]+=2
                for b in (1,2,3,7):
                    for order in range(1,min(b,4)+1):
                        for index,x,d0,base in [(0,a,n+k+1,rho),(1,beta,n+4*k+1,tau)]:
                            total=sum((comb(b,r)*(-1)**r*up(x,r)/up(Q(d0),r)*base for r in range(order)),Q(0))
                            rem=(-1)**order*(rho_tau(k,n+b,s)[index]-total)
                            upper=comb(b,order)*up(x,order)/up(Q(d0),order)*base
                            assert 0<=rem<=upper
                            checks["newton_remainder"]+=1
    worst=Q(0)
    for n in (24,40,80,160):
        for v in (2,n//4,n//2,n):
            for w in sorted(set((2,max(2,v//2),v))):
                vals=inner(v,w)
                for b in (1,2,3):
                    result=generic_euler(5,n,b,min(vals),max(vals),v)
                    if result is not None:
                        worst=max(worst,result);checks["physical_euler"]+=1
    for k in (1,3,5):
        for n in (40,80):
            for s in (2,n//3,n):
                for b in (1,2):
                    for u,v in ((Q(1,1000),Q(1,999)),(Q(1,2),Q(3)),(Q(100),Q(1001,10))):
                        result=generic_euler(k,n,b,u,v,s)
                        if result is not None: checks["auxiliary_euler"]+=1
    a,beta,q=Q(15,4),Q(75,4),Q(7,3)
    C1=a*(q+1)*6+3*beta*21
    A=beta+a*q;B=a*beta*q;K=a+2*beta;L=a*beta+beta*beta
    C2=(a*(a+1)*(q+1)+3*beta*(beta+1))/2+4*(B+L+(A+K)*(K+L/(2*beta)))
    assert C1==(4815+90*q)/4
    assert C2==(475260+34485*q)/32
    result={"status":"PASS","arithmetic":"fractions.Fraction exact","checks":checks,
            "total_checks":sum(checks.values()),"physical_worst_error_to_bound_upper":str(Q((worst.numerator*10**6+worst.denominator-1)//worst.denominator,10**6)),
            "scope":"Author-side finite checks; universal statements proved in DISCRETE_JET_PROOF.md"}
    print(json.dumps(result,indent=2))
if __name__=="__main__":main()

