"""Critical H^{1/2} linearized NS energy bounds on the normalized torus.

Analytic full-tail bounds are in RESEARCH_NOTE.md. Floating-point spectra below
are diagnostics, NOT validated eigenvalue bounds. The interval Gershgorin bound
is the certified finite-block option for rational real/imaginary input coefficients.
"""
from __future__ import annotations
import math, itertools
from typing import Mapping
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh

Mode = tuple[int,int,int]
Modes = Mapping[Mode, np.ndarray]

def radius(k: Mode) -> float:
    return math.sqrt(sum(x*x for x in k))

def projector(k: Mode) -> np.ndarray:
    a=np.asarray(k,dtype=float); r2=float(a@a)
    if r2==0: raise ValueError('zero mode is excluded')
    return np.eye(3)-np.outer(a,a)/r2

def sphere_modes(n: int) -> list[Mode]:
    if type(n) is not int or n<1: raise ValueError('cutoff must be a positive integer')
    return [k for k in itertools.product(range(-n,n+1),repeat=3)
            if 0<sum(x*x for x in k)<=n*n]

def dweight(m: float) -> float:
    """Bound for each symmetrized displacement, when |k|,|l| >= 1."""
    if m<=0: return 0.
    t=math.sqrt(1+m)
    return .5*m*(1+t+1/t)

def beta(v: Modes) -> float:
    return sum(dweight(radius(m))*float(np.linalg.norm(a)) for m,a in v.items() if any(m))

def heat_exponent(v0: Modes, nu: float) -> float:
    if nu<=0: raise ValueError('nu must be positive')
    return 2/nu*sum(dweight(radius(m))*float(np.linalg.norm(a))/radius(m)**2
                    for m,a in v0.items() if any(m))

def T_block(k: Mode,l: Mode,v: Modes) -> np.ndarray:
    m=tuple(a-b for a,b in zip(k,l)); c=v.get(m)
    if c is None:return np.zeros((3,3),complex)
    z=np.asarray(c,complex); mv=np.asarray(m,float); lv=np.asarray(l,float)
    return 1j*math.sqrt(radius(k)/radius(l))*projector(k) @ \
         (np.dot(z,lv)*np.eye(3)+np.outer(z,mv)) @ projector(l)

def S_block(k: Mode,l: Mode,v: Modes) -> np.ndarray:
    """Minus Hermitian part; positive quadratic form = error growth."""
    m=tuple(a-b for a,b in zip(k,l)); c=v.get(m)
    if c is None:return np.zeros((3,3),complex)
    a=radius(k);b=radius(l);z=np.asarray(c,complex); mv=np.asarray(m,float)
    ratio=math.sqrt(a/b)
    core=(ratio-1/ratio)*np.dot(z,np.asarray(l,float))*np.eye(3) \
         +ratio*np.outer(z,mv)+(1/ratio)*np.outer(mv,z)
    return -.5j*projector(k) @ core @ projector(l)

def assemble(v: Modes,n: int,nu: float=1.,reserve: float=.25):
    """Return finite Hermitian S_v - reserve*nu*Lambda^2, allowing longitudinal modes.
    Longitudinal modes make the certificate conservative; no divergence-free
    perturbation mode is removed. Mean mode is fixed to zero.
    """
    ks=sphere_modes(n); ids={k:i for i,k in enumerate(ks)}
    rows=[];cols=[];vals=[]
    for l,j in ids.items():
      for m in v:
        k=tuple(l[a]+m[a] for a in range(3));i=ids.get(k)
        if i is None:continue
        block=S_block(k,l,v)
        for a in range(3):
          for b in range(3):
            z=block[a,b]
            if z!=0:rows.append(3*i+a);cols.append(3*j+b);vals.append(z)
      for a in range(3):
        rows.append(3*j+a);cols.append(3*j+a)
        vals.append(-reserve*nu*radius(l)**2)
    A=sparse.csr_matrix((vals,(rows,cols)),shape=(3*len(ks),)*2,dtype=complex)
    return A,ks

def tail_bound(a: float,b: float,h: float) -> float:
    return .5*(a+h+math.hypot(a-h,2*b))

