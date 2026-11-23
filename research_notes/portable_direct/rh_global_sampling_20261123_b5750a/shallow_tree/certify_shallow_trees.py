#!/usr/bin/env python3
"""Shallow near-optimal interpolation trees, from certified existing samples.

The actual-road check reads only two previous finite certificates, never the
full road cache. Arithmetic uses outward integer intervals with scale 10**60.
The auxiliary quadratic family uses exact Fraction comparisons.
"""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import argparse
import hashlib
import json
import time

SCALE = 10**60
ZERO = (0, 0)


def ceildiv(a, b):
    return -((-a)//b)


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def sub(a, b):
    return a[0]-b[1], a[1]-b[0]


def scale(a, q):
    q = F(q)
    p, d = q.numerator, q.denominator
    u, v = (a[0]*p, a[1]*p) if p >= 0 else (a[1]*p, a[0]*p)
    return u//d, ceildiv(v, d)


def mul(a, b):
    v = [x*y for x in a for y in b]
    return min(v)//SCALE, ceildiv(max(v), SCALE)


def divide(a, b):
    assert b[0] > 0 or b[1] < 0
    v = [F(x*SCALE, y) for x in a for y in b]
    lo, hi = min(v), max(v)
    return lo.numerator//lo.denominator, ceildiv(hi.numerator, hi.denominator)


def positive(a):
    return max(a[0], 0), max(a[1], 0)


def imax(*args):
    return max(a[0] for a in args), max(a[1] for a in args)


def square(a):
    lo = 0 if a[0] <= 0 <= a[1] else min(a[0]**2, a[1]**2)
    return lo//SCALE, ceildiv(max(a[0]**2, a[1]**2), SCALE)


def sqrt_iv(a):
    assert a[0] >= 0
    lo, hi = isqrt(a[0]*SCALE), isqrt(a[1]*SCALE)
    return lo, hi+(hi*hi < a[1]*SCALE)


def load_iv(r):
    assert r['denominator_power_of_10'] == 60
    return tuple(map(int, r['integer_bounds']))


def decimal(q, digits=30, upper=False):
    z = ceildiv(q*10**digits, SCALE) if upper else q*10**digits//SCALE
    sign = '-' if z < 0 else ''
    z = abs(z)
    return f'{sign}{z//10**digits}.{z%10**digits:0{digits}d}'


def record(a):
    return {'lower':decimal(a[0]), 'upper':decimal(a[1], upper=True),
            'integer_bounds':[str(a[0]), str(a[1])], 'denominator_power_of_10':60}


def interp(v, left, right, x):
    return add(scale(v[left], F(right-x, right-left)),
               scale(v[right], F(x-left, right-left)))


def piecewise(v, nodes):
    return {x:interp(v, l, r, x) for l, r in zip(nodes, nodes[1:])
            for x in range(l, r+1)}


def energy(v, a, b):
    ans = ZERO
    for n in range(a, b+1):
        ans = add(ans, scale(square(positive(v[n])), F(1, n*n)))
    return ans


def bucket_tree(nodes, labels):
    """Smallest bucket first; spatial median within that bucket."""
    if not nodes:
        return None
    label = min(labels[n] for n in nodes)
    candidates = [n for n in nodes if labels[n] == label]
    x = candidates[len(candidates)//2]
    k = nodes.index(x)
    return (x, bucket_tree(nodes[:k], labels), bucket_tree(nodes[k+1:], labels))


def edges(tree, left, right):
    ans = [(left, right)]
    if tree is not None:
        x, l, r = tree
        ans += edges(l, left, x)+edges(r, x, right)
    return ans


def depth(tree):
    return 0 if tree is None else 1+max(depth(tree[1]), depth(tree[2]))


def envelope(values, tree, left, right):
    out = {n:ZERO for n in range(left, right+1)}
    for a, b in edges(tree, left, right):
        for n in range(a, b+1):
            out[n] = imax(out[n], interp(values, a, b, n))
    return out


def edge_slacks(nodes, values):
    """Enclose exact continuous excess of each chord above max(0, fine r)."""
    ans = {}
    for i in range(len(nodes)-1):
        for j in range(i+1, len(nodes)):
            if j == i+1 or (values[nodes[i]][1] <= 0 and values[nodes[j]][1] <= 0):
                ans[i,j] = ZERO
                continue
            l, r = nodes[i], nodes[j]
            chord = {n:interp(values, l, r, n) for n in nodes[i:j+1]}
            tests = [ZERO]
            for n in nodes[i+1:j]:
                tests.append(positive(sub(chord[n], positive(values[n]))))
            for a, b in zip(nodes[i:j], nodes[i+1:j+1]):
                va, vb = values[a], values[b]
                if va[1] < 0 < vb[0]:
                    numerator = sub(mul(vb, chord[a]), mul(va, chord[b]))
                    tests.append(positive(divide(numerator, sub(vb, va))))
                elif vb[1] < 0 < va[0]:
                    numerator = sub(mul(va, chord[b]), mul(vb, chord[a]))
                    tests.append(positive(divide(numerator, sub(va, vb))))
            ans[i,j] = imax(*tests)
    return ans


def slack_dp(nodes, slacks, max_depth):
    """Bounds the exact minimum L-infinity slack over every depth-limited tree.

    A chosen tree achieves the reported upper bound. Overlapping candidate
    intervals are enclosed, not declared uniquely ordered or exactly tied.
    """
    N = len(nodes)
    dp, chosen, heights = {}, {}, {}
    for d in range(max_depth+1):
        for length in range(1, N):
            for i in range(N-length):
                j = i+length
                key = d,i,j
                if length == 1:
                    dp[key] = ZERO
                    heights[key] = 0
                    continue
                options = []
                if d:
                    for k in range(i+1, j):
                        a, b = dp[d-1,i,k], dp[d-1,k,j]
                        if a is not None and b is not None:
                            height = 1+max(heights[d-1,i,k],heights[d-1,k,j])
                            options.append((imax(slacks[i,j], a, b), k, height))
                if not options:
                    dp[key] = None
                else:
                    best = min(options, key=lambda t:(t[0][1],t[2],t[1]))
                    dp[key] = (min(v[0] for v,k,h in options), best[0][1])
                    chosen[key] = best[1]
                    heights[key] = best[2]

    def build(d,i,j):
        if j == i+1:
            return None
        k = chosen[d,i,j]
        return nodes[k], build(d-1,i,k), build(d-1,k,j)

    return dp[max_depth,0,N-1], build(max_depth,0,N-1)


def actual_cert(source_root):
    order_path = source_root/'rh_tree_order_20261122/optimal_tree_order_certificate.json'
    triangle_path = source_root/'rh_triangle_certificate_20261122/dyadic_triangle_certificate.json'
    previous, triangle = json.loads(order_path.read_bytes()), json.loads(triangle_path.read_bytes())
    road = triangle['roads']['q']
    a,b = triangle['window']['A'], triangle['window']['B']
    endpoints = {p['n']:load_iv(p['value']) for p in road['true_dyadic_endpoint_samples']}
    J = piecewise(endpoints, triangle['partition']['backbone'])
    rem = load_iv(road['energies']['fine_local_positive_remainder_energy'])
    terminal = load_iv(road['energies']['true_two_endpoint_direct_energy'])
    source_blocks=[]
    for block in previous['blocks']:
        nodes=[r['n'] for r in block['residual_nodes']]
        values={r['n']:load_iv(r['residual']) for r in block['residual_nodes']}
        source_blocks.append((nodes,values,edge_slacks(nodes,values)))

    runs=[]
    configurations=[('slack_dp',0),('slack_dp',1)]
    configurations += [('additive_bins',F(k)) for k in ['1/100','1/20','1/10','1/4','1/2','1','2','4']]
    for mode,param in configurations:
        global_upper={}
        blocks=[]
        for nodes,values,slacks in source_blocks:
            N=len(nodes)-2
            min_height=N.bit_length()
            if mode=='slack_dp':
                slack,tree=slack_dp(nodes,slacks,min_height+param)
                detail={'depth_cap':min_height+param,
                        'optimal_continuous_additive_slack_enclosure':record(slack),
                        'achieving_tree_upper_bound':record((0,slack[1]))}
            else:
                delta=param
                labels={}
                for n in nodes[1:-1]:
                    lo,hi=values[n]
                    if hi <= 0:
                        labels[n]=0
                    else:
                        assert lo>0
                        k=ceildiv(lo*delta.denominator,SCALE*delta.numerator)
                        assert hi*delta.denominator <= k*SCALE*delta.numerator
                        assert lo*delta.denominator > (k-1)*SCALE*delta.numerator
                        labels[n]=k
                tree=bucket_tree(nodes[1:-1],labels)
                counts={c:sum(z==c for z in labels.values()) for c in set(labels.values())}
                bound=sum(n.bit_length() for n in counts.values())
                assert depth(tree)<=bound
                slack=(0,ceildiv(delta.numerator*SCALE,delta.denominator))
                detail={'bin_width':str(delta),'bin_counts':counts,'proven_depth_bound':bound}
            env=envelope(values,tree,nodes[0],nodes[-1])
            for n,z in env.items():
                global_upper[n]=add(J[n],z)
            certified_slack=imax(*(slacks[nodes.index(l),nodes.index(r)] for l,r in edges(tree,nodes[0],nodes[-1])))
            assert certified_slack[1] <= slack[1]
            blocks.append({'X':nodes[0],'Y':nodes[-1],'internal_node_count':N,
                           'tree_depth':depth(tree),'tree':tree,
                           'chosen_tree_actual_continuous_slack':record(certified_slack),**detail})
        en=energy(global_upper,a+1,b-1)
        budget=add(square(add(sqrt_iv(en),sqrt_iv(rem))),terminal)
        runs.append({'mode':mode,'parameter':str(param),'blocks':blocks,
                     'interior_envelope_positive_energy':record(en),
                     'closed_squared_budget':record(budget)})
    return {'window':{'A':a,'B':b},'fine_node_count':44,'packet_count':38,
            'prior_exact_optimal_closed_budget':previous['closed_optimal_tree_budget'],
            'complete_road_recomputed':False,
            'input_files':[{'path':str(p.relative_to(source_root)),
                            'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
                           for p in [order_path,triangle_path]],'runs':runs}


def balanced(a,b):
    if b-a<=1:
        return None
    k=(a+b)//2
    return k,balanced(a,k),balanced(k,b)


def geometric_quadratic_tree(s,rho):
    anchors=[1]
    while anchors[-1]<s-1:
        x=anchors[-1]
        anchors.append(min(s-1,max(x+1,(rho.numerator*x)//rho.denominator)))
    tree=None
    for i in range(len(anchors)-1,-1,-1):
        prev=0 if i==0 else anchors[i-1]
        tree=(anchors[i],balanced(prev,anchors[i]),tree)
    return tree,anchors


def exact_ratio(nodes,tree):
    s=nodes[-1]
    ans=F(1)
    for a,b in edges(tree,0,s):
        ya=a*a
        yb=b*b if b<s else 0
        for j in range(max(1,a),min(b,s-1)+1):
            chord=F(ya*(b-j)+yb*(j-a),b-a)
            ans=max(ans,chord/(j*j))
    return ans


def hard_family_cert():
    out=[]
    for rho in [F(6,5),F(3,2),F(2)]:
        factor=(rho+1)**2/(4*rho)
        rows=[]
        for s in [8,16,32,64,128,256,512,1024,4096]:
            tree,anchors=geometric_quadratic_tree(s,rho)
            ratio=exact_ratio(list(range(s+1)),tree)
            assert ratio<=factor
            rows.append({'s':s,'exact_optimal_required_depth':s-1,
                         'constructed_depth':depth(tree),'anchor_count':len(anchors),
                         'maximum_pointwise_ratio':str(ratio),
                         'maximum_pointwise_ratio_decimal':float(ratio)})
        out.append({'rho':str(rho),'universal_pointwise_factor':str(factor),
                    'universal_squared_energy_factor':str(factor**2),'rows':rows})
    return out


def relative_obstruction_cert():
    """Exact forced-root comparisons for the new exponential-platform family."""
    out=[]
    for factor in [F(25,24),F(2),F(10)]:
        for s in [8,16,32,64,128]:
            m=s//2
            K=ceildiv(2*factor.numerator*s,factor.denominator)+1
            y=[F(0)]+[F(s*s,K**(m-j)) for j in range(1,m)]
            y += [F(s*s)]*(s-m)+[F(0)]
            assert len(y)==s+1
            count=0
            least_margin=None
            for k in range(m-1):
                # At this stage roots 1,...,k have been forced; every other
                # next root j>k+1 overshoots the fine node k+1.
                for j in range(k+2,s):
                    chord=y[k]+(y[j]-y[k])/F(j-k)
                    margin=chord-factor*y[k+1]
                    assert margin>0
                    least_margin=margin if least_margin is None else min(least_margin,margin)
                    count+=1
            # Monotone rise, plateau, and one final drop give the analytic
            # source/remainder bounds. Verify their exact discrete input.
            increments=[y[j+1]-y[j] for j in range(s)]
            assert max(abs(z) for z in increments)<=s*s
            assert sum(z*z for z in increments)<=2*s**4
            assert all(z>=0 for z in increments[:-1])
            out.append({'factor':str(factor),'s':s,'K':K,
                        'forced_depth_lower_bound':m-1,
                        'strict_forbidden_next_root_comparisons':count,
                        'minimum_strict_margin':str(least_margin),
                        'full_integer_source_bound':'12/n',
                        'fine_remainder_squared_bound':str(F(1,8*s)),
                        'true_energy_bounds':['1/16','2']})
    return out


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--source-root',type=Path,required=True,
                        help='Directory containing the two prior certificate paths documented in the proof.')
    args=parser.parse_args()
    t=time.perf_counter()
    output={'schema':'EM_NEAR_OPTIMAL_SHALLOW_TREE_V1','status':'PASS',
            'actual_road':actual_cert(args.source_root),'quadratic_depth_obstruction':hard_family_cert(),
            'relative_pointwise_obstruction':relative_obstruction_cert(),
            'claim_scope':'Author analytic theorems and finite certificates; no independent Project Review.',
            'elapsed_seconds':time.perf_counter()-t}
    path=Path(__file__).with_name('shallow_tree_certificate.json')
    path.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    for r in output['actual_road']['runs']:
        print(r['mode'],r['parameter'],[b['tree_depth'] for b in r['blocks']],r['closed_squared_budget']['upper'])
    for c in output['quadratic_depth_obstruction']:
        print('rho',c['rho'],'last',c['rows'][-1])
    print('PASS',path,'seconds',output['elapsed_seconds'])


if __name__=='__main__':
    main()
