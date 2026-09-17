from __future__ import annotations
import hashlib, importlib.util, json, math, platform, statistics, sys, time
from pathlib import Path
import numpy as np
from scipy import fft
from numba import njit

ROOT=Path(__file__).resolve().parents[1]
ARTIFACT=ROOT/'research_artifacts/CFD_SPECTRAL_HYBRID_292BCE_20260917'
spec=importlib.util.spec_from_file_location('sca',ARTIFACT/'static_carrier_native_adapter.py')
sca=importlib.util.module_from_spec(spec); sys.modules['sca']=sca; spec.loader.exec_module(sca)

TASK='RS-CFD-SPECTRAL-HYBRID-20260910'
RESEARCHER='EM-DIRECT-292BCE'
N=16
K=N//2-1
M=3*N//2
LIMIT=384
DT=0.002
STEPS=12
NU=0.01
REPEATS=7


def native_operators(n):
    cutoff=n//2-1
    f=np.rint(fft.fftfreq(n)*n).astype(np.int64)
    g=np.arange(n//2+1,dtype=np.int64)
    k=np.array(np.meshgrid(f,f,g,indexing='ij'))
    k2=np.sum(k*k,axis=0); inv=1.0/np.where(k2==0,1,k2)
    keep=np.all(np.abs(k)<=cutoff,axis=0)
    return cutoff,k,k2,inv,keep

class DealiasedFFT:
    """Independent 3/2 padded finite-Galerkin rotational evaluator, not spectralDNS."""
    def __init__(self,n):
        self.n=n; self.K=n//2-1; self.M=3*n//2
        fn=np.rint(fft.fftfreq(n)*n).astype(np.int64)
        fm=np.rint(fft.fftfreq(self.M)*self.M).astype(np.int64)
        gm=np.arange(self.M//2+1,dtype=np.int64)
        self.km=np.array(np.meshgrid(fm,fm,gm,indexing='ij'))
        self.valid=[(i,int(x)) for i,x in enumerate(fn) if abs(x)<=self.K]
    def rotational(self,h):
        hp=np.zeros((3,self.M,self.M,self.M//2+1),dtype=np.complex128)
        for ix,x in self.valid:
            for iy,y in self.valid:
                hp[:,x%self.M,y%self.M,:self.K+1]=h[:,ix,iy,:self.K+1]
        u=fft.irfftn(hp,s=(self.M,)*3,axes=(1,2,3),norm='forward',workers=1)
        wh=1j*np.cross(self.km,hp,axisa=0,axisb=0,axisc=0)
        w=fft.irfftn(wh,s=(self.M,)*3,axes=(1,2,3),norm='forward',workers=1)
        gp=fft.rfftn(np.cross(u,w,axisa=0,axisb=0,axisc=0),axes=(1,2,3),norm='forward',workers=1)
        g=np.zeros_like(h)
        for ix,x in self.valid:
            for iy,y in self.valid:
                g[:,ix,iy,:self.K+1]=gp[:,x%self.M,y%self.M,:self.K+1]
        return g

@njit(cache=False,fastmath=False)
def rotational_pairs_into(p,a,out,n,cutoff):
    out[:] = 0
    w=np.empty_like(a)
    for j in range(len(p)):
        w[j,0]=1j*(p[j,1]*a[j,2]-p[j,2]*a[j,1])
        w[j,1]=1j*(p[j,2]*a[j,0]-p[j,0]*a[j,2])
        w[j,2]=1j*(p[j,0]*a[j,1]-p[j,1]*a[j,0])
    for i in range(len(p)):
        for j in range(i,len(p)):
            x,y,z=p[i,0]+p[j,0],p[i,1]+p[j,1],p[i,2]+p[j,2]
            if z<0 or z>cutoff or abs(x)>cutoff or abs(y)>cutoff: continue
            v0=a[i,1]*w[j,2]-a[i,2]*w[j,1]
            v1=a[i,2]*w[j,0]-a[i,0]*w[j,2]
            v2=a[i,0]*w[j,1]-a[i,1]*w[j,0]
            if i!=j:
                v0+=a[j,1]*w[i,2]-a[j,2]*w[i,1]
                v1+=a[j,2]*w[i,0]-a[j,0]*w[i,2]
                v2+=a[j,0]*w[i,1]-a[j,1]*w[i,0]
            out[0,x%n,y%n,z]+=v0; out[1,x%n,y%n,z]+=v1; out[2,x%n,y%n,z]+=v2
    return out

def extract_support(h,n):
    loc=np.argwhere(np.any(h!=0,axis=0))
    a=np.ascontiguousarray(h[:,loc[:,0],loc[:,1],loc[:,2]].T)
    p=loc.copy(); p[:,:2]=np.where(p[:,:2]<n//2,p[:,:2],p[:,:2]-n)
    mirror=p[:,2]>0
    return (np.ascontiguousarray(np.concatenate((p,-p[mirror]))),
            np.ascontiguousarray(np.concatenate((a,a[mirror].conjugate()))))

def project(g,k,inv,keep):
    pressure=np.sum(k*g,axis=0)*inv
    return (g-k*pressure)*keep

class FFTEngine:
    def __init__(self,n=N):
        self.n=n; self.cutoff,self.k,self.k2,self.inv,self.keep=native_operators(n); self.fft=DealiasedFFT(n)
        self.stats={'fft_calls':0,'nonlinear_seconds':0.0,'projection_diffusion_seconds':0.0}
    def rhs(self,h):
        t=time.perf_counter(); g=self.fft.rotational(h); self.stats['nonlinear_seconds']+=time.perf_counter()-t; self.stats['fft_calls']+=1
        t=time.perf_counter(); r=project(g,self.k,self.inv,self.keep)-NU*self.k2*h; self.stats['projection_diffusion_seconds']+=time.perf_counter()-t
        return r

class StaticEngine:
    def __init__(self,h0,n=N,limit=LIMIT):
        self.n=n; self.cutoff,self.k,self.k2,self.inv,self.keep=native_operators(n); self.fft=DealiasedFFT(n)
        self.stats={'detector_seconds':0.0,'decision':None,'carrier_size':None,'lower_bound':None,'detector_rounds':None,'detector_pair_tests':None,
                    'gather_seconds':0.0,'allocation_seconds':0.0,'nonlinear_seconds':0.0,'projection_diffusion_seconds':0.0,'static_sparse_calls':0,'fft_calls':0}
        t=time.perf_counter(); p0,_=extract_support(h0,n); res=sca.truncated_additive_carrier((tuple(map(int,v)) for v in p0),self.cutoff,limit); self.stats['detector_seconds']=time.perf_counter()-t
        self.stats.update(decision=res.status,carrier_size=res.carrier_size,lower_bound=res.lower_bound,detector_rounds=res.rounds,detector_pair_tests=res.pair_tests)
        self.dense=res.status!='CERTIFIED_STATIC_CARRIER'; self.gather=None
        if not self.dense:
            assert res.carrier is not None and sca.verify_carrier(res.carrier,self.cutoff)
            self.gather=sca.build_fixed_rfft_gather(res.carrier,n)
    def rhs(self,h):
        if self.dense:
            t=time.perf_counter(); g=self.fft.rotational(h); self.stats['nonlinear_seconds']+=time.perf_counter()-t; self.stats['fft_calls']+=1
        else:
            t=time.perf_counter(); p,a=sca.gather_fixed_rfft(h,self.gather); self.stats['gather_seconds']+=time.perf_counter()-t
            t=time.perf_counter(); out=np.zeros((3,self.n,self.n,self.n//2+1),dtype=np.complex128); self.stats['allocation_seconds']+=time.perf_counter()-t
            t=time.perf_counter(); g=rotational_pairs_into(p,a,out,self.n,self.cutoff); self.stats['nonlinear_seconds']+=time.perf_counter()-t; self.stats['static_sparse_calls']+=1
        t=time.perf_counter(); r=project(g,self.k,self.inv,self.keep)-NU*self.k2*h; self.stats['projection_diffusion_seconds']+=time.perf_counter()-t
        return r

def rk4(h,engine):
    y=h.copy()
    for _ in range(STEPS):
        a=engine.rhs(y); b=engine.rhs(y+DT/2*a); c=engine.rhs(y+DT/2*b); d=engine.rhs(y+DT*c)
        y += DT/6*(a+2*b+2*c+d)
        if not np.isfinite(y).all(): raise FloatingPointError('nonfinite local surrogate trajectory')
    return y

def set_mode(h,p,a):
    x,y,z=map(int,p); n=h.shape[1]; h[:,x%n,y%n,z]=a
    if z==0: h[:,(-x)%n,(-y)%n,0]=a.conjugate()

def div_free_amp(p,rng,scale):
    p=np.asarray(p,dtype=float); a=rng.normal(size=3)+1j*rng.normal(size=3); a-=p*np.dot(p,a)/np.dot(p,p); return scale*a

STRUCT_SEEDS={'heldout-oblique-line':926201,'heldout-even-axis':926202,'heldout-xy-plane-generators':926203}
def structured(name):
    h=np.zeros((3,N,N,N//2+1),dtype=np.complex128); rng=np.random.default_rng(STRUCT_SEEDS[name])
    if name=='heldout-oblique-line': ps=[np.array([1,1,0])]
    elif name=='heldout-even-axis': ps=[np.array([0,2,0])]
    elif name=='heldout-xy-plane-generators': ps=[np.array([1,0,0]),np.array([0,1,0])]
    else: raise ValueError(name)
    for p in ps: set_mode(h,p,div_free_amp(p,rng,0.04))
    return h

def random_initial(s,seed):
    rng=np.random.default_rng(seed); ax=np.arange(-K,K+1,dtype=np.int64); pts=np.array(np.meshgrid(ax,ax,ax,indexing='ij')).reshape(3,-1).T
    pos=((pts[:,2]>0)|((pts[:,2]==0)&(pts[:,1]>0))|((pts[:,2]==0)&(pts[:,1]==0)&(pts[:,0]>0)))
    pts=pts[pos]; chosen=pts[rng.choice(len(pts),s//2,replace=False)]
    h=np.zeros((3,N,N,N//2+1),dtype=np.complex128)
    for p in chosen: set_mode(h,p,div_free_amp(p,rng,0.025/math.sqrt(s/2)))
    return h

def err(a,b):
    absolute=float(np.max(np.abs(a-b))); scale=float(np.max(np.abs(a))); return {'absolute_max':absolute,'relative_max':absolute/max(scale,1e-30),'pass':absolute<=5e-11+5e-10*scale}

def timed(h,mode):
    t=time.perf_counter(); e=FFTEngine() if mode=='fft' else StaticEngine(h); setup=time.perf_counter()-t
    t=time.perf_counter(); y=rk4(h,e); trajectory=time.perf_counter()-t
    return y,{'setup_seconds':setup,'trajectory_seconds':trajectory,'total_seconds':setup+trajectory,'stats':e.stats}

def median_breakdown(trials):
    keys=['detector_seconds','gather_seconds','allocation_seconds','nonlinear_seconds','projection_diffusion_seconds']
    out={}
    for k in keys:
        vals=[t['stats'].get(k,0.0) for t in trials]
        out[k]=float(statistics.median(vals))
    out['setup_seconds']=float(statistics.median(t['setup_seconds'] for t in trials))
    out['trajectory_seconds']=float(statistics.median(t['trajectory_seconds'] for t in trials))
    out['total_seconds']=float(statistics.median(t['total_seconds'] for t in trials))
    return out



class _FakeVT:
    def forward(self, real, spec):
        spec[:] = fft.rfftn(real, axes=(1,2,3), norm='forward', workers=1)
        return spec

class _FakeParams:
    def __init__(self,n):
        self.N=np.array([n,n,n]); self.L=np.array([2*np.pi]*3); self.dealias='3/2-rule'; self.mask_nyquist=True

class _FakeContext:
    def __init__(self,n,h):
        self.U_hat=np.asarray(h).copy(); self.U=np.zeros((3,n,n,n),dtype=float); self.VT=_FakeVT(); self.Tp=object(); self.VTp=object()
        f=np.rint(np.fft.fftfreq(n)*n).astype(int); g=np.arange(n//2+1,dtype=int)
        self.K=(f[:,None,None], f[None,:,None], g[None,None,:])

def pair_kernel_alloc(p,a,n,cutoff):
    out=np.zeros((3,n,n,n//2+1),dtype=np.complex128)
    return rotational_pairs_into(p,a,out,n,cutoff)

def adapter_interface_test(h,limit=LIMIT):
    c=_FakeContext(N,h); params=_FakeParams(N); dense_eval=DealiasedFFT(N)
    def dense_callback(rhs,u_hat,work,Tp,VTp,K,u_dealias):
        rhs[:] = dense_eval.rotational(np.asarray(u_hat)); return rhs
    ad=sca.StaticCarrierNativeVortexAdapter(c,params,dense_callback,pair_kernel_alloc,extract_support,comm_size=1,sparse_limit=limit)
    cert=ad.validate_initial(c.U_hat)
    rhs=np.zeros_like(c.U_hat); ad(rhs,c.U_hat,None,c.Tp,c.VTp,c.K,None)
    ref=dense_eval.rotational(c.U_hat)
    e=err(ref,rhs)
    if not e['pass']: raise AssertionError(('adapter_interface',cert.status,e))
    return {'decision':cert.status,'carrier_size':cert.carrier_size,'lower_bound':cert.lower_bound,'comparison':e,'stats':ad.stats}

def main():
    # Environment gate: this run deliberately uses no hosted computation.
    missing=[]
    for mod in ['spectralDNS','shenfun','mpi4py']:
        try: __import__(mod)
        except Exception as e: missing.append({'module':mod,'error':type(e).__name__})

    # JIT warmup is separately recorded and excluded from all held-out trials.
    hw=structured('heldout-oblique-line'); ew=StaticEngine(hw); t=time.perf_counter(); ew.rhs(hw); warm=time.perf_counter()-t

    cases=[
        ('heldout-oblique-line',hw),
        ('heldout-even-axis',structured('heldout-even-axis')),
        ('heldout-xy-plane-generators',structured('heldout-xy-plane-generators')),
        ('heldout-random48-seed926211',random_initial(48,926211)),
        ('heldout-random96-seed926212',random_initial(96,926212)),
    ]
    rows=[]
    for name,h in cases:
        # Pre-timing single-RHS exact comparison between pair path and 3/2 padded reference where certified.
        se=StaticEngine(h); fe=FFTEngine(); r_static=se.rhs(h); r_fft=fe.rhs(h); single=err(r_fft,r_static)
        if not single['pass']: raise AssertionError((name,'single_rhs',single))
        trials={'fft':[],'static':[]}; last={}
        for rep in range(REPEATS):
            order=['fft','static'] if rep%2==0 else ['static','fft']
            for mode in order:
                y,t=timed(h,mode); trials[mode].append(t); last[mode]=y
            e=err(last['fft'],last['static'])
            if not e['pass']: raise AssertionError((name,'trajectory',e))
        mb={m:median_breakdown(trials[m]) for m in trials}
        ratio=mb['fft']['total_seconds']/mb['static']['total_seconds']
        s=trials['static'][-1]['stats']
        row={'name':name,'initial_full_signed_support':len(extract_support(h,N)[0]),'single_rhs_comparison':single,'trajectory_comparison':err(last['fft'],last['static']),
             'decision':s['decision'],'carrier_size':s['carrier_size'],'proved_lower_bound':s['lower_bound'],'detector_rounds':s['detector_rounds'],'detector_pair_tests':s['detector_pair_tests'],
             'median_breakdown_seconds':mb,'ratio_fft_over_static_total':ratio,'trials':trials}
        rows.append(row); print(name,s['decision'],s['carrier_size'],s['lower_bound'],ratio)

    adapter_tests={'certified_line':adapter_interface_test(structured('heldout-oblique-line')),'dense_fallback_random48':adapter_interface_test(random_initial(48,926211))}

    payload={'schema':'EM_CFD_STATIC_CARRIER_NATIVE_SURROGATE_V1','task_id':TASK,'publication_id':'TP2-C3B717C14153D5AC45BF','researcher_id':RESEARCHER,
      'status':'PASS_LOCAL_NATIVE_3_2_FINITE_SURROGATE','original_spectralDNS_host_executed':False,
      'original_host_blocker':{'missing_local_modules':missing,'hosted_compute_used':False,'statement':'No spectralDNS/shenfun/FFTW host was run in this research session. The exact pinned native adapter interface was integrated in source, while trajectory timings below come from an independent serial 3/2-padded finite-Galerkin surrogate.'},
      'frozen_scope':{'n_storage':N,'native_cutoff':K,'dealiased_physical_grid':M,'domain':'2pi periodic cube (wavevector labels only in local surrogate)','precision':'complex128','viscosity':NU,'dt':DT,'steps':STEPS,'repeats_interleaved':REPEATS,'sparse_limit_full_signed':LIMIT,'pruning_used':False},
      'timing_scope':{'included':['static-carrier detection in static setup','local surrogate 3/2 padding/allocation','all nonlinear evaluations','projection/diffusion','RK4 algebra','finite checks'],
                      'excluded':['dependency installation','JIT warmup','disk output/report writing'],'jit_warmup_seconds':warm,
                      'allocation_note':'static sparse allocation is separately timed; dense FFT allocation/padding is internal to nonlinear_seconds in this local surrogate; the real spectralDNS host owns rhs/work allocation and was not executed'},
      'brc_audit':{'resolution':'REUSE_APPLIED','carrier':'Boolean exact signed wavevector labels','observer':'support membership/cardinality only','complex_amplitudes_phase_multiplicity':'preserved','positive_weight_compression':False,'future_operations':['retained pairwise convolution','diagonal pressure/viscosity multipliers','RK linear combinations']},
      'cases':rows,'adapter_interface_tests':adapter_tests,'adapter_source_sha256':hashlib.sha256((ARTIFACT/'static_carrier_native_adapter.py').read_bytes()).hexdigest(),
      'environment':{'python':platform.python_version(),'numpy':np.__version__}}
    out=ARTIFACT/'local_native_surrogate_results.json'; out.write_text(json.dumps(payload,indent=2)+'\n'); print('wrote',out)

if __name__=='__main__': main()
