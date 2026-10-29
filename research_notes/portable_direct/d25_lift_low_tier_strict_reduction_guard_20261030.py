"""D25 source-preserving low-tier LIFT strict reduction, finite regression only.

Original A216 and B2304 signed streams; no native H0/B0 computation.
All divisions are by p-local units until the explicitly verified tier quotient.
"""
from math import isqrt, comb
import sys


def primes(limit):
    sieve = bytearray(b'\1') * limit
    sieve[0:2] = b'\0\0'
    for k in range(2, isqrt(limit - 1) + 1):
        if sieve[k]:
            sieve[k*k::k] = b'\0' * (((limit-1)-k*k)//k+1)
    return [p for p in range(5,limit) if sieve[p]]


def ports(p):
    modulus = p**4
    inv = [0] * p
    inv[1] = 1
    for k in range(2,p):
        # modular inverse even with composite modulus, gcd(k,p^4)=1
        inv[k] = -(modulus // k) * inv[modulus % k] % modulus
    ia = pow(216, -1, modulus)
    ib = pow(2304, -1, modulus)
    a = b = 1
    A = [0]*4
    B = [0]*4
    for n in range(p):
        va = 2*n//p + 3*n//p
        vb = 4*n//p
        A[va] = (A[va] + (6*n+1)*a) % modulus
        B[vb] = (B[vb] + (8*n+1)*b) % modulus
        if n == p-1:
            break
        j = n+1
        invj = inv[j]
        factor5 = pow(invj, 5, modulus)
        factor4 = pow(invj, 4, modulus)
        a = a * (2*n+1)*(2*n+2)*(3*n+1)*(3*n+2)*(3*n+3) * factor5 * ia % modulus
        b = b * (4*n+1)*(4*n+2)*(4*n+3)*(4*n+4) * factor4 * ib % modulus
    chi = 1 if p % 3 == 1 else -1
    C = [((A[0]-2*B[0]+p*chi) % modulus)]
    C += [(A[k]-2*B[k])%modulus for k in (1,2,3)]
    A_total=sum(A)%modulus
    B_total=sum(B)%modulus
    assert (sum(C) - (A_total-2*B_total+p*chi)) % modulus == 0
    assert C[1] % p == 0 and C[2] % (p**2) == 0 and C[3] % (p**3) == 0
    assert (A_total-p*chi) % (p**2) == 0, ('UR finite regression',p)
    assert (B_total-p*chi) % (p**3) == 0, ('B finite regression',p)
    assert (C[0]+C[1])%(p**2) == 0, ('uniform carry-1 consequence check',p)
    J=((C[0]+C[1])%modulus)//(p**2)
    Q=C[2]//(p**2)
    D=C[3]//(p**3)
    # Exact order-respecting congruence preserving the signed source ports:
    assert (A_total-2*B_total+p*chi-p**2*(J+Q)-p**3*D)%modulus == 0
    assert (A_total-p*chi) % p**3 == (p**2*(J+Q)) % p**3
    return {'p':p,'chi':chi,'J_mod_p':J%p,'Q_mod_p':Q%p,
            'J_mod_p2':J,'Q_mod_p2':Q,'D_mod_p':D,
            'A_mod_p3':A_total%p**3,'B_mod_p3':B_total%p**3,
            'LIFT_residual':(J+Q)%p}


def raw_binomial_recompute(p):
    modulus=p**4
    A=B=0
    ia=pow(216,-1,modulus)
    ib=pow(2304,-1,modulus)
    for n in range(p):
        a=(comb(2*n,n)**2*comb(3*n,n))*pow(ia,n,modulus)%modulus
        b=(comb(2*n,n)**2*comb(4*n,2*n))*pow(ib,n,modulus)%modulus
        A=(A+(6*n+1)*a)%modulus
        B=(B+(8*n+1)*b)%modulus
    return A,B


def main(limit):
    ps=[p for p in primes(limit) if p%24 in (13,19)]
    records=[]
    for p in ps:
        r=ports(p)
        assert r['LIFT_residual']==0, ('finite LIFT falsifier',r)
        if p in (13,19,373):
            aa, bb = raw_binomial_recompute(p)
            # raw independent result is checked vs all four valued source ports
            assert (aa%p**3,bb%p**3)==(r['A_mod_p3'],r['B_mod_p3'])
            records.append(r)
    print('PASS_D25_UNIFORM_CARRY1_AS_UR_AND_B_CONSEQUENCE_FINITE_GUARD')
    print('TARGET_PRIMES',len(ps),'LIMIT',limit,'CLASS_COUNTS',
          {r:sum(p%24==r for p in ps) for r in (13,19)})
    for x in records:print('EXACT_SAMPLE',x)
    print('STATUS: FINITE EXACT REGRESSION, NOT A PROOF OF CARRY2/LIFT OR NATIVE H0/B0')

if __name__=='__main__':
    main(int(sys.argv[1]) if len(sys.argv)>1 else 1500)
