"""Independent exact modular certificate for two complementary hypergeometric mirrors.

Original p-adic recurrence is evaluated at all indices, without invoking
any previously published tail prefix formula. Pure Python standard library.
"""
from math import isqrt


def primes_1_mod_6(bound: int):
    sieve = bytearray(b'\x01') * bound
    sieve[:2] = b'\x00\x00'
    for d in range(2, isqrt(bound - 1) + 1):
        if sieve[d]:
            sieve[d*d:bound:d] = b'\x00' * (1 + (bound - 1 - d*d)//d)
    return [p for p in range(7, bound) if sieve[p] and p % 6 == 1]


def check_prime(p: int):
    m = (p - 1) // 6
    p2, p3, p4 = p*p, p**3, p**4
    # Original Gauss sequence b[n] from independent full recurrence mod p^3.
    b = [1] * p
    for n in range(1,p):
        j=n-1
        b[n] = b[n-1]*(6*j+1)*(3*j+1)*pow(36*n*n,-1,p3)%p3
    # Complementary Gauss sequence c[n], only its unit prefix is used.
    c = [1] * (4*m+1)
    for n in range(1,4*m+1):
        j=n-1
        c[n] = c[n-1]*(6*j+5)*(3*j+2)*pow(36*n*n,-1,p)%p
    assert b[p-1] % p2 == 0
    assert b[p-1]//p2 % p == pow(10,-1,p)
    gauss_pair_count=0
    for k in range(1,4*m+1):
        assert c[k] != 0
        assert b[p-k] % p2 == 0
        assert 36*k*k*c[k]*(b[p-k]//p2) % p == 1,(p,k,'Gauss')
        gauss_pair_count+=1
    signed_r = None
    if p % 24 in (13, 19):
        # Formula in frozen original source, retaining signed weights.
        # Independent low-index mirror alternative uses 1/c[k].
        v0=v1=0; u0=u1=0; old=new=0
        for i in range(1,m+1):
            v = b[p-i]//p2 % p
            v0 = (v0 + v)%p
            v1 = (v1 + i*v)%p
            inv_c = pow(c[i],-1,p)
            u0 = (u0+pow(i*i,-1,p)*inv_c)%p
            u1 = (u1+pow(i,-1,p)*inv_c)%p
            old = (old+2*(b[i]%p)*((1+6*i)*v0-6*v1))%p
            new = (new+pow(18,-1,p)*(b[i]%p)*((1+6*i)*u0-6*u1))%p
        assert old == new,(p,old,new)
        signed_r=old
    # Original Clausen coefficients from full recurrence mod p^4.
    a=[1]*p
    for n in range(1,p):
        j=n-1
        a[n] = a[n-1]*(2*j+1)*(3*j+1)*(3*j+2)*pow(36*n**3,-1,p4)%p4
    assert a[p-1] % p3 == 0
    assert a[p-1]//p3 % p == p-1
    clausen_pairs=0; q_direct=q_mirror=0
    for k in range(1,2*m+1):
        high=a[p-k]
        low=a[k]%p
        assert low!=0 and high%p3==0
        high_unit=high//p3%p
        assert 18*k**3*low*high_unit%p==p-1,(p,k,'Clausen')
        q_direct += (6*(p-k)+1)*high_unit
        q_mirror += (6*k-1)*pow(18*k**3*low,-1,p)
        clausen_pairs += 1
    assert q_direct%p == q_mirror%p,(p,q_direct,q_mirror)
    return (p,m,gauss_pair_count,clausen_pairs,signed_r,q_direct%p)

if __name__=='__main__':
    ps=primes_1_mod_6(5000)
    gauss_pairs=clausen_pairs=target_count=0
    anchors={}
    for p in ps:
        row=check_prime(p)
        gauss_pairs+=row[2];clausen_pairs+=row[3]
        target_count+=(row[4] is not None)
        if p in (7,13,19,37,157,373,1327,3349):anchors[p]=row
    print(f'PRIMES {len(ps)} TARGET_CLASS {target_count}')
    print(f'GAUSS_MIRROR_PAIRS {gauss_pairs} CLAUSEN_MIRROR_PAIRS {clausen_pairs}')
    for p,row in anchors.items():print('ANCHOR p,m,GaussPairs,ClausenPairs,R,Q:',row)
    print('PASS_D25_COMPLEMENTARY_GAUSS_AND_CLAUSEN_MIRRORS_EXACT')
