#!/usr/bin/env python3
"""EC49FAH exact finite local-observer-cover + weighted signed-prefix-clique certificate."""
import collections, hashlib, itertools, json, sys
from pathlib import Path
P=Path(__file__).resolve().parent
X=P.parent/'EC49EXY_H8_M5_EXACT_CROSS_FIBER_CAPS'
if not X.exists():X=P/'EC49EXY_H8_M5_EXACT_CROSS_FIBER_CAPS'
J=P.parent/'EC49EXJ_H8_M4_S6_GLOBAL_EXACT'
if J.joinpath('SCREEN_H5_EC49EXJ.py').is_file():
    sys.path.insert(0,str(J))
    from SCREEN_H5_EC49EXJ import words, T2, T4
else:  # local reproduction with identical pinned generator extracted from prior archive
    sys.path.insert(0,str(X))
    from PINNED_NATIVE_WORDS_EC49EXJ import words, T2, T4
raw=(X/'EC49EXY_DOUBLE_CANDIDATES.tsv').read_bytes()
assert hashlib.sha256(raw).hexdigest()=='1e5f75bdc2491f355db6e2632fb6789a55397f7943c77c6ebf249807ee20712a'
rows=[];groupset=set();families=set()
for ln in raw.decode().splitlines():
    if not ln or ln.startswith('#'):continue
    v=list(map(int,ln.split()));a,b,c,d=v[2:6]
    hs=((a,b),(c,d))+tuple((h,) for h in range(2,9) if h not in (a,b,c,d))
    keys=tuple(tuple(v[6+3*i:9+3*i]) for i in range(5))
    gr=tuple(zip(hs,keys));rows.append((v,gr))
    for hh,k in gr:
        groupset.add((hh,k))
        families.update((h,k,4 if k[0]+k[1]-h-1>=1 else 2) for h in hh)
assert len(rows)==12356 and len(families)==137
# Use one immutable ID per actual ordered signed native primitive-step prefix.
trie={};nextid=1;fam={}
for key in sorted(families):
    perdepth=collections.defaultdict(dict);t=key[2]
    for st,signature,_ in words(*key):
        bit=1<<(T4 if t==4 else T2).index(signature);node=0
        for dep,step in enumerate(st,1):
            edge=(node,step)
            if edge not in trie:trie[edge]=nextid;nextid+=1
            node=trie[edge]
            perdepth[dep][node]=perdepth[dep].get(node,0)|bit
    fam[key]=perdepth

def setcover(masks,full):
    D={0:0}
    for mask in set(masks):
        for old,steps in tuple(D.items()):
            m=old|mask
            if steps+1<D.get(m,1000):D[m]=steps+1
    return D[full]
# Exact minimum signature-cover count independently for each key-group and depth.
G={}
for hh,k in groupset:
    maps=collections.defaultdict(dict);shift=0
    for h in hh:
        t=4 if k[0]+k[1]-h-1>=1 else 2
        for depth,mm in fam[h,k,t].items():
            for pid,mask in mm.items():maps[depth][pid]=maps[depth].get(pid,0)|(mask<<shift)
        shift+=t
    length=2*(sum(k)-1)
    assert all(d in maps for d in range(1,length+1))
    q={d:setcover(maps[d].values(),(1<<shift)-1) for d in range(1,length+1)}
    G[hh,k]=(q,length,{d:frozenset(m) for d,m in maps.items()})
# Original cross-fiber capacity matrix (complete signed-axis words, not histogram surrogate).
lines=[x for x in (X/'EC49EXY_CAPS_TABLE.txt').read_text().splitlines() if x and not x.startswith('#')]
assert lines[0]=='164'
mat=[tuple(map(int,x.split())) for x in lines[1:]]
lookup={(z[0],tuple(z[1:4])):i for i,z in enumerate(mat)}
assert len(mat)==164
CAP={}
for ri,(v,gr) in enumerate(rows):
    for i,j in itertools.combinations(range(5),2):
        a,b=gr[i],gr[j]
        if (a,b) not in CAP:
            CAP[a,b]=max(mat[lookup[h,a[1]]][5+lookup[g,b[1]]] for h in a[0] for g in b[0])
# Exact five-fiber incompatibility clique sum per depth; mathematically valid lower bound.
hist=collections.Counter();triple_gain_rows=0;triple_gain_total=0;triple_events=0
for ri,(v,gr) in enumerate(rows):
    L=max(G[x][1] for x in gr);sum_pair=0;sum_triple=0
    for d in range(1,L+1):
        q=[G[x][0].get(d,0) for x in gr]
        p={(i,j):CAP[gr[i],gr[j]]>=d for i,j in itertools.combinations(range(5),2)}
        pair=max((sum(q[i] for i in S) for m in range(1,32)
            if (S:=[i for i in range(5) if (m>>i)&1])
            and all(not p[i,j] for i,j in itertools.combinations(S,2))),default=0)
        # EC49FAG's concrete absent common signed prefixes impose 3-set capacity 2.
        triple=pair
        for i,j,k in itertools.combinations(range(5),3):
            if not all((q[x]>0 for x in (i,j,k))):continue
            if not (p[i,j] and p[i,k] and p[j,k]):continue
            ai,bj,ck=(G[gr[x]][2][d] for x in (i,j,k))
            if not any(s in bj and s in ck for s in ai):
                triple_events+=1
                triple=max(triple,(q[i]+q[j]+q[k]+1)//2)
        sum_pair+=pair;sum_triple+=triple
    hist[sum_pair]+=1
    if sum_triple>sum_pair:
        triple_gain_rows+=1;triple_gain_total+=sum_triple-sum_pair
    if sum_pair<76:raise AssertionError(('counterexample_required',ri,sum_pair))
assert min(hist)==76 and hist[76]==66 and sum(hist.values())==12356
R={'id':'EC49FAH','status':'AUTHOR_FINITE_CERTIFICATE_UNREVIEWED',
  'source_tsv_sha256':hashlib.sha256(raw).hexdigest(),
  'full_schedule_rows':len(rows),'distinct_word_families':len(families),
  'signed_prefix_tree_nodes':nextid-1,'group_depth_exact_covers':sum(len(x[0]) for x in G.values()),
  'pairwise_bound_minimum':min(hist),'pairwise_bound_equal_76':hist[76],
  'pairwise_bound_lt76':sum(n for e,n in hist.items() if e<76),
  'pairwise_bound_histogram':dict(sorted(hist.items())),
  'triple_obstruction_events':triple_events,'triple_refined_schedule_count':triple_gain_rows,
  'triple_refined_total_increment':triple_gain_total,
  'previous_explicit_76_edge_witnesses':4,
  'mother_exact_optimum_given_published_prior_classification':76,
  'native_admission':'PENDING','independent_driver_review':'PENDING'}
print(json.dumps(R,ensure_ascii=False,indent=2))
