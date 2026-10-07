#!/usr/bin/env python3
"""Compact same-author replay; run beside continue_field.py and pinned sources."""
from fractions import Fraction as Q
import json
import continue_field as c
r,o=c.r,c.o
checks=0
def ck(x):
    global checks
    checks+=1
    if not x:raise AssertionError(checks)
z=r.ZERO;e=r.direction(0);X=(z,tuple(2*a for a in e));Y=(e,X[1])
lam=Q(1,48);rho=Q(1,4);f=c.RetainedField(rho)
p=o.marked_pulse(X,2,rho);F=p['layers'][-1]
first=o.successor_branches(X,p['demands'],wait=lam)
all_weight=[];returns=[];states={};n=0
for i,b in enumerate(first):
    field,retired=f.advance(F,b['cells'],3);states[i]=field
    ck(c.total_readout(field)+c.total_readout(retired)==c.total_readout(F))
    ds=c.fresh_probe(field,b['cells'],3)
    following=o.successor_branches(b['cells'],ds,wait=lam)
    ck(r.total(t['measure'] for t in following).total==1)
    for t in following:
        w=r.serial(b['measure'],t['measure']);all_weight.append(w);n+=1
        ck(len(set(t['cells']))==2)
        for token in p['demands']:
            v=c.residual_readout(token,t['cells'][token.actor])
            ck(tuple(a+d for a,d in zip(t['cells'][token.actor],v))==token.destination)
        if b['cells']==Y and t['cells']==X:returns.append((i,w))
ck(n==53 and r.total(all_weight).total==1)
ck(r.total(w for i,w in returns).total==Q(97,11222274))
j=next(i for i,b in enumerate(first) if b['cells']==X)
k=returns[0][0];static=states[j];moved=states[k]
d3=c.difference_readout(moved,static)
expected={}
for q in r.PORTS:
    a=Q(-3) if q==0 else (Q(1) if q==1 else Q(1,5))
    expected[1,r.advance(z,q),q^1]=a*lam**3
ck(d3==expected)
future={};rows={}
for name,field in [('static',static),('returned',moved)]:
    ff,rr=f.advance(field,X,4);rows[name]=c.row(ff,1,z)
    ds=c.fresh_probe(ff,X,4);bs=o.successor_branches(X,ds,wait=lam)
    ck(r.total(b['measure'] for b in bs).total==1)
    weight=r.total(b['measure'] for b in bs if b['cells'][0]==r.advance(z,1)).total
    future[name]=weight
ck(future=={'static':Q(0),'returned':Q(1,110656)})
for q in r.PORTS:
    a=Q(36) if q==0 else (Q(0) if q==1 else Q(14,5))
    b=Q(33) if q==0 else (Q(1) if q==1 else Q(3))
    ck(rows['static'][q].total==a*lam**4)
    ck(rows['returned'][q].total==b*lam**4)
for row in rows.values():ck(r.total(row).total==64*lam**4)
for origin in (e,(3,-2,1,4,-1,0),z):
    chart=c.passive_rechart(moved,origin)
    ck(c.undo_rechart(chart,origin)==moved)
    ck(r.total(chart.values())==r.total(moved.values()))
sq=(z,e,tuple(a+b for a,b in zip(e,r.direction(2))),r.direction(2))
sp=o.marked_pulse(sq,1,rho);sf=sp['layers'][-1]
for shift in range(4):
    ck(f.advance(sf,sq[shift:]+sq[:shift],2)==f.advance(sf,sq,2))
print(json.dumps({'status':'SAME_AUTHOR_COMPACT_REPLAY_NOT_NATIVE_PHYSICS','checks':checks,
 'BRC_calls':dict(r.CALLS),'histories':n,'return_weight':'97/11222274',
 'outward_static':str(future['static']),'outward_returned':str(future['returned']),
 'native_force_lift':False},indent=2))
