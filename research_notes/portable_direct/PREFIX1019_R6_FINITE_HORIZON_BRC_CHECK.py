#!/usr/bin/env python3
"""Exact frozen Stage46 candidate signed BRC, no floating-point.
Arbitrary input diagnostic; link {0,e1} absorption, all negative grades combined.
"""
from collections import defaultdict
from json import dump
from pathlib import Path

D=6
ZERO=(0,)*D
basis=[tuple(int(i==j) for i in range(D)) for j in range(D)]
negative=[tuple(-a for a in b) for b in basis]
steps=basis+negative
h0=negative[0]

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def shift(packet,offset):return {(add(x,offset),h):v for (x,h),v in packet.items()}
def step(packet,absorb=True):
    out=defaultdict(int)
    for (x,h),v in packet.items():
        for d in steps:
            if absorb and ((x==ZERO and d==basis[0]) or (x==basis[0] and d==negative[0])):continue
            key=(add(x,d),neg(d))
            out[key]+=v*(1-6*(h==d))
    return {k:v for k,v in out.items() if v}

def byport(packet,kind):
    acc=defaultdict(int)
    for (x,h),v in packet.items():
        port=neg(h) # actual final direction
        acc[port]+=v if kind=='signed' else v*v
    return dict(acc)

def flux(packet):
    return sum((sum((1-6*(h==d))*v for (x,h),v in packet.items() if x==cell))**2 for cell,d in ((ZERO,basis[0]),(basis[0],negative[0])))

def norm(packet):
    return sum(v*v for v in packet.values())

def test_flux():
    v={(ZERO,negative[0]):2, (ZERO,basis[0]):-3, (basis[0],basis[0]):4, (tuple(2*z for z in basis[0]),negative[1]):-5}
    assert norm(v)==54
    assert flux(v)==305
    assert norm(step(v,False))==36*norm(v)
    assert norm(step(v,True))==36*norm(v)-flux(v)==1639
    cur=v.copy()
    lost=[]
    for t in range(4):
        loss=flux(cur)
        nxt=step(cur,True)
        assert norm(nxt)==36*norm(cur)-loss
        lost.append(loss)
        cur=nxt
    assert 36**4*54 - norm(cur)==sum(lost[t]*36**(3-t) for t in range(4))
    return {'input_norm':54,'step0_flux':305,'step1_masked_norm':1639,'four_step_fluxes':lost,'four_step_masked_norm':norm(cur)}

def test(r):
    a=tuple(r*x for x in basis[1]);b=tuple((r+2)*x for x in basis[1]);delta=tuple(y-x for x,y in zip(a,b))
    A={(a,h0):1};B={(b,h0):1}; rows=[]
    for t in range(r+2):
        As=byport(A,'signed');Bs=byport(B,'signed')
        Aq=byport(A,'gram');Bq=byport(B,'gram')
        if t<=r:
            assert shift(A,delta)==B,(r,t,'full_packet_failed')
            assert As==Bs and Aq==Bq,(r,t,'port_failed')
        else:
            assert t==r+1
            diff=defaultdict(int)
            Ashift=shift(A,delta)
            for k,v in B.items():diff[k]+=v
            for k,v in Ashift.items():diff[k]-=v
            diff={k:v for k,v in diff.items() if v}
            assert diff=={(add(basis[0],delta),neg(basis[0])):1},(r,t,diff)
            assert Bs[basis[0]]-As[basis[0]]==1
            assert Bq[basis[0]]-Aq[basis[0]]==1
            for port in steps:
                if port!=basis[0]:
                    assert Bs.get(port,0)==As.get(port,0)
                    assert Bq.get(port,0)==Aq.get(port,0)
        rows.append({'step':t,'a_nonzero_fibres':len(A),'b_nonzero_fibres':len(B),'signed_port_total_A':sum(As.values()),'signed_port_total_B':sum(Bs.values()),'gram_port_total_A':sum(Aq.values()),'gram_port_total_B':sum(Bq.values()),'plus_e1_signed_A':As.get(basis[0],0),'plus_e1_signed_B':Bs.get(basis[0],0),'plus_e1_gram_A':Aq.get(basis[0],0),'plus_e1_gram_B':Bq.get(basis[0],0)})
        if t<r+1:
            A=step(A);B=step(B)
    return {'r':r,'near_cell':a,'far_cell':b,'last_step':r+1,'rows':rows,'status':'PASS'}

if __name__=='__main__':
    flux_control=test_flux()
    results=[test(r) for r in range(1,5)]
    out={'schema':'PREFIX1019_R6_EXACT_CHECK_V1','science_scope':'P000 V5 / Stage46 candidate signed BRC / all-grade arbitrary-source inputs','link':'{0,e1} both orientations absorbed','weight':'1-6*[h=d], next h=-d','cases':results,'flux_general_packet_control':flux_control,'integer_only':True,'status':'PASS'}
    with open(Path(__file__).with_name('PREFIX1019_R6_EXACT_RESULTS.json'),'w',encoding='utf-8') as f: dump(out,f,ensure_ascii=False,indent=2)
    for item in results:
        r=item['r'];last=item['rows'][-1]
        print('r',r,'t',r+1,'total_sq',last['gram_port_total_A'],last['gram_port_total_B'],'e1',last['plus_e1_gram_A'],last['plus_e1_gram_B'],'fibres',last['a_nonzero_fibres'])
    print('ALL CHECKS PASSED')
