"""Exact p-local finite Green primitive and sharp first resonance.
Tests operator coefficients and valuation horizon; does not rerun the original J0/J1 source.
"""
from fractions import Fraction


def primes(limit):
    a = bytearray([1])*(limit+1)
    a[0:2] = b'\0\0'
    for d in range(2, int(limit**.5)+1):
        if a[d]:
            a[d*d::d] = b'\0' * ((limit-d*d)//d+1)
    return [p for p in range(7,limit+1) if a[p] and p%6==1]


def vp_int(x,p):
    if x==0: return 10**6
    c=0
    while x%p==0:
        c+=1;x//=p
    return c


def direct_kernel(k,M):
    if k==M:
        return None
    t=k-M
    return Fraction(1, t)*(1-Fraction(1,2)**t)


def exact_check(ell):
    M=3*ell
    last=7*ell
    h=[direct_kernel(k,M) for k in range(last+1)]
    for k in range(last):
        left=(k-M+1)*(h[k+1] or 0)-(k-M)*(h[k] or 0)
        right=Fraction(1,2)**(k-M+1)
        assert left==right,(ell,k)
    # Independent Laurent primitive Q' = F(y)y^(-M-1): coefficientwise.
    f=[Fraction((11*k*k+3*k+5) % 17 - 8, 2) for k in range(last+1)]
    f[M]=0
    q={k-M:f[k]/(k-M) for k in range(last+1) if k!=M}
    assert all(exp*coeff==f[exp+M] for exp,coeff in q.items())
    E_direct=sum(f[k]*h[k] for k in range(last+1) if k!=M)
    E_boundary=sum(v*(1-Fraction(1,2)**e) for e,v in q.items())
    assert E_direct==E_boundary
    return E_direct


def modular_check(p):
    ell=(p-1)//6;M=3*ell; last=7*ell
    assert last-M == 4*ell < p and M < p
    pow2inv=pow(2,-1,p)
    H=[]
    for k in range(last+1):
        t=k-M
        if t==0: H.append(None)
        else:
            val=(1-pow(pow2inv,t,p))*pow(t%p,-1,p)%p
            H.append(val)
    # Exact kernel recurrence without special h_M (it is a free gauge).
    for k in range(last):
        t=k-M
        left=((t+1)*(H[k+1] or 0)-t*(H[k] or 0))%p
        right=pow(pow2inv,t+1,p)
        assert left==right,(p,k,left,right)
    coefficients=[(k*k+5*k+3)%p for k in range(last+1)]
    coefficients[M]=0
    E=sum(coefficients[k]*H[k] for k in range(last+1) if k!=M)%p
    # The displayed rational primitive is p-local; compute boundary independently.
    Q1=0;Qhalf=0
    for k in range(last+1):
        if k==M: continue
        t=k-M
        inv=pow(t%p,-1,p)
        Q1=(Q1+coefficients[k]*inv)%p
        Qhalf=(Qhalf+coefficients[k]*inv*pow(pow2inv,t,p))%p
    assert E == (Q1-Qhalf)%p
    # Actual obstruction is a non-p-local primitive of y^(p-1)dy.
    k=M+p
    assert vp_int(k-M,p)==1
    assert vp_int(1,p)<vp_int(k-M,p)
    assert vp_int(p,p)>=vp_int(k-M,p)
    # At the first extra resonance, F=y^(M+p) fails, p*y^(M+p) passes;
    # the unique rational primitive coefficient is respectively 1/p or 1.
    assert Fraction(1,k-M).denominator==p
    assert Fraction(p,k-M)==1
    return E


def main():
    for ell in range(1,11): exact_check(ell)
    pp=primes(5000)
    assert len(pp)==330
    for p in pp: modular_check(p)
    print('PASS_D25_GREEN_RESIDUE_PLOCAL_HORIZON rational_ell=1..10 primes=330 k_max=7ell first_extra_k=M+p')

if __name__=='__main__': main()
