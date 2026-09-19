#!/usr/bin/env python3
"""Exact-support Fourier NS nonlinearity probe; NOT an industrial solver benchmark.

Compares a real-FFT rotational form with direct, pair-grouped convection, followed
by the same Leray projection on |k_i| <= K. N > 3K excludes aliasing into that cube.
All complex amplitudes, conjugate partners, and generated output modes are kept.
No thresholding or time integration is performed. This is an independent small
implementation of standard formulas, not a modified spectralDNS distribution.
Requires numpy, scipy and numba. Run: python probe.py --output results.json
"""
from __future__ import annotations
import argparse
import json
import os
import platform
import sys
import time
from pathlib import Path
import numpy as np
import scipy
from scipy import fft
import numba
from numba import njit


def operators(n: int):
    if n < 12 or n % 2:
        raise ValueError('n must be even and >= 12')
    cutoff = n // 3 - 1
    f = np.rint(fft.fftfreq(n) * n).astype(np.int64)
    g = np.arange(n // 2 + 1, dtype=np.int64)
    k = np.array(np.meshgrid(f, f, g, indexing='ij'))
    k2 = np.sum(k*k, axis=0)
    inv = 1.0 / np.where(k2 == 0, 1, k2)
    keep = np.all(np.abs(k) <= cutoff, axis=0)
    return cutoff, k, inv, keep


def initial_state(n: int, s: int, seed: int):
    cutoff = n // 3 - 1
    if s % 2 or s > (2*cutoff+1)**3 - 1:
        raise ValueError('s must be even and fit within the retained cube')
    rng = np.random.default_rng(seed)
    ax = np.arange(-cutoff, cutoff+1, dtype=np.int64)
    pts = np.array(np.meshgrid(ax, ax, ax, indexing='ij')).reshape(3,-1).T
    # One representative from each conjugate pair; neither mean nor Nyquist.
    pos = ((pts[:,2] > 0) | ((pts[:,2] == 0) & (pts[:,1] > 0)) |
           ((pts[:,2] == 0) & (pts[:,1] == 0) & (pts[:,0] > 0)))
    pts = pts[pos]
    selected = pts[rng.choice(len(pts), s//2, replace=False)]
    h = np.zeros((3,n,n,n//2+1), dtype=np.complex128)
    for p in selected:
        a = rng.standard_normal(3) + 1j*rng.standard_normal(3)
        a -= p * (np.dot(p,a) / np.dot(p,p))
        a /= np.sqrt(s)
        h[:,p[0]%n,p[1]%n,p[2]] = a
        if p[2] == 0:
            h[:,(-p[0])%n,(-p[1])%n,0] = a.conjugate()
    return h


def fft_rhs(h, n, k, inv, keep):
    """P(u x curl u), equivalent to -P((u.grad)u) for divergence-free u."""
    u = fft.irfftn(h, s=(n,n,n), axes=(1,2,3), norm='forward', workers=1)
    wh = 1j*np.cross(k, h, axisa=0, axisb=0, axisc=0)
    w = fft.irfftn(wh, s=(n,n,n), axes=(1,2,3), norm='forward', workers=1)
    cross = np.cross(u,w,axisa=0,axisb=0,axisc=0)
    out = fft.rfftn(cross, axes=(1,2,3), norm='forward', workers=1)
    dot = np.sum(k*out,axis=0)*inv
    out -= k*dot
    out *= keep
    return out


def extract_support(h, n):
    """Full scan and conjugate reconstruction included in sparse timing."""
    loc = np.argwhere(np.any(h != 0, axis=0))
    a = np.ascontiguousarray(h[:,loc[:,0],loc[:,1],loc[:,2]].T)
    p = loc.copy()
    p[:,:2] = np.where(p[:,:2] < n//2, p[:,:2], p[:,:2]-n)
    mirror = p[:,2] > 0
    return (np.ascontiguousarray(np.concatenate((p,-p[mirror]))),
            np.ascontiguousarray(np.concatenate((a,a[mirror].conjugate()))))


@njit(cache=True, fastmath=False)
def grouped_rhs(p, a, n, cutoff):
    """Aggregate (p,q) and (q,p); don't discard generated output modes."""
    out = np.zeros((3,n,n,n//2+1), dtype=np.complex128)
    for i in range(len(p)):
        for j in range(i,len(p)):
            x,y,z = p[i,0]+p[j,0],p[i,1]+p[j,1],p[i,2]+p[j,2]
            if z < 0 or z > cutoff or abs(x)>cutoff or abs(y)>cutoff:
                continue
            qa = p[j,0]*a[i,0]+p[j,1]*a[i,1]+p[j,2]*a[i,2]
            pa = p[i,0]*a[j,0]+p[i,1]*a[j,1]+p[i,2]*a[j,2]
            for d in range(3):
                v = qa*a[j,d]
                if i != j:
                    v += pa*a[i,d]
                out[d,x%n,y%n,z] += -1j*v
    for ix in range(n):
        x = ix if ix < n//2 else ix-n
        for iy in range(n):
            y = iy if iy < n//2 else iy-n
            for z in range(n//2+1):
                r = x*x+y*y+z*z
                if r:
                    b = (x*out[0,ix,iy,z]+y*out[1,ix,iy,z]+z*out[2,ix,iy,z])/r
                    out[0,ix,iy,z] -= x*b
                    out[1,ix,iy,z] -= y*b
                    out[2,ix,iy,z] -= z*b
    return out


def sparse_rhs(h,n,cutoff):
    p,a = extract_support(h,n)
    return grouped_rhs(p,a,n,cutoff)


def median_interleaved(f,g,repeats=5):
    tf,tg = [],[]
    for r in range(repeats):
        order = ((f,tf),(g,tg)) if r%2 == 0 else ((g,tg),(f,tf))
        for fn,times in order:
            t=time.perf_counter(); fn(); times.append(time.perf_counter()-t)
    return float(np.median(tf)),float(np.median(tg)),tf,tg


def full_mode_count(h):
    mask = np.max(np.abs(h),axis=0)>1e-12
    return int(np.count_nonzero(mask[:,:,0])+2*np.count_nonzero(mask[:,:,1:]))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',default='results.json')
    args=parser.parse_args()
    # JIT compilation excluded, and explicitly reported.
    h=initial_state(16,16,7); c,k,iv,keep=operators(16)
    t=time.perf_counter(); sparse_rhs(h,16,c); compile_warmup=time.perf_counter()-t
    records=[]
    for n,slist in [(32,[32,128,512,2048,4096]),(64,[32,128,512,2048,8192])]:
        cutoff,k,inv,keep=operators(n)
        for s in slist:
            seed=20260910+s+n
            h=initial_state(n,s,seed)
            f=lambda:fft_rhs(h,n,k,inv,keep)
            g=lambda:sparse_rhs(h,n,cutoff)
            a,b=f(),g()
            err=float(np.max(np.abs(a-b))/max(np.max(np.abs(a)),1e-30))
            if err>2e-11:
                raise AssertionError(f'nonlinear mismatch n={n},s={s}: {err}')
            tf,tg,ft,gt=median_interleaved(f,g)
            row=dict(n_fft=n,cutoff=cutoff,active_full_modes=s,
                     retained_full_modes=(2*cutoff+1)**3-1,
                     output_full_modes=full_mode_count(b),seed=seed,
                     relative_max_rhs_difference=err,
                     fft_median_seconds=tf,sparse_total_median_seconds=tg,
                     ratio_fft_over_sparse=tf/tg,fft_trials=ft,sparse_trials=gt)
            records.append(row)
            print(json.dumps(row),flush=True)
    payload=dict(status='FINITE_KERNEL_PROBE_NOT_SOLVER_BENCHMARK',
                 created_at=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
                 python=sys.version,platform=platform.platform(),numpy=np.__version__,
                 scipy=scipy.__version__,numba=numba.__version__,
                 fft_workers=1,sparse_parallel=False,precision='complex128/float64',
                 jit_warmup_seconds=compile_warmup,records=records,
                 scope='single RHS evaluation; sparse scan, conjugate reconstruction, output allocation and projection included',
                 exclusions=['time integration','viscosity','forcing','MPI/GPU','rigorous interval certificate',
                             'spectralDNS production/FFTW benchmark','approximate support thresholding'])
    Path(args.output).write_text(json.dumps(payload,indent=2)+'\n')

if __name__ == '__main__':
    main()