def numerical_diagnostic(v:Modes,n:int,nu:float=1.) -> dict:
    A,ks=assemble(v,n,nu)
    av=float(eigsh(A,k=1,which='LA',return_eigenvectors=False,tol=1e-10)[0])
    row=np.asarray(abs(A).sum(axis=1)).ravel()+A.diagonal().real-abs(A.diagonal())
    ag=float(np.max(row));bv=beta(v);hv=bv-nu*n*n/4
    err=A-A.getH()
    return {'cutoff':n,'modes':len(ks),'matrix_size':A.shape[0],
      'Hermitian_roundoff_max':float(max(abs(err.data),default=0)),
      'largest_eigenvalue_diagnostic':av,'Gershgorin_float':ag,'beta':bv,
      'tail_diagonal_upper':hv,'tail_coupling_upper':bv,
      'full_bound_using_eigenvalue_UNVALIDATED':tail_bound(av,bv,hv),
      'full_bound_using_Gershgorin_float_UNVALIDATED':tail_bound(ag,bv,hv),
      'spectral_values_are_not_certificates':True}


def interval_gershgorin(v_rat: Mapping[Mode,tuple],n:int,nu=1):
    """Outward-rounded interval bound. Input coefficient components and nu are
    rational strings/integers, or pairs (real,imag), interpreted EXACTLY. No float input.
    Returns decimal interval endpoints: spectral bounds use upper endpoints.
    """
    import mpmath as mp
    from fractions import Fraction
    iv=mp.iv;iv.dps=40
    def q(x):
      if isinstance(x,float):raise TypeError('use rational input, never float')
      f=Fraction(x);return iv.mpf(f.numerator)/iv.mpf(f.denominator)
    zero=iv.mpf(0);one=iv.mpf(1)
    def rr(k):return iv.sqrt(sum(x*x for x in k))
    def matmul(A,B):
      return [[sum((A[i][l]*B[l][j] for l in range(3)),zero) for j in range(3)] for i in range(3)]
    def PP(k):
      r2=sum(x*x for x in k)
      return [[q(int(i==j))-q(k[i]*k[j])/r2 for j in range(3)] for i in range(3)]
    ks=sphere_modes(n);seen=set(ks); proj={k:PP(k) for k in ks}; rad={k:rr(k) for k in ks}
    def cr(x):
      if isinstance(x,(list,tuple)):
        if len(x)!=2:raise ValueError('complex rational input must be (real,imag)')
        if any(isinstance(t,float) for t in x):raise TypeError('use exact rational input')
        return Fraction(x[0]),Fraction(x[1])
      if isinstance(x,float):raise TypeError('use exact rational input')
      return Fraction(x),Fraction(0)
    exact={}
    for m,z in v_rat.items():
      if len(m)!=3 or any(type(x) is not int for x in m) or not any(m):
        raise ValueError('nonzero integer wavevectors required')
      if len(z)!=3:raise ValueError('three vector components required')
      exact[m]=[cr(x) for x in z]
    for m,z in exact.items():
      if any(sum(m[i]*z[i][j] for i in range(3)) for j in (0,1)):
        raise ValueError('reference must be divergence free')
      if exact.get(tuple(-x for x in m))!=[(a,-b) for a,b in z]:
        raise ValueError('conjugate negative modes required for real reference')
    if Fraction(nu)<=0:raise ValueError('nu must be positive')
    coeff={m:[iv.mpc(q(a),q(b)) for a,b in z] for m,z in exact.items()}
    bound=None
    boundary_rows={k:[zero for _ in range(3)] for k in ks}
    boundary_cols={}
    def iv_block(k,l,m,z):
      pk=proj.get(k);pl=proj.get(l)
      if pk is None: pk=PP(k)
      if pl is None: pl=PP(l)
      rk=rad.get(k);rl=rad.get(l)
      if rk is None:rk=rr(k)
      if rl is None:rl=rr(l)
      ratio=iv.sqrt(rk/rl);dot=sum((z[i]*l[i] for i in range(3)),zero)
      core=[[(ratio-1/ratio)*dot*int(i==j)+ratio*z[i]*m[j]+(1/ratio)*m[i]*z[j]
              for j in range(3)] for i in range(3)]
      return matmul(matmul(pk,core),pl)
    for k in ks:
      rows=[-q(nu)*sum(x*x for x in k)/4 for _ in range(3)]
      for m,z in coeff.items():
        l=tuple(k[j]-m[j] for j in range(3))
        if not any(l):continue
        block=iv_block(k,l,m,z)
        if l in seen:
          for i in range(3):rows[i]+=sum((abs(block[i][j])/2 for j in range(3)),zero)
        else:
          boundary_cols.setdefault(l,[zero for _ in range(3)])
          for i in range(3):boundary_rows[k][i]+=sum((abs(block[i][j])/2 for j in range(3)),zero)
          for j in range(3):boundary_cols[l][j]+=sum((abs(block[i][j])/2 for i in range(3)),zero)
      for row in rows:
        if bound is None or row.b > bound.b:bound=row
    be=zero;be_tail=zero
    for m,z in coeff.items():
      r=rr(m);t=iv.sqrt(1+r);tt=iv.sqrt(1+r/n)
      norm=iv.sqrt(sum((abs(x)**2 for x in z),zero))
      be+=r*(1+t+1/t)*norm/2
      be_tail+=r*(1+tt+1/tt)*norm/2
    br=max((x.b for v in boundary_rows.values() for x in v),default=zero)
    bc=max((x.b for v in boundary_cols.values() for x in v),default=zero)
    b=iv.sqrt(br*bc).b
    a=bound.b;h=be_tail.b-q(nu)*n*n/4
    full=(a+h+iv.sqrt((a-h)**2+4*b*b))/2
    return {'cutoff':n,'modes':len(ks),'matrix_size':3*len(ks),
      'finite_block_upper_interval':str(bound.b),'beta_upper_interval':str(be.b),
      'high_high_norm_upper_interval':str(be_tail.b),
      'boundary_coupling_upper_interval':str(b),
      'tail_upper_interval':str(h),'full_operator_upper_interval':str(full.b),
      'method':'40-decimal outward interval arithmetic, scalar Gershgorin + finite boundary Schur + analytic infinite tail',
      'input':'exact rational real/imaginary Fourier coefficients','no_floating_eigenvalue_used':True}


