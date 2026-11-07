#!/usr/bin/env python3
"""EC49EP: complete H=4 3-resource Pareto frontier under native X6 + symbolic BRC.

Mathematics: returns +2E1, terminal nine-by-five observer, h2/h3/h4.
All decisions are exact. The finite field P=1_000_003 is rank-faithful for 9-by-9
0/1 minors (Hadamard bound 3**9 < P). Dynamic programming is a complete
weighted-prefix-trie search over all observer-signature subsets.
"""
from collections import defaultdict
from itertools import combinations, product
import json

OPS={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
     'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
ATOMS=(('N',0),('N',1),('N',2),('A',0),('A',2),('B',0),('B',1),('AB',0),('BA',0))
BUCKETS=('N','A','B','AB','BA')
PRIME=1000003

def native(w): return tuple(k for ch in w for k in OPS[ch])
def displacement(w):
    p=native(w)
    return tuple(p.count(i)-p.count(-i) for i in range(1,7))
def count_positive(w):
    p=native(w)
    return tuple(p.count(i) for i in range(1,7))
def transfer(w):
    path=native(w); out=[]
    for state,last in ATOMS:
        for k in path:
            if last==1 and k==2: state={'N':'A','B':'BA'}.get(state,state)
            if last==2 and k==1: state={'N':'B','A':'AB'}.get(state,state)
            last=k
        out.append(BUCKETS.index(state))
    return tuple(out)
def rank(sigs):
    piv={};r=0
    for tr in sigs:
        for b in range(5):
            v=[int(k==b) for k in tr]
            for row in range(9):
                if v[row]==0:continue
                if row in piv:
                    factor=v[row]
                    for j in range(row,9):v[j]=(v[j]-factor*piv[row][j])%PRIME
                else:
                    inv=pow(v[row],-1,PRIME)
                    piv[row]=[(t*inv)%PRIME for t in v]
                    r+=1; break
    return r

def prefixes(ws):
    return {p[:j] for w in ws for p in [native(w)] for j in range(1,len(p)+1)}

def groups(words):
    gs=defaultdict(list)
    for w in words:gs[transfer(w)].append(w)
    return dict(gs)

def minimal_signature_sets(signatures):
    sig=list(signatures)
    for k in range(1,len(sig)+1):
        for c in combinations(range(len(sig)),k):
            ss=[sig[i] for i in c]
            if rank(ss)==9 and all(rank(ss[:j]+ss[j+1:])!=9 for j in range(len(ss))):
                yield tuple(ss)

def horizon_options(h,p,fibers):
    gs=groups(fibers[h][p]); mins=list(minimal_signature_sets(gs))
    for sig in mins:
        for words in product(*(gs[t] for t in sig)):
            yield words

class Trie:
    def __init__(self): self.child={};self.words=[]

def make_trie(words):
    root=Trie()
    for w in words:
        t=root
        for d in native(w):t=t.child.setdefault(d,Trie())
        t.words.append(w)
    return root

def optimal_h4_signature_mask(trie,already_paid,signature_order):
    """All exact minima by selected h4 transfer-signature mask.

    DP invariant: dp_node(prefix)[mask] is smallest *unpaid* native-edge cost
    of any descendant words whose union of signature labels is exactly mask.
    Every child branch is independent except for OR-ing masks, and every
    newly used edge has weight 0 iff already present in earlier horizons.
    """
    sigbits={sig:1<<i for i,sig in enumerate(signature_order)}
    def f(node,prefix):
        dp={0:(0,())}
        for w in node.words:
            m=sigbits[transfer(w)]
            if m not in dp:dp[m]=(0,(w,))
        for step,child in node.child.items():
            newprefix=prefix+(step,)
            childdp=f(child,newprefix)
            result={}
            for m1,(c1,w1) in dp.items():
                for m2,(c2,w2) in childdp.items():
                    mask=m1|m2
                    cost=c1+c2+(int(newprefix not in already_paid) if m2 else 0)
                    if mask not in result or cost<result[mask][0]:
                        result[mask]=(cost,w1+w2)
            dp=result
        return dp
    return f(trie,())

def masks_to_sets(signatures):
    n=len(signatures)
    return {mask:tuple(signatures[i] for i in range(n) if mask>>i&1)
            for mask in range(1,1<<n)}

def solve():
    words_by_h={h:[] for h in (2,3,4)}
    fibers={h:defaultdict(list) for h in (2,3,4)}
    for h in (2,3,4):
        for chars in product(OPS,repeat=h):
            w=''.join(chars)
            if displacement(w)==(2,0,0,0,0,0):
                words_by_h[h].append(w)
                fibers[h][count_positive(w)].append(w)
    assert tuple(len(words_by_h[h]) for h in (2,3,4))==(8,51,304)
    base=('ce','de','ec','ed'); p0=count_positive('ce')
    assert len(prefixes(base))==28 and rank(transfer(w) for w in base)==9
    assert len({count_positive(w) for w in base})==1
    assert not any(count_positive(w)==p0 for w in words_by_h[4])
    # At h2 the unique rank-9 same-p fiber is forced (exact 255 subset check).
    valid_base=[]
    for mask in range(1,1<<len(words_by_h[2])):
        ws=tuple(w for j,w in enumerate(words_by_h[2]) if mask>>j&1)
        if len({count_positive(w) for w in ws})==1 and rank(transfer(w) for w in ws)==9:
            valid_base.append(ws)
    assert valid_base and all(set(base).issubset(ws) for ws in valid_base)
    # Exhaustive full-H4 domain: choose exactly one full-rank p fiber at h3
    # and exactly one at h4. Any solution contains a minimal rank-nine subset
    # of transfer signatures at h3, with one primitive word per signature.
    # Removing other words never increases E, M, or S. At h4, the weighted
    # signed-primitive trie DP considers every exact signature mask.
    full4=[p for p,ws in fibers[4].items() if rank(transfer(w) for w in ws)==9]
    full3=[p for p,ws in fibers[3].items() if rank(transfer(w) for w in ws)==9]
    case_list=[(('A' if p3==p0 else 'B' if p3==p4 else 'C'),p3,p4)
               for p3 in sorted(full3) for p4 in sorted(full4)]
    per_case=[]; best_by_s={}; best_by_ms={}; total_h3=0; all_dp=0; num_m2=0; num_m3=0
    base_sigs={transfer(w) for w in base}
    # Reuse the sorted h3 representative choices, h4 signature masks and trie.
    cache3={p:list(horizon_options(3,p,fibers)) for p in full3}
    cache4={}
    for p in full4:
        gs4=groups(fibers[4][p]);sig4=list(gs4)
        sig_masks=masks_to_sets(sig4)
        full_masks={mask for mask,ss in sig_masks.items() if rank(ss)==9}
        cache4[p]=(sig4,sig_masks,full_masks,make_trie(fibers[4][p]))
    for kind,p3,p4 in case_list:
        sig4,sig_masks,full_masks,trie=cache4[p4]
        best_case_by_s={};tested_h3=0
        M=len({p0,p3,p4})
        assert M in (2,3)
        if M==2:num_m2+=1
        else:num_m3+=1
        for ws3 in cache3[p3]:
            tested_h3+=1; total_h3+=1
            already=prefixes(base+ws3)
            ss0=base_sigs|{transfer(w) for w in ws3}
            h4_dp=optimal_h4_signature_mask(trie,already,sig4)
            all_dp+=1
            for mask in full_masks:
                if mask not in h4_dp:continue
                delta,ws4=h4_dp[mask]
                E=len(already)+delta
                S=len(ss0|set(sig_masks[mask]))
                record={'E':E,'M':M,'S':S,'kind':kind,'p3':p3,'p4':p4,'h3':ws3,'h4':ws4,
                    'prefix_2':28,'prefix_23':len(already),'prefix_234':E}
                if S not in best_case_by_s or E<best_case_by_s[S]['E']:
                    best_case_by_s[S]=record
                if (M,S) not in best_by_ms or E<best_by_ms[M,S]['E']:
                    best_by_ms[M,S]=record
                if M==2 and (S not in best_by_s or E<best_by_s[S]['E']):
                    best_by_s[S]=record
        assert tested_h3>0
        per_case.append({'case':kind,'M':M,'p3':p3[:3],'p4':p4[:3],
                         'h3_representative_combinations':tested_h3,
                         'h4_signature_types':len(sig4),
                         'best_E_by_S':{str(S):row['E'] for S,row in sorted(best_case_by_s.items())}})
    candidates=list(best_by_ms.values())
    frontier=sorted((r['E'],r['M'],r['S']) for r in candidates if not any(
        (rr['E']<=r['E'] and rr['M']<=r['M'] and rr['S']<=r['S'] and
        (rr['E'],rr['M'],rr['S'])!=(r['E'],r['M'],r['S'])) for rr in candidates))
    assert frontier==[(44,3,4),(46,2,6),(56,2,4)],frontier
    assert {k:v['E'] for k,v in best_by_s.items()}=={4:56,6:46,7:51,8:74,9:78,10:82}
    assert best_by_ms[3,4]['E']==44
    chosen=[]
    for t in frontier:
        r=next(row for row in candidates if (row['E'],row['M'],row['S'])==t)
        w2=base;w3=tuple(r['h3']);w4=tuple(r['h4'])
        assert rank(transfer(w) for w in w2)==rank(transfer(w) for w in w3)==rank(transfer(w) for w in w4)==9
        for ww in (w2,w3,w4):
            assert all(displacement(w)==(2,0,0,0,0,0) for w in ww)
            assert len({count_positive(w) for w in ww})==1
        assert (len(prefixes(w2+w3+w4)),len({count_positive(w) for w in w2+w3+w4}),
                len({transfer(w) for w in w2+w3+w4}))==t
        chosen.append({'E':t[0],'M':t[1],'S':t[2],
                       'words':{'2':w2,'3':w3,'4':w4},
                       'p':{str(h):count_positive(ww[0]) for h,ww in ((2,w2),(3,w3),(4,w4))},
                       'rank':{str(h):rank(transfer(w) for w in ww) for h,ww in ((2,w2),(3,w3),(4,w4))},
                       'edges_by_h':{str(h):len(prefixes(tuple(w for k,ws in ((2,w2),(3,w3),(4,w4)) for w in ws if k<=h))) for h in (2,3,4)}})
    # EC49EM nested h>=3 edge-optimal pair, now with exact M/S resource accounting.
    # We check a finite range; the all-H statement rests on the explicit
    # prefix-nesting and first-positive-event argument in README_EC49EP.md.
    multih=[]
    for H in (3,4,5,6,8,16,32,64):
        horizon_groups=[base]+[('fe'+'g'+'f'*(h-3),'ge'+'f'+'f'*(h-3)) for h in range(3,H+1)]
        words=tuple(w for g in horizon_groups for w in g)
        assert all(rank(transfer(w) for w in g)==9 for g in horizon_groups)
        assert all(len({count_positive(w) for w in g})==1 for g in horizon_groups)
        assert all(displacement(w)==(2,0,0,0,0,0) for w in words)
        triple=(len(prefixes(words)),len({count_positive(w) for w in words}),len({transfer(w) for w in words}))
        assert triple==(4*H+30,H-2,6), (H,triple)
        multih.append({'H':H,'E':triple[0],'M':triple[1],'S':triple[2]})
    return {
        'all_H_nested_family':'F_h=feg f^(h-3), G_h=gef f^(h-3) for h>=3; h2=ce,de,ec,ed',
        'all_H_resource_formula':'(E,M,S)=(4H+30,H-2,6), H>=3',
        'nested_family_finite_checks':multih,
        'unit':'EC49EP','status':'PASS','scope':'H=4 complete exact Pareto for native X6 positive-BRC symbolic p and nine-history observer',
        'source_model':'EC49EO frozen scientific inputs; current rules separately read',
        'complete_return_word_count':{str(h):len(words_by_h[h]) for h in (2,3,4)},
        'full_rank_fiber_count':{'2':1,'3':len(full3),'4':len(full4)},
        'mandatory_base':base,'base_prefix_edges':28,'base_p':p0,
        'h4_p0_available':False,
        'M2_scenario_case_count':num_m2,'M3_scenario_case_count':num_m3,
        'all_scenario_case_count':len(case_list),'h3_representative_combinations_checked':total_h3,
        'weighted_prefix_trie_dp_runs':all_dp,
        'all_H4_case_minima':per_case,
        'all_best_E_by_M_S':{f'{m}:{s}':r['E'] for (m,s),r in sorted(best_by_ms.items())},
        'M2_best_E_by_S':{str(s):r['E'] for s,r in sorted(best_by_s.items())},
        'full_H4_Pareto_EMS':frontier,'Pareto_witnesses':chosen,
        'modular_prime':PRIME,'hadamard_bound_9by9':3**9,
        'proof_scope':'Finite complete enumeration h2,h3,h4, full-rank signature minimality, exact native trie DP; all 36 cross-fiber combinations checked for M=2 or M=3, including E_min=44.',
        'next_question':'EC49EQ: H=5 three-resource frontier; first test H5 with M=2 or M=3 via signature-mask trie DP and cross-horizon key-cover states.'}

if __name__=='__main__':
    print(json.dumps(solve(),ensure_ascii=False,indent=2))