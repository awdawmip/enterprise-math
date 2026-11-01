"""D25 p=8t+5: exact modular certificate for the original signed beta clipped square.

AUTHOR-SIDE / UNREVIEWED / NOT_ADMITTED / not an H0/B0 native experiment.
No external dependencies.  All modulus and divisions are exact integers.
"""
from math import comb


def primes(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[:2] = b'\x00\x00'
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            sieve[i*i::i] = b'\x00' * ((limit-i*i)//i + 1)
    return [i for i in range(limit+1) if sieve[i]]


def beta(p, modulus):
    ans = [1]
    inv576 = pow(576, -1, modulus)
    for k in range(p - 1):
        ans.append(ans[-1]*(8*k+1)*(8*k+3)*inv576*pow(k+1,-2,modulus)%modulus)
    return ans


def middle_seed_moments(p, bterms):
    assert p >= 13 and p % 8 == 5
    a, b = (5*p-1)//8, (7*p-3)//8
    m = b-a
    beta_a = comb(b, a)*pow(9,-a,p)%p
    s = beta_a * 10 * pow(441,-1,p) % p
    S = W = 0
    for r in range(m):
        k = a+1+r
        assert bterms[k] % p == 0 and (bterms[k]//p) % p == s, (p,k,s,bterms[k]//p)
        S = (S+s)%p
        W = (W+k*s)%p
        if r < m-1:
            s = s*(8*r+8)*(8*r+10)*pow(9*(8*r+15)**2,-1,p)%p
    predicted = S*(S+16*W)%p
    return predicted, S, W


def signed_tail_direct(p, beta_terms):
    modulus = p**3
    S0 = [0]*(p+1); S1 = [0]*(p+1)
    for k in range(p-1,-1,-1):
        S0[k] = (S0[k+1]+beta_terms[k])%modulus
        S1[k] = (S1[k+1]+k*beta_terms[k])%modulus
    return sum(beta_terms[i]*((8*i+1)*S0[p-i]+8*S1[p-i]) for i in range(1,p))%modulus


def signed_bands_direct(p, beta_terms):
    a,b = (5*p-1)//8,(7*p-3)//8
    segments = ((0,a),(a+1,b),(b+1,p-1))
    modulus=p**3
    result={}
    for row,(lo,hi) in enumerate(segments):
        for col,(lo2,hi2) in enumerate(segments[row:],row):
            v=0
            for i in range(lo,hi+1):
                for j in range(max(lo2,p-i),hi2+1):
                    v += (8*(i+j)+1)*beta_terms[i]*beta_terms[j]*(2 if row != col else 1)
            result[(row,col)]=v%modulus
    return result


def main():
    count = 0
    target = 0
    data=[]
    for p in primes(3000):
        if p<13 or p%8!=5:
            continue
        t = beta(p,p**3)
        a,b=(5*p-1)//8,(7*p-3)//8
        assert all(x%p for x in t[:a+1]); assert all(x%p==0 and x%(p*p) for x in t[a+1:b+1]); assert all(x%(p*p)==0 for x in t[b+1:])
        mm,S,W=middle_seed_moments(p,t)
        # A genuinely separate full-index pair sum for selected cases.
        if p in (13,29,37,53,61,109,373):
            ports=signed_bands_direct(p,t)
            assert ports[(1,1)] == p*p*mm, (p,ports[(1,1)],mm)
            assert ports[(1,2)]==ports[(2,2)]==0
            total=sum(ports.values())%(p**3)
            assert total==signed_tail_direct(p,t)
            highlow=ports[(0,2)]//(p*p)
            if p in (13,37,109,373):
                assert (ports[(0,0)]+ports[(0,1)])%p==0
            data.append((p,S,W,mm,highlow,total, (ports[(0,0)]+ports[(0,1)])%(p*p)))
        count += 1
        target += p%24==13
    assert count==109 and target==53
    print('PASS',count,'p=5(mod8) primes <=3000, of which',target,'p=13(mod24)')
    print('p | S | W | middle/middle divided by p² | high/low divided by p² | full signed tail mod p³ | LL+LM mod p²')
    for d in data: print(' | '.join(map(str,d)))


if __name__=='__main__':
    main()
