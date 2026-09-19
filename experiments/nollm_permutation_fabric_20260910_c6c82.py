#!/usr/bin/env python3
"""Classical recursive Benes fabric applied to the exact transported six ports.
This is a LOGICAL switching-network comparison, not a planar wire-length claim.
Run with experiment.py and its pinned predecessors alongside.
"""
from __future__ import annotations
import argparse,json,random,hashlib,importlib.util,sys
from itertools import permutations,product
from pathlib import Path
ROOT=Path(__file__).resolve().parent
paths=[ROOT/'experiment.py',ROOT/'nollm_finite_carry_routing_20260910_c6c82.py']
path=next((p for p in paths if p.exists()),None)
if path is None:raise FileNotFoundError('finite carry predecessor required')
if hashlib.sha256(path.read_bytes()).hexdigest()!='0bf4e28f978777ac0d25e964f25398a440c499448462f018e7e0718206972940':raise ValueError('source hash mismatch')
spec=importlib.util.spec_from_file_location('finite_carry',path)
e=importlib.util.module_from_spec(spec);sys.modules[spec.name]=e;spec.loader.exec_module(e)

def configure(perm):
    n=len(perm)
    if n<2 or n&(n-1):raise ValueError('power-of-two width required')
    seen=[False]*n
    for v in perm:
        if type(v) is not int or not 0<=v<n or seen[v]:raise ValueError('permutation required')
        seen[v]=True
    if n==2:return {'n':2,'swap':perm[0]}
    inv=[0]*n
    for x,y in enumerate(perm):inv[y]=x
    color=[-1]*n
    for seed in range(n):
        if color[seed]!=-1:continue
        color[seed]=0;stack=[seed]
        while stack:
            x=stack.pop()
            for z in (x^1,inv[perm[x]^1]):
                want=1-color[x]
                if color[z]==-1:color[z]=want;stack.append(z)
                else:assert color[z]==want
    first=[color[2*j] for j in range(n//2)];last=[0]*(n//2)
    sub=[[-1]*(n//2),[-1]*(n//2)]
    for x in range(n):
        c=color[x];y=perm[x];sub[c][x//2]=y//2;last[y//2]=c^(y%2)
    return dict(n=n,first=first,last=last,upper=configure(sub[0]),lower=configure(sub[1]))

def execute(net,values):
    n=net['n']
    if len(values)!=n:raise ValueError('network width')
    if n==2:return values[::-1] if net['swap'] else list(values)
    up=[];down=[]
    for j,s in enumerate(net['first']):
        a,b=values[2*j:2*j+2]
        if s:a,b=b,a
        up.append(a);down.append(b)
    up=execute(net['upper'],up);down=execute(net['lower'],down);out=[]
    for a,b,s in zip(up,down,net['last']):out.extend((b,a) if s else (a,b))
    return out

def switches(net):
    if net['n']==2:return 1
    return net['n']+switches(net['upper'])+switches(net['lower'])

def depth(net):
    if net['n']==2:return 1
    a,b=depth(net['upper']),depth(net['lower']);assert a==b
    return 2+a

def stage_trace(net,values):
    n=net['n']
    if n==2:return [execute(net,values)]
    first=[]
    for j,s in enumerate(net['first']):
        a,b=values[2*j:2*j+2];first.extend((b,a) if s else (a,b))
    up=stage_trace(net['upper'],first[::2]);down=stage_trace(net['lower'],first[1::2])
    rows=[first]+[a+b for a,b in zip(up,down)]
    final=[]
    for a,b,s in zip(up[-1],down[-1],net['last']):final.extend((b,a) if s else (a,b))
    return rows+[final]

def check(perm,net):
    stages=stage_trace(net,list(range(len(perm))))
    assert len(stages)==depth(net)
    assert all(len(set(row))==len(perm) for row in stages)
    out=execute(net,list(range(len(perm))))
    assert stages[-1]==out
    assert all(out[y]==x for x,y in enumerate(perm))
    assert len(set(out))==len(perm)
    return len(out)

def run(out):
    out.mkdir(parents=True,exist_ok=True);rng=random.Random(20260910512)
    tests=checks=0
    for n in (2,4):
        for perm in permutations(range(n)):
            net=configure(list(perm));checks+=check(perm,net);tests+=1
    for n in (8,16,32,64,128,256):
        for _ in range(25):
            perm=list(range(n));rng.shuffle(perm);net=configure(perm);checks+=check(perm,net);tests+=1
    m=55;N=m*m;width=1<<(N-1).bit_length();nodes=list(product(range(m),repeat=2))
    # Ambient CRT physical slots, with the two declared prime-local chart maps.
    phi=[]
    for x in nodes:
        a=e.direct(x,5,2,e.A,13,3);b=e.direct(x,11,2,e.C,1,3)
        y=tuple(e.crt(a[i],b[i],5,11) for i in (0,1));phi.append(y[0]*m+y[1])
    assert len(set(phi))==N
    signal=[(i*37+19)%101 for i in range(N)];g=[0]*width
    for i in range(N):g[phi[i]]=signal[i]
    agg=[0]*width;expected=[0]*N;rows=[];certs=[]
    for d in e.D:
        perm=list(range(width))
        for i,x in enumerate(nodes):
            nb=((x[0]+d[0])%m,(x[1]+d[1])%m);j=nb[0]*m+nb[1]
            perm[phi[i]]=phi[j];expected[j]+=signal[i]
        net=configure(perm);check(perm,net)
        y=execute(net,g);agg=[a+b for a,b in zip(agg,y)]
        assert switches(net)==width//2*(2*(width.bit_length()-1)-1)
        rows.append(dict(direction=d,stages=depth(net),switches=switches(net),
            real_packets=N,padded_idle_slots=width-N,correct_endpoints=N,unit_capacity_wire_conflicts=0))
        certs.append(net)
    assert all(agg[phi[i]]==expected[i] for i in range(N)) and all(v==0 for v in agg[N:])
    result=dict(schema='NOLLM_BENES_PORT_COMPARISON_V1',status='PASS_RESEARCH_NOT_PROMOTED',
       classical_algorithm='recursive alternating-cycle Benes configuration',
       random_and_small_permutation_tests=tests,tested_token_endpoints=checks,
       real_states=N,padded_width=width,stages=rows[0]['stages'],
       switch_elements=rows[0]['switches'],direction_passes=6,
       serial_direction_stage_budget=sum(r['stages'] for r in rows),
       real_message_endpoints=6*N,padded_idle_slots=width-N,
       aggregation_equal=True,rows=rows,
       limits=['switch configuration cost is excluded from stage budget',
        'configuration uses O(width log width) space/work; not the small carry-state table',
        'six directions use separate passes, not all six simultaneously on one wire',
        'interstage wires are nonlocal unless a separate physical embedding is provided',
        'no clock-time, total-energy or Nollm integration performance claim'])
    (out/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    (out/'switch_configurations.json').write_text(json.dumps(certs,separators=(',',':'))+'\n')
    print(json.dumps(result,indent=2))
    return result
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,default=Path('fabric_results'))
    run(p.parse_args().output)
