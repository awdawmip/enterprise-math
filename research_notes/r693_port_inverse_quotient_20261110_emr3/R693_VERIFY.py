#!/usr/bin/env python3
"""R693 exact E* signed-X6 port inverse and BRC source/group quotients."""
from collections import Counter, defaultdict
from itertools import combinations, product
from math import gcd, prod, comb
import json
from pathlib import Path

E=(0,2,4);O=(1,3,5)
T={(0,0):(0,1,2),(1,0):(0,1,3),(2,0):(0,1,4),
   (0,1):(0,2,3),(1,1):(1,2,3),(2,1):(0,1,3)}
Z=(0,)*6

def phase(z):
    return sum(z[i] for i in E)%3,sum(z[i] for i in O)%2

def move(z,ax,sgn):
    v=list(z);v[ax]+=sgn;return tuple(v)

def frame_step(frame,s,t):
    assert len(set(s)&set(t))==2
    old=next(iter(set(s)-set(t)))
    new=next(iter(set(t)-set(s)))
    return tuple(new if x==old else x for x in frame)

def square(z,i,j,s,t):
    origin=z;frame=T[phase(z)];g=[]
    for ax,sgn in ((i,s),(j,t),(i,-s),(j,-t)):
        g.append((z,ax,sgn))
        nxt=move(z,ax,sgn)
        frame=frame_step(frame,T[phase(z)],T[phase(nxt)])
        z=nxt
    assert z==origin
    return tuple(T[phase(z)].index(v) for v in frame),tuple(g)

def sources(z):
    return {(i,j,s,t):square(z,i,j,s,t)
            for i,j in combinations(range(6),2)
            for s,t in product((-1,1),repeat=2)}

def mobius(k):
    x=k;par=0;p=2
    while p*p<=x:
        if x%p==0:
            x//=p;par^=1
            if x%p==0:return 0
            while x%p==0:x//=p
        p+=1
    if x>1:par^=1
    return -1 if par else 1

