#!/usr/bin/env python3
"""R482 exact integer certificates: infinitely many k for every fixed 4<=s<=64.
Frozen scientific input: R462@18783e01e3646c72b7aab3b16d3f565e83e6446f.
This program uses Python standard library integer arithmetic only.
"""
from functools import lru_cache
from itertools import permutations
from hashlib import sha256
from math import comb, factorial, lcm, prod
import json
from pathlib import Path

S_MIN, S_MAX = 4, 64
PERMS = tuple((p, (-1) ** sum(p[i] > p[j] for i in range(4) for j in range(i+1, 4)))
              for p in permutations(range(4)))

@lru_cache(None)
def cat(k):
    return comb(2*k,k) // (k+1) if k>=0 else 0

@lru_cache(None)
def p_num(t,k):
    """Integer polynomial P_t(k) with H(2k+1,t)/Catalan(k)=P_t(k)/(2t)!."""
    if t < 2:
        return 0
    ans = 0
    for q in range((t-1)//2+1):
        term = comb(t-1,2*q)*4**q
        for i in range(q):
            term *= (k-i)*(k+1-i)
        for ell in range(2-t,t+2):
            if 1-2*q <= ell <= 0:
                continue
            term *= 2*k+ell
        ans += term
    return ans

@lru_cache(None)
def denominator(t):
    return factorial(2*t) if t >= 2 else 1

@lru_cache(None)
def prepare(s):
    terms = []
    for perm, sign in PERMS:
        indices = tuple(s+i-perm[i] for i in range(4))
        if min(indices)<2:
            continue
        d = prod(denominator(t) for t in indices)
        terms.append((indices,sign,d))
    M = lcm(*(t[2] for t in terms))
    return M, tuple((idx,sign,M//d) for idx,sign,d in terms)

def Q(s,k):
    """Exactly M_s*D_4(2k+1,2k+1-s)/C_k^4, in Z[k]."""
    M,terms=prepare(s)
    return sum(sign*factor*prod(p_num(t,k) for t in idx) for idx,sign,factor in terms)

def original_h(k,t):
    r=2*k+1
    if t < 2 or t>r:
        return 0
    coef=0
    for q in range(r-t+1):
        lo=r-2*q
        a=comb(2*t,lo) if 0<=lo<=2*t else 0
        b=comb(2*t,lo-1) if 0<=lo-1<=2*t else 0
        coef+=comb(r-t,q)*(a-b)
    return comb(r+t,2*t)*coef

def catalan_h(k,t):
    r=2*k+1
    if t < 2 or t>r:return 0
    return comb(r+t,2*t)*sum(comb(t-1,2*q)*4**q*cat(k-q)
                                     for q in range((t-1)//2+1))

def det4_int(mat):
    return sum(sign*prod(mat[i][perm[i]] for i in range(4))
               for perm,sign in PERMS)

def forward_differences(vals):
    ans=[]
    while vals:
        ans.append(vals[0])
        vals=[vals[i+1]-vals[i] for i in range(len(vals)-1)]
    return ans


S4_REMAINDER_DESC = (
    1642889216,15957508096,66138512384,133061328384,48632222568,
    -453088376892,-1383026944958,-2259280837993,-2459027895869,
    -1840088766279,-890260992501,-233149935816,-20680310340
)

def check_s4_explicit():
    def rem(k):
        result=0
        for c in S4_REMAINDER_DESC:result=result*k+c
        return result
    def factor(k):
        return (65536*k**4*(k-1)*(k+1)**4*(k+2)**2
                *(2*k+1)**4*(2*k+3)**4*(2*k+5)*rem(k))
    # Two degree-<=32 polynomials agree at 33 integer points.
    for k in range(33):assert Q(4,k)==factor(k),(k,'s4_factor')
    coeff_asc=list(reversed(S4_REMAINDER_DESC))
    shifted=[sum(coeff_asc[j]*comb(j,i)*3**(j-i) for j in range(i,13))
             for i in range(13)]
    assert min(shifted)>0
    return shifted

def main():
    shifted_s4=check_s4_explicit()
    summaries=[]
    coeff_total=0
    for s in range(S_MIN,S_MAX+1):
        k0=(s+3)//2  # ceil((s+2)/2): ensures 2k+1>=s+3.
        d=8*s  # every determinant term has degree <=2 sum_i(s+i-p(i))=8s.
        differences=forward_differences([Q(s,k) for k in range(k0,k0+d+2)])
        assert len(differences)==d+2
        assert differences[d+1]==0, (s,'degree_bound')
        assert all(x>0 for x in differences[:-1]), (s,'positive_forward_differences')
        coeff_total+=d+1
        stream='\n'.join(str(x) for x in differences[:-1]).encode('ascii')
        summaries.append({
            's':s, 'k_min':k0, 'degree_bound':d,
            'strictly_positive_forward_differences':d+1,
            'difference_degree_plus_one':0,
            'max_coefficient_bits':max(x.bit_length() for x in differences[:-1]),
            'coefficients_sha256':sha256(stream).hexdigest(),
        })
    cross_checks=0
    # Raw signed-coefficient vs Catalan vs polynomial cancellation.
    for s in range(S_MIN,S_MAX+1):
        k0=(s+3)//2
        for k in (k0,k0+1):
            for t in range(max(2,s-3),s+4):
                orig=original_h(k,t)
                assert orig==catalan_h(k,t),('orig/catalan',k,t)
                assert orig*denominator(t)==cat(k)*p_num(t,k),('polynomial',k,t)
                cross_checks+=1
    determinant_cross_checks=0
    for s in (4,5,6,8,12,16,24,32,48,64):
        for k in ((s+3)//2, (s+3)//2+1):
            raw=det4_int([[original_h(k,s+i-j) for j in range(4)] for i in range(4)])
            M,_=prepare(s)
            assert M*raw==Q(s,k)*cat(k)**4,('determinant',k,s)
            assert raw>0
            determinant_cross_checks+=1
    out={
        'status':'R482_EXACT_PASS',
        'scientific_pin':'18783e01e3646c72b7aab3b16d3f565e83e6446f',
        'theorem':'For all integer 4<=s<=64, all k>=ceil((s+2)/2), D4(2k+1,2k+1-s)>0',
        'certificate':'Newton forward differences of integer polynomials M_s D4/C_k^4 at k_min',
        's_range':[S_MIN,S_MAX], 'family_count':S_MAX-S_MIN+1,
        'positive_integer_coefficients_checked':coeff_total,
        'source_expression_cross_checks':cross_checks,
        'direct_original_determinant_cross_checks':determinant_cross_checks,
        'per_s':summaries,
        's4_explicit_shifted_remainder_coefficients_ascending':shifted_s4,
        'scope':'Exact integer-polynomial certificate for infinitely many k at each of 61 fixed s; author-side; not an all-s proof or review admission.'
    }
    path=Path(__file__).with_name('R482_EVIDENCE.json')
    path.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='per_s'},ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
