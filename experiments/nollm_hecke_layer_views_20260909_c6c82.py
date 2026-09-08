#!/usr/bin/env python3
"""Reproduce the Nollm/EM radix-layer and sampling audit (2026-09-09).

Run: python reproduce.py --output output
Dependencies: numpy; --plots additionally needs matplotlib and plotly.
All matrix/digit/count checks use integers or Fraction. Eigenvalues are readouts.
This is a research experiment, not Nollm runtime code or a theorem admission.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from itertools import combinations, product
import json
import math
from pathlib import Path
import numpy as np

MATS = np.array([
    [[-1,-4],[2,3]], [[-1,-4],[2,3]], [[1,-1],[2,3]], [[1,-2],[1,3]],
    [[1,-1],[3,2]], [[1,-3],[1,2]], [[-1,-3],[3,4]], [[1,-1],[3,2]]
], dtype=np.int64)
E = np.array([[1., .5], [0., math.sqrt(3)/2]])
EINV = np.linalg.inv(E)
LINE = np.array([[j,0] for j in range(-2,3)], dtype=np.int64)

def det(a):
    return int(a[0,0])*int(a[1,1])-int(a[0,1])*int(a[1,0])

def adj(a):
    return np.array([[a[1,1],-a[0,1]],[-a[1,0],a[0,0]]],dtype=np.int64)

def complete(m,d):
    return len(np.unique((d @ adj(m).T) % det(m), axis=0)) == det(m)

def ratio(c):
    ev=np.linalg.eigvalsh(E@c@E.T)
    return None if ev[0] <= 1e-10 else float(math.sqrt(ev[1]/ev[0]))

def objective(c):
    # tr(E C E^T)^2 / det(E C E^T), an exact monotone anisotropy score.
    trace=int(c[0,0]+c[0,1]+c[1,1])
    return Fraction(4*trace*trace,3*det(c))

def compact_options():
    pairs=[np.array(x) for x in ((1,0),(0,1),(1,-1))]
    options=[]
    for m in MATS:
        ds=[np.array([[0,0],u,-u,v,-v],dtype=np.int64)
            for u,v in combinations(pairs,2)]
        options.append([d for d in ds if complete(m,d)])
    assert [len(x) for x in options] == [2]*8
    return options

def optimize_digits():
    options=compact_options(); best=None
    for choice in product(range(2),repeat=8):
        c=np.zeros((2,2),dtype=np.int64)  # five times covariance
        for m,ds,i in zip(MATS,options,choice):
            d=ds[i]; c=m@c@m.T+d.T@d
        candidate=(objective(c),choice)
        if best is None or candidate < best: best=candidate
    return [ds[i] for ds,i in zip(options,best[1])], best

def hull_metrics(points):
    # Exact monotone-chain convex hull in axial integer coordinates.
    ps=sorted(map(tuple,points.tolist()))
    def cross(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    def half(seq):
        h=[]
        for p in seq:
            while len(h)>=2 and cross(h[-2],h[-1],p)<=0: h.pop()
            h.append(p)
        return h
    h=half(ps)[:-1]+half(reversed(ps))[:-1]
    edges=list(zip(h,h[1:]+h[:1]))
    twice=abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in edges))
    boundary=sum(math.gcd(abs(a[0]-b[0]),abs(a[1]-b[1])) for a,b in edges)
    sites=(twice+boundary)//2+1  # Pick's formula, including boundary sites
    return dict(hull_area_twice=twice,hull_boundary_sites=boundary,
                hull_total_lattice_sites=sites,hull_occupied_fraction=len(points)/sites)

def expand(digits):
    pts=np.zeros((1,2),dtype=np.int64); p=np.eye(2,dtype=np.int64)
    c=np.zeros((2,2),dtype=np.int64); layers=[pts]; rows=[]
    for k,(m,d) in enumerate(zip(MATS,digits),1):
        assert det(m)==5 and complete(m,d)
        old=p; p=m@p
        nested=bool(np.all((adj(old)@p)%det(old)==0))
        pts=(pts@m.T)[:,None,:]+d[None,:,:]; pts=pts.reshape(-1,2)
        c=m@c@m.T+d.T@d
        assert len(pts)==5**k
        s=np.linalg.svd(E@p@EINV,compute_uv=False)
        rows.append(dict(k=k,count=len(pts),matrix=p.tolist(),digits=d.tolist(),
            covariance_times5=c.tolist(),map_K=float(s[0]/s[1]),
            cloud_std_ratio=ratio(c),left_prefix_nested=nested))
        layers.append(pts)
    assert p.tolist()==[[0,-625],[625,625]]
    assert len(np.unique(pts%625,axis=0))==625**2
    # Residue bijectivity implies no collision of the actual endpoint vectors.
    assert np.allclose(np.cov((pts@E.T).T,bias=True),E@(c/5)@E.T)
    return layers,rows,hull_metrics(pts)

def counts(d,p,R):
    a=[1]+[0]*R
    for i in range(d):
        for r in range(1,R+1): a[r]+=p**i*a[r-1]
    return a

def gaussian_count(d,p,r):
    v=Fraction(1)
    for i in range(1,d): v*=Fraction(p**(r+i)-1,p**i-1)
    assert v.denominator==1
    return v.numerator

def sigma_sum(X):
    # sum_{n<=X} sigma_1(n), using floor-quotient grouping, exact O(sqrt(X)).
    total=0; lo=1
    while lo<=X:
        q=X//lo; hi=X//q
        total+=q*(lo+hi)*(hi-lo+1)//2; lo=hi+1
    return total

def hnf_hist(p,r):
    hist=[0]*(r//2+1)
    for aexp in range(r+1):
        a=p**aexp; d=p**(r-aexp)
        for b in range(a):  # column HNF [[a,b],[0,d]], 0<=b<a
            g=math.gcd(a,math.gcd(b,d)); j=0
            while g%p==0: j+=1;g//=p
            hist[j]+=1
    return hist

def make_plots(folder,layer_sets,rows):
    import matplotlib.pyplot as plt
    import plotly.graph_objects as go
    for name,layers in layer_sets.items():
        fig=plt.figure(figsize=(9,8)); ax=fig.add_subplot(111,projection='3d')
        for k in range(1,6):
            xy=layers[k]@E.T/math.sqrt(5.**k)
            ax.scatter(xy[:,0],xy[:,1],np.full(len(xy),k),s=5,alpha=.65,
                       label=f'k={k}: {len(xy):,} points')
        ax.set(xlabel='x / sqrt(5^k)',ylabel='y / sqrt(5^k)',zlabel='Depth k',
               title=f'Exact radix layers: {name} digits (not physical layers)')
        ax.view_init(elev=24,azim=-57);ax.legend(fontsize=8)
        fig.savefig(folder/f'{name}_layers.png',dpi=180,bbox_inches='tight');plt.close(fig)
    fig,ax=plt.subplots(figsize=(9,5.5)); ks=np.arange(1,9)
    ax.plot(ks,[x['map_K'] for x in rows['original']],'o-',label='Transform axis ratio')
    ax.plot(ks[1:],[x['cloud_std_ratio'] for x in rows['original'][1:]],'s-',label='Original cloud axis ratio')
    ax.plot(ks,[x['cloud_std_ratio'] for x in rows['compact']],'^-',label='Compact cloud axis ratio')
    ax.set(xlabel='Radix expansion depth',ylabel='Axis ratio',xticks=ks)
    ax.legend();ax.grid(alpha=.25)
    fig.savefig(folder/'shape_vs_coverage.png',dpi=180,bbox_inches='tight');plt.close(fig)
    fig=go.Figure()
    for name,layers in layer_sets.items():
        for k in range(1,9):
            pts=layers[k];shown=pts[::max(1,math.ceil(len(pts)/4000))]
            xy=shown@E.T/math.sqrt(5.**k)
            fig.add_trace(go.Scatter3d(x=xy[:,0],y=xy[:,1],z=np.full(len(xy),k),
                mode='markers',marker=dict(size=2),visible=(name=='original'),
                name=f'{name} k={k}: {len(shown)}/{len(pts)} shown'))
    fig.update_layout(title='Exact radix layers: sampled display; full-data statistics',height=850,
        scene=dict(xaxis_title='x / sqrt(5^k)',yaxis_title='y / sqrt(5^k)',zaxis_title='Depth k'),
        updatemenus=[dict(buttons=[
            dict(label='Original',method='update',args=[{'visible':[True]*8+[False]*8}]),
            dict(label='Compact',method='update',args=[{'visible':[False]*8+[True]*8}])])])
    fig.write_html(folder/'interactive_layers.html',include_plotlyjs=True,auto_open=False)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('reproduced'))
    parser.add_argument('--plots',action='store_true')
    args=parser.parse_args(); args.output.mkdir(parents=True,exist_ok=True)
    ds,best=optimize_digits(); results={}; layer_sets={}; row_sets={}
    for name,digits in [('original',[LINE]*8),('compact',ds)]:
        layers,rows,hull=expand(digits);layer_sets[name]=layers;row_sets[name]=rows
        results[name]=dict(layers=rows,endpoint_hull=hull)
        np.savez_compressed(args.output/f'{name}_layers.npz',**{f'L{k}':x for k,x in enumerate(layers)})
    results['compact_search']=dict(family_size=256,choice=best[1],exact_score=str(best[0]))
    check_count=0
    for d,p in product(range(2,7),(2,3,5,7)):
        a=counts(d,p,24)
        for r in range(25):
            assert a[r]==gaussian_count(d,p,r);check_count+=1
        for r in range(25):
            hist=[a[r-d*j]-(a[r-d*(j+1)] if r-d*(j+1)>=0 else 0) for j in range(r//d+1)]
            assert sum(hist)==a[r] and min(hist)>=0
    results['count_formula_checks']=check_count
    results['hnf_histograms']={}
    for r in range(9):
        hist=hnf_hist(5,r);a=counts(2,5,r)
        expected=[a[r-2*j]-(a[r-2*j-2] if r-2*j-2>=0 else 0) for j in range(r//2+1)]
        assert hist==expected;results['hnf_histograms'][r]=hist
    results['rank_tails']=[]
    for d in (2,3,4,6):
        a=counts(d,5,24);v=Fraction(a[24-d],a[24])
        results['rank_tails'].append(dict(rank=d,r=24,tail_exact=str(v),tail=float(v),limit=5.**(-d*(d-1))))
    results['pooled_tails']=[]
    for X in (100,1000,10000,100000,1000000):
        den=sigma_sum(X);num=sigma_sum(X//25)
        results['pooled_tails'].append(dict(X=X,total=den,common_5=num,probability=float(Fraction(num,den))))
    assert sigma_sum(100)==sum(sum(d for d in range(1,n+1) if n%d==0) for n in range(1,101))
    v={0:1}
    for _ in range(8):
        nxt={}
        for s,mass in v.items():
            if s==0: nxt[1]=nxt.get(1,0)+6*mass
            else:
                nxt[s-1]=nxt.get(s-1,0)+mass
                nxt[s+1]=nxt.get(s+1,0)+5*mass
        v=nxt
    assert v=={0:12786,2:121080,4:402000,6:675000,8:468750}
    results['walk_shell_masses_r8']=v
    # Moments of repeated eight-step blocks; not enumeration of 5^48 points.
    A=E@np.array([[0,-625],[625,625]])@EINV
    C8=E@(np.array(row_sets['original'][-1]['covariance_times5'])/5)@E.T
    C=np.zeros((2,2));results['macrocycle_moments']=[]
    for t in range(1,7):
        C=A@C@A.T+C8; ev,vec=np.linalg.eigh(C)
        results['macrocycle_moments'].append(dict(depth=8*t,axis_ratio=float(math.sqrt(ev[1]/ev[0])),
            angle_mod180=math.degrees(math.atan2(vec[1,1],vec[0,1]))%180))
    results['status']='CHECKED_FINITE_EXPERIMENT_NOT_MATHEMATICAL_PROMOTION'
    (args.output/'results.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
    if args.plots: make_plots(args.output,layer_sets,row_sets)
    print(json.dumps({'checks':check_count,'compact_axis_ratio':row_sets['compact'][-1]['cloud_std_ratio'],
        'original_axis_ratio':row_sets['original'][-1]['cloud_std_ratio'],'pooled_tail':results['pooled_tails'][-1],
        'status':'PASS'},indent=2))

if __name__=='__main__':
    main()
