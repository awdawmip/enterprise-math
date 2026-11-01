"""Author-side source-typed D25 bridge: signed full beta clipping and CM Wronskian
moment at every p-adic lift of the same simple root. No native H0/B0 execution.
"""
from math import comb
from d25_beta_middle_moment_fourport_20261101 import primes


def eval_poly(coeff,z,n):
    out=0
    for c in coeff[::-1]:out=(out*z+c)%n
    return out


def mul(x,y,p):
    z=[0]*(len(x)+len(y)-1)
    for i,xi in enumerate(x):
        if xi:
            for j,yj in enumerate(y):z[i+j]=(z[i+j]+xi*yj)%p
    return z


def cm_data(p):
    t=(p-5)//8; a=5*t+3; h=(p-1)//2
    assert p>=13 and p%24==13
    Q=[(-1)**j*comb(t,j)*comb(a+j,j) for j in range(t+1)]
    qprime=[(j*Q[j])%p for j in range(1,len(Q))]
    binom=[(-1)**j*comb(h,j)%p for j in range(h+1)]
    # V'(z)= -1/4 (1+3z)(1-z)^h Q(z)^2, V(0)=0.
    Vprime=mul(mul([1,3],binom,p),mul([q%p for q in Q],[q%p for q in Q],p),p)
    V=[0]*(len(Vprime)+1)
    for j,u in enumerate(Vprime):
        assert (j+1)%p
        V[j+1]=(-u*pow(4*(j+1),-1,p))%p
    return Q,qprime,V,h


def raw_clausen(p,z):
    N=p*p
    # z is a chosen p-local lift of the same residue root.
    g=0; h=0; b=0; beta=[]
    u=1;v=1
    for k in range(p):
        beta.append(u)
        g=(g+u)%N
        h=(h+(16*k+1)*u)%N
        b=(b+(8*k+1)*v)%N
        if k<p-1:
            u=u*(8*k+1)*(8*k+3)*z*pow(64*(k+1)*(k+1),-1,N)%N
            v=v*(4*k+1)*(4*k+2)*(4*k+3)*z*pow(64*(k+1)**3,-1,N)%N
    # Independently read signed and clipped original beta square.
    s0=[0]*(p+1);s1=[0]*(p+1)
    for j in range(p-1,-1,-1):
        s0[j]=(s0[j+1]+beta[j])%N
        s1[j]=(s1[j+1]+j*beta[j])%N
    tail=sum(beta[i]*((8*i+1)*s0[p-i]+8*s1[p-i]) for i in range(1,p))%N
    assert (g*h-b-tail)%N==0,(p,z,g,h,b,tail)
    assert g%p==0
    assert h%p!=0
    return g,h,b,tail


def check(p,deltas=(0,1,2,7)):
    N=p*p; z0=pow(9,-1,N); lam=z0%p
    Q,Qd,V,hh=cm_data(p)
    assert eval_poly(Q,lam,p)==0
    qp=eval_poly(Qd,lam,p)
    assert qp!=0
    assert pow((1-lam)%p,hh,p)==p-1  # Legendre (8/9|p)=-1 for p=13 mod24.
    v0=eval_poly(V,lam,p)
    result=[]
    for delta in deltas:
        z=(z0+p*delta)%N
        qz=eval_poly(Q,z,N)
        assert qz%p==0
        M=(8*lam*pow(1-lam,hh+2,p)*qp*(qz//p)-v0+5*lam)%p
        g,h,b,tail=raw_clausen(p,z)
        D=((b+tail)%N)//p%p
        assert D==h%p*(g//p)%p
        assert D==(-2*M)%p,(p,delta,D,M)
        result.append((delta,D,M,b%N,tail%N))
    return p,qp,v0,result


def main():
    rows=[check(p) for p in (13,37,61,109,373)]
    print('PASS_BETA_LL_CM_MOMENT_SIGNED_LIFT 5 target primes x 4 p-adic lifts')
    for p,qp,v,rr in rows:
        print('p=',p,'Qprime=',qp,'V=',v,'(delta, (B+T)/p, M, B_mod_p2, T_mod_p2)=',rr)
if __name__=='__main__':main()
