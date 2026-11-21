#!/usr/bin/env python3
"""R284CU finite Port top-R core uniqueness through R=1564. Stdlib only.
Run from research_notes/portable_direct beside R284CO_spectral_witness_checker.py.
"""
from R284CO_spectral_witness_checker import P,D,Z,SELECT,FROZEN_SHA,words,arcs,dist
from hashlib import sha256
from pathlib import Path
import json

RMAX=1564

def digest(X,idx):
    return sha256(b''.join(v.to_bytes(8,'big') for v in sorted(X[i] for i in idx))).hexdigest()

def check_core(X,A,rows,C,r):
    observed=[[] for _ in range(64)]
    for i in C:
        for k,v in enumerate(sorted(dist(X[i],a) for a in A)):
            if k: observed[k].append(v)
    for k in range(1,64):
        assert sorted(observed[k],reverse=True)[:r]==[v for v,_ in rows[k][:r]],(r,k)
    assert len(C)>=r

def run():
    X,A=words(),arcs()
    assert len(X)==65536 and len(set(X))==65536 and len(A)==64
    rows=[[] for _ in range(64)]
    for i,x in enumerate(X):
        for k,v in enumerate(sorted(dist(x,a) for a in A)):
            if k: rows[k].append((v,i))
    for k in range(1,64):rows[k].sort(reverse=True)
    C64={i for k in range(1,64) for _,i in rows[k][:64]}
    assert len(C64)==3712 and digest(X,C64)=='a0e267546733e53951097484b32cf97ae49472fba905121c5b23612796d10b1c'
    tie_ranks=[]
    for r in range(1,RMAX+1):
        ties=[k for k in range(1,64) if rows[k][r-1][0]==rows[k][r][0]]
        assert len(ties)<=1
        if ties:
            k=ties[0];v=rows[k][r][0]
            assert (r==1 or rows[k][r-2][0]>v) and rows[k][r+1][0]<v
            tie_ranks.append((r,k))
    assert [r for r,_ in tie_ranks]==[155,599,779,905,957,1017,1101,1139,1177,1195,1263,1337,1377,1385,1395,1397,1443,1487,1563]
    events=[]; nonunique=[]; specials={779,780,1262,1263,1264,1562,1563,1564}
    for r in sorted(set(specials)|{r for r,_ in tie_ranks}):
        M=set()
        for k in range(1,64):
            t=rows[k][r-1][0]
            if rows[k][r][0]<t: M.update(i for _,i in rows[k][:r])
            else: M.update(i for v,i in rows[k][:r] if v>t)
        hit=[k for rr,k in tie_ranks if rr==r]
        alternatives=[M];info=None
        if hit:
            k=hit[0]
            pair=[rows[k][r-1][1],rows[k][r][1]]
            forced=[i for i in pair if i in M]
            if not forced:
                nonunique.append(r)
                alternatives=[M|{i} for i in pair]
            info={'level':k+1,'cutoff':rows[k][r-1][0],
                  'candidate_residues':sorted(X[i] for i in pair),
                  'forced_residues':sorted(X[i] for i in forced)}
        if r in specials:
            for C in alternatives: check_core(X,A,rows,C,r)
        events.append({'rank':r,'boundary':info,
                       'minimum_size':len(alternatives[0]),
                       'number_of_minima':len(alternatives),
                       'core_sha256':sorted(digest(X,C) for C in alternatives),
                       'full_core_recomputed':r in specials})
    assert nonunique==[779,1263,1563]
    ans={'schema':'R284CU_FIRST_THREE_NONUNIQUE_CORE_EVENTS_V1',
         'status':'AUTHOR_PROVED_EXACT_FINITE_CERTIFIED_NOT_REVIEWED',
         'pins':{'P':P,'D':D,'Z':Z,'SELECT':SELECT,'frozen_sha256':FROZEN_SHA},
         'population':len(X),'arc_count':len(A),'max_verified_rank':RMAX,
         'integer_arc_distances':len(X)*len(A),'checked_rank_boundaries':63*RMAX,
         'tie_event_count':len(tie_ranks),'nonunique_ranks':nonunique,
         'previous_C64_sha256':digest(X,C64),'events':events,
         'independent_review':'NOT_REVIEWED'}
    return ans

if __name__=='__main__':
    data=run()
    Path(__file__).with_name('R284CU_rank1564_certificate.json').write_text(
        json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'events':data['tie_event_count'],
                      'nonunique':data['nonunique_ranks'],
                      'verified_up_to':data['max_verified_rank']}))
