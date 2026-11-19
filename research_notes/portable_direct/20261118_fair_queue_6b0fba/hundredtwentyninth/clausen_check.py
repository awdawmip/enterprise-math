"""Exact finite Euler--Clausen check, including the finite upper boundary."""
from fractions import Fraction
from math import comb, isqrt
import json


def prime(p):
    return p>1 and all(p%d for d in range(2,isqrt(p)+1))


def mod(x, q):
    return x.numerator*pow(x.denominator,-1,q)%q


def integer_j(n):
    return sum(comb(n,k)*comb(2*n+1,k)*(1<<(n-k)) for k in range(n+1))


def direct(p):
    M=(2*p-1)//3
    q=p**3
    W=E=0
    e=1
    for k in range(M+1):
        b=comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,q)%q
        W=(W+(6*k+1)*b)%q
        E=(E+(6*k+1)*e)%q
        e=-e*(3*k+1)**3*pow(27*(k+1)**3,-1,q)%q
    return W,E


def normalized(p):
    L=(p+1)//6
    M=4*L-1
    q=p*p
    # q_k = 2^(-k) b_k with the two known p's removed as integers.
    z=[1]
    for k in range(1,M+1):
        a,b=6*k-1,3*k-1
        if k==L:
            assert a==p
            a//=p
        if k==2*L:
            assert b==p
            b//=p
        z.append(z[-1]*a*b*pow(36*k*k,-1,q)%q)
    return z


def truncation_tail(p, z):
    L=(p+1)//6
    n=L-1
    M=4*L-1
    sums=[0]
    deriv=[0]
    for k in range(L):
        sums.append((sums[-1]+z[k])%p)
        deriv.append((deriv[-1]+k*z[k])%p)
    val=0
    for j in range(2*L,M+1):
        # i+j<=M for the first term; i+j+1<=M for the second.
        u=min(n,M-j)+1
        v=min(n,M-j-1)+1
        val+=z[j]*((1+6*j)*sums[u]+6*deriv[u]-
                    pow(2,-1,p)*((7+6*j)*sums[v]+6*deriv[v]))
    return val%p


def correction(p):
    L=(p+1)//6
    n=L-1; m=2*n+1
    q=p*p
    z=normalized(p)
    H=sum(z[L:2*L])%q
    slope=6*(sum(k*z[k] for k in range(L))+
             p*sum(k*z[k] for k in range(L,2*L)))%q
    assert slope%p
    tail=truncation_tail(p,z)
    a=b=0
    h=squares=0
    for k in range(1,n+1):
        v=pow(6*(n-k+1),-1,q)
        w=pow(3*(m-k+1),-1,q)
        h=(h+v+w)%q
        squares=(squares+v*v+w*w)%p
        ck=comb(n,k)*comb(m,k)*pow(2,-k,q)%q
        a=(a+ck*h)%q
        b=(b+ck*(h*h-squares)*pow(2,-1,p))%p
    invd=pow(slope,-1,q)
    vstar=(-invd+p*invd*(5*pow(2,-1,p)*invd**2-2*tail))%q
    expected=(pow(2,n,q)*(vstar+a-p*b-H))%q
    j=integer_j(n)
    assert j%p==0
    jp=j//p%q
    assert (jp-expected)%p==0
    digit=(slope*pow(108*(1<<n),-1,p)*((jp-expected)//p))%p
    return dict(p=p,n=n,j_reduced=jp,predicted=expected,upper_boundary=tail,
                slope_mod_p=slope%p,third_digit=digit,
                digit_if_high_block_omitted=(digit-2*tail*pow(108,-1,p))%p)


def exact_sums(p):
    L=(p+1)//6; n=L-1; M=4*L-1
    q=p**3
    coeff=[Fraction(1)]
    for k in range(1,M+1):
        coeff.append(coeff[-1]*(6*k-1)*(3*k-1)/(36*k*k))
    # z already evaluated at 1/2. A z-shift costs a further factor 1/2.
    prodvalue=sum((1+6*(i+j))*u*v -
                   ((7+6*(i+j))*u*v/2 if i+j<M else 0)
                   for i,u in enumerate(coeff)
                   for j,v in enumerate(coeff[:M+1-i]))
    ordinary=sum(Fraction((6*k+1)*comb(2*k,k)**2*comb(3*k,k),216**k)
                 for k in range(M+1))
    assert prodvalue==ordinary
    d=direct(p)[0]
    assert mod(prodvalue,q)==d
    lost_core=-(6*M+1)*coeff[2*L-1]**2/2
    assert mod(lost_core,q)%(p*p)==0 and mod(lost_core,q)!=0
    K=sum(coeff[:2*L])
    DK=sum(i*u for i,u in enumerate(coeff[:2*L]))
    core=K*(6*DK-5*K/2)
    rr=sum(coeff[i]*coeff[j]/(p*p)*((1+6*(i+j))-
                (Fraction(7+6*(i+j),2) if i+j<M else 0))
                for j in range(2*L,M+1) for i in range(min(n,M-j)+1))
    assert (mod(core,q)+2*p*p*mod(rr,p))%q==d
    assert mod(rr,p)==truncation_tail(p,normalized(p))
    return dict(p=p,core=mod(core,q),twice_tail_mod_p=2*mod(rr,p)%p,
                exact_original=mod(prodvalue,q))


def check_algebraic(limit):
    # u=t(1+u)^2(1+2u), and J=(1+u)/(1-t(4+10u+6u^2)).
    def mul(a,b):
        return [sum(a[j]*b[k-j] for j in range(k+1)) for k in range(limit+1)]
    u=[0]*(limit+1)
    for k in range(1,limit+1):
        u2=mul(u,u)
        u[k]=(int(k==1)+4*u[k-1]+5*u2[k-1]+2*mul(u,u2)[k-1])
    u2=mul(u,u)
    deriv=[4*int(k==0)+10*u[k]+6*u2[k] for k in range(limit+1)]
    j=[integer_j(k) for k in range(limit+1)]
    rhs=mul(j,deriv)
    for k in range(limit+1):
        assert j[k]-(rhs[k-1] if k else 0)==int(k==0)+u[k]
    return j[:7]


def main():
    names=(17,23,41,47,71,89,167,311,503,1193)
    rows=[]; witnesses=[]; zero=0; total=0; discrepancies=0
    for p in range(5,1201):
        if p%24 not in (17,23) or not prime(p):
            continue
        row=correction(p)
        W,E=direct(p)
        assert (W+p)%(p*p)==0 and (E+2*p)%p**3==0
        assert row['third_digit']==((W+p)//(p*p))*pow(108,-1,p)%p
        total+=1
        discrepancies+=int(row['third_digit']!=0)
        zero+=(row['upper_boundary']==0)
        if p in names or (row['upper_boundary']==0 and not witnesses):
            rows.append(row)
        if row['upper_boundary']==0:
            witnesses.append(p)
    return dict(target_primes=total,upper_bound=1200,
                original_digit_nonzero=discrepancies,
                upper_boundary_zero_primes=witnesses,
                upper_boundary_nonzero_count=total-zero,
                algebraic_initial=check_algebraic(18),samples=rows,
                exact_rational_replays=[exact_sums(p) for p in (17,23,41,47)])


if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
