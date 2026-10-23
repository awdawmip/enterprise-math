#!/usr/bin/env python3
"""PREFIX-108: complete exact local a=3 terminal-port enumeration.

Witness controls re-check earlier a=0 and a=1 32-state graphs. This program
never searches all 31-state graphs. Global a=3 bound additionally depends on
the explicit shell/alias lemma proved in PREFIX108 Markdown.
"""
from collections import Counter, defaultdict
from itertools import combinations_with_replacement, product
from pathlib import Path
from hashlib import sha256
import json

HERE = Path(__file__).resolve().parent
ROOTS = ('s0','s1','s3','t0','t1','t3')
COUNTS = {'s0':3,'s1':13,'s3':16,'t0':3,'t1':13,'t3':16}
PORTS = tuple((label,kind) for label in (0,1) for kind in ('Z','O','I','U'))
PAIRS = tuple(combinations_with_replacement(PORTS,2))
HIST_PRE = [{0:1},{0:2},{0:4},{0:4,1:4},{0:8,2:8},
            {0:3,1:13,3:16},{0:1,1:6,2:25,4:32}]
TAIL = {'s':{0:1,2:55,5:64},'t':{1:14,3:50,4:56}}
TYPES = {'Z':{0:1},'O':{0:2},'I':{1:2},'U':{1:1}}

def name(p): return ','.join(str(lbl)+kind for lbl,kind in p)

def demanded(b):
    assert b in (0,1)
    return {
      's0':Counter({(0,'Z'):1,(1,'I'):2+b,(1,'U'):3-b}),
      's1':Counter({(0,'I'):1-b,(0,'U'):b,(1,'O'):21,(1,'Z'):4}),
      's3':Counter({(1,'I'):32}),
      't0':Counter({(0,'I'):1,(1,'O'):5}),
      't1':Counter({(0,'O'):1,(1,'I'):25}),
      't3':Counter({(1,'O'):24,(1,'Z'):8}),
    }

