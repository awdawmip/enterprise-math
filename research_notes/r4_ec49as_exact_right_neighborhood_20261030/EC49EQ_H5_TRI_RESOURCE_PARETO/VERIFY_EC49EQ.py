#!/usr/bin/env python3
"""EC49EQ: exact H=5 native X6 / positive-BRC triple Pareto certificate.
Self-contained standard-library program. The 281 relevant fiber assignments are
covered by a complete integer OR-mask dynamic program on native-prefix trees.
No LP, floating-point, heuristic pruning, or untyped BRC replacement is used.
"""
import json
from itertools import product
from collections import defaultdict
from fractions import Fraction

OPS={'a':(-1,-1), 'b':(-2,-2), 'c':(1,2,-1,-2), 'd':(2,1,-2,-1),
     'e':(3,1,1,-3), 'f':(1,-1), 'g':(2,-2)}
STATES=(('N',0),('N',1),('N',2),('A',0),('A',2),('B',0),('B',1),('AB',0),('BA',0))
BUCKETS=('N','A','B','AB','BA')
PRIME=1_000_003
BASE=('ce','de','ec','ed')

def path(word):
    return tuple(step for op in word for step in OPS[op])

def displacement(word):
    p=path(word)
    return tuple(p.count(i)-p.count(-i) for i in range(1,7))

def poscount(word):
    p=path(word)
    return tuple(p.count(i) for i in range(1,7))

def signature(word):
    result=[]
    for event,previous in STATES:
        for step in path(word):
            if previous==1 and step==2:
                event={'N':'A','B':'BA'}.get(event,event)
            elif previous==2 and step==1:
                event={'N':'B','A':'AB'}.get(event,event)
            previous=step
        result.append(BUCKETS.index(event))
    return tuple(result)

def rank_mod(signatures):
    pivots={};r=0
    for tr in signatures:
        for bucket in range(5):
            vec=[int(t==bucket) for t in tr]
            for i in range(9):
                if not vec[i]:continue
                if i in pivots:
                    fac=vec[i]
                    for j in range(i,9):vec[j]=(vec[j]-fac*pivots[i][j])%PRIME
                else:
                    inv=pow(vec[i],-1,PRIME)
                    pivots[i]=[(v*inv)%PRIME for v in vec]
                    r+=1
                    break
    return r

def rank_rational(signatures):
    cols=[]
    for tr in signatures:
        for bucket in range(5):cols.append([Fraction(int(v==bucket)) for v in tr])
    mat=[[c[i] for c in cols] for i in range(9)]
    row=0
    for j in range(len(cols)):
        pivot=next((i for i in range(row,9) if mat[i][j]),None)
        if pivot is None:continue
        mat[row],mat[pivot]=mat[pivot],mat[row]
        v=mat[row][j]
        mat[row]=[x/v for x in mat[row]]
        for i in range(9):
            if i!=row and mat[i][j]:
                factor=mat[i][j]
                mat[i]=[x-factor*y for x,y in zip(mat[i],mat[row])]
        row+=1
        if row==9:break
    return row

def prefixes(words):
    return {p[:k] for w in words for p in [path(w)] for k in range(1,len(p)+1)}

PAID_BASE=prefixes(BASE)

def all_fibers():
    fs={}
    for h in (2,3,4,5):
        d=defaultdict(list)
        for letters in product(OPS,repeat=h):
            w=''.join(letters)
            if displacement(w)==(2,0,0,0,0,0):d[poscount(w)].append(w)
        fs[h]=dict(d)
    return fs

def essential_signatures(words):
    sig=sorted({signature(w) for w in words})
    n=len(sig)
    ranks=[rank_mod(sig[i] for i in range(n) if mask>>i&1) for mask in range(1<<n)]
    if ranks[-1]!=9:return None
    good=[m for m,r in enumerate(ranks) if r==9]
    minimal=[m for m in good if all(ranks[m & ~(1<<i)]<9 for i in range(n) if m>>i&1)]
    assert len(minimal)==1,(len(sig),minimal)
    return frozenset(sig[i] for i in range(n) if minimal[0]>>i&1)

class Node:
    __slots__=('children','terminal')
    def __init__(self):self.children={};self.terminal=0

def trie_optimal(fibers, p3,p4,p5):
    root=Node();required={};color_index={}
    for h,p in ((3,p3),(4,p4),(5,p5)):
        words=fibers[h][p]
        necessary=essential_signatures(words)
        assert necessary and len(necessary) in (2,4)
        required[h]=necessary
        for tr in sorted(necessary):
            color_index[(h,tr)]=len(color_index)
        for w in words:
            tr=signature(w)
            if tr not in necessary:continue
            node=root
            for step in path(w):node=node.children.setdefault(step,Node())
            node.terminal |= 1<<color_index[(h,tr)]
    visited=0;maxstate=0
    def solve_node(node,prefix):
        nonlocal visited,maxstate
        visited+=1
        curr={0:0}
        for step,child in node.children.items():
            sub=solve_node(child,prefix+(step,))
            merged={}
            for m1,c1 in curr.items():
                for m2,c2 in sub.items():
                    key=m1|m2;cost=c1+c2
                    if key not in merged or cost<merged[key]:merged[key]=cost
            curr=merged
        if prefix:
            cost=int(prefix not in PAID_BASE)
            selected={0:0}
            for mask,value in curr.items():
                if mask or node.terminal:
                    key=mask|node.terminal
                    price=value+cost
                    if key not in selected or price<selected[key]:selected[key]=price
            curr=selected
        maxstate=max(maxstate,len(curr))
        return curr
    dp=solve_node(root,())
    full=(1<<len(color_index))-1
    assert full in dp
    return len(PAID_BASE)+dp[full], {'color_groups':len(color_index),'nodes':visited,'max_dp_states':maxstate,'root_states':len(dp)}

