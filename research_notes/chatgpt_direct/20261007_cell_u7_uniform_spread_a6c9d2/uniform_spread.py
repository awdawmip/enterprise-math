"""U7 comparison interfaces for the unchanged U5 positive response circuit.
Density, adjoint and variance are comparison observers, NOT native dynamics.
"""
from __future__ import annotations
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
import hashlib, importlib.util, sys
ROOT=Path(__file__).resolve().parent
SRC=ROOT/'lifecycle.py'
if not SRC.exists(): SRC=ROOT.parent/'20261007_cell_u5_lifecycle_3e72b9'/'lifecycle.py'
raw=SRC.read_bytes()
if hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()!='389bd51a2a71a62a4c533ef781920bef00783bc3':
    raise RuntimeError('U5 source pin mismatch')
spec=importlib.util.spec_from_file_location('u7_pinned_u5',SRC)
u=importlib.util.module_from_spec(spec);sys.modules[spec.name]=u;spec.loader.exec_module(u)
c,r,o=u.c,u.r,u.o
A,D=0,1

def put(out,key,v):
    if v.live: out[key]=r.merge(out.get(key,r.brc.CWM_ZERO),v)

def scaled(v,q):
    return r.serial(v,r.edge(q)) if q else r.brc.CWM_ZERO

class Comparison:
    def __init__(self,rho=Q(1,4),epsilon=Q(1,8)):
        if not 0<rho<1 or not 0<epsilon<1: raise ValueError('open parameter range')
        self.rho,self.epsilon=rho,epsilon
        self.h=(1-rho)/epsilon
        self.mu=(Q(1),self.h)
        self.mu_min=min(self.mu);self.mu_max=max(self.mu)
        self.transport=c.RetainedField(rho)
        self.material={p:dict(col) for p,col in self.transport.material.items()}
        self.bulk=dict(self.transport.bulk)
        self.cv=r.serial(r.edge(1-rho),r.edge(1-epsilon)).total
        self.ce=r.serial(r.serial(r.edge(rho),r.edge(1-rho)),r.edge(Q(1,15))).total
        self.comparison_constant=Q(9216)*self.mu_max/min(self.cv,self.ce)
        self.nash_constant=Q(1152)/self.mu_min
        self.a=1/(self.comparison_constant*self.nash_constant)
        self.kernel_constant=max(8/self.mu_min,(18/self.a)**3)

    def column(self,x,p,cells):
        return self.material[p] if x in cells else self.bulk

    def row(self,key,cells,adjoint=False):
        s,z,p=key
        if s==D:
            return (((A,z,p),r.edge(self.epsilon)),((D,z,p),r.edge(1-self.epsilon)))
        ans=[((D,z,p),r.edge(1-self.rho))]
        if adjoint:
            for q,w in self.column(z,p,cells).items():
                ans.append(((A,r.advance(z,q),q^1),w))
        else:
            prev=r.advance(z,p);q=p^1
            for old in r.PORTS:
                w=self.column(prev,old,cells).get(q)
                if w is not None: ans.append(((A,prev,old),w))
        return tuple(ans)

    def apply(self,f,cells,adjoint=False):
        """Positive BRC density readout; forward calls the original U5 step."""
        cells=set(cells)
        if not adjoint:
            active={(0,z,p):v for (s,z,p),v in f.items() if s==A}
            dormant={(0,z,p):scaled(v,self.h) for (s,z,p),v in f.items() if s==D}
            fa,fd,parts=u.local_release_step(active,dormant,tuple(cells),1,self.transport,self.epsilon)
            out={(A,z,p):v for (src,z,p),v in fa.items()}
            out.update({(D,z,p):scaled(v,1/self.h) for (src,z,p),v in fd.items()})
            return out
        # Exact positive weighted transpose, not a new physical propagation.
        sites={z for s,z,p in f}
        sites|={r.advance(z,q) for z in tuple(sites) for q in r.PORTS}
        out={}
        for z in sorted(sites):
            for s in (A,D):
                for p in r.PORTS:
                    v=r.total(r.serial(f[old],w) for old,w in self.row((s,z,p),cells,True) if old in f)
                    if v.live:out[s,z,p]=v
        return out

    def norm(self,f,power=1):
        return sum((self.mu[s]*v.total**power for (s,z,p),v in f.items()),Q(0))

    def reference_energy(self,f):
        """Squared differences are comparison observations, not force/energy."""
        E=Q(0)
        for s in (A,D):
            for p in r.PORTS:
                sites={z for ss,z,pp in f if ss==s and pp==p}
                for j in range(6):
                    bases=sites|{r.advance(z,2*j+1) for z in sites}
                    for z in bases:
                        z1=r.advance(z,2*j)
                        d=f.get((s,z,p),r.brc.CWM_ZERO).total-f.get((s,z1,p),r.brc.CWM_ZERO).total
                        E+=self.mu[s]*d*d
        return E

    def graph_energy(self,f,adjoint=False):
        """Uniform subgraph of exact Jensen pairs, with the sector-swapped adjoint."""
        ss,tt=(D,A) if adjoint else (A,D)
        sites={z for s,z,p in f};vv=Q(0);ee=Q(0)
        for z in sites:
            for p in r.PORTS:
                d=f.get((A,z,p),r.brc.CWM_ZERO).total-f.get((D,z,p),r.brc.CWM_ZERO).total
                vv+=d*d
        bases=sites|{r.advance(z,q) for z in sites for q in r.PORTS}
        for z in bases:
            for p in r.PORTS:
                a=f.get((ss,z,p),r.brc.CWM_ZERO).total
                for q in r.PORTS:
                    if q==p^1:continue
                    b=f.get((tt,r.advance(z,q),q^1),r.brc.CWM_ZERO).total
                    ee+=(a-b)**2
        return self.cv*vv+self.ce*ee

    def jensen_identity(self,f,cells,adjoint=False):
        """Retain all nonzero comparison pairs at all possibly affected rows."""
        sites={z for s,z,p in f};sites|={r.advance(z,q) for z in tuple(sites) for q in r.PORTS}
        total=r.brc.CWM_ZERO;records=[]
        for z in sorted(sites):
            for s in (A,D):
                for p in r.PORTS:
                    row=self.row((s,z,p),set(cells),adjoint)
                    values=[f.get(key,r.brc.CWM_ZERO).total for key,w in row]
                    row_sum=r.total(w for key,w in row).total
                    if row_sum!=1:raise AssertionError('non-Markov comparison row')
                    for i,(a,w) in enumerate(row):
                        for j in range(i):
                            d=values[i]-values[j]
                            if not d:continue
                            b,v=row[j]
                            coeff=r.serial(scaled(w,self.mu[s]),v)
                            term=scaled(coeff,d*d)
                            total=r.merge(total,term)
                            records.append(((s,z,p),a,b,coeff,term))
        return total.total,records


