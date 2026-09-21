from __future__ import annotations
import json, math, time, platform, sys
from pathlib import Path
import numpy as np
from scipy import fft
from numba import njit
import scipy, numba


def operators(n:int):
    cutoff=n//3-1
    f=np.rint(fft.fftfreq(n)*n).astype(np.int64)
    g=np.arange(n//2+1,dtype=np.int64)
    k=np.array(np.meshgrid(f,f,g,indexing='ij'))
    k2=np.sum(k*k,axis=0)
    inv=1.0/np.where(k2==0,1,k2)
    keep=np.all(np.abs(k)<=cutoff,axis=0)
    return cutoff,k,k2,inv,keep

def initial_state(n:int,s:int,seed:int):
    cutoff=n//3-1
    rng=np.random.default_rng(seed)
    ax=np.arange(-cutoff,cutoff+1,dtype=np.int64)
    pts=np.array(np.meshgrid(ax,ax,ax,indexing='ij')).reshape(3,-1).T
    pos=((pts[:,2]>0)|((pts[:,2]==0)&(pts[:,1]>0))|((pts[:,2]==0)&(pts[:,1]==0)&(pts[:,0]>0)))
    pts=pts[pos]
    selected=pts[rng.choice(len(pts),s//2,replace=False)]
    h=np.zeros((3,n,n,n//2+1),dtype=np.complex128)
    for p in selected:
        a=rng.standard_normal(3)+1j*rng.standard_normal(3)
        a-=p*(np.dot(p,a)/np.dot(p,p))
        a/=np.sqrt(s)
        h[:,p[0]%n,p[1]%n,p[2]]=a
        if p[2]==0:
            h[:,(-p[0])%n,(-p[1])%n,0]=a.conjugate()
    return h

def fft_rhs(h,n,k,inv,keep):
    u=fft.irfftn(h,s=(n,n,n),axes=(1,2,3),norm='forward',workers=1)
    wh=1j*np.cross(k,h,axisa=0,axisb=0,axisc=0)
    w=fft.irfftn(wh,s=(n,n,n),axes=(1,2,3),norm='forward',workers=1)
    cross=np.cross(u,w,axisa=0,axisb=0,axisc=0)
    out=fft.rfftn(cross,axes=(1,2,3),norm='forward',workers=1)
    dot=np.sum(k*out,axis=0)*inv
    out-=k*dot
    out*=keep
    return out

def extract_support(h,n):
    loc=np.argwhere(np.any(h!=0,axis=0))
    a=np.ascontiguousarray(h[:,loc[:,0],loc[:,1],loc[:,2]].T)
    p=loc.copy()
    p[:,:2]=np.where(p[:,:2]<n//2,p[:,:2],p[:,:2]-n)
    mirror=p[:,2]>0
    return (np.ascontiguousarray(np.concatenate((p,-p[mirror]))),
            np.ascontiguousarray(np.concatenate((a,a[mirror].conjugate()))),
            int(len(p)+np.count_nonzero(mirror)), int(len(loc)))

@njit(cache=True,fastmath=False)
def grouped_rhs(p,a,n,cutoff):
    out=np.zeros((3,n,n,n//2+1),dtype=np.complex128)
    for i in range(len(p)):
        for j in range(i,len(p)):
            x,y,z=p[i,0]+p[j,0],p[i,1]+p[j,1],p[i,2]+p[j,2]
            if z<0 or z>cutoff or abs(x)>cutoff or abs(y)>cutoff:
                continue
            qa=p[j,0]*a[i,0]+p[j,1]*a[i,1]+p[j,2]*a[i,2]
            pa=p[i,0]*a[j,0]+p[i,1]*a[j,1]+p[i,2]*a[j,2]
            for d in range(3):
                v=qa*a[j,d]
                if i!=j: v+=pa*a[i,d]
                out[d,x%n,y%n,z]+=-1j*v
    for ix in range(n):
        x=ix if ix<n//2 else ix-n
        for iy in range(n):
            y=iy if iy<n//2 else iy-n
            for z in range(n//2+1):
                r=x*x+y*y+z*z
                if r:
                    b=(x*out[0,ix,iy,z]+y*out[1,ix,iy,z]+z*out[2,ix,iy,z])/r
                    out[0,ix,iy,z]-=x*b; out[1,ix,iy,z]-=y*b; out[2,ix,iy,z]-=z*b
    return out

def full_support_count(h,n):
    _,_,c,_=extract_support(h,n); return c

def relative_max(a,b):
    return float(np.max(np.abs(a-b))/max(float(np.max(np.abs(a))),1e-30))

def divergence_max(h,k):
    return float(np.max(np.abs(np.sum(k*h,axis=0))))

def energy(h,n):
    u=fft.irfftn(h,s=(n,n,n),axes=(1,2,3),norm='forward',workers=1)
    return float(0.5*np.mean(np.sum(u*u,axis=0)))

def calibrate(n=16, supports=(8,16,32,64,128,256), repeats=5):
    cutoff,k,k2,inv,keep=operators(n)
    rows=[]
    for s in supports:
        if s%2: continue
        h=initial_state(n,s,20260921+n+s)
        p,a,fc,sc=extract_support(h,n)
        fs=grouped_rhs(p,a,n,cutoff)
        ff=fft_rhs(h,n,k,inv,keep)
        err=relative_max(ff,fs)
        sparse=[]; guard=[]; dense=[]; combined=[]
        for r in range(repeats):
            t=time.perf_counter(); p,a,fc2,sc2=extract_support(h,n); tg=time.perf_counter()-t
            t=time.perf_counter(); grouped_rhs(p,a,n,cutoff); ts=time.perf_counter()-t
            t=time.perf_counter(); fft_rhs(h,n,k,inv,keep); td=time.perf_counter()-t
            guard.append(tg); sparse.append(ts); combined.append(tg+ts); dense.append(td)
        rows.append(dict(requested_full_modes=s,actual_full_modes=fc,stored_modes=sc,
                         rhs_relative_max_error=err,
                         guard_median_s=float(np.median(guard)),
                         sparse_kernel_median_s=float(np.median(sparse)),
                         guard_plus_sparse_median_s=float(np.median(combined)),
                         dense_fft_median_s=float(np.median(dense))))
    eligible=[r['actual_full_modes'] for r in rows if r['guard_plus_sparse_median_s'] < r['dense_fft_median_s'] and r['rhs_relative_max_error'] <= 2e-11]
    threshold=max(eligible) if eligible else 0
    return rows,threshold

class EvalStats:
    def __init__(self): self.calls=[]

def hybrid_nonlinear(h,n,cutoff,k,inv,keep,threshold,stats:EvalStats):
    t0=time.perf_counter(); p,a,full_count,stored=extract_support(h,n); guard=time.perf_counter()-t0
    if full_count<=threshold:
        t=time.perf_counter(); out=grouped_rhs(p,a,n,cutoff); comp=time.perf_counter()-t; route='SPARSE'
    else:
        t=time.perf_counter(); out=fft_rhs(h,n,k,inv,keep); comp=time.perf_counter()-t; route='FFT_FALLBACK'
    stats.calls.append(dict(route=route,full_support=full_count,stored_support=stored,guard_s=guard,compute_s=comp,total_eval_s=guard+comp))
    return out

def dense_rhs(h,n,k,k2,inv,keep,nu,stats):
    t=time.perf_counter(); nl=fft_rhs(h,n,k,inv,keep); nonlinear=time.perf_counter()-t
    out=nl - nu*k2*h
    stats.append(nonlinear)
    return out

def hybrid_rhs(h,n,cutoff,k,k2,inv,keep,nu,threshold,stats):
    return hybrid_nonlinear(h,n,cutoff,k,inv,keep,threshold,stats) - nu*k2*h

def rk4_step_dense(y,dt,args,stats):
    n,k,k2,inv,keep,nu=args
    k1=dense_rhs(y,n,k,k2,inv,keep,nu,stats)
    k2v=dense_rhs(y+0.5*dt*k1,n,k,k2,inv,keep,nu,stats)
    k3=dense_rhs(y+0.5*dt*k2v,n,k,k2,inv,keep,nu,stats)
    k4=dense_rhs(y+dt*k3,n,k,k2,inv,keep,nu,stats)
    return (y+(dt/6)*(k1+2*k2v+2*k3+k4))*keep

def rk4_step_hybrid(y,dt,args,threshold,stats):
    n,cutoff,k,k2,inv,keep,nu=args
    k1=hybrid_rhs(y,n,cutoff,k,k2,inv,keep,nu,threshold,stats)
    k2v=hybrid_rhs(y+0.5*dt*k1,n,cutoff,k,k2,inv,keep,nu,threshold,stats)
    k3=hybrid_rhs(y+0.5*dt*k2v,n,cutoff,k,k2,inv,keep,nu,threshold,stats)
    k4=hybrid_rhs(y+dt*k3,n,cutoff,k,k2,inv,keep,nu,threshold,stats)
    return (y+(dt/6)*(k1+2*k2v+2*k3+k4))*keep

def run_case(seed,s,threshold,n=16,steps=5,dt=5e-4,nu=1e-2):
    cutoff,k,k2,inv,keep=operators(n)
    y0=initial_state(n,s,seed)
    dense=y0.copy(); hybrid=y0.copy()
    dense_times=[]; hs=EvalStats(); step_rows=[]
    for step in range(steps):
        td=time.perf_counter(); dense=rk4_step_dense(dense,dt,(n,k,k2,inv,keep,nu),dense_times); td=time.perf_counter()-td
        th=time.perf_counter(); hybrid=rk4_step_hybrid(hybrid,dt,(n,cutoff,k,k2,inv,keep,nu),threshold,hs); th=time.perf_counter()-th
        step_rows.append(dict(step=step+1,dense_step_s=td,hybrid_step_s=th,
                              rel_max_state=relative_max(dense,hybrid),
                              dense_full_support=full_support_count(dense,n),
                              hybrid_full_support=full_support_count(hybrid,n),
                              dense_divergence_max=divergence_max(dense,k),
                              hybrid_divergence_max=divergence_max(hybrid,k),
                              dense_energy=energy(dense,n),hybrid_energy=energy(hybrid,n)))
    return dict(seed=seed,initial_full_modes=s,n=n,steps=steps,dt=dt,nu=nu,threshold_full_modes=threshold,
                final_relative_max_state=relative_max(dense,hybrid),
                final_energy_relative_error=abs(energy(dense,n)-energy(hybrid,n))/max(abs(energy(dense,n)),1e-30),
                route_counts={r:sum(c['route']==r for c in hs.calls) for r in ['SPARSE','FFT_FALLBACK']},
                hybrid_calls=hs.calls,step_rows=step_rows,
                dense_total_s=float(sum(x['dense_step_s'] for x in step_rows)),
                hybrid_total_s=float(sum(x['hybrid_step_s'] for x in step_rows)))

def main(out='/tmp/cfd_r10_results.json'):
    h=initial_state(16,8,1); c,k,k2,inv,keep=operators(16); p,a,*_=extract_support(h,16)
    t=time.perf_counter(); grouped_rhs(p,a,16,c); warm=time.perf_counter()-t
    cal,threshold=calibrate()
    cases=[run_case(seed,s,threshold) for seed,s in [(91001,16),(91003,32),(91007,64)]]
    payload={
      'status':'SURROGATE_3D_FULL_TRAJECTORY_CHECKPOINT_NOT_SPECTRALDNS_NATIVE_HOST',
      'source_model':'research_notes/CFD-B1F673/prior_3d/probe.py formulas reimplemented for bounded RK4 checkpoint',
      'frozen':{'n':16,'cutoff':16//3-1,'precision':'complex128/float64','fft_norm':'forward','fft_workers':1,'viscosity':1e-2,'dt':5e-4,'steps':5,'source':'zero','dealiasing':'retained cube |k_i|<=4; N>3K','integrator':'classical fixed-step RK4'},
      'jit_warmup_s':warm,'calibration':cal,'calibrated_sparse_threshold_full_modes':threshold,'cases':cases,
      'environment':{'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__,'numba':numba.__version__,'platform':platform.platform()},
      'limits':['not spectralDNS/shenfun/FFTW native host','not MPI','not production benchmark','threshold calibrated only on this surrogate host/grid','strict h!=0 support','no approximate pruning','no speedup claim beyond observed surrogate timing']
    }
    Path(out).write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps({'threshold':threshold,'case_summary':[{k:c[k] for k in ['seed','initial_full_modes','final_relative_max_state','route_counts','dense_total_s','hybrid_total_s']} for c in cases]},indent=2))
if __name__=='__main__': main()
