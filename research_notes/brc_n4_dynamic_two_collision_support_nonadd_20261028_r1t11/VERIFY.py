#!/usr/bin/env python3
"""Exact author-side reproduction of a dual-measure depth-4 dynamic fan-in example.
No external dependencies. All numerical quantities are fractions.Fraction.
The two reductions are t2 and t3 (time, P/Q)-signature coupling.
"""
import json
from fractions import Fraction as F
from itertools import product
from collections import defaultdict

# Observable time is a separately typed index 1,2,3,4; tree nodes retain paths.
NODES = {1: {'A': (F(1,2),F(1,2),None), 'B': (F(1,2),F(3,2),None)}, 2:{}}
NODES[2].update({
    'AU': (F(1,6),F(1),'A'), 'AV': (F(1,3),F(1,4),'A'),
    'BU': (F(1,4),F(1),'B'), 'BV': (F(1,4),F(2),'B')})
NODES[3] = {}
T3_RADIUS = {'AU': F(1,10), 'AV': F(0), 'BU': F(4,5), 'BV': F(0)}
for par, (q,r,_) in NODES[2].items():
    for i,sgn in enumerate((-1,1)):
        NODES[3][f'{par}{i}']=(q/2, r*(1+sgn*T3_RADIUS[par]), par)
NODES[4] = {}
T4_RADIUS = {s: (F(0) if s=='AV0' else (F(3,50) if s=='AV1' else F(1,20))) for s in NODES[3]}
for par,(q,r,_) in NODES[3].items():
    for i,sgn in enumerate((-1,1)):
        NODES[4][f'{par}{i}']=(q/2, r*(1+sgn*T4_RADIUS[par]), par)

LAMBDA=(F(100),F(2501,100),F(0),F(1,10))
ACTS='PQC'

def fstr(x):
    return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'

def check_tree():
    for t in NODES:
        assert len(NODES[t])==2**t
        assert all(q>0 and r>0 for q,r,_ in NODES[t].values())
        assert sum(q for q,r,p in NODES[t].values())==1
        assert sum(q*r for q,r,p in NODES[t].values())==1
        if t!=4:
            for name,(q,r,_) in NODES[t].items():
                cs=[(cq,cr) for cq,cr,pa in NODES[t+1].values() if pa==name]
                assert len(cs)==2
                assert sum(cq for cq,cr in cs)==q
                assert sum(cq*cr for cq,cr in cs)==q*r
    assert NODES[2]['AU'][1] == NODES[2]['BU'][1] ==1
    assert NODES[3]['AV0'][1]==NODES[3]['AV1'][1]==F(1,4)
    def next_r(t,n):return tuple(sorted(r for q,r,p in NODES[t+1].values() if p==n))
    assert next_r(2,'AU')==(F(9,10),F(11,10))
    assert next_r(2,'BU')==(F(1,5),F(9,5))
    assert next_r(3,'AV0')==(F(1,4),F(1,4))
    assert next_r(3,'AV1')==(F(47,200),F(53,200))

def cost(t,r,a):
    x,y,u,v=LAMBDA
    assert a in 'PQ'
    return (y if a=='P' else x*r) + t*(u*r+v)

# Grouped minimization: t1 and t2 actions exhaustively chosen; t3 optimal
# per reachable (t,r) equivalence class, which is valid because t4 is terminal
# and carries no further inter-class coupling.
def optimize(couple2,couple3):
    group2={n: ((2,r) if couple2 else n) for n,(q,r,p) in NODES[2].items()}
    group3={n: ((3,r) if couple3 else n) for n,(q,r,p) in NODES[3].items()}
    labels2=list(dict.fromkeys(group2.values()))
    candidates=0
    by_root={}
    best=None; bestpol=None
    terminal_action={n:('P' if cost(4,r,'P')<=cost(4,r,'Q') else 'Q') for n,(q,r,p) in NODES[4].items()}
    c3={}
    for n,(q,r,p) in NODES[3].items():
        c3[n]={'P':cost(3,r,'P'),'Q':cost(3,r,'Q')}
        c3[n]['C']=sum(q4*cost(4,r4,terminal_action[m])/q for m,(q4,r4,par) in NODES[4].items() if par==n)
    for root_actions in product(ACTS,repeat=2):
        racts=dict(zip(NODES[1].keys(),root_actions))
        rootlabel='/'.join(f'{n}:{racts[n]}' for n in ('A','B'))
        rbest=None; rpol=None
        for actions2 in product(ACTS,repeat=len(labels2)):
            candidates+=1
            a2=dict(zip(labels2,actions2))
            total=F(0)
            live_t3=set()
            for n,(q,r,p) in NODES[1].items():
                if racts[n]!='C':total+=q*cost(1,r,racts[n])
            for n,(q,r,p) in NODES[2].items():
                if racts[p]!='C':continue
                a=a2[group2[n]]
                if a=='C':
                    live_t3.update(child for child,(cq,cr,cp) in NODES[3].items() if cp==n)
                else: total+=q*cost(2,r,a)
            groups=defaultdict(list)
            for n in live_t3:groups[group3[n]].append(n)
            a3={}
            for grp,names in groups.items():
                alt={a:sum(NODES[3][n][0]*c3[n][a] for n in names) for a in ACTS}
                action=min(ACTS,key=lambda a:alt[a])
                a3[grp]=action
                total+=alt[action]
            if rbest is None or total<rbest:
                rbest,rpol=total,(racts.copy(),a2.copy(),a3.copy())
        by_root[rootlabel]=rbest
        if best is None or rbest<best:
            best,bestpol=rbest,rpol
    # Complete coverage: 3^2 choices at t1, 3^(3 or 4) at t2;
    # all t3 choices are exactly separable by their reachable signature groups.
    assert candidates == 3**2*3**len(labels2)
    return best,bestpol,by_root,candidates,group2,group3,terminal_action

