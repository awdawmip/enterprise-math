#!/usr/bin/env python3
"""R615: exact information hierarchy in frozen signed twelve-branch BRC.
Scientific pin: R462@18783e01e3646c72b7aab3b16d3f565e83e6446f,
research_notes/r388_signed_k3_corank16_20261029_emr3/r388_exact.py theta=0.
Arithmetic: arbitrary precision integers. Type gates are formal probes, not
native X6 heartbeat operations. B0-source response is an auxiliary tangent.
"""
from itertools import product
from math import comb, factorial
from collections import defaultdict
from pathlib import Path
import json, hashlib

def C(n,k):return comb(n,k) if 0<=k<=n else 0

def add(a,b):
    z=[0]*max(len(a),len(b))
    for j,v in enumerate(a):z[j]+=v
    for j,v in enumerate(b):z[j]+=v
    return tuple(z)

def sub(a,b):return add(a,tuple(-v for v in b))

def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        if v:
            for j,w in enumerate(b):
                if w:z[i+j]+=v*w
    return tuple(z)

def coeff(a,i):return a[i] if 0<=i<len(a) else 0

def mono(n,c,shift):return tuple([0]*shift+[c*C(n,j) for j in range(n+1)]) if n>=0 else (0,)

def K(i):
    ds=(-C(4,i)+C(2,i-1), C(5,i-1)-C(5,i-2), C(7,i-2),-C(9,i-3))
    z=(0,)
    for j,v in enumerate(ds,1):
        if v:z=add(z,mono(i+1-j,-v,i-1))
    return z

def J(s):
    z=(0,)
    for v,n in ((-C(3,s-1),s),(-C(6,s-1),s-1),(C(8,s-2),s-2)):
        if v:z=add(z,mono(n,v,s))
    return z

KS={i:K(i) for i in range(1,13)}
B0=(1,1)

def state(n, gates=None, with_J=True, max_i=12):
    gates={} if gates is None else gates
    B=[B0]
    for s in range(1,n+1):
        b=J(s) if with_J else (0,)
        for i in range(1,min(s,max_i)+1):
            if gates.get(i,1):b=add(b,mul(KS[i],B[s-i]))
        B.append(b)
    return B

def histories(s,max_i=12,terminal_only=False):
    if s==0:return [((),0,B0)]
    out=[] if terminal_only else [((),s,J(s))]
    for i in range(1,min(max_i,s)+1):
        for chain,r,p in histories(s-i,max_i,terminal_only):
            out.append(((i,)+chain,r,mul(KS[i],p)))
    return out

def support(chain):return frozenset(chain)
def countvector(chain,types):return tuple(chain.count(i) for i in range(1,types+1))
def canonical(p):
    while len(p)>1 and p[-1]==0:p=p[:-1]
    return p

def all_equal(a,b):return canonical(a)==canonical(b)

def D(B,q,k):
    return sum((-1)**(k-w)*C(k,w)*2**(q-w)*coeff(B[q+w],q)
               for w in range(k+1))

def paths_compositions(n,types):
    return histories(n,types,True)

