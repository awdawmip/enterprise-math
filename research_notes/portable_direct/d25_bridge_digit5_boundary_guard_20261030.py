"""Exact author-side D25 A216/B2304 p-adic bridge and tail-port checks.

Uses only Python's standard-library integers. No native H0/B0 operation is run.
Claims: finite p<5000 residues modulo p**5, exact fixed-prime
counterexamples to a uniform p**5 bridge, and a separate p**4
factorial/harmonic restoration formula for p=6m+1.
"""
from math import comb


def primes_below(limit):
    prime = bytearray(b"\x01") * limit
    prime[:2] = b"\x00\x00"
    for d in range(2, int(limit**0.5) + 1):
        if prime[d]:
            prime[d*d:limit:d] = b"\x00" * (((limit-1-d*d)//d) + 1)
    return [n for n in range(5, limit) if prime[n]]


def bridge_mod(p, precision=5):
    """Return A_p, B_p, A_p-2B_p+p*(-3/p) in Z/p^precision.

    The factorial recurrence strips factors of p before division.
    All denominator units are inverted modulo p**precision.
    """
    modulus = p**precision
    def strip(x):
        v = 0
        while x % p == 0:
            x //= p
            v += 1
        return v, x % modulus

    def coefficients(factors, base, denominator_degree):
        v, unit = 0, 1
        for n in range(p):
            yield (p**v * unit) % modulus
            if n == p - 1:
                break
            for x in factors(n):
                dv, xunit = strip(x)
                v += dv
                unit = unit * xunit % modulus
            dv, dunit = strip((n+1)**denominator_degree)
            v -= dv
            assert v >= 0
            unit = unit * pow(dunit * base % modulus, -1, modulus) % modulus

    a = coefficients(lambda n: (2*n+1, 2*n+2, 3*n+1, 3*n+2, 3*n+3), 216, 5)
    b = coefficients(lambda n: (4*n+1, 4*n+2, 4*n+3, 4*n+4), 2304, 4)
    A = sum((6*n+1)*c for n,c in enumerate(a)) % modulus
    B = sum((8*n+1)*c for n,c in enumerate(b)) % modulus
    chi = 1 if p % 3 == 1 else -1  # (-3/p), p>3.
    D = (A - 2*B + p*chi) % modulus
    return (A,B,D)


def original_integer_binomial_mod(p, precision=5):
    """Independent direct original integer binomial sums (small fixed primes)."""
    modulus = p**precision
    A = sum((6*n+1)*comb(2*n,n)**2*comb(3*n,n)*pow(216, -n, modulus)
            for n in range(p)) % modulus
    B = sum((8*n+1)*comb(2*n,n)**2*comb(4*n,2*n)*pow(2304, -n, modulus)
            for n in range(p)) % modulus
    D = (A-2*B+p*(1 if p%3==1 else -1)) % modulus
    return A,B,D


def tail_port_formula(p):
    """Three p**3-normalized source ports for p=6m+1, modulo p.

    The middle B port uses its Wilson quotient/harmonic expansion modulo p**2.
    Its aggregate is known divisible by p (GZ half-tail).
    """
    assert p >= 7 and p % 6 == 1
    m = (p-1)//6
    p2 = p*p
    fact = [1]*p
    for n in range(1,p):
        fact[n] = fact[n-1]*n % p2
    assert (fact[p-1]+1)%p == 0
    Wilson = ((fact[p-1]+1)//p)%p
    harmonic = [0]*p
    for n in range(1,p):
        harmonic[n] = (harmonic[n-1]+pow(n,-1,p))%p
    def inv_den(n,degree,base,mod):
        return pow(fact[n]**degree*pow(base,n,mod)%mod,-1,mod)
    Ahi = sum(-2*(6*n+1)*fact[2*n-p]*fact[3*n-2*p]*inv_den(n,5,216,p)
              for n in range(4*m+1,p))%p
    n0 = (p+1)//2
    n3 = (3*p-1)//4
    Bzone2 = sum(2*(8*n+1)*fact[4*n-2*p] *
                 (1+2*p*((harmonic[4*n-2*p]-Wilson)%p)) *
                 inv_den(n,4,2304,p2)
                 for n in range(n0,n3+1))%p2
    assert Bzone2%p == 0, (p,Bzone2)
    Bzone3 = sum(-6*(8*n+1)*fact[4*n-3*p]*inv_den(n,4,2304,p)
                 for n in range(n3+1,p))%p
    return Ahi, (Bzone2//p)%p, Bzone3


def direct_tail_ports(p):
    """Independent direct integer-binomial source-port sums modulo p**4."""
    assert p >= 7 and p%6 == 1
    m=(p-1)//6
    modulus = p**4
    n0=(p+1)//2
    n3=(3*p-1)//4
    def A(n):
        return ((6*n+1)*comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,modulus))%modulus
    def B(n):
        return ((8*n+1)*comb(2*n,n)**2*comb(4*n,2*n)*pow(2304,-n,modulus))%modulus
    blocks = [sum(A(n) for n in range(4*m+1,p))%modulus,
              sum(B(n) for n in range(n0,n3+1))%modulus,
              sum(B(n) for n in range(n3+1,p))%modulus]
    assert all(x%p**3==0 for x in blocks)
    return tuple((x//p**3)%p for x in blocks)


def direct_minimal_bridge_port(p):
    """The old p**3 MIN-BRIDGE, now measured one digit deeper.

    This is a diagnostic, not a theorem that MIN-BRIDGE is zero mod p**4.
    """
    assert p >= 7 and p%6 == 1
    m=(p-1)//6
    modulus=p**4
    A=sum((6*n+1)*comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,modulus)
          for n in range(4*m+1))%modulus
    B=sum((8*n+1)*comb(2*n,n)**2*comb(4*n,2*n)*pow(2304,-n,modulus)
          for n in range(3*m+1))%modulus
    value=(p+A-2*B)%modulus
    assert value%p**3==0
    return value//p**3%p


def main():
    ps=primes_below(5000)
    assert len(ps)==667
    p4_fail=[]
    p5_hold=[]
    target_count=0
    fixed={}
    for p in ps:
        A,B,D=bridge_mod(p,5)
        target_count += p%24 in (13,19)
        if D % p**4:
            p4_fail.append(p)
        if D==0:
            p5_hold.append(p)
        if p in (5,7,11,13,19,373):
            direct=original_integer_binomial_mod(p,5)
            assert (A,B,D)==direct, (p,(A,B,D),direct)
            fixed[p]=(A,B,D,(D//p**4)%p)
    assert not p4_fail
    assert target_count==166
    assert p5_hold==[5,7],p5_hold
    assert fixed[13]==(276835,195546,257049,9)
    assert fixed[19]==(603611,1865667,1824494,14)
    assert fixed[373][-1]==174

    tested_ports=0
    port_examples={}
    for p in ps:
        if p<500 and p%6 == 1:
            direct=direct_tail_ports(p)
            derived=tail_port_formula(p)
            assert direct==derived,(p,direct,derived)
            tested_ports+=1
            if p in (7,13,19,37):
                port_examples[p]=direct
    p=373
    direct=direct_tail_ports(p)
    derived=tail_port_formula(p)
    assert direct==derived
    port_examples[p]=direct
    assert ((direct[0]-2*(direct[1]+direct[2]))%p)==318
    minimal_ports={p:direct_minimal_bridge_port(p) for p in (13,19,373)}
    assert minimal_ports=={13:0,19:2,373:55}
    for q in (13,19,373):
        ports=port_examples[q]
        assert (minimal_ports[q]+ports[0]-2*(ports[1]+ports[2]))%q == 0
    print('PRIMES_EXHAUSTED',len(ps),'FROZEN_13_19',target_count)
    print('BRIDGE_MOD_P4_FAILURES',p4_fail)
    print('BRIDGE_MOD_P5_EXCEPTIONS',p5_hold)
    print('FIXED_DIRECT_INTEGER_BINOMIAL',fixed)
    print('TAIL_FORMULA_CROSSCHECK_COUNT',tested_ports+1)
    print('TAIL_PORT_EXAMPLES_A_HIGH_B_ZONE2_B_ZONE3',port_examples)
    print('OLD_MINIMAL_BRIDGE_P3_RESIDUES',minimal_ports)
    print('PASS_D25_DIGIT5_SHARPNESS_AND_TAIL_RESTORATION')

if __name__=='__main__':
    main()
