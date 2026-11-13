#!/usr/bin/env python3
"""R137B exact Farey-gap integer algorithm and independent Fraction tests."""
from fractions import Fraction

def word(theta, K, m):
    L = K - 1
    return tuple(int((L+i+1)*theta) - int((L+i)*theta) for i in range(m))

def strict_word(theta, K, m):
    return tuple(int(((K+i)*theta) % 1 < theta % 1) for i in range(m))

def farey_witnesses(K, m):
    assert K >= 1 and m >= 1
    fr = sorted({Fraction(a,b) for b in range(1,m+1) for a in range(b+1)})
    L = K - 1
    patterns = {}
    if K == 1:
        for r,s in zip(fr,fr[1:]):
            theta = (r+s)/2
            patterns.setdefault(word(theta,K,m),theta)
        return patterns
    for r,s in zip(fr,fr[1:]):
        alpha0 = (r+s)/2
        cuts = [(Fraction(0),0,0),(Fraction(1),1,0)]
        for j in range(1,m+1):
            x = j*alpha0
            p = x.numerator//x.denominator + 1
            cuts.append((p-j*alpha0,p,j))
        cuts.sort()
        for (_,p,j),(_,q,k) in zip(cuts,cuts[1:]):
            lower = (L+k)*r-q
            upper = (L+j)*s-p
            N = lower.numerator//lower.denominator + 1
            if N >= upper:
                continue
            ell = max(r, Fraction(N+p,L+j))
            h = min(s, Fraction(N+q,L+k))
            assert ell < h
            theta = (ell+h)/2
            assert p-j*theta < (L*theta)-N < q-k*theta
            w = word(theta,K,m)
            assert w == strict_word(theta,K,m)
            patterns.setdefault(w,theta)
    return patterns

def chronological_words(K,m):
    L = K-1
    cuts = sorted({Fraction(a,n) for n in range(max(L,1),L+m+1)
                   for a in range(1,n)})
    values = [Fraction(0)] + cuts + [Fraction(1)]
    return {word((r+s)/2,K,m) for r,s in zip(values,values[1:])}

def phi(q):
    from math import gcd
    return sum(gcd(a,q)==1 for a in range(1,q+1))

def run():
    tests = 0
    for m in range(1,11):
        for K in range(2,40):
            assert set(farey_witnesses(K,m)) == chronological_words(K,m), (K,m)
            tests += 1
    assert tests == 380
    for m in range(1,11):
        assert set(farey_witnesses(1,m)) == chronological_words(1,m)
    big = 10**80+137
    max_bits = 0
    for m in range(1,21):
        certs = farey_witnesses(big,m)
        F = 1+sum((m+1-q)*phi(q) for q in range(1,m+1))
        assert len(certs)==F,(m,len(certs),F)
        max_bits = max(max_bits,max(t.denominator.bit_length() for t in certs.values()))
    assert max_bits==533,max_bits
    print("R137B_FAREY_INTEGER_CRITERION_PASS")
    print({"chronological_exact_pairs":tests, "K1_special_cases":10,
           "large_K_cases":20, "large_K_m20_patterns":944, "max_witness_denominator_bits":max_bits})
if __name__ == "__main__":
    run()
