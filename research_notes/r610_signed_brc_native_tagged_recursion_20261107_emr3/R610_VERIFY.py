#!/usr/bin/env python3
"""R610: Exact tagged history lift of frozen R388/R462 original signed BRC K/J->B recursion.

Reimplements immutable R388_exact.py kernel formulas (R462 pin), keeping all twelve signed K branches.
Only Python integer polynomial algebra. No native dynamics/physical-time inference.
"""
from math import comb
from pathlib import Path
from hashlib import sha256
import json


def C(n,j): return comb(n,j) if 0 <= j <= n else 0

def add(a,b):
    n=max(len(a),len(b))
    return tuple((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n))

def mul(a,b):
    if not a or not b: return ()
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return tuple(out)

def monomial(n,c,shift):
    return (0,)*shift+tuple(c*C(n,j) for j in range(n+1)) if n>=0 else ()

def K(i):
    assert 1<=i<=12
    ds=(-C(4,i)+C(2,i-1), C(5,i-1)-C(5,i-2), C(7,i-2), -C(9,i-3))
    z=(0,)
    for j,v in enumerate(ds,1):
        if v:z=add(z,monomial(i+1-j,-v,i-1))
    return z

def J(s):
    assert s>=1
    z=(0,)
    for v,n in ((-C(3,s-1),s),(-C(6,s-1),s-1),(C(8,s-2),s-2)):
        if v:z=add(z,monomial(n,v,s))
    return z

def tagged(max_s):
    """Word tags are ordered K branch indices; terminal marker is J_t or B0."""
    T=[{((),0):(1,1)}]  # key=(ordered tuple of branch indices, terminal s), 0 means B0
    for s in range(1,max_s+1):
        layer={}
        injection=J(s)
        if any(injection):layer[((),s)]=injection
        for i in range(1,min(12,s)+1):
            for (word,terminal),coeff in T[s-i].items():
                key=((i,)+word,terminal)
                assert key not in layer
                layer[key]=mul(K(i),coeff)
        T.append(layer)
    return T

def bare(max_s):
    B=[(1,1)]
    for s in range(1,max_s+1):
        p=J(s)
        for i in range(1,min(12,s)+1):p=add(p,mul(K(i),B[s-i]))
        B.append(p)
    return B

def collapse(layer):
    z=(0,)
    for q in layer.values():z=add(z,q)
    return z

def coeff(z,i):return z[i] if i<len(z) else 0

def tagged_D(q,k,T):
    assert 0<=k<=q and q+k<len(T)
    out={}
    for w in range(k+1):
        factor=(-1)**(k-w)*C(k,w)*2**(q-w)
        for key,poly in T[q+w].items():
            out[key]=out.get(key,0)+factor*coeff(poly,q)
    return {key:value for key,value in out.items() if value}

def bare_D(q,k,B):
    assert 0<=k<=q and q+k<len(B)
    return sum((-1)**(k-w)*C(k,w)*2**(q-w)*coeff(B[q+w],q) for w in range(k+1))

def main():
    assert K(1)==(2,3),K(1)
    assert K(2)==(0,-1,4,4),K(2)
    assert all(len(K(i))<=2*i+1 for i in range(1,13))
    upper=9
    T=tagged(upper); B=bare(upper)
    for s in range(upper+1):
        assert collapse(T[s])==B[s],('collapse',s)
        # each terminal K_{i1}...K_{im} J_t or B0, independent product check
        for (word,term),actual in T[s].items():
            assert sum(word)+term==s,('index',s,word,term)
            prod=(1,)
            for i in word:prod=mul(prod,K(i))
            prod=mul(prod,((1,1) if term==0 else J(term)))
            assert prod==actual,(s,word,term)
    # Independent D projection check: exact original linear readout on every tagged B.
    d_cases=[]
    for q in range(upper+1):
        for k in range(q+1):
            if q+k>upper:continue
            td=tagged_D(q,k,T)
            assert sum(td.values())==bare_D(q,k,B),(q,k)
            d_cases.append((q,k))
    p12=T[3][((1,2),0)]; p21=T[3][((2,1),0)]
    assert p12==p21==mul(mul(K(1),K(2)),(1,1))
    assert coeff(p12,1)==coeff(p21,1)==-2
    assert ((1,2),0)!=((2,1),0)
    td21=tagged_D(2,1,T)
    assert td21[((1,2),0)]==td21[((2,1),0)]==6
    assert bare_D(2,1,B)==sum(td21.values())
    # The two tagged legitimate expansion terms are distinct but collapse to same signed polynomial.
    # Both words also occur with nonzero weight at t^1, not just zero formal branches.
    # Verify all unordered two-distinct-branch pairs i+j<=9 at base terminal B0.
    comparisons=[]
    for i in range(1,13):
        for j in range(i+1,13):
            s=i+j
            if s>upper:continue
            a=T[s][((i,j),0)];b=T[s][((j,i),0)]
            assert a==b==mul(mul(K(i),K(j)),(1,1))
            nonzero=any(a)
            comparisons.append({'i':i,'j':j,'s':s,'nonzero':nonzero,'first_nonzero_degree':next((d for d,v in enumerate(a) if v),None)})
    assert comparisons and all(r['nonzero'] for r in comparisons)
    result={
      'schema':'R610_NATIVE_SIGNED_BRC_TAGGED_RECURSION_V1',
      'source_pin':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
      'source_formula':'R388_exact.py frozen at R462: 12 signed K_i and J_s; B_0=1+t, B_s=J_s+sum(K_i B_(s-i))',
      'check_max_s':upper,'tagged_expansion_counts':{str(s):len(T[s]) for s in range(upper+1)},
      'complete_scalar_collapse_and_terminal_product_check':'PASS',
      'complete_D_readout_projection_check':'PASS',
      'checked_D_qk_pairs':len(d_cases),
      'two_step_distinct_branch_pairs':comparisons,
      'small_witness':{'s':3,'terminal':'B_0','word_12':[1,2],'word_21':[2,1],
                       'signed_polynomial':list(p12),'signed_t1_coefficient':-2,
                       'D_q2_k1_both_tagged_coefficients':6,
                       'history_difference':'distinct ordered branch labels with identical signed scalar contribution'},
      'scope':'legitimate branch-history terms of original signed BRC K/J->B->D recursion, not distinct full native X6 states',
      'terminal_marker':'R610_SIGNED_BRC_RECURSION_HISTORY_PASS'
    }
    body=json.dumps(result,indent=2,ensure_ascii=False,sort_keys=True)+'\n'
    Path(__file__).with_name('R610_EVIDENCE.json').write_text(body,encoding='utf-8')
    print(result['terminal_marker'])
    print('tagged histories s<=9:',result['tagged_expansion_counts'])
    print('nonzero i<j test pairs:',len(comparisons))
    print('D exact q,k cases:',len(d_cases),'witness at D(2,1):',td21[((1,2),0)],td21[((2,1),0)])
    print('witness polynomial:',p12,'[t]=',coeff(p12,1))
    print('evidence sha256',sha256(body.encode('utf-8')).hexdigest())
if __name__=='__main__':main()
