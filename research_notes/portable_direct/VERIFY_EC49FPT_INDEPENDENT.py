#!/usr/bin/env python3
"""Independent exact replay of EC49FPT mixed decision tree against 242 original source configurations.
Verifies only upper bound; global lower bound belongs to VERIFY_EC49FPS.py Bellman search.
"""
import csv, hashlib, itertools, json, collections, sys
from pathlib import Path
B=Path(sys.argv[1]); C=json.loads(Path(sys.argv[2]).read_text())
MASTER=B/'frozen_original_master.txt'; COST=B/'EC49FPG_PROFILE.csv'
assert hashlib.sha256(MASTER.read_bytes()).hexdigest()==C['original_master_sha256']
assert hashlib.sha256(COST.read_bytes()).hexdigest()==C['root_cost_table_sha256']
RR=(3,5,6,7)
with MASTER.open() as f:
    n_family,n_words,n_cfg=map(int,f.readline().split())
    assert (n_family,n_words,n_cfg)==(94,178850,38169)
    families=[]; words_read=0
    for _ in range(n_family):
        n=int(f.readline());words_read+=n;masks=[0]*4
        for _ in range(n):
            label,word=f.readline().split()
            masks[RR.index(bytes.fromhex(word)[0])]|=1<<int(label)
        families.append(masks)
    configs=[tuple(map(int,f.readline().split())) for _ in range(n_cfg)]
    assert words_read==n_words

def signature(cfg):
    sig=[0]*24
    for family_idx in cfg:
        for j,mask in enumerate(families[family_idx]):
            for label in range(24):
                if mask&(1<<label):sig[label]|=1<<j
    return tuple(sig)
tgt=signature(configs[16995]);ids=[idx for idx,cfg in enumerate(configs) if signature(cfg)==tgt]
assert len(ids)==242 and ids[0]==16995
root_rows=collections.defaultdict(dict)
with COST.open(newline='') as f:
    for rec in csv.DictReader(f):
        cid=int(rec['config'])
        if cid in set(ids):
            key=(int(rec['root']),int(rec['subset']))
            assert key not in root_rows[cid]
            root_rows[cid][key]=int(rec['cost'])
assert len(root_rows)==242
keys=sorted(root_rows[ids[0]])
assert len(keys)==96
assert all(set(root_rows[c])==set(keys) for c in ids)
profile_to_id={}
for cid in ids:
    p=tuple(root_rows[cid][k] for k in keys)
    if p not in profile_to_id:profile_to_id[p]=len(profile_to_id)
assert len(profile_to_id)==112
assert [cid for cid in ids if tuple(root_rows[cid][k] for k in keys) in profile_to_id] == ids
profile_reps=[None]*112
for cid in ids:
    p=tuple(root_rows[cid][k] for k in keys)
    ix=profile_to_id[p]
    if profile_reps[ix] is None:profile_reps[ix]=cid
assert profile_reps==C['profile_source_ids']
opt=[label for label in range(24) if tgt[label].bit_count()>1]
assignments=list(itertools.product(*(tuple(root for j,root in enumerate(RR) if tgt[l]>>j&1) for l in opt)))
assert len(assignments)==324
assert len(C['canonical_action_indices'])==395

def action_price_and_value(cid,action):
    if action[0]=='R':return 1,root_rows[cid][tuple(action[1:])]
    assert action[0]=='T'; assignment=assignments[action[1]]
    subs={r:0 for r in RR}
    for l,r in zip(opt,assignment):subs[r]|=1<<l
    return 2,sum(root_rows[cid][(r,subs[r])] for r in RR)

def walk(cid):
    node=C['tree'];total=0;history=[]
    while 'leaf' not in node:
        act=node['action'];assert act[0] in ('T','R')
        if act[0]=='T':assert node['action_index']==act[1]
        else:
            expected=324+sum(2**len([l for l in opt if tgt[l]>>j&1]) for j in range(RR.index(act[1])))
            # index is fixed by sorted subset ordering and root order
            all_sub=sorted({s for c in root_rows.values() for r,s in c if r==act[1]})
            assert node['action_index']==expected+all_sub.index(act[2])
        price,val=action_price_and_value(cid,act)
        total+=price; history.append((act,val))
        node=node['children'][str(val)]
    return node['leaf'],total,history
hist=collections.Counter()
root_queries=terminal_queries=0
observed_paths={}
for cid in ids:
    leaf,price,history=walk(cid)
    profile=tuple(root_rows[cid][k] for k in keys)
    assert leaf==profile_to_id[profile]
    rr=sum(1 for a,val in history if a[0]=='R')
    tt=sum(1 for a,val in history if a[0]=='T')
    assert price==rr+2*tt
    root_queries+=rr
    terminal_queries+=tt
    hist[(rr,tt)]+=1
    if leaf in observed_paths: assert observed_paths[leaf]==history
    else:observed_paths[leaf]=history
assert len(observed_paths)==112
assert (root_queries,terminal_queries)==(C['mixed_root_weighted_queries'],C['mixed_terminal_weighted_queries'])==(762,44)
assert sum(hist.values())==242
from fractions import Fraction
assert Fraction(44,79)<Fraction(199,254)
for r in (Fraction(3,5),Fraction(2,3),Fraction(3,4)):
    mixed=762*r+44
    assert mixed<841*r and mixed<641
print("EC49FPT_INDEPENDENT_FULL_REPLAY_PASS",root_queries,terminal_queries,sorted(hist.items()))
