#!/usr/bin/env python3
"""EC49FWL, exact Z/10 x Z/11 CRT-factor classifier and direct checks."""
import json

def D(S,n):
    S=set(S)
    return tuple(sum(((x in S)!=((c-x)%n in S)) for x in range(n)) for c in range(n))

def spectrum(U,z=None):
    d=D(U,10); w=len(U)
    return tuple(11*d[c%10] if z is None else
                 (10*d[c%10] if c%11==2*z%11 else 9*d[c%10]+2*w)
                 for c in range(110))

def direct(U,z=None):
    V=set(range(11)) if z is None else set(range(11))-{z}
    W={x for x in range(110) if x%10 in U and x%11 in V}
    return D(W,110)

def decode(s):
    R=[sum(s[c] for c in range(110) if c%11==b) for b in range(11)]
    if len(set(R))==1:
        if not any(s): return ('ZERO',)
        assert all(s[c]==s[c%10] for c in range(110))
        assert all(t%11==0 for t in s)
        return ('FULL', tuple(s[a]//11 for a in range(10)))
    b=min(range(11),key=lambda b:R[b]); g=max(R)-min(R)
    w=next((w for w in range(1,11) if 2*w*w==g),None)
    assert w is not None and all(R[j]==max(R) for j in range(11) if j!=b)
    d=tuple(s[next(c for c in range(110) if c%10==a and c%11==b)]//10 for a in range(10))
    assert all(s[c]==(10*d[c%10] if c%11==b else 9*d[c%10]+2*w) for c in range(110))
    return ('HOLE',6*b%11,w,d,g)

def main():
    h=f=0
    for mask in range(1024):
        U={j for j in range(10) if mask>>j&1}; w=len(U); d=D(U,10)
        assert sum(d)==2*(10*w-w*w)
        q=decode(spectrum(U))
        assert q==(('ZERO',) if w in (0,10) else ('FULL',d))
        assert spectrum(U)==direct(U)
        f+=1
        for z in range(11):
            s=spectrum(U,z)
            assert decode(s)==(('ZERO',) if not w else ('HOLE',z,w,d,2*w*w))
            if z==0 or mask%4==0:
                assert s==direct(U,z)
                h+=1
    A={0,2,3,4,7}; B={0,1,3,4,6}
    assert A!=B and D(A,10)==D(B,10) and spectrum(A,3)==spectrum(B,3)
    assert decode(spectrum(A,3))==('HOLE',3,5,D(A,10),50)
    result={'status':'ALL PASS','science_pin':'BRC16943','ten_bit_supports':1024,
            'one_hole_formula_decode_tests':11264,'direct_full_110_tests':f,
            'direct_one_hole_110_tests':h,'identified_nonempty_one_hole_cases':11253,
            'unique_special_row_b_for_z3':6,'row_sum_gap_for_weight5':50,
            'zero_spectrum_ambiguity':'empty W vs complete W',
            'residual_U_ambiguity':{'A':sorted(A),'B':sorted(B),'same_weight':5,'same_hole_z':3},
            'claim_scope':'auxiliary exact CRT spectrum; no Farey dynamics or independent review'}
    print(json.dumps(result,sort_keys=True,indent=2))

if __name__=='__main__':main()
