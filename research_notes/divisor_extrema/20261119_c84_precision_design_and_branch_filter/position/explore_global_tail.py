"""Exploratory paired Haar sampling for the all-source high-L design constant.

For endpoint-normalized F_theta, the relevant scalar is
I_theta = integral_0^infinity [1-F_theta(t**20)] dt
        = E[s_critical**(1/10)].
This is ordinary floating Monte Carlo, not a mathematical certificate.
The vector search uses a deterministic inverse-basis box for every sample;
there is no fixed vector-radius truncation or independent-point approximation.
"""
from argparse import ArgumentParser
from pathlib import Path
from math import sin, cos, sqrt, pi, floor, ceil, gcd
import json
import numpy as np
from time import perf_counter

THETAS=np.array([0.0,0.125,0.25,0.375,0.5])

def scales(vectors, phases):
    x=vectors[:,0]; y=vectors[:,1]
    middle=(1-THETAS[:,None])*x[None,:]+THETAS[:,None]*y[None,:]
    marks=np.stack([np.broadcast_to(x,middle.shape),middle,
                    np.broadcast_to(y,middle.shape)],axis=2)
    limits=np.where(marks>0,1-phases,phases)
    plus=np.divide(limits,np.abs(marks),out=np.full_like(marks,np.inf),where=marks!=0).min(axis=2)
    limits=np.where(marks>0,phases,1-phases)
    minus=np.divide(limits,np.abs(marks),out=np.full_like(marks,np.inf),where=marks!=0).min(axis=2)
    return np.maximum(plus,minus).max(axis=1)

def run(count,seed):
    rng=np.random.default_rng(seed)
    moments=np.empty((count,len(THETAS)))
    candidate_sum=0;max_candidates=0;max_box=0
    start=perf_counter()
    for index in range(count):
        angle=rng.uniform(-pi/6,pi/6)
        x=sin(angle);y=cos(angle)/rng.random()
        phi=rng.uniform(0,pi);cs=cos(phi);sn=sin(phi)
        root=sqrt(y)
        basis=np.array([[cs/root,cs*x/root-sn*root],
                        [sn/root,sn*x/root+cs*root]])
        phases=rng.random(3)
        initial=np.array([[1,0],[0,1],[1,1],[1,-1]])@basis.T
        best=scales(initial,phases)
        radius=1/best.min()
        inv=np.array([[basis[1,1],-basis[0,1]],[-basis[1,0],basis[0,0]]])
        mb=ceil(radius*np.abs(inv[0]).sum())
        nb=ceil(radius*np.abs(inv[1]).sum())
        # An outward two-integer padding protects the exploratory search
        # from floating endpoint rounding. It is not a rigorous arithmetic claim.
        mb+=2;nb+=2
        ints=[]
        for n in range(-nb,nb+1):
            for m in range(0,mb+1):
                if (m==0 and n<=0) or gcd(m,abs(n))!=1:continue
                a=basis[0,0]*m+basis[0,1]*n
                b=basis[1,0]*m+basis[1,1]*n
                if max(abs(a),abs(b))<=radius*(1+1e-13):ints.append((a,b))
        if ints:best=np.maximum(best,scales(np.array(ints),phases))
        moments[index]=best**0.1
        candidate_sum+=len(ints);max_candidates=max(max_candidates,len(ints))
        max_box=max(max_box,(mb+1)*(2*nb+1))
    means=moments.mean(axis=0)
    stderrs=moments.std(axis=0,ddof=1)/sqrt(count)
    diffs=moments-moments[:,-1,None]
    return {'status':'exploratory_not_certified',
            'definition':'I_theta=E[s_critical^(1/10)]=integral(1-F_theta(t^20),dt)',
            'samples':count,'seed':seed,
            'theta':THETAS.tolist(),'mean':means.tolist(),'standard_error':stderrs.tolist(),
            'paired_difference_from_midpoint':diffs.mean(axis=0).tolist(),
            'paired_difference_standard_error':(diffs.std(axis=0,ddof=1)/sqrt(count)).tolist(),
            'average_primitive_candidates':candidate_sum/count,
            'maximum_primitive_candidates':max_candidates,'maximum_integer_box_size':max_box,
            'runtime_seconds':perf_counter()-start,
            'scope':'Full-source asymptotic ordering is not proved by these samples. Haar shape and phase are coupled across designs; integer vector dependence is retained.'}

if __name__=='__main__':
    parser=ArgumentParser(description=__doc__)
    parser.add_argument('--samples',type=int,default=50000)
    parser.add_argument('--seed',type=int,default=841903)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('global_tail_exploration.json'))
    args=parser.parse_args()
    result=run(args.samples,args.seed)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
