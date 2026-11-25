#!/usr/bin/env python3
"""Exhaustive closed-integer energy optimization over the 114 depth-four trees.

All numerical decisions use exact fractions or outward integer intervals.
The eleven true nodes and values are read from the saved predecessor.
"""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import argparse
import hashlib
import json

S=10**60


def ceildiv(a,b):return -((-a)//b)


def decimal(v,digits=45,upper=False):
    d=10**digits
    z=ceildiv(v*d,S) if upper else v*d//S
    sign='-' if z<0 else '';z=abs(z)
    return sign+str(z//d)+'.'+str(z%d).zfill(digits)


def record(bounds):
    return {'lower':decimal(bounds[0]),'upper':decimal(bounds[1],upper=True),
            'scaled_integer_bounds':list(map(str,bounds)),'scale':str(S)}


def fraction_record(bounds):
    l,u=bounds
    return record((l.numerator*S//l.denominator,ceildiv(u.numerator*S,u.denominator)))


@lru_cache(None)
def trees(i,j,d):
    if j==i+1:return (None,)
    if d==0 or j-i>2**d:return ()
    return tuple((k,l,r) for k in range(i+1,j)
                 for l in trees(i,k,d-1) for r in trees(k,j,d-1))


def edges(tree,i,j):
    yield i,j
    if tree is not None:
        k,l,r=tree
        yield from edges(l,i,k);yield from edges(r,k,j)


def levels(tree,x):
    out=[]
    def walk(t,depth):
        if t is None:return
        while len(out)<=depth:out.append([])
        k,l,r=t;out[depth].append(x[k]);walk(l,depth+1);walk(r,depth+1)
    walk(tree,0)
    return [sorted(row) for row in out]


def curve(edge_set,x,chords):
    lower=[0]*(x[-1]-x[0]+1);upper=lower.copy()
    for i,j in edge_set:
        base=x[i]-x[0];cl,cu=chords[i,j]
        for k,(l,u) in enumerate(zip(cl,cu)):
            p=base+k
            if l>lower[p]:lower[p]=l
            if u>upper[p]:upper[p]=u
    return lower,upper


def energy(c,x):
    lower=upper=0
    for n,l,u in zip(range(x[0],x[-1]+1),*c):
        den=S*n*n;lower+=l*l//den;upper+=ceildiv(u*u,den)
    return lower,upper


def chord_coeff(i,j,y,x):
    if y==x[i]:return {i:F(1)}
    if y==x[j]:return {j:F(1)}
    return {i:F(x[j]-y,x[j]-x[i]),j:F(y-x[i],x[j]-x[i])}


def difference_upper(left,right,q):
    coefficients=left.copy()
    for k,v in right.items():coefficients[k]=coefficients.get(k,F(0))-v
    return sum((v*q[k][1 if v>=0 else 0] for k,v in coefficients.items()),F(0))


def certify_common_root_envelope(tied,candidates,x,q,root):
    """Every selected tree has E=max(F,P_root), continuously, via affine comparisons."""
    comparisons=0;edge_rows=[]
    for tree_id in tied:
        assert candidates[tree_id][0]==root
        for i,j in edges(candidates[tree_id],0,len(x)-1):
            if i==0 and j==len(x)-1:
                values=[difference_upper(chord_coeff(i,j,x[k],x),
                       chord_coeff(0,root,x[k],x) if k<=root else chord_coeff(root,j,x[k],x),q)
                        for k in (0,root,j)]
                comparisons+=len(values);assert max(values)<=0
                edge_rows.append({'tree':tree_id,'edge':[x[i],x[j]],'dominated_by':'first_split_polygon'})
                continue
            values=[difference_upper(chord_coeff(i,j,x[k],x),{k:F(1)},q) for k in range(i,j+1)]
            comparisons+=len(values)
            if max(values)<=0:
                edge_rows.append({'tree':tree_id,'edge':[x[i],x[j]],'dominated_by':'complete_F'})
                continue
            assert j<=root or i>=root
            a,b=(0,root) if j<=root else (root,len(x)-1)
            values=[difference_upper({k:F(1)},chord_coeff(a,b,x[k],x),q) for k in (i,j)]
            comparisons+=len(values);assert max(values)<=0
            edge_rows.append({'tree':tree_id,'edge':[x[i],x[j]],'dominated_by':'first_split_polygon'})
    return {'scope':'Continuous entire closed interval; all four envelopes equal max(F,P_4096).',
            'exact_rational_interval_comparisons':comparisons,'edge_dominance':edge_rows}


def continuous_overrun_comparison(candidates,x,q,rows,energy_best):
    midpoint=[(l+u)/2 for l,u in q]
    radius=max((u-l)/2 for l,u in q)
    def line(i,j,y):
        return ((x[j]-y)*midpoint[i]+(y-x[i])*midpoint[j])/(x[j]-x[i])
    critical=list(zip(map(F,x),midpoint))
    for k in range(len(x)-1):
        l=midpoint[k]-line(0,len(x)-1,x[k])
        r=midpoint[k+1]-line(0,len(x)-1,x[k+1])
        if l*r<0:
            y=(r*x[k]-l*x[k+1])/(r-l)
            critical.append((y,line(0,len(x)-1,y)))
    critical=[(y,max(v,line(0,len(x)-1,y))) for y,v in critical]
    costs={(i,j):max([F(0)]+[line(i,j,y)-v for y,v in critical if x[i]<=y<=x[j]])
           for i in range(len(x)) for j in range(i+1,len(x))}
    nominal=[max(costs[e] for e in edges(t,0,len(x)-1)) for t in candidates]
    bounds=[(max(F(0),v-2*radius),v+2*radius) for v in nominal]
    best=min(range(len(candidates)),key=lambda i:bounds[i][1])
    tied=[i for i,b in enumerate(bounds) if b[0]<=bounds[best][1]]
    assert tied==[52,53,70,71]
    shared=(0,2);strict_dominance=0
    for i in tied:
        es=list(edges(candidates[i],0,len(x)-1));assert shared in es
        for edge in es:
            if edge!=shared:
                assert costs[edge]+4*radius<costs[shared]
                strict_dominance+=1
    residuals=[]
    for k in (1,2):
        jc=chord_coeff(0,len(x)-1,x[k],x)
        residuals.append((-difference_upper(jc,{k:F(1)},q),difference_upper({k:F(1)},jc,q)))
    assert residuals[0][1]<0<residuals[1][0]
    slope_difference={0:F(1,x[2]-x[0]),1:-F(1,x[2]-x[1]),
                      2:F(1,x[2]-x[1])-F(1,x[2]-x[0])}
    slope_lower=-difference_upper({},slope_difference,q);assert slope_lower>0
    l,u=residuals
    cross_bounds=((u[0]*x[1]-l[1]*x[2])/(u[1]-l[0]),
                  (u[1]*x[1]-l[0]*x[2])/(u[0]-l[1]))
    assert x[1]<cross_bounds[0]<=cross_bounds[1]<x[2]
    nearest=min(bounds[i][0] for i in range(len(candidates)) if i not in tied)
    gap=nearest-bounds[best][1];assert gap>0
    for row,b in zip(rows,bounds):row['continuous_overrun']=fraction_record(b)
    e_lower=int(rows[best]['energy']['scaled_integer_bounds'][0])
    selected_upper=int(rows[energy_best]['energy']['scaled_integer_bounds'][1])
    assert e_lower>selected_upper
    return {'scope':'Continuous supremum of E_T-max(J,F), with every original fine node and every midpoint residual zero included; true-input perturbation paid by 2*max node radius.',
            'midpoint_critical_points':len(critical),'max_node_radius_exact':str(radius),
            'complete_minimizer_ids':tied,'shared_maximal_edge':[x[0],x[2]],
            'shared_edge_strict_dominance_comparisons':strict_dominance,
            'shared_edge_unique_maximizer':'The actual F/J crossing between1536 and2048; two residual signs and the strict line/F slope difference were certified.',
            'shared_edge_maximizer_interval':fraction_record(cross_bounds),
            'minimum_continuous_overrun':fraction_record(bounds[best]),
            'all_other_overrun_gap_lower_exact':str(gap),
            'selected_minimax_tree_levels':rows[best]['levels'],
            'selected_minimax_tree_square_energy':rows[best]['energy'],
            'energy_minimizer_continuous_overrun':fraction_record(bounds[energy_best]),
            'minimax_tree_extra_square_energy_lower':decimal(e_lower-selected_upper)}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--previous',type=Path,required=True,
        help='riemann_signed_green_thickness_phase_20261124 package')
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('depth_four_energy_certificate.json'))
    args=parser.parse_args()
    rel='prior/riemann_native_residual_growth_20261124/prior/riemann_matching_isotonic_anchors_20261124/seams/saved_anchor_certificate.json'
    source=args.previous/rel;data=json.loads(source.read_text())
    x=[r['x'] for r in data['anchors']]
    q=[tuple(map(F,r['actual']['exact_bounds'])) for r in data['anchors']]
    assert x==[1024,1536,2048,3072,4096,6144,8192,12288,16384,24576,32768]
    qi=[(l.numerator*S//l.denominator,ceildiv(u.numerator*S,u.denominator)) for l,u in q]
    chords={}
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            gap=x[j]-x[i];lo=[];hi=[]
            for n in range(x[i],x[j]+1):
                a=x[j]-n;b=n-x[i]
                lo.append((a*qi[i][0]+b*qi[j][0])//gap)
                hi.append(ceildiv(a*qi[i][1]+b*qi[j][1],gap))
            chords[i,j]=lo,hi
    candidates=trees(0,10,4)
    assert len(candidates)==114 and not trees(0,10,3)
    rows=[]
    for index,t in enumerate(candidates):
        b=energy(curve(edges(t,0,10),x,chords),x)
        rows.append({'id':index,'levels':levels(t,x),'tree':t,'energy':record(b)})
    best=min(range(len(rows)),key=lambda i:int(rows[i]['energy']['scaled_integer_bounds'][1]))
    upper=int(rows[best]['energy']['scaled_integer_bounds'][1])
    tied=[r['id'] for r in rows if int(r['energy']['scaled_integer_bounds'][0])<=upper]
    assert tied==[10,11,16,17]
    continuous=certify_common_root_envelope(tied,candidates,x,q,4)
    assert all(rows[i]['energy']['scaled_integer_bounds']==rows[best]['energy']['scaled_integer_bounds'] for i in tied)
    next_row=min((r for r in rows if r['id'] not in tied),
                 key=lambda r:int(r['energy']['scaled_integer_bounds'][0]))
    strict_gap=int(next_row['energy']['scaled_integer_bounds'][0])-upper
    assert strict_gap>0
    baseline=energy(curve([(0,10)]+[(i,i+1) for i in range(10)],x,chords),x)
    best_bounds=tuple(map(int,rows[best]['energy']['scaled_integer_bounds']))
    excess=(best_bounds[0]-baseline[1],best_bounds[1]-baseline[0])
    relative=(best_bounds[0]*S//baseline[1]-S,ceildiv(best_bounds[1]*S,baseline[0])-S)
    assert excess[0]>0
    overrun=continuous_overrun_comparison(candidates,x,q,rows,best)
    result={'schema':'EM_FIXED_DEPTH_CLOSED_ENERGY_V1','status':'PASS',
        'scope':'Exact minimum closed-integer positive square energy among all legal trees of depth at most four on the original eleven anchors. Four minimizers are certified; author computation, no independent Review.',
        'arithmetic':'Exact fractions for inputs and continuous comparisons; outward integer interval chord and energy computations at scale 10^60; no floating pass/fail decisions.',
        'input':{'relative_path':rel,'sha256':hashlib.sha256(source.read_bytes()).hexdigest()},
        'node_count':11,'new_q_queries':0,'closed_integer_points':x[-1]-x[0]+1,
        'depth':4,'complete_candidate_count':len(rows),'best_candidate':best,
        'minimum_depth_without_energy_constraint':4,'depth_three_candidate_count':0,
        'complete_minimizer_ids':tied,'minimizer_count':len(tied),
        'baseline_M_energy':record(baseline),'optimal_depth_four_energy':record(best_bounds),
        'strict_square_energy_excess':record(excess),'relative_square_energy_excess':record(relative),
        'nearest_nonminimal_candidate_id':next_row['id'],
        'all_nonminimal_energy_gap_lower':decimal(strict_gap),
        'all_nonminimal_energy_gap_lower_scaled':str(strict_gap),
        'continuous_minimizer_envelope_identity':continuous,
        'continuous_overrun_objective_comparison':overrun,
        'square_energy_integer_terms_checked':(len(rows)+1)*(x[-1]-x[0]+1),
        'candidates':rows}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':'PASS','candidate_count':len(rows),'best_levels':rows[best]['levels'],
        'all_minimizers':tied,'optimal_energy':record(best_bounds),'M':record(baseline),
        'excess':record(excess),'relative_excess':record(relative),
        'continuous_comparisons':continuous['exact_rational_interval_comparisons'],
        'nearest_excluded_gap_lower':decimal(strict_gap)},ensure_ascii=False))


if __name__=='__main__':main()
