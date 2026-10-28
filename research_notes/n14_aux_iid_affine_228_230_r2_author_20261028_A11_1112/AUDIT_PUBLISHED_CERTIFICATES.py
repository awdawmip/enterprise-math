#!/usr/bin/env python3
"""Independent arithmetic-only audit of Stage228–230 JSON certificates.
Does not re-run primal search or confer independent researcher review.
"""
from fractions import Fraction as Q
from pathlib import Path
from itertools import combinations
import json
folder=Path(__file__).resolve().parent
load=lambda n:json.loads((folder/n).read_text(encoding='utf8'))
rat=lambda x:Q(str(x))
obs=lambda x:tuple(map(rat,x))
a=load('certificate228.json');b=load('certificate229_polytope.json');c=load('certificate230.json');z=load('null_pivots_228_to_229.json');q231=load('certificate231_dual.json')
assert [r['stage'] for r in (a,b,c)]==[228,229,230]
for x in (a,c):
    K=rat(x['K']);H=rat(x['H']);corners={k:obs(v) for k,v in x['corners'].items()}
    assert len(corners)==4
    for v in corners.values():assert v[2]+K*(v[0]+v[1])==H
    baseline=corners['00'];du=tuple(x-y for x,y in zip(corners['10'],baseline));dz=tuple(x-y for x,y in zip(corners['01'],baseline))
    assert tuple(corners['11'][i]-corners['10'][i]-corners['01'][i]+baseline[i] for i in range(4))==(Q(0),)*4
    assert tuple(map(rat,x['du']))==du and tuple(map(rat,x['dz']))==dz
    zz0=-(baseline[0]-baseline[1])/(dz[0]-dz[1]);zzs=-(du[0]-du[1])/(dz[0]-dz[1])
    assert [zz0,zzs,zz0+zzs]==list(map(rat,[x['z0'],x['zs'],x['z1']]))
    for u,alpha,value,margin in [(Q(0),x['alpha_left'],x['value_left'],x['time_margin_left']),(Q(1),x['alpha_right'],x['value_right'],x['time_margin_right'])]:
        w=zz0+zzs*u;assert 0<w<1
        v=tuple(baseline[j]+du[j]*u+dz[j]*w for j in range(4))
        assert v[0]==v[1]==rat(alpha) and v[2]==rat(value)
        assert v[2]-v[3]==rat(margin)>0
        assert v[2]+2*K*v[0]==H
    assert rat(x['delta'])==rat(x['alpha_right'])-rat(x['alpha_left'])
    assert rat(x['slope'])==-2*K
    assert sum(x['dfs_nodes'].values())==x['total_dfs_nodes']
assert len(z)==3
for i,x in enumerate(z):
    assert x['delta']=='0/1' and x['root_reachable'] is False
    assert x['four_corner_certificate']['du']==['0/1']*4
    assert x['four_corner_certificate']['alpha_left']==a['alpha_right']
    assert x['four_corner_certificate']['value_right']==a['value_right']
K=rat(b['K']);H=rat(b['H']);corners={key:obs(vec) for key,vec in b['corners'].items()}
assert K==72 and len(corners)==16 and b['equal_error_vertices']==64
assert sum(b['dfs_nodes'].values())==b['total_dfs_nodes']==67816
assert all(v[2]>v[3] and v[2]+K*(v[0]+v[1])==H for v in corners.values())
vertices=[]
for u,v in corners.items():
    if v[0]==v[1]:vertices.append((v[0],(u,),[Q(1)],v))
for u,w in combinations(corners,2):
    v=corners[u];x=corners[w];d=v[0]-v[1];e=x[0]-x[1]
    if d*e>=0:continue
    p=-e/(d-e)
    y=tuple(p*v[i]+(1-p)*x[i] for i in range(4))
    assert y[0]==y[1] and 0<p<1
    vertices.append((y[0],(u,w),[p,1-p],y))
assert len(vertices)==64
lower=min(vertices,key=lambda x:x[0]);upper=max(vertices,key=lambda x:x[0])
assert lower[0]==rat(b['alpha_left']) and upper[0]==rat(b['alpha_right'])
assert b['left_witness_bits']==list(lower[1]) and b['right_witness_bits']==list(upper[1])
assert list(map(rat,b['left_witness_weights']))==lower[2]
assert list(map(rat,b['right_witness_weights']))==upper[2]
assert upper[3][2]==rat(b['value_right'])
assert rat(a['alpha_right'])==rat(b['alpha_left']) and rat(a['value_right'])==rat(b['value_left'])
assert rat(b['alpha_right'])==rat(c['alpha_left']) and rat(b['value_right'])==rat(c['value_left'])
assert rat(b['delta'])==rat(b['alpha_right'])-rat(b['alpha_left'])
assert H==rat(a['H'])+2*rat(a['alpha_right'])*(K-rat(a['K']))
assert rat(c['H'])==H+2*rat(b['alpha_right'])*(rat(c['K'])-K)
assert rat(q231['H'])==rat(c['H'])+2*rat(c['alpha_right'])*(rat(q231['K'])-rat(c['K']))
assert sum(x['total_dfs_nodes'] for x in [a,c])+sum(x['total_dfs_nodes'] for x in z)+b['total_dfs_nodes']==155430
print('REMOTE_READY_INDEPENDENT_CERTIFICATE_ARITHMETIC_PASS stages=228,229,230 null_pivots=3 equal_error_vertices=64 ordered_dfs=155430')
