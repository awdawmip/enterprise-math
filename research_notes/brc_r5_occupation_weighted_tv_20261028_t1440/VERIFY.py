#!/usr/bin/env python3
"""Exact check for occupancy-weighted, stage-sensitive LR compression bounds.
External finite passive P/Q observation model; no native X6 operation.
"""
from collections import defaultdict
from fractions import Fraction as F

Z, ONE = F(0), F(1)
R = (F(1,2), ONE, F(3,2))
BASE=(F(1,4),F(1,2),F(1,4))
PERT=(F(1,8),F(3,4),F(1,8))

def build():
    nodes={}
    for tag in ('A','B'):
        h=(tag,)
        nodes[h]=(1,ONE,F(1,2),[])
        row=BASE if tag=='A' else PERT
        for i,(q,r) in enumerate(zip(row,R)):
            k=(tag,i)
            nodes[k]=(2,r,F(1,2)*q,[])
            if i==1:
                next_row=BASE if tag=='A' else PERT
                destinations=R
            else:
                next_row=(F(1,2),F(1,2))
                destinations=(r*F(3,4),r*F(5,4))
            for j,(conditional_q,s) in enumerate(zip(next_row,destinations)):
                child=(tag,i,j)
                nodes[child]=(3,s,nodes[k][2]*conditional_q,[])
                nodes[k][3].append(child)
            nodes[h][3].append(k)
    assert len(nodes)==22
    assert sum(v[2] for h,v in nodes.items() if v[0]==3)==1
    assert sum(v[1]*v[2] for h,v in nodes.items() if v[0]==3)==1
    for h,(t,r,q,children) in nodes.items():
        assert q>0 and r>0
        if children:
            assert sum(nodes[c][2] for c in children)==q
            assert sum(nodes[c][1]*nodes[c][2] for c in children)==q*r
    return nodes

def policy(nodes,seed=None):
    a={}
    if seed is not None:
        for h,(t,_,__,___) in nodes.items():
            num=(1 if h[0]=='A' else 3)+5*(h[1] if len(h)>1 else 0)+7*(h[2] if len(h)>2 else 0)
            x=F(1+(seed+num)%7); y=F(1+(3*seed+2*num)%11)
            z=Z if t==3 else F(1+(2*seed+3*num)%13)
            a[h]=(x/(x+y+z),y/(x+y+z),z/(x+y+z))
        return a
    a[('A',)]=(F(1,4),F(1,4),F(1,2))
    a[('B',)]=(F(1,8),F(1,8),F(3,4))
    a[('A',0)]=(F(1,8),F(1,4),F(5,8))
    a[('B',0)]=(F(1,3),F(1,3),F(1,3))
    a[('A',1)]=(F(1,6),F(1,6),F(2,3))
    a[('B',1)]=(F(1,3),F(1,3),F(1,3))
    a[('A',2)]=(F(1,5),F(2,5),F(2,5))
    a[('B',2)]=(F(1,4),F(1,2),F(1,4))
    for h,(t,_,__,___) in nodes.items():
        if t==3:
            num=1+(1 if h[0]=='A' else 2)+2*h[1]+h[2]
            z=F(num,15)
            a[h]=(z,ONE-z,Z)
    assert len(a)==len(nodes)
    return a

def enact(nodes,acts,compressed=False):
    active={h:nodes[h][2] for h in nodes if len(h)==1}
    terminal={'P':defaultdict(lambda:Z),'Q':defaultdict(lambda:Z)}
    continues={'P':defaultdict(lambda:Z),'Q':defaultdict(lambda:Z)}
    for t in range(1,4):
        nxt=defaultdict(lambda:Z)
        for h,w in active.items():
            _,r,q,children=nodes[h]
            v=acts[(t,r)] if compressed else acts[h]
            assert sum(v)==ONE and all(x>=0 for x in v)
            for mu,w_mu in (('Q',w),('P',w*r)):
                terminal[mu][(t,'P')]+=w_mu*v[0]
                terminal[mu][(t,'Q')]+=w_mu*v[1]
                if children: continues[mu][(t,r)]+=w_mu*v[2]
            for c in children:
                nxt[c]+=w*v[2]*nodes[c][2]/q
        active=nxt
    assert not active
    assert all(sum(terminal[mu].values())==ONE for mu in ('P','Q'))
    obs=(sum(v for (t,a),v in terminal['P'].items() if a=='Q'),
         sum(v for (t,a),v in terminal['Q'].items() if a=='P'),
         sum(t*v for (t,a),v in terminal['P'].items()),
         sum(t*v for (t,a),v in terminal['Q'].items()))
    return obs,terminal,continues