def internal_path(z,p,t):
    """A-port change via one shared Jensen neighbor; NOT a physical path."""
    if p==t:return [(A,z,p)]
    q=next(q for q in r.PORTS if q not in (p^1,t^1))
    return [(A,z,p),(D,r.advance(z,q),q^1),(A,z,t)]


def reference_path(sector,p,j,adjoint=False):
    """Translation-covariant comparison certificate, length at most eight."""
    s=sector^int(adjoint);z=r.ZERO;end=r.advance(z,2*j);q=2*j
    pp=p if p!=q^1 else next(v for v in r.PORTS if v!=q^1)
    path=internal_path(z,p,pp)
    path.extend([(D,end,q^1),(A,end,q^1)])
    path.extend(internal_path(end,q^1,p)[1:])
    if s==D:path=[(D,z,p)]+path+[(D,end,p)]
    if adjoint:path=[(ss^1,x,port) for ss,x,port in path]
    return tuple(path)


def edge_type(a,b,adjoint=False):
    if adjoint:
        a=(a[0]^1,a[1],a[2]);b=(b[0]^1,b[1],b[2])
    if a[0]==D:a,b=b,a
    if a[0]!=A or b[0]!=D:raise ValueError('not a comparison graph edge')
    s,z,p=a;t,y,v=b
    if z==y and p==v:return ('vertical',p)
    q=v^1
    if y!=r.advance(z,q) or q==p^1:raise ValueError('missing uniform Jensen edge')
    return ('scatter',p,q)
