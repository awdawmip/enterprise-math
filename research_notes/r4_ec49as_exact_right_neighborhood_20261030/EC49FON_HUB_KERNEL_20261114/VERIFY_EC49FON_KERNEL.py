#!/usr/bin/env python3
"""Exact EC49FON hub kernel, rank and all native same-domain pairs.
Usage: python VERIFY_EC49FON_KERNEL.py EC49FOM_PROFILES.csv EC49FOM_MOBIUS_84.csv
Frozen upstream profiles are root-cover results; no source science is re-pinned.
"""
import csv, itertools, json, sys
from collections import defaultdict
from fractions import Fraction

E={5:(5,7),7:(6,7),13:(6,7),15:(3,5,7),
   17:(3,6,7),19:(3,5,7),21:(3,6,7)}
R=(3,5,6,7); HUB=7; L=tuple(E)
V={r:tuple(l for l in L if r in E[l]) for r in R}
B={r:tuple(l for l in L if E[l]==(r,HUB)) for r in R if r!=HUB}
C=tuple((r,S) for r in R for k in range(len(V[r])+1)
        for S in itertools.combinations(V[r],k))
index={key:i for i,key in enumerate(C)}
assignments=tuple(dict(zip(L,ss)) for ss in
                  itertools.product(*(E[l] for l in L)))
matrix=[]
for rho in assignments:
    row=0
    for r in R:
        S=tuple(l for l in V[r] if rho[l]==r)
        row |= 1<<index[r,S]
    assert row.bit_count()==4
    matrix.append(row)

def gf2_rank(vectors):
    piv={}
    for x in vectors:
        while x:
            k=x.bit_length()-1
            if k in piv:x ^= piv[k]
            else:
                piv[k]=x;break
    return len(piv)

basis=[]
for r in R:
    if r==HUB:continue
    basis.append(('constant_'+str(r),
                  {(s,S):(int(s==r)-int(s==HUB)) for s,S in C}))
for l in L:
    basis.append(('unary_'+str(l),{(r,S):
                  (int(l not in S) if r==HUB else
                   -int(l in S) if r in E[l] else 0)
                  for r,S in C}))
for r,spokes in B.items():
    for k in range(2,len(spokes)+1):
        for Q in itertools.combinations(spokes,k):
            q=set(Q)
            basis.append(('interaction_'+str(r)+'_'+','.join(map(str,Q)),
                          {(s,S):(int(q.isdisjoint(S)) if s==HUB else
                                   -int(q.issubset(S)) if s==r else 0)
                           for s,S in C}))

def rank_q(vectors):
    echelon={}
    for g in vectors:
        vec={i:Fraction(g[key]) for i,key in enumerate(C) if g[key]}
        while vec:
            i=min(vec)
            if i not in echelon:
                x=vec[i]
                echelon[i]={j:v/x for j,v in vec.items()}
                break
            x=vec[i]
            for j,v in echelon[i].items():
                z=vec.get(j,0)-x*v
                if z:vec[j]=z
                elif j in vec:del vec[j]
    return len(echelon)

assert len(assignments)==648 and len(C)==168
assert gf2_rank(matrix)==157
assert len(basis)==11 and rank_q([g for _,g in basis])==11
for name,g in basis:
    for rho in assignments:
        assert sum(g[(r,tuple(l for l in V[r] if rho[l]==r))]
                   for r in R)==0, (name,rho)

profile=defaultdict(dict); meta={}
with open(sys.argv[1],newline='') as f:
    for row in csv.DictReader(f):
        k=int(row['config']);r=int(row['root'])
        must=int(row['must']); opt=int(row['opt'])
        S=int(row['subset']);cost=int(row['cost'])
        assert (S & ~opt)==0
        if (k,r) in meta:assert meta[k,r]==(must,opt)
        meta[k,r]=(must,opt)
        assert S not in profile[k,r]
        profile[k,r][S]=cost
with open(sys.argv[2],newline='') as f:
    edges=list(csv.DictReader(f))
assert len(edges)==84 and len(profile)==204
equal_edges=0; changed_entries=0; comparable_edges=0
for row in edges:
    if row['same_domain']!='1':continue
    comparable_edges+=1
    a,b=int(row['src']),int(row['dst'])
    mismatch=0
    for r in R:
        assert meta[a,r]==meta[b,r]
        assert profile[a,r].keys()==profile[b,r].keys()
        mismatch+=sum(profile[a,r][S]!=profile[b,r][S]
                      for S in profile[a,r])
    changed_entries+=mismatch
    expected_total_equal=int(row['polynomial_terms'])==0
    assert expected_total_equal==(mismatch==0)
    if expected_total_equal:equal_edges+=1
assert (comparable_edges,equal_edges,changed_entries)==(82,32,790)

classes=defaultdict(list)
for k in sorted({k for k,r in profile}):
    classes[tuple(meta[k,r] for r in R)].append(k)
pairs=[];classes_summary=[]
for domain,configs in classes.items():
    optional=tuple(l for l in range(24)
                   if any((opt>>l)&1 for must,opt in domain))
    options={l:tuple(r for r,(must,opt) in zip(R,domain)
                     if (opt>>l)&1) for l in optional}
    masks=[]
    for values in itertools.product(*(options[l] for l in optional)):
        rho=dict(zip(optional,values))
        masks.append(tuple(sum(1<<l for l in optional if rho[l]==r)
                           for r in R))
    terminal={}; root_signature={}
    for k in configs:
        terminal[k]=tuple(sum(profile[k,r][mask] for r,mask in zip(R,ms))
                          for ms in masks)
        root_signature[k]=tuple(tuple((S,profile[k,r][S])
                                for S in sorted(profile[k,r])) for r in R)
    same=0
    for a,b in itertools.combinations(configs,2):
        eq_terminal=int(terminal[a]==terminal[b])
        eq_root=int(root_signature[a]==root_signature[b])
        assert eq_terminal==eq_root
        pairs.append((a,b,len(masks),eq_terminal,eq_root))
        same+=eq_terminal
    classes_summary.append({'configs':len(configs),'assignments':len(masks),
                            'pairs':len(configs)*(len(configs)-1)//2,
                            'equal_pairs':same,
                            'distinct_terminal_maps':len(set(terminal.values()))})
assert len(pairs)==1000 and sum(p[3] for p in pairs)==364
assert sorted((g['configs'],g['assignments'],g['equal_pairs'])
              for g in classes_summary)==[(1,1944,0),(5,648,4),(45,648,360)]

with open('EC49FON_ALL_PAIRS.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerow(('src','dst','legal_assignments','same_terminal_map',
                'same_reachable_root_profiles'))
    w.writerows(pairs)
result={'schema':'EC49FON_EXACT_V1',
 'frozen_input':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
 'assignments':648,'reachable_root_profiles':168,
 'incidence_rank_mod2':157,'kernel_rank_over_Z':11,
 'basis':[name for name,g in basis],
 'native_original_edges':84,'common_domain_edges':82,
 'equal_original_edges':32,'changed_root_entries':790,
 'same_domain_pairs_all_51_configs':1000,
 'terminal_equal_pairs':364,'terminal_equal_but_root_profiles_different':0,
 'domain_classes':classes_summary,'review':'NOT_REVIEWED'}
with open('EC49FON_RESULT.json','w') as f:json.dump(result,f,indent=2);f.write('\n')
print('EC49FON_EXACT_PASS assignments=648 profiles=168 rank_GF2=157 kernel=11')
print('EC49FON_NATIVE_PASS edges=82 zero=32 entries=790 pairs=1000 equal=364 nontrivial=0')
