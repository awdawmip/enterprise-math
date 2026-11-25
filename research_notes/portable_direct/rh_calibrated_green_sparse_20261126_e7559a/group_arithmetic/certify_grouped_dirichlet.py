#!/usr/bin/env python3
"""Exact finite coarsening/Dirichlet checks and saved-anchor interval certificate."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations, product
import argparse
import hashlib
import importlib.util
import json


def hat(a,b,c,x):
    if a<=x<=b:return F(x-a,b-a)
    if b<=x<=c:return F(c-x,c-b)
    return F(0)


def coarse_sets(n):
    for k in range(n-1):
        for middle in combinations(range(1,n-1),k):yield (0,)+middle+(n-1,)


def positive_gradient(x,v):
    result=F(0)
    for a,b,u,w in zip(x,x[1:],v,v[1:]):
        if u<=0 and w<=0:continue
        length=F(b-a)
        if u<0:length*=w/(w-u)
        elif w<0:length*=u/(u-w)
        result+=(w-u)**2/(b-a)**2*length
    return result


def generic_checks():
    counts={'roads':0,'blocks':0,'positive_gradient_identities':0,
            'centered_variance_identities':0,'coarse_moment_identities':0,
            'source_hat_compositions':0,'integer_energy_bounds':0,
            'closed_integer_points':0,'green_parabola_identities':0,
            'quartic_sums':0}
    grids=([2,3,4],[2,3,5,7],[3,4,6,8,10],list(range(2,9)))
    for x in grids:
        coarse=list(coarse_sets(len(x)))
        for idx in coarse:
            for a,b,c in zip(idx,idx[1:],idx[2:]):
                for n in range(x[0],x[-1]+1):
                    fine=sum((hat(x[a],x[b],x[c],x[k])*hat(x[k-1],x[k],x[k+1],n)
                              for k in range(1,len(x)-1)),F(0))
                    assert fine==hat(x[a],x[b],x[c],n)
                    counts['source_hat_compositions']+=1
        for inner in product((-2,0,3),repeat=len(x)-2):
            q=list(map(F,(2,)+inner+(-1,)))
            slopes=[(v-u)/(b-a) for a,b,u,v in zip(x,x[1:],q,q[1:])]
            t=[slopes[k-1]-slopes[k] for k in range(1,len(x)-1)]
            counts['roads']+=1
            for idx in coarse:
                for a,b,c in zip(idx,idx[1:],idx[2:]):
                    direct=(q[b]-q[a])/(x[b]-x[a])-(q[c]-q[b])/(x[c]-x[b])
                    rebuilt=sum((hat(x[a],x[b],x[c],x[k])*t[k-1]
                                 for k in range(1,len(x)-1)),F(0))
                    assert direct==rebuilt;counts['coarse_moment_identities']+=1
            for i in range(len(x)-1):
                for j in range(i+1,len(x)):
                    a,b=x[i],x[j];h=b-a;mean=(q[j]-q[i])/h
                    v=[q[k]-q[i]-(x[k]-a)*mean for k in range(i,j+1)]
                    signed=sum((t[k-1]*max(v[k-i],0) for k in range(i+1,j)),F(0))
                    assert signed==positive_gradient(x[i:j+1],v)>=0
                    full=sum((F(x[k+1]-x[k])*(slopes[k]-mean)**2 for k in range(i,j)),F(0))
                    B=[sum(t[i:k],F(0)) for k in range(i,j)]
                    width=[F(x[k+1]-x[k]) for k in range(i,j)]
                    bar=sum((z*w for z,w in zip(B,width)),F(0))/h
                    variance=sum((w*(z-bar)**2 for z,w in zip(B,width)),F(0))
                    pair=sum((width[k]*width[l]*(B[k]-B[l])**2
                              for k in range(len(B)) for l in range(k+1,len(B))),F(0))/h
                    assert variance==pair==full and signed<=full
                    # Fully rational upper bound: log(b/a) <= h(1/a+1/b)/2,
                    # pi >= 3. It bounds the sharper analytic constant above.
                    ell=F(h,2)*(F(1,a)+F(1,b))
                    c=(1+F(a+1,a+2)**2)/2
                    C=(ell*ell/(9+ell*ell/4)+F(1,6*(a+1)**2))/c
                    energy=F(0)
                    for k in range(i,j):
                        for n in range(x[k],x[k+1]):
                            z=v[k-i]+F(n-x[k])*(slopes[k]-mean)
                            energy+=max(z,0)**2/(n*n)
                            counts['closed_integer_points']+=1
                    counts['closed_integer_points']+=1 # zero right endpoint
                    assert energy<=C*signed
                    counts['blocks']+=1;counts['positive_gradient_identities']+=1
                    counts['centered_variance_identities']+=1;counts['integer_energy_bounds']+=1
    for h in range(1,41):
        assert sum(F(r*r*(h-r)**2) for r in range(h+1))==F(h**5-h,30)
        counts['quartic_sums']+=1
        for x in range(h+1):
            value=sum((F(min(x,z)*(h-max(x,z)),h) for z in range(1,h)),F(0))
            assert value==F(x*(h-x),2)
            counts['green_parabola_identities']+=1
    return {'counts':counts,'directional_witness':{
        'nodes':[2,3,4,5,6],'residual_values':['0','-2u','-u','-2u','0'],
        'interior_moments':['-3u','2u','-3u'],'parameter':'u>0',
        'positive_dirichlet_energy':'0','positive_moment_nonzero':True}}


def module_at(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


def atan_bounds(x,terms):
    total=sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(terms)),F(0))
    next_term=(-1)**terms*x**(2*terms+1)/F(2*terms+1)
    return min(total,total+next_term),max(total,total+next_term)


def pi_bounds():
    a=atan_bounds(F(1,5),70);b=atan_bounds(F(1,239),20)
    twice=2*F(1,5)/(1-F(1,5)**2);four=2*twice/(1-twice**2)
    assert (four-F(1,239))/(1+four*F(1,239))==1
    result=16*a[0]-4*b[1],16*a[1]-4*b[0]
    assert 3<result[0]<result[1]<4
    return result


def saved_checks(previous):
    base=previous/'prior/riemann_native_residual_growth_20261124/prior/riemann_matching_isotonic_anchors_20261124'
    data_path=base/'seams/saved_anchor_certificate.json'
    helper_path=base/'prior/riemann_directed_local_20261124/prior/riemann_cumulative_haar_20261123/dependencies/certify_fast_harmonic_energy.py'
    m=module_at('group_dirichlet_interval',helper_path)
    data=json.loads(data_path.read_text());anchors=data['anchors']
    x=[a['x'] for a in anchors]
    q=[(m.rat(F(a['actual']['exact_bounds'][0]))[0],m.rat(F(a['actual']['exact_bounds'][1]))[1]) for a in anchors]
    slopes=[m.qmul(m.sub(v,u),1,b-a) for a,b,u,v in zip(x,x[1:],q,q[1:])]
    t=[m.sub(slopes[k-1],slopes[k]) for k in range(1,len(x)-1)]
    pi_lo,pi_hi=pi_bounds();rows=[];lookup={};point_count=0
    strict_signed_savings=0;zero_blocks=0
    for i in range(len(x)-1):
        for j in range(i+1,len(x)):
            L,R=x[i],x[j];h=R-L;mean=m.qmul(m.sub(q[j],q[i]),1,h)
            v=[m.ZERO]+[m.sub(q[k],m.add(m.qmul(q[i],R-x[k],h),m.qmul(q[j],x[k]-L,h))) for k in range(i+1,j)]+[m.ZERO]
            dplus=m.total(m.mul(t[k-1],m.positive(v[k-i])) for k in range(i+1,j))
            dplus=(max(0,dplus[0]),max(0,dplus[1]))
            negative=m.total(m.mul(m.positive(m.neg(t[k-1])),m.positive(v[k-i])) for k in range(i+1,j))
            full=m.total(m.qmul(m.square(m.sub(slopes[k],mean)),x[k+1]-x[k]) for k in range(i,j))
            assert dplus[0]<=full[1]
            ell=m.sub(m.log_int(R),m.log_int(L));ellu=F(ell[1],m.S)
            c=(1+F(L+1,L+2)**2)/2
            Cupper=(ellu**2/(pi_lo**2+ellu**2/4)+F(1,6*(L+1)**2))/c
            bound=m.qmul(dplus,Cupper)
            full_bound=m.qmul(full,Cupper)
            positive_charge_bound=m.qmul(m.add(dplus,negative),Cupper)
            energy=m.ZERO
            for k in range(i,j):
                for n in range(x[k],x[k+1]):
                    z=m.add(m.qmul(v[k-i],x[k+1]-n,x[k+1]-x[k]),m.qmul(v[k+1-i],n-x[k],x[k+1]-x[k]))
                    energy=m.add(energy,m.qmul(m.square(m.positive(z)),1,n*n));point_count+=1
            point_count+=1
            assert energy[1]<=bound[1],(L,R,m.record(energy),m.record(bound))
            if negative[0]>0:strict_signed_savings+=1
            if dplus[1]==0:zero_blocks+=1;assert energy==(0,0)
            row={'L':L,'R':R,'interior_anchor_count':j-i-1,
                 'positive_residual_square_energy':m.record(energy),
                 'signed_positive_dirichlet_energy':m.record(dplus),
                 'centered_slope_variance':m.record(full),
                 'negative_moment_subtraction':m.record(negative),
                 'closed_constant_upper':m.record(m.rat(Cupper)),
                 'directional_energy_upper':m.record(bound),
                 'full_variance_energy_upper':m.record(full_bound),
                 'positive_moments_only_energy_upper':m.record(positive_charge_bound)}
            rows.append(row);lookup[i,j]=row
    partitions=[]
    for step in (2,4,8,10):
        cuts=list(range(0,len(x)-1,step))+[len(x)-1]
        selected=[lookup[a,b] for a,b in zip(cuts,cuts[1:])]
        totals={name:m.record(m.total(m.decode(r[name]) for r in selected)) for name in
                ('positive_residual_square_energy','directional_energy_upper','full_variance_energy_upper','positive_moments_only_energy_upper')}
        partitions.append({'coarse_nodes':[x[k] for k in cuts],'totals':totals})
    return {'input_anchor_count':len(x),'new_q_queries':0,'new_D_queries':0,
            'subintervals_checked':len(rows),'closed_integer_points':point_count,
            'identically_nonpositive_residual_blocks':zero_blocks,
            'blocks_with_strict_negative_moment_subtraction':strict_signed_savings,
            'pi_bounds':list(map(str,(pi_lo,pi_hi))),
            'dependencies':[{'path':str(p.relative_to(previous)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in (data_path,helper_path)],
            'partitions':partitions,'subintervals':rows}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--previous',type=Path,required=True)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('grouped_dirichlet_certificate.json'))
    args=parser.parse_args()
    result={'schema':'EM_GROUPED_DIRECTIONAL_DIRICHLET_V1','status':'PASS',
            'scope':'Author finite checks of exact arithmetic coarsening, positive-part Dirichlet identity, centered variance and closed integer bound; all 55 saved-anchor endpoint subintervals. Infinite statements are proved analytically in the companion note.',
            'arithmetic':'Exact fractions for generic identities; 80-digit outward integer intervals for actual data and logarithms; pi enclosed by exact alternating arctangent series and rational Machin identity.',
            'generic':generic_checks(),'saved_actual':saved_checks(args.previous)}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'generic':result['generic']['counts'],
                     'actual_subintervals':result['saved_actual']['subintervals_checked'],
                     'actual_closed_points':result['saved_actual']['closed_integer_points'],
                     'strict_signed_savings':result['saved_actual']['blocks_with_strict_negative_moment_subtraction'],
                     'zero_residual_blocks':result['saved_actual']['identically_nonpositive_residual_blocks'],
                     'dyadic_partition':result['saved_actual']['partitions'][0]},ensure_ascii=False))


if __name__=='__main__':main()
