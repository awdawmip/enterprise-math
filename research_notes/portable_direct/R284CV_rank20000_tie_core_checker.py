#!/usr/bin/env python3
"""R284CV: exact frozen Port top-R core atlas, ranks 1..20,000.

Run in research_notes/portable_direct/ alongside the unchanged pinned
R284CO_spectral_witness_checker.py. Python standard library only.
"""
from R284CO_spectral_witness_checker import P, D, Z, SELECT, FROZEN_SHA, words, arcs, dist
from hashlib import sha256
from pathlib import Path
import json

RMAX = 20000
TARGETS = {7586, 7587, 7588, 20000}
KNOWN = [779, 1263, 1563, 7587]

def core_digest(X, members):
    return sha256(b''.join(v.to_bytes(8,'big') for v in sorted(X[i] for i in members))).hexdigest()

def check_core(rows, core, rank):
    for k, row in enumerate(rows):
        observed=sorted((v for v, i in row if i in core), reverse=True)[:rank]
        expected=[v for v, i in row[:rank]]
        assert observed == expected, (rank,k+2)
    assert len(core) >= rank

def run():
    X,A=words(),arcs()
    assert len(X)==len(set(X))==65536 and len(A)==64
    rows=[[] for _ in range(63)]
    for i,x in enumerate(X):
        for k,v in enumerate(sorted(dist(x,a) for a in A)[1:]):
            rows[k].append((v,i))
    for row in rows:
        row.sort(reverse=True)
    old={i for row in rows for _,i in row[:64]}
    assert len(old)==3712
    assert core_digest(X,old)=='a0e267546733e53951097484b32cf97ae49472fba905121c5b23612796d10b1c'

    counts=[0]*len(X)
    union_size=0
    tie_event_count=0
    multiple_tie_count=0
    nonunique=[]
    featured=[]
    first_simultaneous=[]
    max_event_levels=0
    for rank in range(1,RMAX+1):
        for row in rows:
            i=row[rank-1][1]
            if counts[i]==0: union_size+=1
            counts[i]+=1
        tied=[k for k,row in enumerate(rows) if row[rank-1][0]==row[rank][0]]
        if tied:
            tie_event_count+=1
            if len(tied)>1:
                multiple_tie_count+=1
                if len(first_simultaneous)<12:
                    first_simultaneous.append({'rank':rank,'levels':[k+2 for k in tied]})
            max_event_levels=max(max_event_levels,len(tied))
        drops=[]
        groups=[]
        for k in tied:
            row=rows[k]
            cutoff=row[rank-1][0]
            lo=rank-1
            while lo>0 and row[lo-1][0]==cutoff:lo-=1
            hi=rank
            while hi<len(X) and row[hi][0]==cutoff:hi+=1
            for pos in range(lo,rank):
                i=row[pos][1]
                counts[i]-=1
                if counts[i]==0:union_size-=1
                drops.append(i)
            groups.append((k,cutoff,lo,hi))
        unresolved=[]
        details=[]
        for k,cutoff,lo,hi in groups:
            members=[rows[k][pos][1] for pos in range(lo,hi)]
            forced=[i for i in members if counts[i]>0]
            missing=[i for i in members if counts[i]==0]
            required=rank-lo
            deficit=max(0,required-len(forced))
            if deficit:
                unresolved.append((missing,deficit))
            if rank in TARGETS or deficit:
                details.append({'level':k+2,'cutoff':cutoff,'group_size':len(members),
                                'required':required,'already_forced':len(forced),
                                'deficit':deficit,'residues':sorted(X[i] for i in members)})
        if unresolved:
            assert len(unresolved)==1, ('multi_constraint',rank,details)
            optional,deficit=unresolved[0]
            assert deficit==1 and len(optional)==2, ('non_binary',rank,details)
            nonunique.append(rank)
        if rank in TARGETS or unresolved:
            mandatory={i for i,n in enumerate(counts) if n>0}
            assert len(mandatory)==union_size
            minima=[mandatory|{i} for i in unresolved[0][0]] if unresolved else [mandatory]
            if rank in (7587,7588):
                for core in minima:check_core(rows,core,rank)
            featured.append({'rank':rank,'minimum_size':len(minima[0]),
                             'minimum_count':len(minima),'forced_union_size':union_size,
                             'tie_groups':details,
                             'core_sha256':sorted(core_digest(X,core) for core in minima),
                             'full_top_rank_recomputed':rank in (7587,7588)})
        for i in drops:
            if counts[i]==0:union_size+=1
            counts[i]+=1
    assert nonunique==KNOWN, nonunique
    assert first_simultaneous[0]=={'rank':2269,'levels':[4,38]}
    d={i['rank']:i for i in featured}
    assert d[7587]['minimum_size']==42637 and d[7588]['minimum_size']==42640
    assert d[7587]['minimum_count']==2 and d[7588]['minimum_count']==1
    assert d[7587]['tie_groups'][0]['level']==3 and d[7587]['tie_groups'][1]['level']==64
    output={
        'schema':'R284CV_TOP20000_MINIMUM_CORE_ATLAS_V1',
        'status':'AUTHOR_PROVED_EXACT_FINITE_CERTIFIED_NOT_REVIEWED',
        'model':{'P':P,'D':D,'Z':Z,'SELECT':SELECT,'frozen_codeword_sha256':FROZEN_SHA,
                 'codeword_count':len(X),'arcs':len(A)},
        'domain':{'rank_min':1,'rank_max':RMAX,'nontrivial_levels':63,
                  'exact_integer_arc_distances':len(X)*len(A)},
        'tie_events':tie_event_count,'simultaneous_tie_ranks':multiple_tie_count,
        'maximum_simultaneously_tied_levels':max_event_levels,
        'first_simultaneous_events':first_simultaneous,
        'nonunique_minimum_core_ranks':nonunique,
        'featured':featured,
        'method':'For each r, all strict-higher rank prefixes are mandatory. Each tied group contributes a residual quota; prefix-frequency counts determine already-forced elements; all nonzero deficits found are one-of-two at exactly four ranks.',
        'independent_review':'NOT_REVIEWED'
    }
    return output

if __name__=='__main__':
    data=run()
    out=Path(__file__).with_name('R284CV_rank20000_tie_core_certificate.json')
    out.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'tie_events':data['tie_events'],'simultaneous':data['simultaneous_tie_ranks'],
                      'nonunique':data['nonunique_minimum_core_ranks'],
                      'featured':[(v['rank'],v['minimum_size'],v['minimum_count']) for v in data['featured'] if v['rank']>=7586]}))
