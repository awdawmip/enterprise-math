#!/usr/bin/env python3
"""Exact Peano-kernel checks and strict complete-reference sampling examples."""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse
import hashlib
import importlib.util
import json


def peano_checks():
    checks=0
    for l in range(1,6):
        for h in (F(1,2),F(2,3),F(3,2),F(5)):
            r=F(l)+h
            for j in range(1,5):
                x=F(l)+h*j/5
                for degree in range(2,9):
                    f=lambda t:t**degree/F(degree*(degree-1))
                    chord=((r-x)*f(F(l))+(x-l)*f(r))/h
                    k=degree-2
                    left=(r-x)/h*((x**(k+2)-F(l)**(k+2))/F(k+2)-l*(x**(k+1)-F(l)**(k+1))/F(k+1))
                    right=(x-l)/h*(r*(r**(k+1)-x**(k+1))/F(k+1)-(r**(k+2)-x**(k+2))/F(k+2))
                    assert chord-f(x)==left+right
                    assert 0<=left+right<=(x-l)*(r-x)*r**k/2
                    checks+=1
    grids=0;integer_points=0
    for length in range(2,12):
        for mask in range(1<<(length-1)):
            nodes=[0]+[n for n in range(1,length) if mask>>(n-1)&1]+[length]
            interiors=[n for l,r in zip(nodes,nodes[1:]) for n in range(l+1,r)]
            assert len(interiors)==len(set(interiors))==sum(r-l-1 for l,r in zip(nodes,nodes[1:]))
            assert set(interiors)|set(nodes)==set(range(length+1))
            grids+=1;integer_points+=length+1
    return {'rational_peano_identities_and_bounds':checks,'closed_integer_grids':grids,'closed_grid_integer_points':integer_points}


def load_module(path):
    spec=importlib.util.spec_from_file_location('sparse_skeleton_intervals',path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


def root_interval(m,v):
    low=isqrt(max(0,v[0])*m.S);high=isqrt(max(0,v[1])*m.S)
    if high*high<max(0,v[1])*m.S:high+=1
    return low,high


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--previous',type=Path,required=True,help='riemann_signed_green_thickness_phase_20261124 package')
    ap.add_argument('--output',type=Path,default=Path(__file__).with_name('sparse_skeleton_certificate.json'))
    args=ap.parse_args()
    old=args.previous/'prior/riemann_native_residual_growth_20261124/prior/riemann_matching_isotonic_anchors_20261124/prior/riemann_directed_local_20261124/prior/riemann_cumulative_haar_20261123'
    helper=old/'dependencies/certify_fast_harmonic_energy.py';fixed=old/'prefix_compute/fixed_matched_family.json'
    m=load_module(helper);data=json.loads(fixed.read_text())
    gamma=(m.rat(F(data['gamma']['lower']))[0],m.rat(F(data['gamma']['upper']))[1])
    B=32768;prime=[True]*(B+1);prime[0]=prime[1]=False
    for p in range(2,isqrt(B)+1):
        if prime[p]:
            for n in range(p*p,B+1,p):prime[n]=False
    lam=[m.ZERO]*(B+1);prime_count=power_count=0
    for p in range(2,B+1):
        if prime[p]:
            prime_count+=1;n=p;logp=m.log_int(p)
            while n<=B:
                assert lam[n]==m.ZERO
                lam[n]=logp;power_count+=1;n*=p
    q=[m.ZERO]*(B+1);harm=mass=m.ZERO
    for n in range(1,B+1):
        harm=m.add(harm,m.qmul(lam[n],1,n));mass=m.add(mass,lam[n])
        q[n]=m.sub(m.qmul(m.add(m.sub(m.add(m.ONE,gamma),m.log_int(n)),harm),n),mass)
    direct_checks=0
    for y in range(1,129):
        direct=m.qmul(m.sub(m.add(m.ONE,gamma),m.log_int(y)),y)
        for n in range(2,y+1):direct=m.add(direct,m.qmul(lam[n],y-n,n))
        assert m.overlap(q[y],direct)
        direct_checks+=1
    rows=[];point_evaluations=0;node_zero_checks=0
    for X in (1024,2048,4096,8192,16384):
        full=m.total(m.qmul(m.square(m.positive(q[n])),1,n*n) for n in range(X,2*X+1))
        for cell_count in (2,4,8,16,32,64):
            h=X//cell_count;nodes=list(range(X,2*X+1,h));sampled=error=m.ZERO
            for i,(l,r) in enumerate(zip(nodes,nodes[1:])):
                for n in range(l,r+(i==len(nodes)-2)):
                    if n==l or n==r:
                        f=q[n];difference=m.ZERO;node_zero_checks+=1
                    else:
                        f=m.add(m.qmul(q[l],r-n,r-l),m.qmul(q[r],n-l,r-l))
                        difference=m.sub(f,q[n])
                    sampled=m.add(sampled,m.qmul(m.square(m.positive(f)),1,n*n))
                    error=m.add(error,m.qmul(m.square(difference),1,n*n))
                    point_evaluations+=1
            rf=root_interval(m,full);rs=root_interval(m,sampled);re=root_interval(m,error)
            assert max(0,rf[0]-rs[1],rs[0]-rf[1])<=re[1]
            rows.append({'X':X,'Y':2*X,'cells':cell_count,'nodes':cell_count+1,'max_gap':h,'complete_reference_positive_energy':m.record(full),'sampled_reference_positive_energy':m.record(sampled),'absolute_interpolation_error_energy':m.record(error),'absolute_interpolation_root_upper':m.record((0,re[1]))})
    result={'schema':'EM_SPARSE_SKELETON_SAMPLING_V1','status':'PASS','scope':'Finite Peano identities and complete-reference q* examples only; the unbounded zero-counting and growth-exponent theorem is proved analytically in the accompanying note. No new actual-thickness q_D samples are used.','arithmetic':'Exact fractions and 80-digit outward integer intervals; full prime sieve to32768, no end-to-end sublinear computation claim.','dependencies':[{'path':str(p.relative_to(args.previous)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in (helper,fixed)],'kernel_checks':peano_checks(),'reference_computation':{'B':B,'all_source_integers':B,'primes':prime_count,'prime_powers':power_count,'direct_complete_prefix_checks':direct_checks,'grid_rows':len(rows),'closed_grid_point_evaluations':point_evaluations,'exact_zero_at_grid_nodes':node_zero_checks},'rows':rows}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':'PASS','kernel_checks':result['kernel_checks'],'reference_computation':result['reference_computation'],'last_block':[{k:r[k] for k in ('cells','max_gap','sampled_reference_positive_energy','absolute_interpolation_error_energy')} for r in rows if r['X']==16384]},ensure_ascii=False))


if __name__=='__main__':main()
