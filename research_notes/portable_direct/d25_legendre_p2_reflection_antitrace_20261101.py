#!/usr/bin/env python3
"""D25 portable theorem certificate: p^2 reflection of truncated 1/4,3/4
hypergeometric polynomial; quadratic anti-trace and first nonzero p^3 defect.
This is author-side exact modular arithmetic, not a native H0/B0 benchmark.
"""
from math import comb


def primes_to(bound):
    arr = [True] * (bound + 1)
    arr[0] = arr[1] = False
    for d in range(2, int(bound ** 0.5) + 1):
        if arr[d]:
            for x in range(d*d, bound+1, d):
                arr[x] = False
    return [p for p in range(5, bound+1) if arr[p]]


def period_coefficients(p, precision=2):
    """Exact (1/4)_k (3/4)_k / (k!)^2 in Z/p^precision, k < p."""
    modulus = p ** precision
    result = [1]
    for k in range(p-1):
        multiplier = (4*k + 1)*(4*k + 3)
        denom = 16*(k+1)**2
        assert denom % p != 0
        result.append((result[-1]*multiplier*pow(denom, -1, modulus)) % modulus)
    return result


def reflected_coefficients(coefficients, modulus):
    """Coefficient list for U(1-z), with no polynomial interpolation."""
    n = len(coefficients)
    return [((-1)**j)*sum(coefficients[k]*comb(k,j)
                                for k in range(j,n)) % modulus
            for j in range(n)]


def mul_quad(x,y,mod):
    """Ring (Z/mod)[T]/(T^2-2), preserving both quadratic coordinates."""
    a,b=x; c,d=y
    return ((a*c+2*b*d)%mod,(a*d+b*c)%mod)


def evaluate_quad(coefficients,t,mod):
    out=(0,0)
    for coeff in coefficients[::-1]:
        out=mul_quad(out,t,mod)
        out=((out[0]+coeff)%mod,out[1])
    return out


def gauss_beta(p):
    """Separate original 1/8,3/8 Gauss sum at 1/9, reduced mod p^2."""
    modulus=p*p
    coeff=1
    total=0
    for k in range(p):
        total=(total+coeff)%modulus
        if k<p-1:
            coeff=coeff*(8*k+1)*(8*k+3)*pow(576*(k+1)**2,-1,modulus)%modulus
    return total


def check_reflection(p):
    modulus=p*p
    seq=period_coefficients(p)
    n=(p-1)//4
    sign=(-1)**n
    reflected=reflected_coefficients(seq,modulus)
    assert all((reflected[k]-sign*seq[k])%modulus==0 for k in range(p)),p
    assert sum(seq)%modulus == sign%modulus,p
    assert seq[-1] % modulus == 0,p
    # Reduction modulo p agrees with the terminating degree-n Legendre polynomial.
    leg=[((-1)**k)*comb(n,k)*comb(n+k,k)%p for k in range(n+1)]
    assert [x%p for x in seq] == leg + [0]*(p-n-1),p
    # The p^2 symmetry is usually sharp already at the constant coefficient.
    seq3=period_coefficients(p,3)
    defect=(sum(seq3)-sign)%(p**3)
    assert defect%(p*p)==0
    return defect//(p*p)


def quadratic_pullback_coefficients(p):
    """All coefficients of F_beta,p(4t(1-t)) mod p^2; no formal-series black box."""
    modulus=p*p
    beta=[1]
    for k in range(p-1):
        beta.append(beta[-1]*(8*k+1)*(8*k+3)*
                    pow(64*(k+1)**2,-1,modulus)%modulus)
    poly=[0]*(2*p-1)
    for k,b in enumerate(beta):
        factor=b*pow(4,k,modulus)%modulus
        for r in range(k+1):
            j=k+r
            poly[j]=(poly[j]+factor*((-1)**r)*comb(k,r))%modulus
    leg=period_coefficients(p)
    assert poly[:p]==leg,('quadratic transform low coefficient mismatch',p)
    return poly[p:]


def check_quadratic_high_tail(p):
    modulus=p*p
    t=(pow(2,-1,modulus),-pow(3,-1,modulus)%modulus)
    conjugate=((1-t[0])%modulus,(-t[1])%modulus)
    high=quadratic_pullback_coefficients(p)
    # R_p(t)=t^p * [sum_{j=p}^{2p-2} coeff_j*t^(j-p)] exactly.
    for x in (t,conjugate):
        tail=mul_quad(evaluate_quad(high,x,modulus),
                      tuple_power_quad(x,p,modulus),modulus)
        period=evaluate_quad(period_coefficients(p),x,modulus)
        target=(gauss_beta(p),0)
        assert ((tail[0]+period[0])%modulus,(tail[1]+period[1])%modulus)==target, (p,x)
    left=mul_quad(evaluate_quad(high,t,modulus),tuple_power_quad(t,p,modulus),modulus)
    right=mul_quad(evaluate_quad(high,conjugate,modulus),tuple_power_quad(conjugate,p,modulus),modulus)
    assert ((left[0]+right[0])%modulus,(left[1]+right[1])%modulus)==(2*gauss_beta(p)%modulus,0)
    return left,right


def tuple_power_quad(x, n, modulus):
    total=(1,0)
    while n:
        if n&1:
            total=mul_quad(total,x,modulus)
        x=mul_quad(x,x,modulus)
        n>>=1
    return total


def check_quadratic(p):
    modulus=p*p
    assert p%8==5
    seq=period_coefficients(p)
    t=(pow(2,-1,modulus),-pow(3,-1,modulus)%modulus)
    other=((1-t[0])%modulus,(-t[1])%modulus)
    assert (4*mul_quad(t,other,modulus)[0])%modulus == pow(9,-1,modulus)
    assert mul_quad(t,other,modulus)[1]==0
    u=evaluate_quad(seq,t,modulus)
    v=evaluate_quad(seq,other,modulus)
    assert (u[0]+v[0])%modulus==0 and (u[1]+v[1])%modulus==0
    assert u[0]==0 and v[0]==0, (p,u,v)
    assert u[1] == (-v[1]) % modulus
    assert pow(2,(p-1)//2,p)==p-1
    return u,gauss_beta(p)


def main():
    ps=primes_to(211)
    defects={p:check_reflection(p) for p in ps}
    assert len(ps)==45,(len(ps),ps)
    controls=(5,13,29,37,53,61,109,373)
    rows={p:check_quadratic(p) for p in controls}
    assert rows[13]==((0,39),0)
    assert rows[29]==((0,836),287)
    assert rows[373]==((0,42895),0)
    assert defects[13]==12
    tails={p:check_quadratic_high_tail(p) for p in (13,29,37,373)}
    print('PASS_REFLECTION_COEFFICIENTWISE:',len(ps),'primes 5<=p<=211')
    print('p^3 constant-term defect at p=13: 12*p^2 (mod p^3)')
    print('PASS_QUADRATIC_ANTITRACE:',len(rows),'primes p=5 mod8')
    print('PASS_EXACT_QUADRATIC_HIGH_TAIL:',len(tails),'primes [13,29,37,373]')
    for p in controls:
        u,g=rows[p]
        print('p=',p,'U_p(1/2-sqrt(2)/3) [rational,sqrt2] modulo p^2=',u,
              'original_G_beta(1/9) modulo p^2=',g)
    for p,(left,right) in tails.items():
        print('tail p=',p,'left/right quadratic coordinates=',left,right)


if __name__=='__main__':
    main()
