"""Finite construction costs. Wall-clock measurements vary on replay."""
import json
import platform
import statistics
import sys
from time import perf_counter_ns
import numpy as np
import scipy
from scipy import fft

from envelope import ScalarPlan, VelocityPlan
from envelope_check import fixture, reference


def dense_input(dim, k, points,rows,keep):
    n=2*k+1
    shape=(n,)*dim
    field=np.zeros(shape+(len(rows[0]),),dtype=np.complex128)
    flags=np.zeros(shape,dtype=bool)
    for p,z,retained in zip(points,rows,keep):
        ix=tuple(v+k for v in p)
        field[ix]=z
        flags[ix]=retained
    return field,flags


def extract(k,field,flags):
    loc=np.argwhere(np.any(field!=0,axis=-1))
    ix=tuple(loc.T)
    return list(map(tuple,(loc-k).tolist())),list(map(tuple,field[ix].tolist())),flags[ix].tolist()


def fft2_reference(field,k):
    """One full signed 2D dealiased RHS; operator arrays, padding and extraction included."""
    n=fft.next_fast_len(3*k+1)
    f=np.arange(-k,k+1)
    ix=np.ix_(f%n,f%n)
    h=np.zeros((n,n),dtype=np.complex128)
    h[ix]=field[:,:,0]
    wave=np.rint(fft.fftfreq(n)*n)
    x,y=wave[:,None],wave[None,:]
    r=x*x+y*y
    r[0,0]=1.
    def spatial(v): return fft.ifft2(v,norm='forward',workers=1).real
    u,v=spatial(1j*y*h/r),spatial(-1j*x*h/r)
    dx,dy=spatial(1j*x*h),spatial(1j*y*h)
    return fft.fft2(-(u*dx+v*dy),norm='forward',workers=1)[ix]


def timings(cases):
    # Warm each path once. Rotate trial order to interleave named paths.
    names=list(cases)
    for f in cases.values(): f()
    observations={name:[] for name in names}
    for r in range(7):
        for name in names[r%len(names):]+names[:r%len(names)]:
            start=perf_counter_ns()
            cases[name]()
            observations[name].append(perf_counter_ns()-start)
    return {n:{'median_ms':statistics.median(v)/1e6,'trials_ns':v} for n,v in observations.items()}


def main():
    records=[]
    for dim in (2,3):
        for k,count in [(8,56),(16,240),(32,960)]:
            p,z,keep=fixture(dim,k,count,'holdout_v1')
            field,flags=dense_input(dim,k,p,z,keep)
            def build(points,detailed=False):
                return ScalarPlan(points,k,angular=detailed) if dim==2 else VelocityPlan(points,k)
            def compute(plan,rows,kp,detailed):
                return plan.bound(rows,kp,detailed=detailed) if dim==2 else plan.bound(rows,kp)
            def full(dense,detailed):
                pts,rows,kp=extract(k,field,flags) if dense else (p,z,keep)
                return compute(build(pts,detailed),rows,kp,detailed)
            def exact_basic_dense():
                pts,rows,kp=extract(k,field,flags)
                return reference(dim,k,pts,rows,kp,'basic')
            simple=build(p)
            cases={'mask_scan_extract':lambda:extract(k,field,flags),
                   'simple_plan':lambda:build(p),
                   'simple_reuse':lambda:compute(simple,z,keep,False),
                   'simple_total_sparse':lambda:full(False,False),
                   'simple_total_dense':lambda:full(True,False),
                   'fraction_original_total_dense':exact_basic_dense}
            if dim==2:
                angular=build(p,True)
                cases.update(angular_plan=lambda:build(p,True),
                             angular_reuse=lambda:compute(angular,z,keep,True),
                             angular_total_dense=lambda:full(True,True),
                             dense_fft2_rhs=lambda:fft2_reference(field,k))
                assert compute(angular,z,keep,True)==full(True,True)
            assert compute(simple,z,keep,False)==full(True,False)
            records.append({'dim':dim,'cutoff':k,'signed_modes':count,'timings':timings(cases)})
    print(json.dumps({'python':sys.version,'architecture':platform.machine(),'numpy':np.__version__,
                      'scipy':scipy.__version__,'repetitions':7,'clock':'perf_counter_ns',
                      'scope':'synthetic held-out finite construction; single shared machine; no solver time stepping',
                      'rows':records},indent=2))


if __name__=='__main__':
    main()
