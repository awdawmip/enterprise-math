"""Finite Fourier checks for the forced helical heat-Gram balance.

Not an OpenAI candidate simulation, not an infinite-dimensional proof, and not
an independent Lean kernel check. All convolution outputs are retained.
Run: python check_forced_gram.py
Requires Python 3.10+ and numpy. Complex phases and input heat rates are retained.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np

Vec = tuple[int, int, int]
Field = dict[Vec, np.ndarray]
Packets = dict[Vec, dict[int, np.ndarray]]
ZERO = (0, 0, 0)

def r(k: Vec) -> float:
    return float(np.linalg.norm(k))

def add(*fields: Field) -> Field:
    out: Field = {}
    for f in fields:
        for k, v in f.items():
            out[k] = out.get(k, np.zeros(3, complex)) + v
    return out

def scale(f: Field, c: float) -> Field:
    return {k: c*v for k, v in f.items()}

def lam(f: Field, power: float) -> Field:
    return {k: r(k)**power*v for k, v in f.items() if k != ZERO}

def project(f: Field) -> Field:
    return {k: v - np.asarray(k)*np.dot(k, v)/np.dot(k, k)
            for k, v in f.items() if k != ZERO}

def helicity(f: Field, s: int) -> Field:
    f = project(f)
    return {k: (v + s*1j*np.cross(k, v)/r(k))/2 for k, v in f.items()}

def cross(f: Field, g: Field) -> Field:
    out: Field = {}
    for p, a in f.items():
        for q, b in g.items():
            k = tuple(p[i]+q[i] for i in range(3))
            out[k] = out.get(k, np.zeros(3, complex)) + np.cross(a,b)
    return out

def nonlinearity(u: Field) -> Field:
    omega = {k: 1j*np.cross(k, v) for k, v in u.items()}
    return project(cross(u, omega))

def inner(f: Field, g: Field, weight: float = 0) -> float:
    return float(sum(r(k)**weight*np.vdot(v, g.get(k,np.zeros(3,complex))).real
                     for k, v in f.items() if k != ZERO))

def put(out: Packets, k: Vec, sig: int, v: np.ndarray) -> None:
    # k=0 vanishes for the radial commutator: p+q=0 implies |p|=|q|.
    if k == ZERO:
        return
    row = out.setdefault(k, {})
    row[sig] = row.get(sig, np.zeros(3,complex)) + v

def packets(v: Field) -> Packets:
    out: Packets = {}
    for p,a in v.items():
        for q,b in v.items():
            k = tuple(p[i]+q[i] for i in range(3))
            sig = sum(i*i for i in p)+sum(i*i for i in q)
            put(out,k,sig,0.5*(r(p)-r(q))*np.cross(a,b))
    return out

def differential_packets(v: Field,h: Field) -> Packets:
    # Polarized full quadratic convolution, with ordered pairs combined exactly.
    out: Packets = {}
    for p,a in v.items():
        for q,b in h.items():
            k = tuple(p[i]+q[i] for i in range(3))
            sig = sum(i*i for i in p)+sum(i*i for i in q)
            put(out,k,sig,(r(p)-r(q))*np.cross(a,b))
    return out

def gram(a: Packets,b: Packets) -> float:
    total=0.0
    for k,row in a.items():
        other=b.get(k,{})
        for sig,x in row.items():
            for tau,y in other.items():
                total += np.vdot(x,y).real/(r(k)*(sig+tau))
    return float(total)

def instantaneous(a: Packets) -> Field:
    return {k:sum(row.values(),np.zeros(3,complex)) for k,row in a.items()}

def J(v: Field) -> float:
    a=packets(v)
    return gram(a,a)

def DJ(v: Field,h: Field) -> float:
    return 2*gram(packets(v),differential_packets(v,h))

def random_field(rng: np.random.Generator, modes: list[Vec], amp: float) -> Field:
    out: Field={}
    for k in modes:
        z=amp*(rng.normal(size=3)+1j*rng.normal(size=3))
        z=z-np.asarray(k)*np.dot(k,z)/np.dot(k,k)
        out[k]=z
        out[tuple(-i for i in k)]=np.conj(z)
    return out

def relative(a: float,b: float) -> float:
    return abs(a-b)/(1+abs(a)+abs(b))

def run() -> dict:
    rng=np.random.default_rng(20260909)
    modes=[(1,0,0),(0,1,0),(1,1,0),(1,0,1),(0,1,1),(2,1,0)]
    fmodes=[(1,0,0),(0,1,1),(2,0,1)]
    maxima={k:0.0 for k in ['heat_balance','critical_identity','forced_chain_rule',
                             'combined_inequality_violation','directional_fd']}
    cases=[]
    for i in range(12):
        nu=[0.2,1.0,3.0][i%3]
        u=random_field(rng,modes,0.1*(1+i%4))
        g=random_field(rng,fmodes,0.07*(1+i%3))
        n=nonlinearity(u)
        rhs=add(scale(lam(u,2),-nu),n,g)
        sectors=[helicity(u,s) for s in [1,-1]]
        C=[instantaneous(packets(v)) for v in sectors]
        K=inner(u,u,1); Q=inner(u,u,3)
        jj=sum(J(v) for v in sectors)
        A=sum(inner(c,c,-1) for c in C)
        IN=sum(DJ(v,helicity(n,s)) for v,s in zip(sectors,[1,-1]))
        IF=sum(DJ(v,helicity(g,s)) for v,s in zip(sectors,[1,-1]))
        Jdot=sum(DJ(v,helicity(rhs,s)) for v,s in zip(sectors,[1,-1]))
        heat=sum(DJ(v,scale(lam(v,2),-nu)) for v in sectors)
        pc=inner(u,n,1)
        pchelical=2*inner(lam(sectors[0],1),C[1])-2*inner(lam(sectors[1],1),C[0])
        Kdot=2*inner(u,rhs,1)
        Fdot=Jdot+nu**2*Kdot/4
        force_work=nu**2*inner(u,g,1)/2
        violation=max(0.,Fdot+nu**3*Q/4-(IN+IF+force_work))
        eps=2e-6
        fd=sum((J(add(v,scale(helicity(g,s),eps)))-J(add(v,scale(helicity(g,s),-eps))))/(2*eps)
               for v,s in zip(sectors,[1,-1]))
        errs={'heat_balance':relative(heat,-nu*A),'critical_identity':relative(pc,pchelical),
              'forced_chain_rule':relative(Jdot+nu*A,IN+IF),
              'combined_inequality_violation':violation/(1+abs(Fdot)+abs(IN)+abs(IF)+abs(force_work)),
              'directional_fd':relative(fd,IF)}
        for key,val in errs.items():
            maxima[key]=max(maxima[key],val)
        assert all(errs[k]<2e-9 for k in errs), (i,errs)
        assert jj>=-1e-12 and A>=-1e-12
        cases.append({'case':i,'nu':nu,'input_modes':len(u),'full_nonlinear_output_modes':len(n),
                      'K':K,'J':jj,'A':A,'I_NL':IN,'I_force':IF})
    return {'status':'PASS','cases':len(cases),'seed':20260909,
            'maximum_normalized_errors':maxima,
            'scope':'Finite Fourier algebra and floating-point consistency only; no PDE trajectory, candidate simulation, interval certification, or Lean build.',
            'checks':['Heat generator balance','helical critical identity','forced Frechet chain rule',
                      'combined positive-energy inequality','directional finite difference'],
            'case_data':cases}

if __name__=='__main__':
    result=run()
    destination=Path(__file__).with_name('check_results.json')
    destination.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='case_data'},indent=2))
