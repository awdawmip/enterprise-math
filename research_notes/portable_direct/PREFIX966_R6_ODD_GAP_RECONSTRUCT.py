#!/usr/bin/env python3
"""Independent exact residual/quotient inversion for m in {1,3,5}.
Auxiliary named XOR integer observer; no native X6 or BRC inference.
Reproduces original named witness multiplicity, not just pair membership.
"""
import json
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import product
from pathlib import Path
from struct import pack
from time import perf_counter

PIN='f42f2906d77f24085c123f3ccfe9667d41caa96d'

def residual_terms(p):
    terms=defaultdict(list)
    for i in range(p):
        for j in range(p):
            for sign in (-1,1):
                terms[(1<<i)-sign*(1<<j)].append((i,j,sign))
    return terms

def actual_count(x,named):
    return sum(((x>>j)&1)==(sign==-1) for i,j,sign in named)

def invert_odd_gap(p,k,m,include_diagonal=False):
    assert p>=4 and k>=1 and k%2==1 and k+2<(1<<(p-1)) and m>0 and m%2==1
    H=1<<(p-1); lo=H+1; hi=2*H-1
    z=residual_terms(p)
    # parity delta = C-c = 2a-mb is necessarily odd for m odd, hence c,C opposite parity
    even=[(v,n) for v,n in z.items() if v%2==0]
    odd=[(v,n) for v,n in z.items() if v%2]
    counter=Counter(); witnesses=[]; full_named=[]; stat=Counter(); tmax=2*k
    for first,second in ((even,odd),(odd,even)):
        for c,cs in first:
            for C,Cs in second:
                delta=C-c
                N=k*C-(k+2)*c
                assert N&1, (c,C,N)
                stat['numeric_residual_pairs']+=1
                for t in range(1,tmax+1):
                    d=2*t-k*m
                    if not d: raise AssertionError('odd m and odd k cannot resonate')
                    stat['nonresonant_integer_divisibility_tests']+=1
                    if N%d: continue
                    b=N//d
                    if b<lo or b>hi or not(b&1): continue
                    a2=m*b+delta
                    if a2&3 != 2:continue
                    a=a2//2
                    if a<lo or a>hi or (not include_diagonal and a==b):continue
                    stat['arithmetic_modulus_candidates']+=1
                    assert k*a-t*b==c and (k+2)*a-(t+m)*b==C
                    n1=actual_count(k*a,cs)
                    n2=actual_count((k+2)*a,Cs)
                    stat['named_predicates_tested']+=len(cs)+len(Cs)
                    if not(n1 and n2):continue
                    idx=((a-lo)//2)*(H//2)+(b-lo)//2
                    counter[idx]+=n1*n2
                    stat['reconstructed_named_histories']+=n1*n2
                    if p<=6:witnesses.append((a,b,t,t+m,c,C,n1,n2))
                    for i,j,sgn in cs:
                        if ((k*a>>j)&1)!=(sgn==-1):continue
                        for I,J,Sgn in Cs:
                            if ((((k+2)*a)>>J)&1)!=(Sgn==-1):continue
                            assert (((k*a)^(1<<j))-(1<<i))==t*b
                            assert ((((k+2)*a)^(1<<J))-(1<<I))==(t+m)*b
                            full_named.append((a,b,t,t+m,i,j,I,J))
    assert len(full_named)==sum(counter.values())
    assert len(set(full_named))==len(full_named)
    full_named.sort()
    raw=b''.join(pack('<Q',idx) for idx in sorted(counter))
    if p==19 and k==21 and not include_diagonal:
        Path(f'/mnt/data/PREFIX966_R6_Q19_GAP{m}_NAMED_WITNESSES.csv').write_text('a,b,t,T,i,j,I,J\n'+'\n'.join(','.join(map(str,w)) for w in full_named)+'\n')
    return counter,{
        'p':p,'k':k,'m':m,'off_diagonal_only':not include_diagonal,
        'distinct_ordered_pairs':len(counter),
        'named_joint_histories':sum(counter.values()),
        'pair_ids_sha256':sha256(raw).hexdigest(),
        'pair_ids_bytes':len(raw),
        'all_named_tuple_sha256':sha256(('\n'.join(','.join(map(str,w)) for w in full_named)+'\n').encode()).hexdigest(),
        'stats':dict(stat),'small_named_value_witnesses':sorted(witnesses)
    }

def direct_odd_gap(p,k,m):
    H=1<<(p-1);n=H//2;low=H+1;counter=Counter()
    for a in range(low,2*H,2):
        left=defaultdict(list);right=defaultdict(list)
        for i in range(p):
            for j in range(p):
                x=((k*a)^(1<<j))-(1<<i)
                y=(((k+2)*a)^(1<<j))-(1<<i)
                if x>0: left[x].append((i,j))
                if y>0: right[y].append((i,j))
        # Instead of iterating pair (a,b), use all original XOR source states; this is independent of D dictionary
        for x,li in left.items():
            for y,ri in right.items():
                for b in range(low,2*H,2):
                    if b!=a and x%b==0 and y==x+m*b:
                        idx=((a-low)//2)*n+(b-low)//2
                        counter[idx]+=len(li)*len(ri)
    return counter

def main():
    small=[]
    for p in (4,5,6,7):
        H=1<<(p-1)
        for k in range(1,H-2,2):
            for m in (1,3,5):
                got,meta=invert_odd_gap(p,k,m)
                direct=direct_odd_gap(p,k,m)
                assert got==direct,(p,k,m,len(got),len(direct),list((got-direct).items())[:4])
                small.append({'p':p,'k':k,'m':m,'pairs':len(got),'named':sum(got.values())})
    outputs=[]
    for m in (1,3,5):
        t0=perf_counter();pair,d=invert_odd_gap(19,21,m)
        d.pop('small_named_value_witnesses')
        d['elapsed_seconds']=round(perf_counter()-t0,4)
        outputs.append(d)
    expected={1:(442,614),3:(839,1286),5:(3,3)}
    for obj in outputs:assert (obj['distinct_ordered_pairs'],obj['named_joint_histories'])==expected[obj['m']],obj
    output={'schema':'PREFIX966_R6_ODD_GAP_FIXED_QUOTIENT_INVERSION_V1',
        'frozen_science_pin':PIN,
        'model':'auxiliary named XOR two odd cores k,k+2, strict odd p-bit Qp',
        'status':'AUTHOR_PROOF_EXACT_COMPUTATION_NOT_REVIEWED',
        'theorem':'for k odd and m odd, N=k*C-(k+2)*c = (2*t-k*m)*b odd, hence N and d nonzero, and every valid named witness is reconstructed from c,C,t and real XOR-bit signs',
        'proof_scope':'all p>=4 odd k>=1 with k+2<2^(p-1) and positive odd m; bounded t<=2*k',
        'independent_small_core_checks':small,
        'q19_k21_results':outputs,
        'limitations':'No formal independent review; numerical auxiliary observer does not assert X6/BRC admissibility. Existing P957/958 results are used only as comparison counts; algorithm generates candidates independently.'}
    with open('/mnt/data/PREFIX966_R6_EXACT_RESULTS.json','w') as f:json.dump(output,f,indent=2,ensure_ascii=False);f.write('\n')
    print(json.dumps({'small_checks':len(small),'q19':outputs},indent=2))
if __name__=='__main__': main()