def primitive(v):
    if not any(v):return ('HALT',)
    d=gcd(*v)
    return tuple(x//d for x in v)

def verify():
    evidence={'schema':'R693_ESTAR_BRC_PORT_IDENTIFIABILITY_V1',
              'date':'2026-11-10',
              'R462_pin':'18783e01e3646c72b7aab3b16d3f565e83e6446f',
              'frozen_source':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
              'R687_Estar':'028d5612f9562bc22ac7593f03426fc32b1a9259',
              'R692':'2b393a2f2df78faadf4dff69b9694742692d29d3',
              'scope':'E* candidate static binary directed gate field; 60 labeled positive BRC paths each of four signed X6 primitive steps; complete finite integer enumeration',
              'phase_results':[], 'two_gate_a0b0':None}
    for a,b in product(range(3),range(2)):
        z=(a,b,0,0,0,0)
        S=sources(z);Q=sorted(S)
        assert len(S)==60
        G=sorted({g for _,gs in S.values() for g in gs})
        uses=Counter(g for _,gs in S.values() for g in gs)
        assert len(G)==140 and sum(uses.values())==240
        assert Counter(uses.values())=={1:120,2:4,4:4,6:4,8:4,10:4}
        assert len({g[0] for g in G})==73
        assert max(sum(abs(x-z[i]) for i,x in enumerate(g[0])) for g in G)==2
        second={q:S[q][1][1] for q in Q}
        third={q:S[q][1][2] for q in Q}
        assert len(set(second.values()))==len(set(third.values()))==60
        assert all(uses[g]==1 for g in second.values())
        assert all(uses[g]==1 for g in third.values())
        assert not set(second.values())&set(third.values())
        for chosen in (set(),set(Q),set(Q[::2]),set(Q[::3])):
            denied={second[q] for q in Q if q not in chosen}
            actual={q for q in Q if all(g not in denied for g in S[q][1])}
            assert actual==chosen
        full=Counter(S[q][0] for q in Q);groups=sorted(full)
        bounds=tuple(full[p] for p in groups)
        expected={0:(24,18,6,12),1:(42,12,6),2:(42,18)}[a]
        assert bounds==expected,(a,b,bounds)
        support=defaultdict(list);lost_hist=defaultdict(list)
        for g in G:
            qlost=tuple(q for q in Q if g in S[q][1])
            support[qlost].append(g)
            v=Counter(S[q][0] for q in qlost)
            lost_hist[tuple(v[p] for p in groups)].append(g)
        assert len(support)==80
        assert Counter(map(len,support.values()))=={1:20,2:60}
        assert all(len(q)==1 for q,gs in support.items() if len(gs)==2)
        assert len(lost_hist)=={0:19,1:18,2:17}[a]
        norm_after={primitive(tuple(full[p]-n for p,n in zip(groups,loss)))
                    for loss in lost_hist}
        assert len(norm_after)==len(lost_hist)
        count_states=prod(n+1 for n in bounds)
        kernel_states=1+sum(mobius(d)*(prod(n//d+1 for n in bounds)-1)
                            for d in range(1,max(bounds)+1))
        brute={primitive(v) for v in product(*(range(n+1) for n in bounds))}
        assert len(brute)==kernel_states
        assert (count_states,kernel_states)=={0:(43225,38619),
              1:(3913,3057),2:(817,472)}[a]
        row={'phase':[a,b],'sources':60,'directed_ports':140,'sites':73,
             'gate_reads':240,'private_gate_pairs':60,
             'single_failure_labeled_source_signatures':len(support),
             'single_failure_group_loss_signatures':len(lost_hist),
             'single_failure_normalized_kernel_signatures':len(norm_after),
             'full_open_holonomy_counts':{''.join(map(str,p)):full[p] for p in groups},
             'possible_labeled_source_bits':60,
             'possible_labeled_source_vectors':'2^60',
             'all_group_count_states':count_states,
             'normalized_group_kernels_including_HALT':kernel_states,
             'group_count_min_fixed_bits':(count_states-1).bit_length(),
             'group_probability_min_fixed_bits':(kernel_states-1).bit_length()}
        evidence['phase_results'].append(row)
        if a==b==0:
            q=(0,1,1,1)
            assert set(support[(q,)])=={second[q],third[q]}
            evidence['one_gate_ambiguity']={
              'source':list(q),
              'private_gate_2':{'site':list(second[q][0]),'axis':second[q][1],'sign':second[q][2]},
              'private_gate_3':{'site':list(third[q][0]),'axis':third[q][1],'sign':third[q][2]}}
            pair_source=defaultdict(int);pair_group=defaultdict(int)
            for g1,g2 in combinations(G,2):
                lost=frozenset(q for q in Q if g1 in S[q][1] or g2 in S[q][1])
                pair_source[lost]+=1
                counts=Counter(S[q][0] for q in lost)
                pair_group[tuple(counts[p] for p in groups)]+=1
            assert sum(pair_source.values())==sum(pair_group.values())==comb(140,2)==9730
            assert len(pair_source)==3108 and len(pair_group)==171
            evidence['two_gate_a0b0']={
                'pairs':9730,'distinct_labeled_source_loss_sets':len(pair_source),
                'distinct_group_loss_histograms':len(pair_group),
                'max_labeled_ambiguity':max(pair_source.values()),
                'max_group_ambiguity':max(pair_group.values())}
    evidence['verification_marker']='R693_PORT_INVERSE_QUOTIENT_EXACT_PASS'
    out=Path(__file__).resolve().parent/'R693_EVIDENCE.json'
    out.write_text(json.dumps(evidence,ensure_ascii=False,sort_keys=True,indent=2)+'\n',
                   encoding='utf-8')
    print(evidence['verification_marker'])
    return evidence

if __name__=='__main__':verify()
