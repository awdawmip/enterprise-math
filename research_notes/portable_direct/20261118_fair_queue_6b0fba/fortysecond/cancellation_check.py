"""Exact cyclotomic certificates, adaptive Arb balls and a frozen sparse 3D NS probe."""
import argparse
import cmath
from functools import lru_cache
from hashlib import sha256
import importlib.util
import json
from math import comb, gcd, isqrt
from pathlib import Path
from statistics import median
from tempfile import TemporaryDirectory
from time import perf_counter_ns

import flint
from flint import acb,arb,ctx,fmpz_poly,fmpq


def divisors(n):
    return [k for k in range(1,n+1) if n%k==0]


def mobius(n):
    sign=1
    for k in range(2,isqrt(n)+1):
        if n%k==0:
            n//=k
            if n%k==0:return 0
            sign=-sign
    return sign if n==1 else -sign


@lru_cache(None)
def ram(q,k):
    return sum(d*mobius(q//d) for d in divisors(gcd(q,k)))


def reduce_period(c,q):
    a=[0]*q
    for j,v in enumerate(c):a[j%q]+=v
    return a


def energy(q,c):
    h=sum(a*b*ram(q,(i-j)%q) for i,a in enumerate(c) if a for j,b in enumerate(c) if b)
    assert h%2==0
    return h//2


def horner(c,z):
    v=z*0
    for a in reversed(c):
        v=v*z+a
    return v


def root(q):
    return acb(fmpq(2,q)).exp_pi_i()


def ball_row(q,c,H,S,d,prec):
    with ctx.workprec(prec):
        value=horner(c,root(q))
        upper=value.abs_upper()
        # If S=0 the exact trace alone settles this case; avoid counting that as a numerical success.
        l1_exclusion=H==0 or (upper*(H**(d-1))<1)
        energy_exclusion=d>1 and S>0 and (upper*upper*S**(d-1)<(d-1)**(d-1))
        state='nonzero' if not value.contains(0) else 'zero' if (value.is_zero() or l1_exclusion or energy_exclusion) else 'unresolved'
        return value,{'prec':prec,'contains_zero':value.contains(0),'proven':state,
                      'lower_abs_display':value.abs_lower().str(8,radius=False),
                      'upper_abs_display':upper.str(8,radius=False),'l1_gap_certifies_zero':bool(l1_exclusion),
                      'ramanujan_gap_certifies_zero':bool(energy_exclusion)}


def arb_fourier_port(q,c,H,d,prec):
    # Build the positive and negative input spectrum explicitly. At k=e_x the z component survives Leray.
    with ctx.workprec(prec):
        z=root(q)
        inputs={}
        for j,integer in enumerate(c):
            if not integer:continue
            t=3*j
            a=integer*z**(j%q)
            for h,u in [((t,1,0),(a,-t*a,acb(0))),((1-t,-1,0),(acb(0),acb(0),acb(1)))]:
                for v,w in ((h,u),(tuple(-n for n in h),tuple(x.conjugate() for x in u))):
                    assert v not in inputs
                    inputs[v]=w
        out=acb(0)
        count=0
        for p,u in inputs.items():
            h=(1-p[0],-p[1],-p[2])
            if h not in inputs:continue
            count+=1
            dot=sum((k*a for k,a in zip(h,u)),acb(0))
            out+=dot*inputs[h][2]
        assert count==2*sum(bool(a) for a in c)
        out*=-acb(0,1)
        end='nonzero' if not out.contains(0) else 'zero' if out.is_zero() or out.abs_upper()*(H**(d-1))<1 else 'unresolved'
        return out,end,count

def terminal(q,m,c,kind):
    with ctx.workprec(1024):
        if kind=='factorized':
            z=root(q)
            return (1-z)**m,horner(c,z),True
        if kind=='phi':return acb(0),horner(c,root(q)),True
        if kind=='float-drop':return acb(1),horner(c,root(q)),True
        return horner(c,root(q)),None,False


def setup(q,c):
    p=fmpz_poly(reduce_period(c,q))
    cyclo=fmpz_poly.cyclotomic(q)
    rem=p%cyclo
    H=sum(map(abs,reduce_period(c,q)))
    d=cyclo.degree()//2
    assert q>2
    S=energy(q,reduce_period(c,q))
    norm=abs(int(cyclo.resultant(p)))
    assert (not rem)==(norm==0)==(S==0)
    return H,d,S,norm,rem


def one(name,q,c,m,kind):
    H,d,S,norm,rem=setup(q,c)
    exact,reread,independent=terminal(q,m,c,kind)
    assert reread is None or exact.overlaps(reread)
    if kind=='factorized':
        assert all(q%j for j in range(2,isqrt(q)+1)) and norm==q**m
    history=[]
    for prec in (24,48,96,192,384,768,1536):
        v,measure=ball_row(q,reduce_period(c,q),H,S,d,prec)
        assert v.overlaps(exact)
        history.append(measure)
        if measure['proven']!='unresolved':break
    assert history[-1]['proven']==('nonzero' if rem else 'zero')
    host_round=[]
    for prec in (24,48,96,192,384,768,1536):
        value,end,hits=arb_fourier_port(q,c,H,d,prec)
        assert value.overlaps(-acb(0,1)*exact)
        host_round.append([prec,end])
        if end!='unresolved':break
    assert end==('nonzero' if rem else 'zero')
    factored_first=None
    if kind=='factorized':
        for p in (24,48,96,192,384):
            with ctx.workprec(p):
                if not ((1-root(q))**m).contains(0):factored_first=p;break
    at_high=None
    with ctx.workprec(1024):
        z=root(q)
        # Independent high-precision checks of the conjugate energy and integer norm.
        conjugates=[abs(horner(c,z**j))**2 for j in range(1,q//2+1) if gcd(j,q)==1]
        est_sum=sum(conjugates,arb(0))
        est_product=arb(1)
        for y in conjugates:est_product*=y
        assert est_sum.contains(S) and est_product.contains(norm)
        at_high=abs(exact).str(12,radius=False)
    wf=complex(0,1) if q==4 else cmath.exp(2j*cmath.pi/q)
    fp=complex(horner(c,wf))
    return {'name':name,'q':q,'input_degree':len(c)-1,'nonzero_input_terms':sum(bool(t) for t in c),
            'H':H,'d':d,'trace_half_energy':S,'resultant_abs':norm,'remainder_coeff':list(map(int,rem.coeffs())),
            'm':m,'arb_ordered_port_history':host_round,'ordered_port_matches':hits,'factored_first_nonzero_bits':factored_first,'independent_expression':independent,'reference_abs_display':at_high,
            'binary64_horner_abs':abs(fp),'binary64_nonzero_flag':bool(fp),
            'fixed_abs_tol_1e-12_nonzero':abs(fp)>1e-12,'arb_history':history}


def cases():
    result=[('float-drop',4,[2**54,0,0,0,1,0,2**54],None,'float-drop'),
            ('norm-one',5,[1,-1,1],None,'unit')]
    for q in (15,30,105):
        result.append((f'phi{q}',q,list(map(int,fmpz_poly.cyclotomic(q).coeffs())),None,'phi'))
    for q,m in ((17,24),(17,64),(29,48),(31,96)):
        result.append((f'power_{q}_{m}',q,[(-1)**j*comb(m,j) for j in range(m+1)],m,'factorized'))
    return result


def hosts(repo):
    import numpy as np
    import scipy,numba
    src=repo/'research_notes/CFD-B1F673/prior_3d/probe.py'
    data=src.read_bytes()
    blob=sha256(data).hexdigest()
    import hashlib
    assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()=='2e7056530cad8b0b6341290ffc70c88aab486b1f'
    fixtures=[('true_one',4,[2**54,0,0,0,1,0,2**54]),('exact_zero',5,[1]*5),('norm_one',5,[1,-1,1])]
    reports=[]
    with TemporaryDirectory() as tmp:
        copied=Path(tmp)/'probe.py'
        copied.write_bytes(data)
        sp=importlib.util.spec_from_file_location('em42_frozen_probe',copied)
        module=importlib.util.module_from_spec(sp);sp.loader.exec_module(module)
        for name,q,c in fixtures:
            s=len(c)-1
            n=max(12,6*((3*s+3)//2))  # even and floor(n/3)-1 >= 3s
            cutoff,k,hold,keep=module.operators(n)
            assert cutoff>=max(1,3*s)
            spec=np.zeros(k.shape,dtype=np.complex128)
            modes={}
            count=0
            for j,val in enumerate(c):
                if not val:continue
                t=3*j
                phase=(1j)**(j%4) if q==4 else cmath.exp(2j*cmath.pi*(j%q)/q)
                for h,u in [((t,1,0),(val*phase,-t*val*phase,0)),((1-t,-1,0),(0,0,1))]:
                    u=np.asarray(u,dtype=np.complex128)
                    for v,w in ((h,u),(tuple(-l for l in h),u.conjugate())):
                        assert v not in modes
                        modes[v]=w
                        spec[:,v[0]%n,v[1]%n,0]=w
                count+=1
            # Enumeration of all ordered input pairs; k·u term is a nonconjugating dot product.
            ordered=np.zeros(3,dtype=np.complex128)
            hits=0
            for p,u in modes.items():
                for h,v in modes.items():
                    if tuple(i+j for i,j in zip(p,h))!=(1,0,0):continue
                    ordered-=1j*np.dot(u,h)*v
                    hits+=1
            assert hits==2*count
            ordered[0]=0
            certified=module.sparse_rhs(spec,n,cutoff)[:,1,0,0]
            fft=module.fft_rhs(spec,n,k,hold,keep)[:,1,0,0]
            exact=horner(c,root(q))*(-acb(0,1))
            assert certified[0]==certified[1]==0
            if q==4:assert certified[2]==0 and exact==acb(0,-1)
            reports.append({'label':name,'grid_n':n,'K':cutoff,'paired_inputs':len(modes),
                            'all_ordered_pairs':len(modes)**2,'matched_ordered_pairs':hits,
                            'cyclotomic_target_zero':not(fmpz_poly(c)%fmpz_poly.cyclotomic(q)),'arb_z_display':str(exact),'sparse_z':[float(certified[2].real),float(certified[2].imag)],
                            'ordered_z':[float(ordered[2].real),float(ordered[2].imag)],
                            'fft_z':[float(fft[2].real),float(fft[2].imag)]})
    return {'source_sha256':blob,'numpy':np.__version__,'scipy':scipy.__version__,'numba':numba.__version__,
            'grid_normalization':"unchanged norm='forward', N>3K",'runs':reports}


def timings():
    samples=[]
    for name,q,c,m,kind in cases():
        results={}
        def geom():
            H,d,S,N,R=setup(q,c)
            return bool(R)
        f=reduce_period(c,q)
        H,d,S,_,_=setup(q,c)
        def adaptive():
            for p in (24,48,96,192,384,768,1536):
                if ball_row(q,f,H,S,d,p)[1]['proven']!='unresolved':return
        def remainder_only():
            return fmpz_poly(reduce_period(c,q))%fmpz_poly.cyclotomic(q)
        for label,fn in [('remainder_only',remainder_only),('exact_setup_with_resultant_trace',geom),('adaptive_after_setup',adaptive)]:
            fn()
            runs=[]
            for _ in range(5):
                start=perf_counter_ns()
                for __ in range(3):fn()
                runs.append((perf_counter_ns()-start)//3)
            results[label]=int(median(runs))
        samples.append({'case':name,'median_ns':results})
    return samples


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--verify',type=Path)
    opt=p.parse_args()
    ctx.prec=80
    result={'semantic':{'versions':{'python_flint':flint.__version__,'FLINT':flint.__FLINT_VERSION__},
                'cases':[one(*c) for c in cases()],'host':hosts(opt.repo)},'local_timings':timings()}
    if opt.verify:
        prev=json.loads(opt.verify.read_text())
        # Host doubles depend on the FFT build. This strict replay checks the recorded environment.
        assert prev['semantic']==result['semantic']
        print('semantic replay OK; wall-clock timings are separate')
    else:print(json.dumps(result,indent=2,sort_keys=True))
