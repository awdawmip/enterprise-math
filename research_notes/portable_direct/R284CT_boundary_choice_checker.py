#!/usr/bin/env python3
"""R284CT: exact top-780 multiset-preserving cores; extends frozen R284CS.
Run beside R284CO_spectral_witness_checker.py; Python standard library only.
"""
from R284CO_spectral_witness_checker import P,D,Z,SELECT,FROZEN_SHA,words,arcs,dist
from heapq import heappush,heapreplace
from hashlib import sha256
from pathlib import Path
import json

Q=781

def build_rows(X,A):
    h=[[] for _ in range(64)]
    for index,x in enumerate(X):
        vals=sorted(dist(x,arc) for arc in A)
        for k,value in enumerate(vals):
            entry=(value,index)
            if len(h[k])<Q:heappush(h[k],entry)
            elif entry>h[k][0]:heapreplace(h[k],entry)
    return [sorted(e,reverse=True) for e in h]

def core_sha(X,indices):
    return sha256(b''.join(X[i].to_bytes(8,'big') for i in sorted(indices,key=X.__getitem__))).hexdigest()

def top_r_preserved(X,A,indices,rows,R):
    table=[[] for _ in range(64)]
    for i in indices:
        ds=sorted(dist(X[i],a) for a in A)
        for j,v in enumerate(ds):
            if j:table[j].append(v)
    for k in range(1,64):
        assert sorted(table[k],reverse=True)[:R]==[v for v,_ in rows[k][:R]],(R,k+1)
    return True

def run():
    X=words(); A=arcs(); rows=build_rows(X,A)
    assert len(X)==65536 and len(A)==64
    C64={idx for k in range(1,64) for _,idx in rows[k][:64]}
    assert len(C64)==3712
    assert core_sha(X,C64)=='a0e267546733e53951097484b32cf97ae49472fba905121c5b23612796d10b1c'
    tied=[]
    for r in range(1,Q):
        for k in range(1,64):
            if rows[k][r-1][0]==rows[k][r][0]:
                value=rows[k][r-1][0]
                indices=[i for v,i in rows[k] if v==value]
                earlier={i for j in range(1,64) if j!=k for v,i in rows[j][:r-1]}
                tied.append({'order':r,'level':k+1,'value':value,
                  'tied_residues':sorted(X[i] for i in indices),
                  'forced_by_other_levels_at_lower_ranks':sorted(X[i] for i in indices if i in earlier),
                  'other_level_lower_rank_references':{str(X[i]):[(j+1,rr+1) for j in range(1,64) if j!=k for rr,(v,ii) in enumerate(rows[j][:r-1]) if ii==i] for i in indices}})
    assert [(x['order'],x['level']) for x in tied]==[(155,16),(599,16),(779,64)],tied
    assert [len(x['forced_by_other_levels_at_lower_ranks']) for x in tied]==[1,1,0]
    cutoffs={}
    for R in (64,154,155,599,778,779,780):
        core={i for k in range(1,64) for _,i in rows[k][:R]}
        cutoffs[str(R)]={'observed_union_size':len(core),'sha256_sorted_u64be':core_sha(X,core)}
    R=779;k=63
    tieval=rows[k][R-1][0]
    assert rows[k][R][0]==tieval and rows[k][R-2][0]>tieval>rows[k][R+1][0]
    choices=[i for value,i in rows[k] if value==tieval]
    assert len(choices)==2
    assert all(rows[j][R-1][0]>rows[j][R][0] for j in range(1,63))
    mandatory={i for j in range(1,63) for value,i in rows[j][:R]}
    mandatory.update(i for value,i in rows[k][:R-1])
    assert not any(i in mandatory for i in choices)
    cores=[mandatory|{choice} for choice in choices]
    assert len(cores[0])==len(cores[1])==len(mandatory)+1
    assert top_r_preserved(X,A,cores[0],rows,R)
    assert top_r_preserved(X,A,cores[1],rows,R)
    C780={i for j in range(1,64) for value,i in rows[j][:780]}
    assert set(choices).issubset(C780) and top_r_preserved(X,A,C780,rows,780)
    info={
      'schema':'R284CT_FIRST_GENUINE_NONUNIQUENESS_AT_779_V1',
      'status':'AUTHOR_PROVED_EXACT_FINITE_CHECKED_NOT_REVIEWED',
      'pins':{'P':P,'D':D,'Z':Z,'SELECT':SELECT,'frozen_sha256':FROZEN_SHA},
      'population':len(X),'arcs':len(A),'max_rank_verified':780,
      'exact_distance_evaluations_full_population':len(X)*len(A),
      'rank_boundary_ties_through_780':tied,
      'first_rank_with_multiple_minimum_multiset_preserving_cores':779,
      'cutoffs':cutoffs,
      'rank779':{'level':64,'boundary_distance':tieval,'required_tie_count':1,
       'choice_residues':sorted(X[i] for i in choices),
       'other_levels_forced_union_size':len(mandatory),
       'minimum_cardinality':len(cores[0]),
       'two_minimum_cores_sha256_sorted_u64be':sorted(core_sha(X,C) for C in cores),
       'two_full_exact_core_recomputations':True},
      'rank780':{'unique_core_size':len(C780),
       'sha256_sorted_u64be':core_sha(X,C780),'full_exact_core_recomputation':True},
      'prior_core64_reproduced':{'size':3712,'sha256':core_sha(X,C64)},
      'independent_review':'NOT_REVIEWED'}
    return info

if __name__=='__main__':
    out=run()
    Path('R284CT_boundary_choice_certificate.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,ensure_ascii=False,indent=2))
