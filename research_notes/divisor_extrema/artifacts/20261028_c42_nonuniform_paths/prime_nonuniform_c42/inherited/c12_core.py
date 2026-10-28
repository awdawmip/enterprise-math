"""C12: prime-factor cell complex, positive C2-BRC weights and loop observers.

Finite exact arithmetic. Graph axes are prime labels, not native spatial axes.
Native source bytes are verified. The one unused relative import is omitted
only from the in-memory AST; native definitions are otherwise unchanged.
"""
from __future__ import annotations
import ast
import hashlib
import itertools
import sys
import types
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parent
SOURCE_BLOB='9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1'

def load_native():
    path=ROOT/'native/brc_histogram.py'; data=path.read_bytes()
    got=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    if got!=SOURCE_BLOB: raise ValueError('Unverified BRC source')
    tree=ast.parse(data,filename=str(path))
    rm=[x for x in tree.body if isinstance(x,ast.ImportFrom) and x.level]
    if len(rm)!=1 or rm[0].module!='brc_rational_holonomy': raise ValueError('Unexpected imports')
    tree.body=[x for x in tree.body if x not in rm]
    mod=types.ModuleType('_c12_native'); mod.__file__=str(path)
    sys.modules[mod.__name__]=mod
    exec(compile(tree,str(path),'exec'),mod.__dict__)
    return mod
native=load_native()

def factor(n:int)->dict[int,int]:
    if n<1: raise ValueError('Positive integers only')
    out={}; d=2
    while d*d<=n:
        while n%d==0: out[d]=out.get(d,0)+1; n//=d
        d+=1
    if n>1: out[n]=out.get(n,0)+1
    return out

def divisors(n:int)->tuple[int,...]:
    out=[1]
    for p,a in factor(n).items(): out=[d*p**j for d in out for j in range(a+1)]
    return tuple(sorted(out))

@dataclass
class Complex:
    vertices:tuple[int,...]
    edges:tuple[tuple[int,int,int],...]
    faces:tuple[tuple[int,int,int,int],...] # bottom,p,q,edge boundary mask
    def face_index(self,bottom=1,p=2,q=3):
        return next(i for i,x in enumerate(self.faces) if x[:3]==(bottom,p,q))

def complex_on(vertices)->Complex:
    vs=tuple(sorted(vertices)); present=set(vs)
    edges=[]
    for v in vs:
        for p in factor(v):
            if v//p in present: edges.append((v//p,v,p))
    edges=tuple(sorted(edges)); idx={(u,v):i for i,(u,v,p) in enumerate(edges)}
    faces=[]
    for v in vs:
        for p,q in itertools.combinations(sorted(factor(v)),2):
            u=v//(p*q)
            if all(w in present for w in (u,u*p,u*q)):
                boundary=0
                for e in [(u,u*p),(u*p,v),(u,u*q),(u*q,v)]: boundary ^=1<<idx[e]
                faces.append((u,p,q,boundary))
    return Complex(vs,edges,tuple(sorted(faces)))

def kernel_basis(masks):
    """Kernel of subset-to-XOR-boundary map, retaining provenance of rows."""
    pivots={}; kernel=[]
    for i,row in enumerate(masks):
        val=row; coeff=1<<i
        while val:
            bit=val.bit_length()-1
            if bit not in pivots:
                pivots[bit]=(val,coeff); break
            prior,c=pivots[bit]; val^=prior; coeff^=c
        if not val: kernel.append(coeff)
    return pivots,tuple(kernel)

def particular(pivots,target):
    coeff=0
    while target:
        b=target.bit_length()-1
        if b not in pivots: return None
        row,c=pivots[b]; target^=row; coeff^=c
    return coeff

def span(basis):
    states=[0]
    for b in basis: states += [x^b for x in states]
    return states

def boundary_histograms(g:Complex,mask:int,maxdim=18):
    pivots,kernel=kernel_basis([f[3] for f in g.faces])
    if len(kernel)>maxdim: raise ValueError('Declared finite enumeration cap')
    states=span(kernel); part=particular(pivots,mask)
    den=Counter(x.bit_count() for x in states)
    num=Counter((x^part).bit_count() for x in states) if part is not None else Counter()
    return den,num,len(pivots),len(kernel)

def brc_polynomial(coeff:Counter,t:F)->F:
    """Positive subset counts -> BRC weighted branches, then mass observer."""
    out=native.weight_histogram([])
    h=native.weight_histogram([1]); powers={0:h}
    for j in range(1,max(coeff,default=0)+1):
        h=native.histogram_serial(h,native.weight_histogram([t] if t else []))
        powers[j]=h
    for j,count in coeff.items():
        repeat=native.WeightHistogram(((F(1),count),))
        out=native.histogram_recoalesce(out,native.histogram_serial(repeat,powers[j]))
    return out.total_mass

def loop_expectation(g,mask,t):
    den,num,rank,dim=boundary_histograms(g,mask)
    return brc_polynomial(num,t)/brc_polynomial(den,t)

def direct_assignments(g:Complex,t:F,mask:int,save=False):
    """Full positive edge assignment enumeration; native BRC per local factor."""
    if len(g.edges)>14: raise ValueError('Direct enumeration restricted to E<=14')
    even=native.weight_histogram([]); odd=native.weight_histogram([])
    rows=[]; supported=0; evals=0
    for z in range(1<<len(g.edges)):
        h=native.weight_histogram([1]); signs=[]
        for face in g.faces:
            s=1-2*((face[3]&z).bit_count()%2); signs.append(s)
            w=1+t*s
            if w==0: h=native.weight_histogram([]); break
            h=native.histogram_serial(h,native.weight_histogram([w])); evals+=1
        mass=h.total_mass
        if mass:
            supported+=1; sign=1-2*((mask&z).bit_count()%2)
            if sign==1: even=native.histogram_recoalesce(even,h)
            else: odd=native.histogram_recoalesce(odd,h)
            if save: rows.append({'bits':z,'face_signs':signs,'weight':str(mass),'loop_sign':sign})
    total=even.total_mass+odd.total_mass
    chi=(even.total_mass-odd.total_mass)/total
    # Explicit relative-phase quantum observer: diag parity unitaries, convex mixture.
    pe=even.total_mass/total; po=odd.total_mass/total
    assert pe+po==1 and -1<=chi<=1
    assert ((1+chi)/2,(1-chi)/2)==(pe,po)
    return {'chi':chi,'normalizer':total,'support':supported,'raw_assignments':1<<len(g.edges),'native_serial_calls':evals,'rows':rows}

def cycle_mask(g:Complex,path1,path2):
    edges={tuple(sorted((u,v))):i for i,(u,v,p) in enumerate(g.edges)}
    mask=0
    for path in [path1,path2]:
        for u,v in zip(path,path[1:]): mask^=1<<edges[tuple(sorted((u,v)))]
    return mask

def serialize(obj):
    if isinstance(obj,F): return str(obj)
    if isinstance(obj,Counter): return {str(k):v for k,v in sorted(obj.items())}
    if isinstance(obj,dict): return {str(k):serialize(v) for k,v in obj.items()}
    if isinstance(obj,(list,tuple)): return [serialize(x) for x in obj]
    return obj