def main():
    assert KS[1]==(2,3) and KS[2]==(0,-1,4,4) and coeff(KS[3],2)==-8
    base=state(10)
    assert [D(base,q,0) for q in range(3)]==[1,6,32]
    assert D(base,2,1)==60
    types=4
    masks=0
    mobius_pairs=0
    word_terms=0
    weighted_terms=0
    for s in range(10):
        paths=histories(s,types)
        word_terms+=len(paths)
        # all binary global gate masks; support zeta identity with signed J.
        tab={}
        for mask in range(1<<types):
            G={i:(mask>>(i-1))&1 for i in range(1,types+1)}
            actual=state(s,G,max_i=types)[s]
            expected=(0,)
            for word,r,p in paths:
                if all(G[i] for i in support(word)):
                    expected=add(expected,p)
            assert all_equal(actual,expected),(s,mask,'history')
            tab[mask]=actual
            masks+=1
        for mask in range(1<<types):
            mobius=(0,)
            for submask in range(1<<types):
                if (submask&mask)==submask:
                    sign=(-1)**((mask.bit_count()-submask.bit_count()))
                    if sign==1:mobius=add(mobius,tab[submask])
                    else:mobius=sub(mobius,tab[submask])
            direct=(0,)
            for word,r,p in paths:
                sup=sum(1<<(i-1) for i in support(word))
                if sup==mask:direct=add(direct,p)
            assert all_equal(mobius,direct),(s,mask,'mobius')
            mobius_pairs+=1
        # weighted multiplicity (Parikh) coefficients, only B0-terminated.
        grouped={}
        for word,r,p in paths_compositions(s,types):
            key=countvector(word,types)
            grouped[key]=add(grouped.get(key,(0,)),p)
        weighted_terms+=len(grouped)
        assert all(sum((i+1)*v for i,v in enumerate(m))==s for m in grouped)
        for m,poly in grouped.items():
            ways=factorial(sum(m))
            for v in m:ways//=factorial(v)
            theoretical=B0
            for i,v in enumerate(m,1):
                for _ in range(v):theoretical=mul(theoretical,KS[i])
            assert all_equal(poly,tuple(ways*x for x in theoretical)),(s,m)

    # R614 signed pair: two genuinely different ORDERED histories, same counts.
    h12=mul(mul(KS[1],KS[2]),B0)
    h21=mul(mul(KS[2],KS[1]),B0)
    assert all_equal(h12,h21)
    assert coeff(h12,2)==3
    relevant=[(w,p) for w,r,p in histories(3,2) if r==0 and countvector(w,2)==(1,1)]
    assert set(w for w,_ in relevant)=={(1,2),(2,1)}
    global_mixed_D21=2*sum(coeff(p,2) for _,p in relevant)
    assert global_mixed_D21==12
    assert [2*coeff(p,2) for _,p in relevant]==[6,6]
    # B0 tangent d/dx of B_s(x), x B0 at terminal, removes all J-r contributions.
    s=5
    b0paths=paths_compositions(s,2)
    assert set(countvector(w,2) for w,r,p in b0paths if set(w)=={1,2})=={(3,1),(1,2)}
    poly31=(0,);poly12=(0,)
    for word,r,p in b0paths:
        if countvector(word,2)==(3,1):poly31=add(poly31,p)
        if countvector(word,2)==(1,2):poly12=add(poly12,p)
    parikh31=coeff(poly31,2)
    parikh12=coeff(poly12,2)
    assert parikh31==-48 and parikh12==6
    assert coeff(mul(mul(mul(mul(KS[1],KS[1]),KS[1]),KS[2]),B0),2)==-12
    assert coeff(mul(mul(mul(KS[1],KS[2]),KS[2]),B0),2)==2
    # 4 evaluations of whole B0 tangent, for type gate subset 00,10,01,11.
    vals={}
    for mask in range(4):
        gates={1:mask&1, 2:(mask>>1)&1}
        vals[mask]=coeff(state(5,gates,with_J=False,max_i=2)[5],2)
    bool_mixed=vals[3]-vals[1]-vals[2]+vals[0]
    assert bool_mixed==-42 and bool_mixed==parikh31+parikh12
    # whole signed recurrence is equal to full J + tangent sector at every type-mask.
    response_checks=0
    for mask in range(1<<types):
        gates={i:(mask>>(i-1))&1 for i in range(1,types+1)}
        full=state(9,gates,True,types)
        noJ=state(9,gates,False,types)
        initial_zero=[(0,)]
        for s in range(1,10):
            b=J(s)
            for i in range(1,min(s,types)+1):
                if gates[i]:b=add(b,mul(KS[i],initial_zero[s-i]))
            initial_zero.append(b)
        for s in range(10):
            assert all_equal(full[s],add(noJ[s],initial_zero[s]))
            response_checks+=1
    evidence={
        'schema':'R615_SIGNED_BRC_TYPE_GATE_INFORMATION_V1',
        'scientific_pin':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
        'source_path':'research_notes/r388_signed_k3_corank16_20261029_emr3/r388_exact.py',
        'source_blob_sha':'7fa7a762f758b30c6090468ac43487daa34abad8',
        'theta':'0', 'arithmetic':'Python arbitrary precision integers',
        'observer':'signed original K/J->B->D with formal global type gates, optional B0 amplitude x',
        'type_gate_count':types, 'verified_layers':'0..9',
        'binary_gate_recurrence_checks':masks,
        'mobius_support_checks':mobius_pairs,
        'ordered_histories_enumerated':word_terms,
        'weighted_parikh_group_checks':weighted_terms,
        'whole_state_B0_response_decompositions':response_checks,
        'baseline_D21':D(base,2,1),
        'ordered_witness_words':['12','21'],
        'ordered_D21': [6,6],
        'type_support_D21':global_mixed_D21,
        'B0_terminal_s5_parikh':{'m1_3_m2_1':parikh31,'m1_1_m2_2':parikh12},
        'B0_terminal_s5_support':bool_mixed,
        'B0_terminal_s5_four_mask_t2':{str(k):v for k,v in vals.items()},
        'strictness':'boolean-type support < formal weighted Parikh < level-address ordered paths',
        'native_X6_bridge':'UNVERIFIED; no physical operation inferred',
        'terminal_marker':'R615_SIGNED_TYPE_GATE_HIERARCHY_EXACT_PASS'
    }
    path=Path(__file__).with_name('R615_EVIDENCE.json')
    output=json.dumps(evidence,sort_keys=True,ensure_ascii=False,indent=2)+'\n'
    path.write_text(output,encoding='utf-8')
    print(evidence['terminal_marker'])
    print('checks',masks,mobius_pairs,word_terms,weighted_terms,response_checks)
    print('witness',global_mixed_D21,parikh31,parikh12,bool_mixed,vals)
    print('evidence_sha256',hashlib.sha256(output.encode()).hexdigest())
if __name__=='__main__':main()
