#!/usr/bin/env python3
"""R164: exact linear-arithmetic certification/decoding of finite Sturmian signatures.
Independent O(m^2) signature oracle used only for exhaustive testing.
"""
from collections import defaultdict
from fractions import Fraction as F
import json


def reference_signature(word):
    m=len(word)
    p=[0]
    for c in word:p.append(p[-1]+int(c))
    alpha,beta=F(0),F(1)
    for i in range(m):
        for j in range(i+1,m+1):
            q,k=p[j]-p[i],j-i
            alpha=max(alpha,F(q-1,k))
            beta=min(beta,F(q+1,k))
    if alpha>=beta:return None
    A=min(F(p[i])-i*alpha for i in range(m+1))
    B=max(F(p[i])-i*beta for i in range(m+1))
    return alpha,beta,int(alpha.denominator*(1+A)),int(beta.denominator*B)


def cert_linear(word, s):
    """O(m) integer operations, O(1) auxiliary memory, exact candidate check."""
    alpha, beta, U, V = s
    if not (F(0) <= alpha < beta <= F(1)):
        return False
    if not isinstance(U, int) or not isinstance(V, int):
        return False
    a,b,c,d = alpha.numerator, alpha.denominator, beta.numerator, beta.denominator
    p = 0
    za_min = za_max = 0
    zb_min = zb_max = 0
    alpha_active = (a == 0)
    beta_active = (c == d)
    for j, bit in enumerate(word, 1):
        if bit not in '01':
            return False
        p += bit == '1'
        za,zb = b*p-a*j, d*p-c*j
        if za-za_min == b:
            alpha_active = True
        if zb_max-zb == d:
            beta_active = True
        za_min=min(za_min,za)
        za_max=max(za_max,za)
        zb_min=min(zb_min,zb)
        zb_max=max(zb_max,zb)
    return (za_min == U-b and zb_max == V
            and za_max-za_min <= b and zb_max-zb_min <= d
            and alpha_active and beta_active)


def decode_linear(m,s):
    """Exact O(m) integer operations for all signed U,V and rational endpoints."""
    alpha,beta,U,V=s
    if not(F(0)<=alpha<beta<=F(1)) or not isinstance(U,int) or not isinstance(V,int):
        return []
    a,b,c,d=alpha.numerator,alpha.denominator,beta.numerator,beta.denominator
    D=b*c-a*d
    p=[];ambiguous=[]
    for i in range(m+1):
        q,r=divmod(U+a*i,b)
        slope_num=i*D+b*V-d*U
        if r:p.append(q)
        elif slope_num>0:p.append(q)
        elif slope_num<0:p.append(q-1)
        else:
            ambiguous.append((i,q))
            p.append(None)
    if len(ambiguous)>1:raise AssertionError('impossible distinct zero derivatives')
    choices=[{}] if not ambiguous else [{ambiguous[0][0]:ambiguous[0][1]-1},{ambiguous[0][0]:ambiguous[0][1]}]
    ans=[]
    for choice in choices:
        ps=[choice.get(i,p[i]) for i in range(m+1)]
        if ps[0]!=0:continue
        diffs=[ps[i]-ps[i-1] for i in range(1,m+1)]
        if any(z not in (0,1) for z in diffs):continue
        w=''.join(str(z) for z in diffs)
        if cert_linear(w,s):ans.append(w)
    return sorted(set(ans))

def main():
    candidates=0; admitted=0; states=0; pairs=0; mismatches=0
    by=[]
    for m in range(1,16):
        groups=defaultdict(list)
        for n in range(1<<m):
            w=f'{n:0{m}b}'
            s=reference_signature(w)
            if s is not None:
                assert cert_linear(w,s)
                groups[s].append(w)
            candidates+=1
        n_pairs=sum(len(ws)==2 for ws in groups.values())
        for s,ws in groups.items():
            dec=decode_linear(m,s)
            assert dec==sorted(ws),(m,s,dec,ws)
            assert len(dec)<=2
        states+=len(groups)
        pairs+=n_pairs
        admitted+=sum(len(z) for z in groups.values())
        by.append({'m':m,'admitted':sum(len(z) for z in groups.values()),'states':len(groups),'pairs':n_pairs})
    assert candidates==65534 and states==1760 and pairs==146
    # Off-image input perturbations. Each rejection is checked using independent oracle.
    invalid_probes=0
    for m in range(1,10):
        signatures={reference_signature(f'{n:0{m}b}') for n in range(1<<m)}
        signatures.discard(None)
        for a,b,U,V in list(signatures):
            for ss in ((a,b,U+1,V),(a,b,U,V+1),(a,b,U-1,V),(a,b,U,V-1)):
                out=decode_linear(m,ss)
                assert all(reference_signature(w)==ss for w in out)
                invalid_probes+=1
    return {'marker':'R164_LINEAR_DECODER_EXACT_PASS','candidate_words_tested':candidates,
            'admitted_words':admitted,'distinct_signatures':states,'two_word_fibers':pairs,
            'perturbed_signature_probes':invalid_probes,'arithmetic':'new decoder integer-only; independent oracle uses Fraction; no floats',
            'm_range':[1,15], 'by_length':by}

if __name__=='__main__':print(json.dumps(main(),ensure_ascii=False,indent=2))