def cross_schur(v:Modes,n:int):
    """Numerical diagnostic only: finite low/high boundary row-column norm."""
    low=sphere_modes(n);lo=set(low);rows={k:np.zeros(3) for k in low};cols={}
    for k in low:
      for m in v:
        l=tuple(k[j]-m[j] for j in range(3))
        if l in lo or not any(l):continue
        block=abs(S_block(k,l,v))
        rows[k]+=block.sum(axis=1)
        cols.setdefault(l,np.zeros(3));cols[l]+=block.sum(axis=0)
    rm=max((max(z) for z in rows.values()),default=0.)
    cm=max((max(z) for z in cols.values()),default=0.)
    return math.sqrt(rm*cm),len(cols)


def single_shell_exponent(mu_upper, shell_squared=2, nu=1):
    """Validated exponent for the whole heat trajectory from one certified
    logarithmic-norm upper bound at time zero (convexity argument).
    Inputs must be rational strings/integers. Returns outward interval bounds.
    """
    import mpmath as mp
    from fractions import Fraction
    mp.iv.dps=40;iv=mp.iv
    def q(z):
      if isinstance(z,float):raise TypeError('use exact rational inputs')
      x=Fraction(z);return iv.mpf(x.numerator)/iv.mpf(x.denominator)
    if Fraction(nu)<=0 or Fraction(shell_squared)<=0:raise ValueError('positive viscosity and shell squared radius required')
    x=q(mu_upper)/q(nu)+q('1/4')
    if x.b<=q('1/4').a:exponent=q(0)
    elif x.a>q('1/4').b:exponent=2/q(shell_squared)*(x-q('1/4')-iv.log(4*x)/4)
    else:raise ValueError('resolve threshold interval before calling')
    return {'exponent_interval':str(exponent),'amplification_factor_interval':str(iv.exp(exponent))}

if __name__=='__main__':
    import json
    reference={(1,-1,0):('1/2','1/2',0),(-1,1,0):('1/2','1/2',0),
               (1,1,0):(0,0,'1/2'),(-1,-1,0):(0,0,'1/2'),
               (0,1,1):('1/6',0,0),(0,-1,-1):('1/6',0,0)}
    certified=interval_gershgorin(reference,8)
    import mpmath as mp
    assert mp.iv.mpf(certified['full_operator_upper_interval']).b < mp.iv.mpf('2.322').a
    print(json.dumps({'instantaneous':certified,
       'entire_heat_trajectory':single_shell_exponent('2.322')},indent=2))
