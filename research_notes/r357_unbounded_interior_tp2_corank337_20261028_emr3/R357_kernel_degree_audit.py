#!/usr/bin/env python3
"""Exact, finite kernel-support verification for the R348 A1 all-index reduction.
Independent formula construction for every nonzero 12 K and 10 J entry.
This is author-side, not a Driver independent review or an X6 proof.
"""
from math import comb
from fractions import Fraction
from pathlib import Path
import json,sys
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent/'r346_unbounded_interior_tp2_corank301_20261028_emr3'))
from R346_verify import K,J

def c(n,k):return comb(n,k) if 0<=k<=n else 0

def alt_K(i):
    # Match the four signed ordered-hex branches, retain every negative term.
    ds=(-c(4,i)+c(2,i-1), c(5,i-1)-c(5,i-2), c(7,i-2), -c(9,i-3))
    v={}
    for j,d in enumerate(ds,1):
        for h in range(max(0,i+2-j)):
            a=i-1+h
            v[a]=v.get(a,0)-d*c(i+1-j,h)
    return v

def alt_J(s):
    ds=((-c(3,s-1),s),(-c(6,s-1),s-1),(c(8,s-2),s-2))
    v={}
    for d,n in ds:
        for h in range(max(0,n+1)):
            a=s+h
            v[a]=v.get(a,0)+d*c(n,h)
    return v

def run():
    kcoeff={}; acoeff={0:{0:1},1:{0:1}}
    checked_k=0;checked_j=0
    for i in range(1,13):
        q=alt_K(i)
        tab=K(i)
        for a in range(max(len(tab),max(q,default=0)+1)):
            assert q.get(a,0)==(tab[a] if a<len(tab) else 0),('K_source',i,a)
            v=q.get(a,0)
            if v:
                assert i<=a+1,('A1_K_degree',i,a,v)
                kcoeff.setdefault(a,{})[i]=v
        checked_k+=1
    for s in range(1,11):
        q=alt_J(s)
        tab=J(s)
        for a in range(max(len(tab),max(q,default=0)+1)):
            assert q.get(a,0)==(tab[a] if a<len(tab) else 0),('J_source',s,a)
            v=q.get(a,0)
            if v:
                assert s<=a,('A1_A_degree',s,a,v)
                acoeff.setdefault(a,{})[s]=v
        checked_j+=1
    assert kcoeff[0]=={1:2},('K0',kcoeff[0])
    assert kcoeff[1]=={1:3,2:-1},('K1',kcoeff[1])
    assert sum(v*Fraction(1,2**i) for i,v in kcoeff[1].items())==Fraction(5,4)
    # Exact denominator-free check of 4*K^(1)(1/2) = 5.
    assert sum(v*(2**(2-i)) for i,v in kcoeff[1].items())==5
    max_k_degree=max(kcoeff);max_a_degree=max(acoeff)
    assert max_k_degree<=23 and max_a_degree<=20
    ev={'schema':'R357_R348_A1_KERNEL_SUPPORT_V1','status':'PASS_AUTHOR_SIDE_EXACT',
        'K_entries_checked':checked_k,'J_entries_checked':checked_j,
        'nonzero_K_t_degree_orders':len(kcoeff),'nonzero_A_t_degree_orders':len(acoeff),
        'max_K_t_degree':max_k_degree,'max_A_t_degree':max_a_degree,
        'K0':'2*x','K1':'3*x-x^2','K1_at_half':'5/4',
        'all_nonzero_K_ta_xi_have_i_le_a_plus_1':True,
        'all_nonzero_A_ta_xs_have_s_le_a':True,
        'all_index_consequence':'deg_x [t^a]K <= a+1; deg_x [t^a]A <= a',
        'proof_basis':'each original fixed K_i/J_s has support bounded by its t-power shift; no additional i/s exist',
        'independent_Driver_review':False,'direct_native_X6_correspondence':False}
    (P/'R357_A1_SUPPORT_EVIDENCE.json').write_text(json.dumps(ev,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(ev,ensure_ascii=False))
if __name__=='__main__':run()
