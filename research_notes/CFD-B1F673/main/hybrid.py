"""Serial, finite Fourier-Galerkin NS hybrid; no pruning by default.

Keeps the unprojected rotational RHS as the host interface: P g alone does not
preserve the host pressure readout. Reuses the imported baseline without edits.
Not a continuous-PDE certificate, not a production spectralDNS integration.
"""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import sys
import time
import numpy as np
from numba import njit
from scipy import fft
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'prior_3d'))
import probe

@njit(cache=True, fastmath=False)
def rotational_pairs(p, a, n, cutoff):
    """Exact pair aggregation for g=F[u x curl(u)], BEFORE pressure projection."""
    w = np.empty_like(a)
    for j in range(len(p)):
        w[j,0] = 1j*(p[j,1]*a[j,2]-p[j,2]*a[j,1])
        w[j,1] = 1j*(p[j,2]*a[j,0]-p[j,0]*a[j,2])
        w[j,2] = 1j*(p[j,0]*a[j,1]-p[j,1]*a[j,0])
    out = np.zeros((3,n,n,n//2+1), dtype=np.complex128)
    for i in range(len(p)):
        for j in range(i,len(p)):
            x,y,z = p[i,0]+p[j,0],p[i,1]+p[j,1],p[i,2]+p[j,2]
            if z < 0 or z > cutoff or abs(x)>cutoff or abs(y)>cutoff:
                continue
            v0=a[i,1]*w[j,2]-a[i,2]*w[j,1]
            v1=a[i,2]*w[j,0]-a[i,0]*w[j,2]
            v2=a[i,0]*w[j,1]-a[i,1]*w[j,0]
            if i != j:
                v0+=a[j,1]*w[i,2]-a[j,2]*w[i,1]
                v1+=a[j,2]*w[i,0]-a[j,0]*w[i,2]
                v2+=a[j,0]*w[i,1]-a[j,1]*w[i,0]
            out[0,x%n,y%n,z]+=v0
            out[1,x%n,y%n,z]+=v1
            out[2,x%n,y%n,z]+=v2
    return out

def fft_rotational(h, n):
    """Unprojected counterpart of the exact same baseline rotational formula."""
    _,k,_,_=probe.operators(n)
    return fft_rotational_with_k(h,n,k)

def fft_rotational_with_k(h,n,k):
    u=fft.irfftn(h,s=(n,n,n),axes=(1,2,3),norm='forward',workers=1)
    wh=1j*np.cross(k,h,axisa=0,axisb=0,axisc=0)
    w=fft.irfftn(wh,s=(n,n,n),axes=(1,2,3),norm='forward',workers=1)
    return fft.rfftn(np.cross(u,w,axisa=0,axisb=0,axisc=0),axes=(1,2,3),norm='forward',workers=1)

def project(g,k,inv,keep):
    pressure_proxy=np.sum(k*g,axis=0)*inv
    return (g-k*pressure_proxy)*keep, pressure_proxy*keep

def support_count(h):
    mask=np.any(h!=0,axis=0)
    return int(np.count_nonzero(mask[:,:,0])+2*np.count_nonzero(mask[:,:,1:])), mask

@dataclass(frozen=True)
class Config:
    n:int=32
    viscosity:float=0.01
    sparse_limit:int=384
    sticky_dense:bool=True

class Hybrid:
    """Switch only evaluation method; never changes coefficients or retained cube.

    Once a dense stage is observed, sticky_dense avoids all later support scans.
    This is a performance policy, NOT an assumption that support cannot shrink.
    An explicit reset makes a new trajectory eligible for sparse work again.
    """
    def __init__(self,config:Config,mode:str='hybrid'):
        if mode not in ('hybrid','fft'): raise ValueError('mode must be hybrid or fft')
        if not np.isfinite(config.viscosity) or config.viscosity<0: raise ValueError('invalid viscosity')
        if config.sparse_limit<0: raise ValueError('invalid sparse limit')
        self.config=config; self.mode=mode
        self.cutoff,self.k,self.inv,self.keep=probe.operators(config.n)
        self.k2=np.sum(self.k*self.k,axis=0)
        self.dense=False
        self.stats={'sparse_calls':0,'fft_calls':0,'scan_calls':0,'scan_seconds':0.,
                    'kernel_seconds':0.,'projection_diffusion_seconds':0.,'first_stage_supports':[]}
    def validate_input(self,h):
        n=self.config.n
        if h.shape!=(3,n,n,n//2+1) or h.dtype!=np.complex128: raise ValueError('requires serial complex128 rFFT array')
        if not np.isfinite(h).all(): raise ValueError('nonfinite input')
        if np.any(h[:,~self.keep]!=0): raise ValueError('input outside frozen retained cube')
        # Real-valued input: the k_z=0 plane must be Hermitian; Nyquist is zero.
        ix=(-np.arange(n))%n
        if not np.allclose(h[:,:,:,0],np.take(np.take(h[:,:,:,0],ix,axis=1),ix,axis=2).conjugate(),rtol=0,atol=1e-13):
            raise ValueError('non-Hermitian zero plane')
    def rotational(self,h):
        use_sparse=False
        if self.mode=='hybrid' and not self.dense:
            t=time.perf_counter(); count,_=support_count(h)
            self.stats['scan_seconds']+=time.perf_counter()-t; self.stats['scan_calls']+=1
            if len(self.stats['first_stage_supports'])<12: self.stats['first_stage_supports'].append(count)
            use_sparse=count<=self.config.sparse_limit
            if not use_sparse and self.config.sticky_dense: self.dense=True
        t=time.perf_counter()
        if use_sparse:
            p,a=probe.extract_support(h,self.config.n)
            g=rotational_pairs(p,a,self.config.n,self.cutoff)
            self.stats['sparse_calls']+=1
        else:
            g=fft_rotational_with_k(h,self.config.n,self.k)
            self.stats['fft_calls']+=1
        self.stats['kernel_seconds']+=time.perf_counter()-t
        return g
    def rhs(self,h):
        g=self.rotational(h)
        t=time.perf_counter()
        rhs,pressure_proxy=project(g,self.k,self.inv,self.keep)
        rhs-=self.config.viscosity*self.k2*h
        self.stats['projection_diffusion_seconds']+=time.perf_counter()-t
        return rhs

def rk4(h,engine,dt,steps):
    if not np.isfinite(dt) or dt<=0 or not isinstance(steps,int) or steps<1:
        raise ValueError('positive dt and integer steps required')
    engine.validate_input(h)
    y=h.copy()
    for _ in range(steps):
        a=engine.rhs(y); b=engine.rhs(y+dt/2*a)
        c=engine.rhs(y+dt/2*b); d=engine.rhs(y+dt*c)
        y+=dt/6*(a+2*b+2*c+d)
        if not np.isfinite(y).all(): raise FloatingPointError('nonfinite trajectory; reduce timestep or inspect input')
    return y

def shear(n):
    h=np.zeros((3,n,n,n//2+1),complex)
    h[0,0,1,0]=-0.5j; h[0,0,n-1,0]=0.5j
    return h

def propose_pruning(h,mask):
    """Proposal only, never called by RK4. No certificate/acceptance is implied."""
    if mask.shape!=h.shape[1:] or mask.dtype!=bool: raise ValueError('boolean spectral mask required')
    n=h.shape[1]; ix=(-np.arange(n))%n
    if not np.array_equal(mask[:,:,0],mask[ix,:,0][:,ix]): raise ValueError('mask must retain conjugate pairs')
    return h*mask,h*(~mask),{'status':'UNVERIFIED_PROPOSAL_DO_NOT_USE_AS_CERTIFIED_TRAJECTORY',
                             'missing_bounds':['roundoff','time_discretization','unresolved_modes','error_propagation']}

class SerialSpectralDNSAdapter:
    """Restricted velocity+pressure safe callback for getConvection('Vortex').

    Only serial cubic 2pi domains, complex128, last-axis rFFT, and this frozen
    cutoff are supported. coefficient_scale_to_forward must be established by
    the host (forward-normalized=1, backward-normalized=1/n**3). No guessing.
    Dense calls go to the UNCHANGED host callback. Returned sparse g is NOT
    projected: spectralDNS's pressure/diffusion stage must see its gradient.
    Host shenfun/MPI integration is untested in this environment.
    """
    def __init__(self,n,dense_callback,*,coefficient_scale_to_forward,
                 comm_size=1,domain=(2*np.pi,)*3,cutoff=None,sparse_limit=384):
        if comm_size!=1 or not np.allclose(domain,(2*np.pi,)*3,rtol=0,atol=1e-14):
            raise ValueError('unsupported communicator/domain')
        if cutoff!=n//3-1: raise ValueError('explicit frozen cutoff required')
        if not callable(dense_callback): raise TypeError('dense callback required')
        scale=float(coefficient_scale_to_forward)
        if not np.isfinite(scale) or scale<=0: raise ValueError('explicit positive normalization scale required')
        self.scale=scale; self.original=dense_callback
        self.engine=Hybrid(Config(n=n,sparse_limit=sparse_limit))
        self.n=n
    def __call__(self,rhs,u_hat,work,Tp,VTp,K,u_dealias):
        h=np.asarray(u_hat)
        self.engine.validate_input(h*self.scale)
        if not np.array_equal(np.asarray(K),self.engine.k): raise ValueError('unsupported wavevector layout')
        if self.engine.dense: return self.original(rhs,u_hat,work,Tp,VTp,K,u_dealias)
        count,_=support_count(h)
        if count>self.engine.config.sparse_limit:
            self.engine.dense=True
            return self.original(rhs,u_hat,work,Tp,VTp,K,u_dealias)
        p,a=probe.extract_support(h*self.scale,self.n)
        rhs[:]=rotational_pairs(p,a,self.n,self.engine.cutoff)/self.scale
        return rhs
