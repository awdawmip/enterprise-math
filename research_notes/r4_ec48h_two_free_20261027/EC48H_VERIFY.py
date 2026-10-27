#!/usr/bin/env python3
"""EC48H: exact rational two-free-decoder path certificate.

Finite exhaustive tests are separate from the general combinatorial proof.
No third-party dependencies; no native X6 claims.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
from itertools import product
import json
import random


def model(P, Q):
    H, Y = len(P), len(P[0])
    assert all(len(r) == Y for r in P + Q)
    assert all(v > 0 for row in P + Q for v in row)
    SP, SQ = sum(map(sum, P)), sum(map(sum, Q))
    p = tuple(tuple(F(v, SP) for v in row) for row in P)
    q = tuple(tuple(F(v, SQ) for v in row) for row in Q)
    return H, Y, p, q


def face_data(p, q, r):
    H, Y = len(p), len(p[0])
    tied = tuple(h for h in range(H) if any(p[h][y] == r*q[h][y] for y in range(Y)))
    other = tuple(h for h in range(H) if h not in tied)
    lower = tuple(tuple(int(p[h][y] > r*q[h][y]) for y in range(Y)) for h in range(H))
    upper = tuple(tuple(int(p[h][y] >= r*q[h][y]) for y in range(Y)) for h in range(H))
    C = tuple(sorted(set(lower[h] for h in other)))
    return tied, other, lower, upper, C


def khull(p, q):
    ratios = sorted({p[h][y]/q[h][y] for h in range(len(p)) for y in range(len(p[0]))})
    chambers = [ratios[0]/2] + [(a+b)/2 for a,b in zip(ratios, ratios[1:])] + [ratios[-1]+1]
    return max(len(set(tuple(int(p[h][y] > x*q[h][y]) for y in range(len(p[0]))) for h in range(len(p)))) for x in chambers), ratios


def row_or(rows, Y):
    return tuple(int(any(row[y] for row in rows)) for y in range(Y))


def serialize(x):
    if isinstance(x, F):
        return f'{x.numerator}/{x.denominator}'
    if isinstance(x, tuple):
        return [serialize(a) for a in x]
    return x


def construct(P, Q, r, K, verify=True):
    H,Y,p,q=model(P,Q)
    tied,other,b,a,C=face_data(p,q,r)
    c=len(C); t=K-c
    bout=tuple(sorted({b[h] for h in tied if b[h] not in C}))
    aout=tuple(sorted({a[h] for h in tied if a[h] not in C}))
    assert t>=0 and len(bout)<=t and len(aout)<=t
    E=tuple(sorted({(b[h],a[h]) for h in tied if b[h] not in C and a[h] not in C}))
    Bactive=tuple(sorted({src for src,dst in E})); Aactive=tuple(sorted({dst for src,dst in E}))
    edges_by_b={src:{dst for x,dst in E if x==src} for src in Bactive}
    edges_by_a={dst:{src for src,x in E if x==dst} for dst in Aactive}
    is_matching=all(len(v)==1 for v in edges_by_b.values()) and all(len(v)==1 for v in edges_by_a.values())
    pivot=row_or(Bactive,Y) if E else tuple(0 for _ in range(Y))
    is_pivot=bool(E) and all(all(pivot[y]<=dst[y] for y in range(Y)) for dst in Aactive)
    if not E:case='empty'
    elif is_matching:case='matching'
    elif is_pivot:case='common_pivot'
    elif len(Bactive)==len(Aactive)==2 and len(E)==3:case='three_edge_switch'
    else:return None

    zeros=tuple(F(0) for _ in range(Y))
    U=[[F(v) for v in row] for row in (C + bout + (tuple(0 for _ in range(Y)),)*max(0,t-len(bout)))]
    assert len(U)==K
    indexC={row:i for i,row in enumerate(C)}
    indexB={row:c+i for i,row in enumerate(bout)}
    pi=[[F(0) for _ in range(K)] for _ in range(H)]
    for h in range(H):
        slot=indexC[b[h]] if b[h] in C else indexB[b[h]]
        pi[h][slot]=F(1)
    support=sum(max(p[h][y]-r*q[h][y],F(0)) for h in range(H) for y in range(Y))
    tie_total=sum(q[h][y] for h in range(H) for y in range(Y) if p[h][y]==r*q[h][y])
    progress=[]; checks=0
    def check(where):
        nonlocal checks
        vals=[];s=F(0); mass=F(0)
        for h in range(H):
            assert sum(pi[h])==1
            for y in range(Y):
                assert all(F(0)<=U[k][y]<=1 for k in range(K))
                z=sum(pi[h][k]*U[k][y] for k in range(K))
                assert F(0)<=z<=1
                if p[h][y]>r*q[h][y]: assert z==1
                if p[h][y]<r*q[h][y]: assert z==0
                if p[h][y]==r*q[h][y]: mass+=q[h][y]*z
                s+=(p[h][y]-r*q[h][y])*z
                vals.append(z)
                checks+=1
        assert s==support,(where,s,support)
        if progress: assert mass>=progress[-1][1],(where,mass,progress[-1])
        progress.append((where,mass))
    def move_encoder(h,slot,label):
        old=pi[h][:]
        target=[F(int(k==slot)) for k in range(K)]
        for lam in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
            pi[h]=[(1-lam)*old[k]+lam*target[k] for k in range(K)]
            if verify: check(label)
        pi[h]=target
    def move_decoder(slot, target, label):
        original=U[slot][:];target=list(map(F,target))
        for lam in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
            U[slot]=[(1-lam)*original[y]+lam*target[y] for y in range(Y)]
            if verify:check(label)
        U[slot]=target

    if verify: check('start')
    # A: histories whose A endpoint belongs to a fixed non-tied decoder.
    for h in tied:
        if a[h] in C:
            move_encoder(h,indexC[a[h]],'absorb-in-C')
    assert all((a[h] not in C) or pi[h][indexC[a[h]]]==1 for h in tied)

    active_source_slot={row:indexB[row] for row in Bactive}
    target_slot={}
    if case=='empty':
        pass
    elif case=='matching':
        for src,dst in E:
            s=active_source_slot[src]
            target_slot[dst]=s
            move_decoder(s,dst,'matching-edge')
    elif case=='three_edge_switch':
        sources={src for src,dst in E}
        leaves=[src for src in sources if sum(int(a0==src) for a0,z in E)==1]
        assert len(leaves)==1
        leaf=leaves[0]; center=next(src for src in sources if src!=leaf)
        shared=next(dst for src,dst in E if src==leaf)
        other=next(dst for src,dst in E if src==center and dst!=shared)
        leaf_slot=active_source_slot[leaf]; center_slot=active_source_slot[center]
        move_decoder(leaf_slot,shared,'leaf-to-shared-A')
        target_slot[shared]=leaf_slot
        for h in tied:
            if b[h]==center and a[h]==shared:
                move_encoder(h,leaf_slot,'cross-edge-private-transfer')
        move_decoder(center_slot,other,'center-to-leaf-A')
        target_slot[other]=center_slot
    elif case=='common_pivot':
        # All existing outside/outside edges admit a common binary pivot.
        pivot=row_or(Bactive,Y)
        assert all(all(pivot[y]<=dst[y] for y in range(Y)) for dst in Aactive)
        for s in range(c,K):
            move_decoder(s,pivot,'many-to-one-pivot')
        for i,dst in enumerate(Aactive):target_slot[dst]=c+i
        for h in tied:
            if b[h] not in C and a[h] not in C:
                move_encoder(h,target_slot[a[h]],'pivot-relabel')
        for dst in Aactive:
            move_decoder(target_slot[dst],dst,'pivot-to-target')

    # Unused free rows can be configured as targets for histories starting in C.
    spare=[s for s in range(c,K) if s not in target_slot.values()]
    for dst in aout:
        if dst not in target_slot:
            assert spare
            s=spare.pop(0)
            assert all(pi[h][s]==0 for h in range(H)),('not a spare slot',s)
            move_decoder(s,dst,'unused-row-to-target')
            target_slot[dst]=s
    assert set(target_slot)==set(aout)
    for h in tied:
        if a[h] not in C and b[h] in C:
            move_encoder(h,target_slot[a[h]],'release-from-C')
    if verify:
        for h in range(H):
            for y in range(Y):
                z=sum(pi[h][s]*U[s][y] for s in range(K))
                assert z==a[h][y],('final is not upper endpoint',h,y,z,a[h][y])
        assert progress[0][1]==0 and progress[-1][1]==tie_total
        assert sum(1 for _,mass in progress if mass==tie_total)>0
        assert all(0<=m<=tie_total for _,m in progress)
    return {'case':case,'r':serialize(r),'K':K,'c':c,'free':t,'B_out':serialize(bout),'A_out':serialize(aout),'edges':serialize(E),'tied_histories':len(tied),'tied_Q':serialize(tie_total),'support':serialize(support),'check_count':checks,'steps':len(progress),'first_last_mass':[serialize(progress[0][1]),serialize(progress[-1][1])] if verify else []}


def verify_model(P,Q):
    _,_,p,q=model(P,Q)
    K,ratios=khull(p,q)
    certificates=[]
    for r in ratios:
        certificate=construct(P,Q,r,K)
        if certificate is not None:
            certificates.append(certificate)
    return K,ratios,certificates


def run():
    # Two mathematically distinct witnesses: 3-edge case lacks a common pivot;
    # complete bipartite 2x2 case uses a common binary pivot.
    examples={
        'three_edge_no_pivot':{'P':[[3,2,2,1],[3,1,2,2],[2,1,2,3]],'Q':[[2]*4 for _ in range(3)]},
        'four_edge_common_pivot':{'P':[[3,2,2,1],[3,2,1,2],[2,3,2,1],[2,3,1,2]],'Q':[[2]*4 for _ in range(4)]},
        'matching_two_free':{'P':[[3,1,1],[2,1,1],[1,2,1],[1,2,3]],'Q':[[2]*3 for _ in range(4)]}
    }
    example_results={}
    for name,data in examples.items():
        K,ratios,certs=verify_model(data['P'],data['Q'])
        # Display only the most demanding middle-ratio critical certificate.
        target=max(certs,key=lambda x:(x['free'],len(x['edges']),x['tied_histories']))
        example_results[name]={'P':data['P'],'Q':data['Q'],'K_hull':K,'critical_count':len(ratios),'target_certificate':target}
    counts=Counter(); structural_cases=Counter(); path_cases=Counter()
    all_faces_two_free=0; structurally_checked=0; checked_faces=0; checked_cells=0
    path_models=0
    def add(P,Q,do_path):
        nonlocal all_faces_two_free,structurally_checked,checked_faces,checked_cells,path_models
        _,_,p,q=model(P,Q)
        K,ratios=khull(p,q)
        counts['models']+=1
        counts['k_'+str(K)]+=1
        relevant=[]
        for r in ratios:
            tied,other,b,a,C=face_data(p,q,r)
            t=K-len(C)
            bout=set(b[h] for h in tied)-set(C)
            aout=set(a[h] for h in tied)-set(C)
            assert len(bout)<=t and len(aout)<=t
            E=set((b[h],a[h]) for h in tied if b[h] not in C and a[h] not in C)
            bs={src for src,dst in E};aa={dst for src,dst in E}
            is_matching=(all(sum(int(src==b0) for b0,dst in E)==1 for src in bs) and
                         all(sum(int(dst==a0) for src,a0 in E)==1 for dst in aa))
            pivot=row_or(tuple(bs),len(p[0])) if E else tuple(0 for _ in range(len(p[0])))
            is_pivot=bool(E) and all(all(pivot[y]<=dst[y] for y in range(len(p[0]))) for dst in aa)
            if not E:case='empty'
            elif is_matching:case='matching'
            elif is_pivot:case='common_pivot'
            elif len(bs)==len(aa)==2 and len(E)==3:case='three_edge_switch'
            else:continue
            structural_cases[case]+=1
            structurally_checked+=1
            relevant.append((r,case))
        if len(relevant)==len(ratios):all_faces_two_free+=1
        if do_path:
            path_models+=1
            for r,case in relevant:
                z=construct(P,Q,r,K)
                assert z['case']==case
                checked_faces+=1
                checked_cells+=z['check_count']
                path_cases[case]+=1
    for H,Y in ((3,2),(4,2)):
        Q=[[2]*Y for _ in range(H)]
        for i,flat in enumerate(product((1,2,4),repeat=H*Y)):
            P=[list(flat[h*Y:(h+1)*Y]) for h in range(H)]
            add(P,Q,do_path=(i%47==0))
    rng=random.Random(480011)
    for H,Y,n in ((4,3,350),(5,4,300),(6,4,200)):
        for i in range(n):
            P=[[rng.randint(1,7) for _ in range(Y)] for _ in range(H)]
            Q=[[rng.randint(1,5) for _ in range(Y)] for _ in range(H)]
            add(P,Q,do_path=(i%19==0))
    out={
        'schema':'EM_EC48H_TWO_FREE_EXACT_REPORT_V1',
        'research_scope':'finite strictly positive normalized two-stage BRC; author-side exact checker',
        'algorithm':'Fraction chamber signatures; exact decoder and stochastic-encoder path; each elementary moving encoder/decoder segment linear',
        'exhaustive_box':'H=3 or 4, Y=2, Praw entries independently in {1,2,4}, Qraw all 2; exactly 3^6+3^8=7290 models',
        'random_box':'850 seeded models with (H,Y)=(4,3):350,(5,4):300,(6,4):200; Praw in [1,7], Qraw in [1,5]',
        'models_structurally_scanned':counts['models'],
        'models_with_all_faces_meeting_criterion':all_faces_two_free,
        'khull_histogram':{k:v for k,v in sorted(counts.items()) if k.startswith('k_')},
        'criterion_critical_faces_structurally_classified':structurally_checked,
        'structural_case_histogram':dict(sorted(structural_cases.items())),
        'models_sampled_for_exact_path':path_models,
        'exact_path_faces_checked':checked_faces,
        'exact_cell_assertions':checked_cells,
        'path_case_histogram':dict(sorted(path_cases.items())),
        'examples':example_results,
        'result':'PASS',
        'limits':'exhaustive criterion classification only for the declared finite box; a deterministic subsample receives full Fraction path checks; universal theorem is proved separately; no native X6 readout or physics claim'
    }
    print(json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__':run()