def fiber_solutions(need,rows):
    """Enumerate *all* nonnegative integer combinations of full two-outedge signatures."""
    avail=[pair for pair in PAIRS if Counter(pair)<=need]
    solutions=[]
    def go(i,left,n,found):
        if i==len(avail):
            if not n and not +left: solutions.append(dict(found))
            return
        p=avail[i]; pc=Counter(p)
        upper=min([n]+[left[k]//v for k,v in pc.items()])
        for m in range(upper+1):
            nleft=left.copy()
            for k,v in pc.items():nleft[k]-=m*v
            if m:found[p]=m
            go(i+1,nleft,n-m,found)
            if m:del found[p]
    go(0,need.copy(),rows,{})
    return solutions

def future_signature(pair):
    h1=Counter(label for label,_ in pair)
    h2=Counter()
    for label,kind in pair:
        for score,m in TYPES[kind].items():h2[score+label]+=m
    return (tuple(sorted(h1.items())),tuple(sorted(h2.items())))

def classify(b):
    need=demanded(b)
    all_fiber={key:fiber_solutions(need[key],COUNTS[key]) for key in ROOTS}
    assert all(all_fiber.values())
    groups=defaultdict(list)
    for selected in product(*(all_fiber[k] for k in ROOTS)):
        palette=tuple(sorted(set().union(*(v.keys() for v in selected)),key=name))
        rows={r:{name(k):v for k,v in sorted(x.items(),key=lambda x:name(x[0]))}
              for r,x in zip(ROOTS,selected)}
        groups[palette].append(rows)
    size_dist=Counter(); signatures=[]
    for palette,allocs in groups.items():
        size_dist[len(palette)]+=len(allocs)
        if len(palette)==7:
            assert len(allocs)==1
            assert len({future_signature(p) for p in palette})==7
            signatures.append({'b':b,'palette':[name(p) for p in palette],
                'rows':allocs[0], 'X_alias':('1Z,1Z' in [name(p) for p in palette])})
    signatures.sort(key=lambda x:x['palette'])
    return {'b':b,'total_allocations':sum(size_dist.values()),
      'fiber_solution_counts':{k:len(all_fiber[k]) for k in ROOTS},
      'palette_size_distribution':dict(sorted(size_dist.items())),
      'minimum_fifth_palette_size':min(size_dist),
      'seven_signature_allocations':signatures}

def hist_chain(edges,root,n):
    curr=Counter({(root,0):1});out=[]
    for _ in range(n+1):
        h=Counter()
        for (u,s),m in curr.items():h[s]+=m
        out.append(dict(sorted(h.items())))
        nxt=Counter()
        for (u,s),m in curr.items():
            for label,v in edges[u]:nxt[(v,s+label)]+=m
        curr=nxt
    return out

def witness_control(fname, expected_a):
    raw=(HERE/fname).read_bytes();m=json.loads(raw); edges=m['edges']
    assert len(edges)==m['states']==32
    assert sum(len(x) for x in edges)==m['edge_occurrences']
    assert all(1<=len(x)<=2 for x in edges)
    initial=m['initial_states']
    for r,u in initial.items():
        h=hist_chain(edges,u,17)
        assert h[:7]==HIST_PRE
        assert all(x==TAIL[r] for x in h[7:])
    sr=[hist_chain(edges,u,8) for u in range(32)]
    assert all(x[7]==x[8] for x in sr)
    assert len({tuple(tuple(sorted(y.items())) for y in x[:8]) for x in sr})==32
    seen=set();now=set(initial.values())
    for _ in range(30):
        seen|=now;now={v for u in now for _,v in edges[u]}
    assert seen==set(range(32))
    pathmass=Counter({(initial['s'],0):1})
    for _ in range(6):
        following=Counter()
        for (u,k),mass in pathmass.items():
            for label,v in edges[u]:following[(v,k+label)]+=mass
        pathmass=following
    a=sum(mass for (u,k),mass in pathmass.items()
          if k==1 and len(edges[u])==1 and edges[u][0][0]==1)
    assert a==expected_a
    return {'filename':fname,'sha256':sha256(raw).hexdigest(),
      'N':32,'E':m['edge_occurrences'],'a':a,
      'root_hist_depth_0_17':'PASS','all_states_R7_eq_R8':'PASS',
      'future_class_count':32,'all_reachable':'PASS'}

def check_terminal_flow():
    d=demanded(0)
    # The full typed sixth-layer masses are independent of b.
    sixth={
      's':{'Z':{0:1,2:4},'O':{2:21},'I':{1:3,4:32},'U':{1:3}},
      't':{'Z':{4:8},'O':{1:6,4:24},'I':{0:1,2:25},'U':{}}
    }
    for r,by_type in sixth.items():
        depth6=Counter();depth7=Counter()
        for kind,by_score in by_type.items():
            for k,m in by_score.items():
                depth6[k]+=m
                for lbl,v in TYPES[kind].items():depth7[k+lbl]+=m*v
        assert dict(sorted(depth6.items()))==HIST_PRE[6]
        assert dict(sorted(depth7.items()))==TAIL[r]
    for b in (0,1):
        dem=demanded(b)
        for r in ROOTS:
            assert sum(dem[r].values())==2*COUNTS[r]
        # Exact flow into score 1 (root s) and into score 2.
        assert dem['s0'][(1,'I')]+dem['s1'][(0,'I')]==3
        assert dem['s0'][(1,'U')]+dem['s1'][(0,'U')]==3
    return sixth

def main():
    assert len(PAIRS)==36
    sixth=check_terminal_flow()
    regimes=[classify(0),classify(1)]
    assert regimes[0]['minimum_fifth_palette_size']==7
    assert regimes[1]['minimum_fifth_palette_size']==8
    seven=regimes[0]['seven_signature_allocations']+regimes[1]['seven_signature_allocations']
    assert len(seven)==4
    xs=[x for x in seven if x['X_alias']]
    assert len(xs)==2 and all(x['b']==0 for x in xs)
    for x in seven:
        assert x['rows']['t0']=={'0I,1O':1,'1O,1O':2}
        assert x['rows']['t1']=={'0O,1I':1,'1I,1I':12}
        assert x['rows']['s3']=={'1I,1I':16}
        if x['X_alias']:
            assert x['rows']['t3']=={'1O,1O':12,'1Z,1Z':4}
            assert x['rows']['s1']=={'0I,1O':1,'1O,1O':10,'1Z,1Z':2}
        else:
            assert x['rows']['t3']=={'1O,1O':8,'1Z,1O':8}
            assert x['rows']['s1']=={'0I,1O':1,'1O,1O':8,'1Z,1O':4}
    controls=[witness_control('witness_32_states_63_edges.json',0),
              witness_control('witness_a1_32_states_62_edges.json',1)]
    certificate={
      'schema':'PREFIX108_A3_EXACT_36_TWO_PORT_TYPED_FLOW_V1',
      'status':'LOCAL_EXACT_PROOF_DRAFT_AND_INTEGER_ENUMERATION_PASS_UNREVIEWED',
      'scope':'auxiliary positive unit weight two-root 0/1 BRC; not native X6',
      'terminal_residual':3,'sixth_typed_masses':sixth,
      'actual_terminal_port_kinds':len(PORTS),'unordered_two_edge_port_signatures':len(PAIRS),
      'b_regimes':regimes,'seven_signature_count':len(seven),
      'seven_signature_X_cases':len(xs),
      'conditional_state_bound':'Assuming the proved combinatorial shell/alias lemma N>=20+|V4|+|V5|-e45-e56 with 0<=e45<=e56<=1, then a=3 => N>=32. No 32-state a3 witness constructed.',
      'legacy_witness_regression':controls,
      'explicitly_not_claimed':['global N>=32 for a=4,5,6','a3 is realizable at N32','full-graph 31-state SAT UNSAT','independent mathematical admission','P000 native X6 transfer'],
      'verifier_sha256':sha256(Path(__file__).read_bytes()).hexdigest()
    }
    out=HERE/'certificate_prefix108.json';out.write_text(json.dumps(certificate,indent=2,ensure_ascii=False,sort_keys=True)+'\n')
    print('PREFIX108 A3 36-SIGNATURE ENUMERATION: EXACT PASS')
    print('palette sizes', [r['palette_size_distribution'] for r in regimes]);
    print('seven-signature allocations',len(seven),'X cases',len(xs),
          'legacy controls',[(q['N'],q['E'],q['a']) for q in controls]);
if __name__=='__main__':main()