def markovize(nodes,acts):
    active={h:nodes[h][2] for h in nodes if len(h)==1}
    totals=defaultdict(lambda:[Z,Z,Z,Z])
    for t in range(1,4):
        nxt=defaultdict(lambda:Z)
        for h,w in active.items():
            _,r,q,children=nodes[h]
            row=totals[(t,r)]; row[0]+=w
            for k in range(3):row[k+1]+=w*acts[h][k]
            for c in children: nxt[c]+=w*acts[h][2]*nodes[c][2]/q
        active=nxt
    return {sig:tuple(v/row[0] for v in row[1:]) for sig,row in totals.items() if row[0]}

def kernels(nodes,mu):
    fibers=defaultdict(list)
    for h,(t,r,q,children) in nodes.items():
        if not children: continue
        k=defaultdict(lambda:Z)
        for c in children:
            _,s,q_c,_=nodes[c]
            k[s]+=q_c/q*(s/r if mu=='P' else ONE)
        assert sum(k.values())==ONE
        fibers[(t,r)].append(k)
    return fibers

def diameter(rows):
    ks=set().union(*map(set,rows))
    return max(sum(abs(a[s]-b[s]) for s in ks)/2 for a in rows for b in rows)

def diameter_map(nodes,mu):
    return {sig:diameter(rows) for sig,rows in kernels(nodes,mu).items()}

def bound(nodes,acts):
    _,_,c=enact(nodes,acts)
    ds={mu:diameter_map(nodes,mu) for mu in ('P','Q')}
    eps={mu:{t:sum(c[mu][sig]*d for sig,d in ds[mu].items() if sig[0]==t)
                 for t in (1,2)} for mu in ('P','Q')}
    # N=3: terminal-declaration error uses both stages; expected time uses t=1 only.
    eb={mu:min(ONE,sum(eps[mu].values())) for mu in ('P','Q')}
    tb={mu:eps[mu][1] for mu in ('P','Q')}
    return ds,eps,eb,tb

def check(nodes,acts):
    full,stopped,c=enact(nodes,acts)
    lr=markovize(nodes,acts)
    reduced,stopped_lr,_=enact(nodes,lr,True)
    ds,eps,eb,tb=bound(nodes,acts)
    dif=tuple(abs(x-y) for x,y in zip(full,reduced))
    assert dif[0]<=eb['P'] and dif[1]<=eb['Q']
    assert dif[2]<=tb['P'] and dif[3]<=tb['Q']
    for mu in ('P','Q'):
        joint_tv=sum(abs(stopped[mu][k]-stopped_lr[mu][k]) for k in set(stopped[mu])|set(stopped_lr[mu]))/2
        assert joint_tv<=eb[mu]
    return full,reduced,dif,ds,eps,eb,tb

nodes=build()
full,reduced,dif,ds,eps,eb,tb=check(nodes,policy(nodes))
assert ds['Q'][(1,ONE)]==ds['P'][(1,ONE)]==F(1,4)
assert ds['Q'][(2,ONE)]==ds['P'][(2,ONE)]==F(1,4)
assert all(d==0 for mu in ('Q','P') for sig,d in ds[mu].items() if sig not in ((1,ONE),(2,ONE)))
assert eps['P']==eps['Q']=={1:F(5,32),2:F(17,384)}
assert eb['Q']==eb['P']==F(77,384)
assert tb['Q']==tb['P']==F(5,32)
assert any(x for x in dif)
for seed in range(100): check(nodes,policy(nodes,seed))
print('EXACT TWO-LEVEL P/Q TREE: 22 histories; 14 positive leaves; 11 LR fibers')
print('both P/Q leaves sum exactly to 1; every local conditional row has sum 1 and preserved LR mean')
print('heterogeneous nonterminal fibers (t,r): (1,1), (2,1)')
print('TV diameters at each heterogeneous fiber under P/Q: 1/4, 1/4')
print('Q/P continuation-mass weighted budgets: epsilon_1=5/32; epsilon_2=17/384')
print('terminal-label TV/error bound for both laws: 77/384')
print('expected stopping-time error bound for both laws: 5/32')
print('predecessor uniform bounds: terminal errors <=1/2, time errors <=1')
print('full O:', full)
print('LR averaged O:', reduced)
print('absolute coordinate differences:',dif)
print('100 deterministic rational policy regression inputs: PASS')
print('ALL EXACT OCCUPATION-WEIGHTED TV CHECKS PASSED')
