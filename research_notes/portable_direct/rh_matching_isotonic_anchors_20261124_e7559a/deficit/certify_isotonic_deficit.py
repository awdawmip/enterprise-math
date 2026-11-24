#!/usr/bin/env python3
"""Fixed-layer directed deficits through certified weighted monotone pools.

The supplied harmonic module owns outward logarithm intervals.  PAV comparisons,
pool means, KKT inequalities and the final budgets use those intervals.  Floating
point is used only for short printed summaries, never a mathematical decision.
"""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
from itertools import product
import argparse
import importlib.util
import json


def load_module(path):
    spec = importlib.util.spec_from_file_location('certified_intervals', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def mass(u, v):
    return F(v-u, u*v)


def exact_pav(values, left):
    pools = []
    for j, value in enumerate(values, left):
        pools.append([j, j+1, F(value)*mass(j,j+1)])
        while len(pools)>1:
            a,b=pools[-2:]
            if a[2]/mass(a[0],a[1]) <= b[2]/mass(b[0],b[1]):
                break
            pools[-2:]=[[a[0],b[1],a[2]+b[2]]]
    return pools


def exact_checks():
    sequences=contrasts=interior_kkt=0
    for h in range(2,7):
        L,R=2,2+h
        for values in product((-2,0,3),repeat=h):
            pools=exact_pav(values,L)
            residual=list(map(F,values))
            for u,v,s in pools:
                mean=s/mass(u,v)
                cumulative=F(0)
                for n in range(u,v):
                    residual[n-L]-=mean
                    cumulative+=mass(n,n+1)*residual[n-L]
                    if n+1<v:
                        assert cumulative>=0
                        interior_kkt+=1
                assert cumulative==0
            V=sum((mass(n,n+1)*residual[n-L]**2 for n in range(L,R)),F(0))
            for x in range(L+1,R):
                a,b=x-L,R-x
                means=[sum((mass(n,n+1)*values[n-L] for n in range(u,v)),F(0))/mass(u,v)
                       for u,v in ((L,x),(x,R))]
                tau=(means[0]-means[1])/x
                tau2=max(tau,F(0))**2
                assert tau2<=F(h,a*b)*V
                crossing=next(((u,v,s) for u,v,s in pools if u<x<v),None)
                if crossing:
                    u,v,s=crossing
                    Vcross=sum((mass(n,n+1)*residual[n-L]**2 for n in range(u,v)),F(0))
                    S=sum((mass(n,n+1)*residual[n-L] for n in range(u,x)),F(0))
                    B=F(h*x,a*b)*S
                    C=F(h*h*(x-u)*(v-x),a*a*b*b*(v-u))*Vcross
                    assert tau2<=B*B<=C<=F(h,a*b)*V
                else:
                    assert tau<=0
                contrasts+=1
            sequences+=1
    positive_sequences=positive_contrasts=0
    for h in range(2,7):
        L,R=2,2+h
        for events in product((0,1,4),repeat=h-1):
            values=[F(0)]
            for event in events:
                values.append(values[-1]+event-1)
            pools=exact_pav(values,L)
            for x in range(L+1,R):
                a,b=x-L,R-x
                means=[sum((mass(n,n+1)*values[n-L] for n in range(u,v)),F(0))/mass(u,v)
                       for u,v in ((L,x),(x,R))]
                tau=(means[0]-means[1])/x
                crossing=next(((u,v,s) for u,v,s in pools if u<x<v),None)
                if crossing:
                    u,v,s=crossing
                    tau_pool=(sum((mass(n,n+1)*values[n-L] for n in range(u,x)),F(0))/mass(u,x)
                              -sum((mass(n,n+1)*values[n-L] for n in range(x,v)),F(0))/mass(x,v))/x
                    background=sum((F(n-u,x-u)/n if n<=x else F(v-n,v-x)/n for n in range(u+1,v)),F(0))
                    ratio=F(h*(x-u)*(v-x),a*b*(v-u))
                    assert 0<=max(tau,F(0))<=ratio*tau_pool<=ratio*background<=F(h*(x-u)*(v-x),2*a*b*u)
                else:
                    assert tau<=0
                positive_contrasts+=1
            positive_sequences+=1
    return {'sequences':sequences,'contrasts':contrasts,'interior_kkt':interior_kkt,
            'input_domain':'L=2; h=2,...,6; all sequences in {-2,0,3}^h',
            'nonnegative_event_sequences':positive_sequences,'nonnegative_event_contrasts':positive_contrasts,
            'nonnegative_event_domain':'L=2; h=2,...,6; A_L=0; successive event weights in {0,1,4}, A increments event−1',
            'all_exact_checks_passed':True}


def compute(m, geometry, prior):
    B=max(block['Y'] for block in geometry['blocks'])
    sieve=bytearray(b'\x01')*(B+1)
    sieve[:2]=b'\x00\x00'
    for p in range(2,isqrt(B)+1):
        if sieve[p]:
            sieve[p*p::p]=b'\x00'*((B-p*p)//p+1)
    theta=m.ZERO
    A=[m.ZERO]*(B+1)
    for n in range(1,B+1):
        if sieve[n]:
            theta=m.add(theta,m.log_int(n))
        A[n]=m.sub(theta,m.rat(n))
    prefix=[m.ZERO]*(B+1)
    square_prefix=[m.ZERO]*(B+1)
    for n in range(1,B):
        prefix[n+1]=m.add(prefix[n],m.qmul(A[n],mass(n,n+1)))
        square_prefix[n+1]=m.add(square_prefix[n],m.qmul(m.square(A[n]),mass(n,n+1)))
    def sum_a(u,v):
        return m.sub(prefix[v],prefix[u])
    def mean(u,v):
        return m.qmul(sum_a(u,v),1/mass(u,v))
    def variance(u,v):
        if v==u+1:
            return m.ZERO
        return m.sub(m.sub(square_prefix[v],square_prefix[u]),m.qmul(m.square(sum_a(u,v)),1/mass(u,v)))
    rows=[]
    counts={'packets':0,'pools':0,'kkt_prefixes':0,'boundary_splits':0,'ambiguous_pool_merges':0}
    for block,oldblock in zip(geometry['blocks'],prior['blocks']):
        X=block['X']
        layers=[]
        for layer,oldlayer in zip(block['levels'],oldblock['levels']):
            packets=[]
            totals={key:m.ZERO for key in ('true_positive','constant_variance','isotonic_variance','crossing_pool_variance','crossing_residual','pooled_geometry')}
            max_pool_width=0
            max_skew=F(1)
            for p,oldp in zip(layer['packets'],oldlayer['packets']):
                L,x,R=p['L'],p['x'],p['R']
                a,b,h=x-L,R-x,R-L
                pools=[]
                for n in range(L,R):
                    pools.append([n,n+1,mean(n,n+1)])
                    while len(pools)>1:
                        u,v=pools[-2:]
                        if u[2][1]<=v[2][0]:
                            break
                        if u[2][0]<=v[2][1]:
                            counts['ambiguous_pool_merges']+=1
                        pools[-2:]=[[u[0],v[1],mean(u[0],v[1])]]
                assert all(pools[i][2][1]<=pools[i+1][2][0] for i in range(len(pools)-1))
                total_variance=m.ZERO
                kkt=True
                for u,v,pool_mean in pools:
                    total_variance=m.add(total_variance,variance(u,v))
                    for z in range(u+1,v):
                        residual=m.sub(sum_a(u,z),m.qmul(sum_a(u,v),mass(u,z)/mass(u,v)))
                        assert residual[0]>=0, (L,x,R,u,z,v,residual)
                        counts['kkt_prefixes']+=1
                direct=m.qmul(m.sub(mean(L,x),mean(x,R)),1,x)
                old_tau=m.decode(oldp['prime_only_tent_deficit'])
                assert m.overlap(direct,old_tau)
                squared=m.qmul(m.square(m.positive(direct)),F(h**3,X**2))
                baseline=m.qmul(variance(L,R),F(h**4,a*b*X**2))
                isotonic=m.qmul(total_variance,F(h**4,a*b*X**2))
                crossing=next(((u,v,mm) for u,v,mm in pools if u<x<v),None)
                if crossing:
                    u,v,mm=crossing
                    S=m.sub(sum_a(u,x),m.qmul(sum_a(u,v),mass(u,x)/mass(u,v)))
                    crossing_var=m.qmul(variance(u,v),F(h**5*(x-u)*(v-x),a*a*b*b*(v-u)*X**2))
                    crossing_res=m.qmul(m.square(S),F(h**5*x*x,a*a*b*b*X**2))
                    if len(pools)==1:
                        assert m.overlap(squared,crossing_res)
                    else:
                        assert squared[1]<=crossing_res[0], (p,squared,crossing_res)
                    pool_info={'u':u,'v':v,'weighted_variance':m.record(variance(u,v)),
                               'prefix_residual':m.record(S)}
                    geometric=m.rat(F(h**5*(x-u)**2*(v-x)**2,4*a*a*b*b*u*u*X*X))
                    assert squared[1]<=geometric[0]
                    max_pool_width=max(max_pool_width,v-u)
                else:
                    assert direct[1]<=0
                    crossing_var=crossing_res=m.ZERO
                    pool_info=None
                    geometric=m.ZERO
                    counts['boundary_splits']+=1
                assert isotonic[1]<=baseline[0] or len(pools)==1
                totals['true_positive']=m.add(totals['true_positive'],squared)
                totals['constant_variance']=m.add(totals['constant_variance'],baseline)
                totals['isotonic_variance']=m.add(totals['isotonic_variance'],isotonic)
                totals['crossing_pool_variance']=m.add(totals['crossing_pool_variance'],crossing_var)
                totals['crossing_residual']=m.add(totals['crossing_residual'],crossing_res)
                totals['pooled_geometry']=m.add(totals['pooled_geometry'],geometric)
                max_skew=max(max_skew,F(h*h,4*a*b))
                packets.append({**p,'pool_intervals':[[u,v] for u,v,_ in pools],
                                'monotonicity_and_all_kkt_prefixes_certified':kkt,
                                'tau':m.record(direct),'crossing_pool':pool_info,
                                'constant_variance_bound':m.record(baseline),
                                'isotonic_variance_bound':m.record(isotonic),
                                'crossing_pool_variance_bound':m.record(crossing_var),
                                'crossing_residual_bound':m.record(crossing_res),
                                'pooled_geometry_bound':m.record(geometric)})
                counts['packets']+=1
                counts['pools']+=len(pools)
            max_geometry=m.rat(max_skew**2*F(max_pool_width**4,4*X**3))
            assert totals['pooled_geometry'][1]<=max_geometry[0] or max_pool_width==0
            layers.append({'level':layer['level'],'max_crossing_pool_width':max_pool_width,
                           'max_skew_exact':str(max_skew),'max_pool_geometry_bound':m.record(max_geometry),
                           'budgets':{k:m.record(v) for k,v in totals.items()},'packets':packets})
        rows.append({'X':X,'Y':block['Y'],'levels':layers})
    return rows,counts


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--prior',type=Path,required=True)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('isotonic_certificate.json'))
    args=parser.parse_args()
    module_path=args.prior/'prior/riemann_cumulative_haar_20261123/dependencies/certify_fast_harmonic_energy.py'
    m=load_module(module_path)
    geometry=json.loads((args.prior/'directed_arithmetic/fixed_triangle_geometry.json').read_text())
    old=json.loads((args.prior/'directed_arithmetic/local_arithmetic_certificate.json').read_text())
    checks=exact_checks()
    rows,counts=compute(m,geometry,old)
    result={'schema':'RH_ISOTONIC_DIRECTED_DEFICIT_V1','status':'PASS',
            'scope':'Author proof plus finite fixed-38-packet certification; unbounded isotonic bound remains open.',
            'arithmetic':{'outward_decimal_digits':m.DIGITS,'prime_sieve_limit':max(b['Y'] for b in geometry['blocks']),
                          'decision_arithmetic':'integer outward intervals and exact rationals'},
            'exact_checks':checks,'counts':counts,'blocks':rows}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    summary=[]
    for block in rows:
        for layer in block['levels']:
            summary.append({'X':block['X'],'level':layer['level'],**{k:v['upper'] for k,v in layer['budgets'].items()}})
    print(json.dumps({'status':'PASS','exact_checks':checks,'counts':counts,'layers':summary},ensure_ascii=False))


if __name__=='__main__':
    main()
