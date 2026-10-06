#!/usr/bin/env python3
"""Compact U2 replay. Same author; no native material or physical admission."""
from fractions import Fraction as Q
from itertools import product
import json
import packet_router as r

count = 0

def check(ok, name):
    global count
    count += 1
    if not ok:
        raise AssertionError(name)

basis = {}
for p in r.PORTS:
    packets = r.packets(p, r.brc.CWM_ONE, tag=('basis',p))
    check(len(packets)==40,'packet incidence count')
    out = r.marginals(packets)
    for q in r.PORTS:
        expected = Q(1,3) if q==p else (Q(0) if q==(p^1) else Q(1,15))
        check(out[q].total==expected,'signed transfer law')
    check(r.total(out.values()).total==1,'total response')
    check(r.total(out.values()).count==120,'refined branch count retained')
    for packet in packets:
        check(len({r.axis(q) for q in packet.ports})==3,'three distinct axes')
        for z,zz in packet.paths():
            check(sum(abs(a-b) for a,b in zip(z,zz))==1,'primitive X6 edge')
    basis[p]=out

for m in product((0,1),repeat=6):
    if not any(m):
        continue
    out={q:r.brc.CWM_ZERO for q in r.PORTS}
    for i,used in enumerate(m):
        if used:
            for q,v in basis[2*i].items():
                out[q]=r.merge(out[q],v)
    T=Q(sum(m)); axes=r.axis_totals(out)
    for i in range(6):
        check(axes[i]==Q(m[i],5)+2*T/15,'axis equation')
        check(3*axes[i]<=T,'universal packet cone')

# Both buffers are generated from one common isotropic response input.
seed=tuple(packet for p in r.PORTS
           for packet in r.packets(p,r.edge(Q(1,12)),tag=('same-source',p)))
P=[(1,2,3),(1,4,5),(2,4,6),(3,5,6)]
S=[(1,2,4),(1,3,5),(2,3,6),(4,5,6)]

def prepare(triples):
    pool=seed; chosen=()
    for triple in triples:
        h={2*(i-1) for i in triple}
        ready,pool=r.gate(pool,set(r.PORTS)-h)
        check(len(ready)==3,'exact selected triple')
        chosen+=ready
        check(r.total(v.budget for v in chosen+pool)==r.total(v.budget for v in seed),
              'reservoir conservation')
    return chosen,pool

a,ra=prepare(P); b,rb=prepare(S)
check(r.marginals(a)==r.marginals(b),'all signed marginals agree')
for p in r.PORTS:
    for q in r.PORTS:
        ca=r.total(x.leg for x in a if p in x.ports and q in x.ports)
        cb=r.total(x.leg for x in b if p in x.ports and q in x.ports)
        check(ca==cb,'all pair-incidence CWM agree')
    aa,_=r.gate(a,{p}); bb,_=r.gate(b,{p})
    check(r.marginals(aa)==r.marginals(bb),'all single-block responses agree')
released_a,held_a=r.gate(a,{0,2}); released_b,held_b=r.gate(b,{0,2})
check(r.marginals(released_a)[4].total==Q(1,480),'P releases positive axis3')
check(r.marginals(released_b)[4].total==0,'Q does not release positive axis3')
check(r.marginals(released_a)[6].total==0,'P does not release positive axis4')
check(r.marginals(released_b)[6].total==Q(1,480),'Q releases positive axis4')
check(r.total(x.budget for x in a).total==Q(1,40),'selected budget')
check(r.total(x.budget for x in ra).total==Q(39,40),'unselected retained budget')
for state in (a,b):
    hist=r.histogram(state)
    for bits in product((0,1),repeat=6):
        B={2*i for i,used in enumerate(bits) if used}
        ready,held=r.gate(state,B)
        projected={p:r.brc.CWM_ZERO for p in r.PORTS}
        for h,value in hist.items():
            if not B.intersection(h):
                leg=r.serial(value,r.THIRD)
                for p in h:
                    projected[p]=r.merge(projected[p],leg)
        check(projected==r.marginals(ready),'exact histogram sufficient')
        check(r.total(x.budget for x in ready+held)==r.total(x.budget for x in state),
              'holding is not cancellation')

z=r.ZERO; e=[r.direction(2*j) for j in range(6)]
layouts={'pair':(z,e[0]),
 'square_221':(z,e[0],e[1],tuple(x+y for x,y in zip(e[0],e[1]))),
 'chain4':tuple(tuple(k*x for x in e[0]) for k in range(4)),
 'three_axis_star4':(z,e[0],e[1],e[2])}
fields={}
for name,cells in layouts.items():
    f=r.field_prefix(cells,depth=4,check=check)
    for i,cell in enumerate(cells):
        d=sum(r.advance(cell,p) in cells for p in r.PORTS)
        check(f['layers'][2]['self_return'][i].total==(12+3*d)*Q(1,48)**2,
              'two-edge return law')
    check(sum(v['CWM'].total for v in f['layers'])+f['tail_total_bound']==f['infinite_total_response'],
          'all-depth response budget')
    fields[name]={'two_edge_self_returns':f['layers'][2]['self_return'],
                  'global_tail_bound':f['tail_total_bound'],
                  'all_depth_total_response':f['infinite_total_response']}
print(json.dumps(r.to_json({'status':'SAME_AUTHOR_EXACT_CIRCUIT_REPLAY',
 'checks':count,'BRC_source_blob':r.BLOB,'actual_BRC_calls':dict(r.CALLS),
 'fields':fields,'material_positions_solved':False,'native_triads_admitted':False,
 'primitive_quantum_realization':False,'physical_time':False,'prime_claim':False}),indent=2))
