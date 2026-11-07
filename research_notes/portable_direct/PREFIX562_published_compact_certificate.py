#!/usr/bin/env python3
"""PREFIX-562: frozen native BRC 64-orbit semilinear exact certificate.
Requires PREFIX550_shared_gauge_compact_certificate.py and PREFIX561_native_port_bijection_certificate.py.
Science pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from collections import Counter
import json
import PREFIX550_shared_gauge_compact_certificate as b
import PREFIX561_native_port_bijection_certificate as p

f=p.construct_lift()
orbits=sorted({tuple(sorted({i,f[i]})) for i in range(96)})
reps=[x[0] for x in orbits]
orb={i:k for k,o in enumerate(orbits) for i in o}
flip={i:i!=reps[orb[i]] for i in range(96)}
def tau(m):return m[:4]+(m[5],m[4])+m[6:]
def step(rows,vec,twisted=False):
    out=[]
    for row in rows:
        a=Counter()
        for key,n in row.items():
            if twisted:j,sw,w=key
            else:j,w=key;sw=False
            for m,v in vec[j].items():
                mm=tau(m) if sw else m
                a[tuple(mm[k]+w[k] for k in range(7))]+=v*n
        out.append(a)
    return out
def rows96(r):
    return [Counter((j,w) for a in b.A for j,w in [b.edge(i,a,r)]) for i in range(96)]
def rows64(r):
    assert p.sigma_root(r)==r
    return [Counter((orb[j],flip[j],w) for a in b.A for j,w in [b.edge(i,a,r)]) for i in reps]
def check():
    assert len(orbits)==64 and sum(len(o)==1 for o in orbits)==32
    roots=(b.ZERO_ROOT,)+b.ROOTS
    fixed=[r for r in roots if p.sigma_root(r)==r]
    assert len(fixed)==9
    edges=0
    for r in roots:
        for i in range(96):
            for a in b.A:
                j,w=b.edge(i,a,r)
                assert sum(b.edge(f[i],aa,p.sigma_root(r))==(f[j],tau(w)) for aa in b.A)==1
                edges+=1
    comparisons=positions=0
    for r in fixed:
        rows=rows96(r);tw=rows64(r)
        x=[Counter({(0,)*7:1}) for _ in range(96)]
        y=[Counter({(0,)*7:1}) for _ in range(64)]
        limit=8 if r==b.ZERO_ROOT else 5
        for d in range(limit+1):
            for i in range(96):
                z=Counter({tau(m):v for m,v in y[orb[i]].items()}) if flip[i] else y[orb[i]]
                assert x[i]==z,(r,i,d)
                comparisons+=1;positions+=len(z)
            if d<limit:x=step(rows,x);y=step(tw,y,True)
    return {'status':'ALL_CHECKS_PASS','frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
            'native_edge_equivariance_checks':edges,'fixed_root_count':len(fixed),
            'generic_six_axis_64_orbit_exact_histogram_checks':comparisons,
            'checked_nonzero_integer_coefficient_positions':positions,
            'proof_scope':'all lengths by native edge equivariance and induction',
            'implementation_check_depth_zero_root':8,'implementation_check_depth_other_fixed_roots':5}
if __name__=='__main__':print(json.dumps(check(),ensure_ascii=False,indent=2))
