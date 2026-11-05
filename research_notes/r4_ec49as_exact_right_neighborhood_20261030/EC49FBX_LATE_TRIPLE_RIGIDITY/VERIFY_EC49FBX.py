#!/usr/bin/env python3
"""Exact radius-three search: two H4/H5/H6 slots plus one H7/H8/H9 slot."""
from itertools import combinations
from pathlib import Path
import json

OPS='acdefg'
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
STEPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
ENC={-1:'a',1:'A',-2:'b',2:'B',-3:'c',3:'C'}
REQ={2:(16,32),3:(16,32),4:(1,2,4,8),5:(16,32),6:(1,2,4,8),7:(1,2,4,8),8:(1,2,4,8),9:(16,32)}
W={2:('fe','ge'),3:('feg','gef'),4:('degf','fegd','cefg','gefc'),5:('feggf','geffg'),6:('aeeddd','dedead','aeeccc','ceceac'),7:('aeeddgf','dedeagf','aeeccfg','ceceafg'),8:('feggfead','geffgaed','geffgaec','feggfeac'),9:('feggfeafg','geffgaegf')}

def observe(w):
    s=0
    for op in w:
        s=T[s][OPS.index(op)]
        if s==8: return None
    return SIG[s]

def primitive_prefixes(w):
    s=''.join(ENC[i] for op in w for i in STEPS[op])
    return tuple(s[:k] for k in range(1,len(s)+1))

def candidates(h):
    x,y,z=(4,2,1) if h<=5 else (7,3,2)
    b=x+y-h-1
    a=z-1; f=x-b-2*z; g=y-b
    assert min(a,b,f,g)>=0
    out={sig:[] for sig in REQ[h]}
    for c in range(b+1):
        m={'a':a,'c':c,'d':b-c,'e':z,'f':f,'g':g}
        def visit(word,state):
            if len(word)==h:
                if SIG[state] in out: out[SIG[state]].append(word)
                return
            for k,op in enumerate(OPS):
                if m[op]>0 and T[state][k]!=8:
                    m[op]-=1
                    visit(word+op,T[state][k])
                    m[op]+=1
        visit('',0)
    return out

def union(xs):
    a=0
    for x in xs: a|=x
    return a

def main():
    chosen={f'{h}:{observe(w)}':w for h,words in W.items() for w in words}
    assert len(chosen)==24
    early=[f'{h}:{s}' for h in (4,5,6) for s in REQ[h]]
    late=[f'{h}:{s}' for h in (7,8,9) for s in REQ[h]]
    pools={}
    size={}
    for h in (4,5,6,7,8,9):
        groups=candidates(h)
        size[str(h)]={str(sig):len(words) for sig,words in groups.items()}
        for sig,words in groups.items():
            key=f'{h}:{sig}'
            pools[key]=words
            assert chosen[key] in words
    all_words=set(chosen.values())|{w for v in pools.values() for w in v}
    pref={w:primitive_prefixes(w) for w in all_words}
    prefix_ids={p:i for i,p in enumerate(sorted({p for ps in pref.values() for p in ps}))}
    bits={w:sum(1<<prefix_ids[p] for p in pref[w]) for w in all_words}
    assert union(bits[w] for w in chosen.values()).bit_count()==158
    records=[]
    rejected_pairs=0; tested_pairs=0
    for a,b in combinations(early,2):
        for c in late:
            trio=(a,b,c)
            rest=union(bits[w] for k,w in chosen.items() if k not in trio)
            base=rest.bit_count()
            A=[bits[w]&~rest for w in pools[a]]
            B=[bits[w]&~rest for w in pools[b]]
            C=[bits[w]&~rest for w in pools[c]]
            cut=158-base
            minimum=158; evaluated=0
            for ba in A:
                for bb in B:
                    tested_pairs+=1
                    joined=ba|bb
                    if joined.bit_count()>=cut:
                        rejected_pairs+=1
                        continue
                    for bc in C:
                        cost=base+(joined|bc).bit_count()
                        evaluated+=1
                        if cost<minimum: minimum=cost
            assert minimum==158,(trio,minimum)
            records.append({'slots':trio,'minimum':minimum,'all_combinations':len(A)*len(B)*len(C),
                            'evaluated':evaluated,'fixed_rest_edges':base})
    report={'schema':'EC49FBX_TWO_EARLY_ONE_LATE_RADIUS_THREE_V1',
        'date':'2026-11-06','frozen_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
        'witness_commit':'b3b43ef6abe2fd816d979792d18a67ee5d0aad50',
        'previous_triple_commit':'1eaf17da5dd0f26c9ab6e600cd40324749f37c3c',
        'witness':W,'baseline_edges':158,'candidate_counts':size,'triple_groups':len(records),
        'full_cartesian_combinations':sum(r['all_combinations'] for r in records),
        'unpruned_combinations_evaluated':sum(r['evaluated'] for r in records),
        'early_pairs_considered':tested_pairs,'early_pairs_pruned':rejected_pairs,
        'minimum_over_all_groups':min(r['minimum'] for r in records),
        'results':records}
    assert report['triple_groups']==450
    assert report['full_cartesian_combinations']==258552000
    assert report['unpruned_combinations_evaluated']==2105760
    assert report['early_pairs_considered']==162000
    assert report['early_pairs_pruned']==160540
    path=Path(__file__).with_name('EXACT_REPORT_EC49FBX.json')
    path.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in ('results','witness')},ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
