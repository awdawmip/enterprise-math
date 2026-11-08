#!/usr/bin/env python3
"""Independent exact 96-native-port integer moment DP, not using the quotient eigensolver.
Run next to PREFIX578_R2_mixed_cumulants_certificate.py (SymPy required by import).
Observations: q1..q4=1, rewards q5,q6 and gate, six labeled actions.
"""
from PREFIX578_R2_mixed_cumulants_certificate import edge,ACTIONS
from fractions import Fraction as F
import json
weights={
 'S':(1,1,0),'D':(1,-1,0),'K':(0,0,1),
 'S+K':(1,1,1),'S-K':(1,1,-1),
 'D+K':(1,-1,1),'D-K':(1,-1,-1),
 'axis5':(1,0,0),'axis5+K':(1,0,1),'axis5-K':(1,0,-1)}
N=96
MAX_DEPTH=96
edges={name:[[ (j,sum(t*x for t,x in zip(v,(w[4],w[5],w[6]))))
          for a in ACTIONS for j,w in [edge(i,a)]] for i in range(N)]
       for name,v in weights.items()}
current={name:[[1]*N,[0]*N,[0]*N,[0]*N] for name in weights}
results=[]
for d in range(MAX_DEPTH+1):
    if d in (1,2,4,8,16,32,64,96):
        third={}
        for name,(mass,x,y,z) in current.items():
            assert all(t==6**d for t in mass)
            norm=96*6**d
            mu=F(sum(x),norm)
            m2=F(sum(y),norm)
            m3=F(sum(z),norm)
            third[name]=m3-3*m2*mu+2*mu**3
        b=third
        mixed={
           'S_K_K':(b['S+K']+b['S-K']-2*b['S'])/6,
           'S_S_K':(b['S+K']-b['S-K']-2*b['K'])/6,
           'D_D_K':(b['D+K']-b['D-K']-2*b['K'])/6,
           'D_K_K':(b['D+K']+b['D-K']-2*b['D'])/6,
           'axis5_K_K':(b['axis5+K']+b['axis5-K']-2*b['axis5'])/6}
        assert mixed['D_K_K']==0
        results.append({'depth':d,
          'third_rate_display':{name:f'{float(v/d):.12f}'
                                for name,v in mixed.items()},
          'gate_third_rate_display':f'{float(third["K"]/d):.12f}'})
    if d==MAX_DEPTH: break
    for name,row in edges.items():
        mass,x,y,z=current[name]
        nmass=[0]*N
        nx=[0]*N
        ny=[0]*N
        nz=[0]*N
        for i,arcs in enumerate(row):
            for j,r in arcs:
                nmass[i]+=mass[j]
                nx[i]+=x[j]+r*mass[j]
                ny[i]+=y[j]+2*r*x[j]+r*r*mass[j]
                nz[i]+=z[j]+3*r*y[j]+3*r*r*x[j]+r*r*r*mass[j]
        current[name]=[nmass,nx,ny,nz]
print(json.dumps({'status':'ALL_CHECKS_PASS','snapshots':results},indent=2))