WITNESSES={
  '50,3,6':{'2':BASE,'3':('feg','gef'),'4':('fegf','geff'),'5':('fegff','gefff')},
  '52,4,4':{'2':BASE,'3':('cef','def','ecf','edf'),'4':('ceff','deff','ecff','edff'),'5':('cefff','defff','ecfff','edfff')},
  '64,2,6':{'2':BASE,'3':('fge','gfe'),'4':('ecgf','fgec','fged','gfed'),'5':('fgefg','gfegf')},
  '64,3,4':{'2':BASE,'3':('cec','ded','ecc','edd'),'4':('cefg','degf','ecfg','edgf'),'5':('cefgf','degff','ecfgf','edgff')},
}

def validate_witnesses():
    out={}
    for name,groups in WITNESSES.items():
        allwords=[w for ws in groups.values() for w in ws]
        triple=(len(prefixes(allwords)),len({poscount(w) for w in allwords}),len({signature(w) for w in allwords}))
        assert tuple(map(int,name.split(',')))==triple,(name,triple)
        checks={}
        for h,ws in groups.items():
            assert all(displacement(w)==(2,0,0,0,0,0) for w in ws)
            assert len({poscount(w) for w in ws})==1
            assert rank_mod({signature(w) for w in ws})==9
            assert rank_rational({signature(w) for w in ws})==9
            checks[h]={'p':poscount(ws[0]),'rank_Q':9,'words':ws}
        out[name]=checks
    return out

def run():
    fs=all_fibers()
    sizes={h:sum(map(len,fs[h].values())) for h in fs}
    assert tuple(sizes[h] for h in (2,3,4,5))==(8,51,304,1770)
    full={h:{p:words for p,words in fs[h].items() if essential_signatures(words)} for h in fs}
    assert [len(full[h]) for h in (2,3,4,5)]==[1,4,9,17]
    p0=poscount('ce')
    assert len(PAID_BASE)==28
    assert set(full[2])=={p0}
    positive={h:[p for p,ws in full[h].items() if len(essential_signatures(ws))==4] for h in (3,4,5)}
    assert [len(positive[h]) for h in (3,4,5)]==[3,7,13]
    base_sigs={signature(w) for w in BASE}
    q0_signature_sets=set()
    for h,fs_h in full.items():
        for p,words in fs_h.items():
            sig=essential_signatures(words)
            if len(sig)==4:assert sig==base_sigs
            else:
                assert len(sig)==2 and not sig&base_sigs
                q0_signature_sets.add(tuple(sorted(sig)))
    assert len(q0_signature_sets)==1
    # Every H=5 cache-minimal solution has p4=p5=p, because p0 is absent at h4/h5.
    common=sorted(set(full[4])&set(full[5]))
    m2=[(p0,p,p) for p in common]
    m2.extend((p,p,p) for p in common if p in full[3])
    assert len(m2)==8
    rows=[]
    for p3,p4,p5 in m2:
        E,info=trie_optimal(fs,p3,p4,p5)
        rows.append({'M':2,'S':6,'p':[list(p[:3]) for p in (p3,p4,p5)],'E':E,'dp':info})
    for p3 in positive[3]:
        for p4 in positive[4]:
            for p5 in positive[5]:
                M=len({p0,p3,p4,p5})
                assert M in (3,4)
                E,info=trie_optimal(fs,p3,p4,p5)
                rows.append({'M':M,'S':4,'p':[list(p[:3]) for p in (p3,p4,p5)],'E':E,'dp':info})
    stats={}
    for r in rows:
        key=f"M{r['M']}_S{r['S']}"
        if key not in stats:stats[key]={'cases':0,'min_E':r['E'],'p_at_min':r['p']}
        stats[key]['cases']+=1
        if r['E']<stats[key]['min_E']:
            stats[key].update(min_E=r['E'],p_at_min=r['p'])
    assert {k:v['min_E'] for k,v in stats.items()}=={'M2_S6':64,'M3_S4':64,'M4_S4':52}
    assert len(rows)==281
    witnesses=validate_witnesses()
    return {'unit':'EC49EQ','status':'PASS','model':'native ordered signed six-axis operations, two positive BRC symbolic channels, 9x5 event observer',
        'horizon_range':'2..5','word_counts':{str(h):sizes[h] for h in sizes},
        'full_rank_fibers':{str(h):len(full[h]) for h in full},'h3_h4_h5_q_positive_fibers':[3,7,13],
        'exhaustive_case_count':281,'case_classes':stats,'case_results':rows,
        'witnesses':witnesses,'complete_pareto':[[50,3,6],[52,4,4],[64,2,6],[64,3,4]],
        'rank_method':f'mod P={PRIME}, 3**9={3**9}<P (9x9 binary minor); witness ranks also checked over Q with Fraction',
        'proof_basis':'Unique minimal full-rank essential signature set in every p fiber; native-prefix-trie OR-mask complete integer DP with already-paid H2 28 edges. S=4 iff all selected fibers are q-positive; S=6 iff any selected fiber is q-zero. M>=2. E>=50 from EC49EM and attaining EC49EP family.',
        'next':'EC49ER: H=6 three-resource frontier, starting M=2 existence and S=4 Pareto with exact trie DP; cost accounting vs input/output resources.'}

if __name__=='__main__':
    result=run()
    with open('EC49EQ_EXECUTED.json','w',encoding='utf-8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
    print(json.dumps({'status':result['status'],'cases':result['exhaustive_case_count'],'classes':result['case_classes'],'frontier':result['complete_pareto']},ensure_ascii=False,indent=2))
