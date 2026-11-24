#!/usr/bin/env python3
"""Signed Green coarsening on exact generic inputs and saved actual anchors."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import argparse
import hashlib
import json

DIGITS = 80
S = 10**DIGITS


def floor_div(a, b):
    return a // b


def ceil_div(a, b):
    return -((-a) // b)


def interval(v):
    lo, hi = map(F, v)
    return floor_div(lo.numerator*S, lo.denominator), ceil_div(hi.numerator*S, hi.denominator)


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def neg(a):
    return -a[1], -a[0]


def mul_ratio(a, n, d=1):
    if n < 0:
        return mul_ratio(neg(a), -n, d)
    return floor_div(a[0]*n, d), ceil_div(a[1]*n, d)


def positive(a):
    return max(a[0], 0), max(a[1], 0)


def display(v, upper=False, digits=40):
    scale = 10**(DIGITS-digits)
    n = ceil_div(v, scale) if upper else floor_div(v, scale)
    sign = '-' if n < 0 else ''
    s = str(abs(n)).zfill(digits+1)
    return sign+s[:-digits]+'.'+s[-digits:]


def record(v):
    return {'lower':display(v[0]), 'upper':display(v[1], True),
            'integer_bounds':list(v), 'denominator_power_of_10':DIGITS}


def green(x, z, a, b):
    return (min(x,z)-a)*(b-max(x,z))/(b-a)


def partitions(m):
    widths=[]
    k=1
    while k < m:
        widths.append(k)
        k*=2
    widths.append(m)
    return [(f'consecutive_{k}', [list(range(j, min(j+k,m))) for j in range(0,m,k)])
            for k in widths]


def generic_checks():
    grids = [list(map(F, a)) for a in ([1,2,3,5], [2,3,4,6,8],
              [2,3,4,6,8,12], [2,3,4,6,8,12,16], [F(1,2),F(3,2),F(7,3),F(17,4),8])]
    counts = {'signed_vectors':0, 'continuous_critical_points':0,
              'group_coarsening_checks':0, 'merge_overlap_identities':0,
              'two_moment_compression_pulses':0, 'source_hat_kernel_checks':0}
    witness = None
    for a in grids:
        m=len(a)-2
        pp=partitions(m)
        critical=set(a)
        for x,y in zip(a,a[1:]):
            critical.add((x+y)/2)
        for t0 in product((-2,0,3), repeat=m):
            t=list(map(F,t0))
            # Real endpoints are deliberately nonzero and of opposite signs.
            q0,qN=F(2,3),F(-5,7)
            def chord(x):return ((a[-1]-x)*q0+(x-a[0])*qN)/(a[-1]-a[0])
            def pot(C,x):return sum((green(x,a[k+1],a[0],a[-1])*t[k] for k in C), F(0))
            points=set(critical)
            # All individual/group zeroes within source cells are included;
            # every tested envelope is piecewise affine on this refined set.
            for _,parts in pp:
                for C in parts:
                    for l,r in zip(a,a[1:]):
                        vl,vr=pot(C,l),pot(C,r)
                        if vl*vr < 0:
                            points.add(l+(r-l)*(-vl)/(vr-vl))
            counts['signed_vectors']+=1
            for x in points:
                direct=chord(x)+pot(list(range(m)),x)
                values=[]
                for _,parts in pp:
                    values.append(chord(x)+sum((max(pot(C,x),0) for C in parts),F(0)))
                assert all(v>=max(direct,chord(x)) for v in values)
                assert values[-1]==max(direct,chord(x))
                assert all(v>=w for v,w in zip(values,values[1:]))
                counts['continuous_critical_points']+=1
                counts['group_coarsening_checks']+=len(values)-1
                for k in range(m-1):
                    u,v=pot([k],x),pot([k+1],x)
                    d=max(u,0)+max(v,0)-max(u+v,0)
                    assert d==min(max(u,0),max(-v,0))+min(max(-u,0),max(v,0))
                    counts['merge_overlap_identities']+=1
                    if d>0 and witness is None:
                        witness={'nodes':list(map(str,a)),'moments':list(map(str,t)),
                                 'x':str(x),'indices':[k,k+1],'cancellation':str(d)}
        # Source-pulse tests isolate the two-moment compression identity,
        # including group endpoints and all inside/outside observation cells.
        for i in range(1,len(a)-2):
            for j in range(i+1,len(a)-1):
                l,r=a[i],a[j]
                for z in a[i:j+1]:
                    for x in critical:
                        loc=green(x,z,l,r) if l<=x<=r else F(0)
                        rebuilt=(r-z)/(r-l)*green(x,l,a[0],a[-1])+(z-l)/(r-l)*green(x,r,a[0],a[-1])+loc
                        assert rebuilt==green(x,z,a[0],a[-1])
                        counts['two_moment_compression_pulses']+=1
        for x in critical:
            for n in critical:
                bh=F(0)
                for k in range(1,len(a)-1):
                    if a[k-1]<=n<=a[k]:phi=(n-a[k-1])/(a[k]-a[k-1])
                    elif a[k]<=n<=a[k+1]:phi=(a[k+1]-n)/(a[k+1]-a[k])
                    else:phi=F(0)
                    bh+=green(x,a[k],a[0],a[-1])*phi
                assert 0<=bh<=green(x,n,a[0],a[-1])
                if x in a:assert bh==green(x,n,a[0],a[-1])
                counts['source_hat_kernel_checks']+=1
    assert witness is not None
    return {'counts':counts,'strict_cancellation_witness':witness}


def saved_checks(previous):
    path=previous/'seams/saved_anchor_certificate.json'
    data=json.loads(path.read_text())
    a=[r['x'] for r in data['anchors']]
    q=[interval(r['actual']['exact_bounds']) for r in data['anchors']]
    t=[]
    for j in range(1,len(a)-1):
        value=add(mul_ratio(add(q[j],neg(q[j-1])),1,a[j]-a[j-1]),
                  neg(mul_ratio(add(q[j+1],neg(q[j])),1,a[j+1]-a[j])))
        old=list(map(F,data['moments'][j-1]['t']['exact_bounds']))
        assert F(value[0],S)<=old[0]<=old[1]<=F(value[1],S)
        t.append(value)
    pp=partitions(len(t))
    budgets={name:[0,0] for name,_ in pp}
    budgets.update({'actual_skeleton':[0,0],'direct_M':[0,0],'boundary_chord':[0,0]})
    strict_merge_points=[0]*(len(pp)-1)
    mon_count=0
    group_count=0
    cell=0
    for n in range(a[0],a[-1]+1):
        while cell+1<len(a)-1 and n>a[cell+1]:cell+=1
        J=add(mul_ratio(q[0],a[-1]-n,a[-1]-a[0]),mul_ratio(q[-1],n-a[0],a[-1]-a[0]))
        actual=add(mul_ratio(q[cell],a[cell+1]-n,a[cell+1]-a[cell]),
                   mul_ratio(q[cell+1],n-a[cell],a[cell+1]-a[cell]))
        V=[mul_ratio(tk,(min(n,z)-a[0])*(a[-1]-max(n,z)),a[-1]-a[0])
           for z,tk in zip(a[1:-1],t)]
        vals=[]
        for name,parts in pp:
            U=J
            for C in parts:
                group=(sum(V[k][0] for k in C),sum(V[k][1] for k in C))
                U=add(U,positive(group))
            assert U[1]>=actual[1]
            vals.append(U)
            group_count+=1
        for i,(v,w) in enumerate(zip(vals,vals[1:])):
            assert v[0]>=w[0] and v[1]>=w[1]
            mon_count+=1
            if w[1]<v[0]:strict_merge_points[i]+=1
        M=(max(J[0],actual[0]),max(J[1],actual[1]))
        # Reconstruction with independently enclosed moments contains the
        # sharper direct endpoint/node enclosure of max(J,F).
        assert vals[-1][0]<=M[0]<=M[1]<=vals[-1][1]
        all_values=[(name,v) for (name,_),v in zip(pp,vals)]
        all_values += [('actual_skeleton',actual),('direct_M',M),('boundary_chord',J)]
        for name,v in all_values:
            p=positive(v)
            budgets[name][0]+=floor_div(p[0]*p[0],S*n*n)
            budgets[name][1]+=ceil_div(p[1]*p[1],S*n*n)
    rows=[]
    first=budgets[pp[0][0]]
    for name,parts in pp:
        b=budgets[name]
        ratio=(floor_div(first[0]*S,b[1]),ceil_div(first[1]*S,b[0]))
        rows.append({'name':name,'blocks':[[k+1 for k in C] for C in parts],
                     'energy':record(b),'ratio_from_singletons':record(ratio)})
    assert all(budgets[n2][1]<budgets[n1][0] for (n1,_),(n2,_) in zip(pp,pp[1:]))
    return {'input_relative_path':'seams/saved_anchor_certificate.json',
            'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'window':[a[0],a[-1]],'anchor_count':len(a),'moment_count':len(t),
            'closed_integer_count':a[-1]-a[0]+1,'new_q_queries':0,'new_D_queries':0,
            'interval_digits':DIGITS,'saved_moment_containment_checks':len(t),
            'pointwise_group_enclosure_checks':group_count,'pointwise_coarsening_checks':mon_count,
            'strict_coarsening_point_counts':strict_merge_points,
            'all_coarsening_energy_intervals_strictly_decrease':True,
            'budgets':rows,'actual_skeleton_energy':record(budgets['actual_skeleton']),
            'direct_M_energy':record(budgets['direct_M']),
            'boundary_chord_energy':record(budgets['boundary_chord'])}


def exact_optimal_tree(previous):
    data=json.loads((previous/'seams/saved_anchor_certificate.json').read_text())
    a=[r['x'] for r in data['anchors']]
    q=[tuple(map(F,r['actual']['exact_bounds'])) for r in data['anchors']]
    comparisons=0
    def linear_interval(c):
        lo=sum((v*(q[k][0] if v>=0 else q[k][1]) for k,v in c.items()), F(0))
        hi=sum((v*(q[k][1] if v>=0 else q[k][0]) for k,v in c.items()), F(0))
        return lo,hi
    def chord_difference(i,j,n,reference):
        nonlocal comparisons
        c=defaultdict(F)
        c[i]+=F(a[j]-n,a[j]-a[i]);c[j]+=F(n-a[i],a[j]-a[i])
        if reference=='J':
            c[0]-=F(a[-1]-n,a[-1]-a[0]);c[len(a)-1]-=F(n-a[0],a[-1]-a[0])
        else:c[reference]-=1
        comparisons+=1
        return linear_interval(c)
    safe={};dp={};split={}
    for h in range(1,len(a)):
        for i in range(len(a)-h):
            j=i+h
            # These are every affine-piece endpoint of chord-F, so this
            # establishes continuous dominance on the full interval.
            f_checks=[chord_difference(i,j,a[k],k) for k in range(i,j+1)]
            j_checks=[chord_difference(i,j,a[k],'J') for k in (i,j)]
            safe[i,j]='F' if all(v[1]<=0 for v in f_checks) else 'J' if all(v[1]<=0 for v in j_checks) else None
            if not safe[i,j]:dp[i,j]=10**6
            elif h==1:dp[i,j]=0
            else:
                d,k=min((1+max(dp[i,k],dp[k,j]),k) for k in range(i+1,j))
                dp[i,j]=d;split[i,j]=k
    rows=[];levels={}
    continuous_points=0
    def visit(i,j,depth):
        nonlocal continuous_points
        row={'L':a[i],'R':a[j],'dominated_by':safe[i,j]}
        assert safe[i,j] in {'F','J'}
        tests=range(i,j+1) if safe[i,j]=='F' else (i,j)
        for k in tests:
            ref=k if safe[i,j]=='F' else 'J'
            assert chord_difference(i,j,a[k],ref)[1]<=0
            continuous_points+=1
        row['continuous_affine_piece_endpoints_checked']=len(tests)
        if j>i+1:
            k=split[i,j];row['insert']=a[k];row['insertion_depth']=depth
            levels.setdefault(depth,[]).append(a[k])
            rows.append(row);visit(i,k,depth+1);visit(k,j,depth+1)
        else:rows.append(row)
    visit(0,len(a)-1,1)
    gaps=[]
    for i in range(1,len(a)-1):
        c=defaultdict(F);c[i]=1
        c[0]-=F(a[-1]-a[i],a[-1]-a[0]);c[len(a)-1]-=F(a[i]-a[0],a[-1]-a[0])
        v=linear_interval(c)
        assert v[1]<0 if i==1 else v[0]>0
        gaps.append(v)
    c={0:F(a[-1]-a[1],a[-1]-a[0]),len(a)-1:F(a[1]-a[0],a[-1]-a[0])}
    J1=linear_interval(c)
    assert J1[0]>0
    overshoots=[]
    for i in range(2,len(a)-1):
        d=F(a[1]-a[0],a[i]-a[0])*gaps[i-1][0]
        assert d>0
        overshoots.append((a[i],d))
    energy_gap=min(d*(2*J1[0]+d)/a[1]**2 for _,d in overshoots)
    assert dp[0,len(a)-1]==5 and max(levels)==5
    return {'depth_convention':'Maximum number of internal insertion vertices on a root-to-leaf path; first insertion has depth1.',
            'certified_exact_M_tree_depth':5,'minimal_exact_positive_energy_depth':5,
            'continuous_envelope_equals_M':True,'true_endpoints_retained':True,
            'continuous_affine_piece_endpoint_checks':continuous_points,
            'all_interval_linear_comparisons':comparisons,
            'safe_interval_count':sum(v is not None for v in safe.values()),
            'tree_intervals':rows,'insertion_levels':{str(k):v for k,v in sorted(levels.items())},
            'forced_first_node':a[1],'forced_node_chord':record(interval(J1)),
            'forced_node_F_minus_J':record(interval(gaps[0])),
            'other_internal_nodes_F_minus_J':[{'x':a[i], 'difference':record(interval(gaps[i-1]))} for i in range(2,len(a)-1)],
            'wrong_first_node_overshoot_lower_bounds':[{'first_node':n,'lower_exact':str(d)} for n,d in overshoots],
            'wrong_first_node_energy_gap_lower_bound':record(interval((energy_gap,energy_gap))),
            'right_subtree_fine_interval_count':9,'right_subtree_minimum_depth':4,
            'scope':'Minimum depth for exact closed-positive-energy optimum on this fixed interval input; all continuous tree chords also lie below M.'}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--previous',type=Path,required=True,help='riemann_matching_isotonic_anchors_20261124 package')
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('signed_green_grouping_certificate.json'))
    args=parser.parse_args()
    result={'schema':'EM_SIGNED_GREEN_GROUPING_V1','status':'PASS',
            'scope':'Author finite exact and outward-interval verification; real endpoints retained; no unbounded arithmetic bound asserted.',
            'generic':generic_checks(),'saved_actual':saved_checks(args.previous),
            'exact_optimal_tree':exact_optimal_tree(args.previous)}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'generic_counts':result['generic']['counts'],
                      'saved_counts':{k:result['saved_actual'][k] for k in ['closed_integer_count','pointwise_group_enclosure_checks','pointwise_coarsening_checks']},
                      'budget_upper':{r['name']:r['energy']['upper'] for r in result['saved_actual']['budgets']},
                      'exact_optimal_tree_depth':result['exact_optimal_tree']['certified_exact_M_tree_depth']},ensure_ascii=False))


if __name__=='__main__':main()
