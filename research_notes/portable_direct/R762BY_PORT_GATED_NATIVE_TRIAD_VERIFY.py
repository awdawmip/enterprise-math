#!/usr/bin/env python3
"""Exact integer BRC branch enumeration for conditional signed-X6 Port triads.

Counts are typed history-multiplicity pushforwards, not physical amplitudes.
The native TRIADIC_CLOSURE_E event predicate remains unlicensed/open.
"""
from collections import defaultdict
from itertools import permutations, product
import json
import sys

AXES=tuple(range(1,7))
F0=(1,2,3)
FRAMES=tuple(permutations(AXES,3))
SIGNS=tuple(product((-1,1),repeat=3))

def successors(f,J):
    for slot in J:
        x=f[slot]
        for y in AXES:
            if y not in f:
                yield f[:slot]+(y,)+f[slot+1:],x,y,slot

def pushforward(J,horizon=8):
    cur={F0:1}
    out=[]
    for m in range(horizon+1):
        end={''.join(map(str,f)):n for f,n in sorted(cur.items()) if set(f)==set(F0)}
        out.append(dict(m=m,path_mass=sum(cur.values()),based_return_mass=sum(end.values()),
                        terminal_holonomy_count=len(end),terminal_distribution=end))
        nxt=defaultdict(int)
        for f,n in cur.items():
            for g,x,y,slot in successors(f,J):nxt[g]+=n
        cur=nxt
    return out

def witnesses(J,lengths=(3,4,5)):
    cur={F0:(F0,)}
    out={}
    for m in range(1,max(lengths)+1):
        nxt={}
        for f,path in cur.items():
            for g,_,_,_ in successors(f,J):
                if g not in nxt:nxt[g]=path+(g,)
        cur=nxt
        if m in lengths:
            out[str(m)]={''.join(map(str,f)):[''.join(map(str,g)) for g in path]
                         for f,path in sorted(cur.items()) if set(f)==set(F0)}
    return out

def covariance_check():
    n=0
    for perm_tuple in permutations(AXES):
        perm=dict(zip(AXES,perm_tuple))
        for f in FRAMES:
            pf=tuple(perm[a] for a in f)
            for k in range(4):
                J=tuple(range(k))
                transported={(tuple(perm[a] for a in g),perm[x],perm[y],slot)
                             for g,x,y,slot in successors(f,J)}
                actual=set(successors(pf,J))
                assert transported==actual
                n+=len(transported)
    return n

def rotation_check():
    out={}
    for k in range(4):
        J=tuple(range(k))
        ok=True
        for f in FRAMES:
            rf=(f[1],f[2],f[0])
            transported={((g[1],g[2],g[0]),(slot-1)%3)
                         for g,_,_,slot in successors(f,J)}
            actual={(g,slot) for g,_,_,slot in successors(rf,J)}
            if transported!=actual:
                ok=False
                break
        out[str(k)]=ok
    assert out=={'0':True,'1':False,'2':False,'3':True}
    return out

def main():
    assert len(FRAMES)==120 and len(SIGNS)==8
    states=[(f,s) for f in FRAMES for s in SIGNS]
    assert len(states)==960
    rows={}
    for k in range(4):
        degrees={len(list(successors(f,tuple(range(k))))) for f,s in states}
        assert degrees=={3*k}
        rows[str(k)]={'signed_states':960,'outgoing_per_state':3*k,
                      'directed_edges':960*3*k}
    comparison_count=covariance_check()
    assert comparison_count==1555200
    rotation=rotation_check()
    tables={}
    witness={}
    for k in range(4):
        table=pushforward(tuple(range(k)))
        for rec in table:
            expected=(3*k)**rec['m'] if k else (1 if rec['m']==0 else 0)
            assert rec['path_mass']==expected
            assert rec['based_return_mass']==sum(rec['terminal_distribution'].values())
        tables[str(k)]=table
        witness[str(k)]=witnesses(tuple(range(k)))
    assert [x['based_return_mass'] for x in tables['0']]==[1,0,0,0,0,0,0,0,0]
    assert [x['based_return_mass'] for x in tables['1']]==[1,0,3,6,21,60,183,546,1641]
    assert [x['based_return_mass'] for x in tables['2']]==[1,0,6,18,138,762,4698,27930,168090]
    assert [x['based_return_mass'] for x in tables['3']]==[1,0,9,36,369,2952,26937,239148,2155617]
    assert [x['terminal_holonomy_count'] for x in tables['3']]==[1,0,1,4,6,6,6,6,6]
    assert [x['terminal_holonomy_count'] for x in tables['2']]==[1,0,1,2,2,2,2,2,2]
    assert [x['terminal_holonomy_count'] for x in tables['1']]==[1,0,1,1,1,1,1,1,1]
    assert all(x['based_return_mass']==(3**x['m']+3*(-1)**x['m'])//4
               for x in tables['1'])
    assert set(witness['3']['4'])=={'123','132','213','231','312','321'}
    assert set(witness['3']['5'])=={'123','132','213','231','312','321'}
    assert set(witness['2']['3'])=={'123','213'}
    assert set(witness['2']['4'])=={'123','213'}
    for f,s in states:
        for g,x,y,i in successors(f,(0,1,2)):
            assert s[i] in (-1,1) and len(set(g))==3
            assert sum(a!=b for a,b in zip(f,g))==1
            assert f[i]==x and g[i]==y and y not in f
    evidence={
       'schema':'ENTERPRISE_MATH_R762BY_PORT_GATED_SIGNED_TRIAD_V1',
       'status':'AUTHOR_EXACT_CHECK_NOT_INDEPENDENTLY_REVIEWED',
       'model':'conditional stationary signed-X6 Cell/Port triad; static eligible Port subset J, q>0',
       'native_event_permission':'NOT_ESTABLISHED',
       'signed_triads_at_fixed_cell_q':960,
       'axis_permutations_checked':720,
       'covariance_transition_comparisons':comparison_count,
       'row_counts':rows,
       'internal_C3_rotation_invariance':rotation,
       'tables':tables,
       'witness_paths':witness,
       'unbounded_holonomy_groups':{'0':'trivial','1':'trivial','2':'S2','3':'S3'},
       'unbounded_terminal_repair_bits':{'0':0,'1':0,'2':1,'3':3}
    }
    dest=sys.argv[1] if len(sys.argv)>1 else 'R762BY_PORT_GATED_NATIVE_TRIAD_EVIDENCE.json'
    with open(dest,'w',encoding='utf-8') as h:
        json.dump(evidence,h,ensure_ascii=False,indent=2,sort_keys=True)
        h.write('\n')
    print(json.dumps({
        'verified':True,'covariance_comparisons':comparison_count,
        'row_counts':rows,'internal_C3_rotation_invariance':rotation,
        'return_totals':{k:[x['based_return_mass'] for x in t] for k,t in tables.items()},
        'terminal_h_counts':{k:[x['terminal_holonomy_count'] for x in t] for k,t in tables.items()}
    },sort_keys=True))

if __name__=='__main__':main()