def observer_vector(policy,group2,group3,terminal_action):
    r1,r2,r3=policy
    v=[F(0) for _ in range(4)]
    for name,(q,r,_) in NODES[4].items():
        hist3=name[:-1];hist2=hist3[:-1];hist1=hist2[0]
        a=r1[hist1]
        t=1
        if a=='C':
            a=r2[group2[hist2]]
            t=2
            if a=='C':
                a=r3[group3[hist3]]
                t=3
                if a=='C':
                    a=terminal_action[name]
                    t=4
        if a=='Q':v[0]+=q*r
        else:v[1]+=q
        v[2]+=t*q*r
        v[3]+=t*q
    assert F(1)<=v[2]<=F(4) and F(1)<=v[3]<=F(4)
    return tuple(v)

def dot(t):return sum(a*b for a,b in zip(LAMBDA,t))

def main():
    check_tree()
    cases={}
    for c2,c3 in [(False,False),(True,False),(False,True),(True,True)]:
        val,pol,table,n,grp2,grp3,terminal=optimize(c2,c3)
        vec=observer_vector(pol,grp2,grp3,terminal)
        assert dot(vec)==val,(c2,c3,vec,val)
        key=('both' if c2 and c3 else 't2' if c2 else 't3' if c3 else 'full')
        cases[key]={'support_value':fstr(val),'vector':list(map(fstr,vec)),
                    'root_policy':pol[0],'t2_policy':{str(k):v for k,v in pol[1].items()},
                    't3_policy':{str(k):v for k,v in pol[2].items()},
                    'root_conditioned_minima':{k:fstr(v) for k,v in table.items()},
                    't1_t2_assignments_checked':n,
                    't2_signatures':len(set(grp2.values())),
                    't3_signatures':len(set(grp3.values()))}
    assert cases['full']['support_value']=='785/32'
    assert cases['t2']['support_value']=='11783/480'
    assert cases['t3']['support_value']=='11783/480'
    assert cases['both']['support_value']=='19647/800'
    vals={k:F(v['support_value']) for k,v in cases.items()}
    gaps={k:vals[k]-vals['full'] for k in ['t2','t3','both']}
    assert gaps['t2']==F(1,60) and gaps['t3']==F(1,60)
    assert gaps['both']==F(11,400)
    nonadd=gaps['t2']+gaps['t3']-gaps['both']
    assert nonadd==F(7,1200)>0
    assert cases['both']['root_conditioned_minima']['A:P/B:C']=='19647/800'
    payload={'status':'PASS_EXACT_FRACTION_N4_DYNAMIC_NONADDITIVITY',
       'scope':'External strictly positive depth-4 dual-measure observation tree; exact signed support minima over all local behavioral policies',
       'lambda':list(map(fstr,LAMBDA)),
       'node_count_by_time':{str(k):len(v) for k,v in NODES.items()},
       'collisions':{'t2':['AU','BU'],'t3':['AV0','AV1']},
       'cases':cases,'gaps':{k:fstr(v) for k,v in gaps.items()},
       'strict_subadditivity':fstr(nonadd),
       'open_lambda_linf_radius':fstr(nonadd/F(40)),
       'limits':'Not a two-law TV minimax distance or a P000 native X6 evolution theorem; no independent review or formal checker.'}
    print(json.dumps(payload,ensure_ascii=False,indent=2,sort_keys=True))

if __name__=='__main__':main()
