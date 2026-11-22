#!/usr/bin/env python3
"""Signed subtree frontiers on the original certified 38-packet trees.

Only the published packet intervals, true skeleton, and remainder are read.
Node budgets count the retained kernel representation, not arithmetic queries.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys
import time

ROOT=Path(__file__).resolve().parents[1]
OUT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'rh_joint_certificate'))
sys.path.insert(0,str(ROOT/'rh_phase_dominance_20261122'))
from certify_joint_energy import (A,B,DIGITS,ZERO,add,sub,scale,mul,square,
    positive,sqrt_interval,isum,record,energy,intersects,interval_from_record,rat)
from certify_ancestor_compression import tent,imax,dirichlet_energy


def imin(a,b):
    return min(a[0],b[0]),min(a[1],b[1])


def plan(cost,frontier,used):
    return {'cost':cost,'frontier':frozenset(frontier),'used':used}


def choose(candidates,checks):
    """An exact DP recurrence, with interval-separated winning decisions."""
    unique={}
    for p in candidates:
        key=p['frontier']
        if key not in unique:
            unique[key]=p
        else:
            assert intersects(unique[key]['cost'],p['cost'])
    ordered=sorted(unique.values(),key=lambda p:(p['cost'][1],p['used'],sorted(p['frontier'])))
    best=ordered[0]
    for other in ordered[1:]:
        checks['comparison_count']+=1
        if best['cost'][1]>other['cost'][0]:
            checks['unresolved_comparison_count']+=1
            checks['unresolved_comparisons'].append({
                'chosen':record(best['cost']),'alternative':record(other['cost']),
                'chosen_frontier':[list(x) for x in sorted(best['frontier'])],
                'alternative_frontier':[list(x) for x in sorted(other['frontier'])]})
    return best


def make_dp(node,cost_key,table,checks):
    children=node['children']
    for _,child in children:
        make_dp(child,cost_key,table,checks)
    dp={}
    for k in range(1,node['size']+1):
        candidates=[plan(node[cost_key],[node['triple']],1)]
        if children:
            if len(children)==1:
                c=children[0][1]
                for ck,cp in c[table].items():
                    if 1+ck<=k:
                        candidates.append(plan(cp['cost'],cp['frontier'],1+cp['used']))
            else:
                left,right=children[0][1],children[1][1]
                for kl,pl in left[table].items():
                    for kr,pr in right[table].items():
                        if 1+kl+kr<=k:
                            candidates.append(plan(add(pl['cost'],pr['cost']),
                                pl['frontier']|pr['frontier'],1+pl['used']+pr['used']))
        dp[k]=choose(candidates,checks)
    node[table]=dp


def combine_forest(roots,checks,table='dp'):
    previous={0:plan(ZERO,[],0)}
    total=0
    for root in roots:
        current={}
        total+=root['size']
        for k in range(1,total+1):
            candidates=[]
            for left_budget,left in previous.items():
                for right_budget,right in root[table].items():
                    if left_budget+right_budget<=k:
                        candidates.append(plan(add(left['cost'],right['cost']),
                            left['frontier']|right['frontier'],left['used']+right['used']))
            if candidates:
                current[k]=choose(candidates,checks)
        previous=current
    return previous


def main():
    started=time.perf_counter()
    source_path=ROOT/'rh_triangle_certificate_20261122/dyadic_triangle_certificate.json'
    ancestor_path=ROOT/'rh_phase_dominance_20261122/ancestor_compression_certificate.json'
    source=json.loads(source_path.read_bytes())
    ancestor=json.loads(ancestor_path.read_bytes())
    assert (source['window']['A'],source['window']['B'])==(A,B)
    output={'schema':'EM_SIGNED_SUBTREE_FRONTIER_V1','status':'PASS',
        'scope':'Original fixed integer trees and the prescribed signed-capacity rooted-pruning family; exact finite DP for weighted error and the actual positive-energy budget. No claim of optimality among all compressions, no new arithmetic road or asymptotic estimate.',
        'science_freeze':'9fc068244e4f1117f1e75df5eb0285c6697d21d7',
        'window':source['window'],
        'arithmetic':{'method':'outward integer intervals; exact rational geometry','denominator_power_of_10':DIGITS},
        'node_cost':'Number of retained kernel nodes in a rooted pruning: expanded nodes plus frontier nodes. This is a representation count, not a number of newly computed arithmetic moments.',
        'inputs':[{'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
            for p in [source_path,ancestor_path,ROOT/'rh_joint_certificate/certify_joint_energy.py',
                      ROOT/'rh_phase_dominance_20261122/certify_ancestor_compression.py']],
        'formulas':{
            'signed_capacity':'u_p=t_p+max(0,lambda_l*(u_l)_+,lambda_r*(u_r)_+); (u_p)_+=alpha_p',
            'frontier_upper':'V_F=sum_(expanded p)t_p*T_p+sum_(frontier p)u_p*T_p >= S',
            'residual':'r_p=u_p*T_p-S_p >=0; V_F-S=sum_(p in F)r_p',
            'exact_error_cost':'||V_F-S||_w^2=sum_(p in F)||r_p||_w^2 by disjoint frontier interiors',
            'exact_budget_cost':'E((J+V_F)_+)=E(I_+)+sum_(p in F)Delta_p, Delta_p=sum_n[((I+r_p)_+)^2-(I_+)^2]/n^2, I=J+S',
            'trace_cost':'||r_p||_w^2<=J_p*(tau_p*(u_p-t_p)^2+sum_(strict descendants r)tau_r*t_r^2)',
            'node_dp':'D_p(k)=min{cost_p, min_(1+k_l+k_r<=k)(D_l(k_l)+D_r(k_r))}; cost_p may be exact weighted error or exact positive-energy excess Delta_p',
            'budget':'(sqrt(interior positive energy of J+V_F)+sqrt(original fine remainder positive energy))^2+original endpoint squares',
            'optional_intersection':'min(Z,V_F) remains an upper envelope; it consumes the pre-existing full Z as well as the frontier representation and is not counted as a k-node representation'},
        'roads':{}}
    for name,road in source['roads'].items():
        checks={'comparison_count':0,'unresolved_comparison_count':0,'unresolved_comparisons':[]}
        energy_checks={'comparison_count':0,'unresolved_comparison_count':0,'unresolved_comparisons':[]}
        sample={r['n']:interval_from_record(r['value']) for r in road['true_dyadic_endpoint_samples']}
        backbone=source['partition']['backbone']
        J=[ZERO]*(B+1)
        for L,R in zip(backbone,backbone[1:]):
            for n in range(L,R+1):
                J[n]=add(scale(sample[L],F(R-n,R-L)),scale(sample[R],F(n-L,R-L)))
        S=[ZERO]*(B+1); Z=[ZERO]*(B+1)
        nodes={}; roots=[]
        for block in road['dyadic_blocks']:
            X,Y=block['X'],block['Y']
            packets={(p['L'],p['R']):p for l in block['levels'] for p in l['packets']}

            def visit(key):
                p=packets[key]; triple=(p['L'],p['x'],p['R']);L,x,R=triple
                children=[]
                for ck in [(L,x),(x,R)]:
                    if ck in packets:
                        child=visit(ck)
                        y=child['triple'][1]
                        lam=tent(child['triple'],y)/tent(triple,y)
                        children.append((lam,child))
                t=interval_from_record(p['signed_charge'])
                cap=imax([ZERO]+[scale(positive(c['u']),lam) for lam,c in children])
                u=add(t,cap)
                alpha=positive(add(t,imax([ZERO]+[scale(c['alpha'],lam) for lam,c in children])))
                assert positive(u)==alpha
                values={}; z={}; residual={}; one_layer={}
                for n in range(L,R+1):
                    own=scale(t,tent(triple,n))
                    values[n]=add(own,isum(c['S'].get(n,ZERO) for _,c in children))
                    z[n]=positive(add(own,isum(c['Z'].get(n,ZERO) for _,c in children)))
                    one_layer[n]=add(own,isum(scale(c['u'],tent(c['triple'],n)) for _,c in children))
                    compressed=scale(u,tent(triple,n))
                    # Nonnegativity is an analytic identity, not inferred from
                    # overlapping intervals. Intersect the interval with [0,+inf).
                    residual[n]=positive(sub(compressed,values[n])) if children else ZERO
                    assert values[n][0]<=one_layer[n][1]
                    assert one_layer[n][0]<=compressed[1]
                cost=isum(scale(square(residual[n]),F(1,n*n)) for n in range(L+1,R))
                tau=F((x-L)*(R-x),R-L)
                source_dirichlet=add(scale(square(t),tau),isum(c['source_dirichlet'] for _,c in children))
                error_dirichlet=add(scale(square(cap),tau),isum(c['source_dirichlet'] for _,c in children))
                trace=isum(rat(F((n-L)*(R-n),(R-L)*n*n)) for n in range(L+1,R))
                trace_bound=mul(trace,error_dirichlet)
                assert cost[0]<=trace_bound[1]
                assert intersects(dirichlet_energy(residual,L,R),error_dirichlet)
                size=1+sum(c['size'] for _,c in children)
                node={'triple':triple,'X':X,'t':t,'u':u,'alpha':alpha,'cap':cap,'children':children,
                    'S':values,'Z':z,'r':residual,'one_layer':one_layer,'cost':cost,
                    'source_dirichlet':source_dirichlet,'error_dirichlet':error_dirichlet,
                    'trace':trace,'trace_bound':trace_bound,'size':size}
                nodes[triple]=node
                return node

            root=visit((X,Y));roots.append(root)
            for n in range(X,Y+1):
                S[n]=root['S'][n];Z[n]=root['Z'][n]
        assert len(nodes)==38
        I=[add(J[n],S[n]) for n in range(B+1)]
        Ienergy=energy(I,A+1,B-1,'positive')
        for node in nodes.values():
            L,_,R=node['triple'];terms=[]
            for n in range(L+1,R):
                r=node['r'][n];base=I[n]
                if r==ZERO:
                    inc=ZERO
                elif base[0]>=0:
                    inc=add(scale(mul(base,r),2),square(r))
                elif base[1]<=0:
                    inc=square(positive(add(base,r)))
                else:
                    inc=positive(sub(square(positive(add(base,r))),square(positive(base))))
                terms.append(scale(inc,F(1,n*n)))
            node['energy_cost']=isum(terms)
        for root in roots:
            make_dp(root,'cost','dp',checks)
            make_dp(root,'energy_cost','energy_dp',energy_checks)
        forest=combine_forest(roots,checks)
        energy_forest=combine_forest(roots,energy_checks,'energy_dp')
        assert checks['unresolved_comparison_count']==0,checks
        assert energy_checks['unresolved_comparison_count']==0,energy_checks
        old=road['energies']
        remainder=interval_from_record(old['fine_local_positive_remainder_energy'])
        endpoints=interval_from_record(old['true_two_endpoint_direct_energy'])
        def budget(v):
            en=energy([add(J[n],v[n]) for n in range(B+1)],A+1,B-1,'positive')
            return add(square(add(sqrt_interval(en),sqrt_interval(remainder))),endpoints)
        baselineS=budget(S);baselineZ=budget(Z)
        nonnegative_floor=budget([positive(v) for v in S])
        assert intersects(baselineS,interval_from_record(ancestor['roads'][name]['closed_squared_budgets']['S']))
        assert intersects(baselineZ,interval_from_record(ancestor['roads'][name]['closed_squared_budgets']['Z']))
        row_sets={}
        for objective,plans in [('weighted_error',forest),('positive_energy',energy_forest)]:
            rows=[]
            for k,p in plans.items():
                errors=[ZERO]*(B+1)
                for triple in p['frontier']:
                    node=nodes[triple];L,_,R=triple
                    for n in range(L+1,R):
                        assert errors[n]==ZERO
                        errors[n]=node['r'][n]
                direct=energy(errors,A+1,B-1)
                error_cost=isum(nodes[t]['cost'] for t in p['frontier'])
                energy_cost=isum(nodes[t]['energy_cost'] for t in p['frontier'])
                assert intersects(direct,error_cost)
                assert intersects(p['cost'],error_cost if objective=='weighted_error' else energy_cost)
                v=[add(S[n],errors[n]) for n in range(B+1)]
                assert intersects(energy([add(J[n],v[n]) for n in range(B+1)],A+1,B-1,'positive'),add(Ienergy,energy_cost))
                clipped=[imin(v[n],Z[n]) for n in range(B+1)]
                result=budget(v)
                clipped_result=budget(clipped)
                exact_root_gap=sub(sqrt_interval(sub(result,endpoints)),sqrt_interval(sub(baselineS,endpoints)))
                assert exact_root_gap[0]<=sqrt_interval(error_cost)[1]
                if k==38:
                    assert energy_cost==ZERO and intersects(result,baselineS)
                rows.append({'node_budget':k,'retained_kernel_nodes':p['used'],
                    'frontier':[list(t) for t in sorted(p['frontier'])],
                    'negative_signed_frontier_count':sum(nodes[t]['u'][1]<0 for t in p['frontier']),
                    'objective':objective,'optimal_objective_value':record(p['cost']),
                    'weighted_error_squared':record(error_cost),'positive_energy_excess':record(energy_cost),
                    'error_root':record(sqrt_interval(error_cost)),
                    'closed_squared_budget':record(result),
                    'with_preexisting_full_Z_intersection_budget':record(clipped_result),
                    'optimality':'all alternative DP costs separated by outward integer intervals'})
            row_sets[objective]=rows
        first_layer=[ZERO]*(B+1)
        first_layer_count=0
        for root in roots:
            first_layer_count+=1+len(root['children'])
            for n,v in root['one_layer'].items():
                first_layer[n]=v
        node_records=[]
        for key,n in sorted(nodes.items()):
            node_records.append({'packet':list(key),'subtree_nodes':n['size'],
                'signed_charge':record(n['t']),'signed_capacity_u':record(n['u']),
                'positive_capacity_alpha':record(n['alpha']),
                'u_positive_part_equals_alpha':positive(n['u'])==n['alpha'],
                'children':[{'packet':list(c['triple']),'lambda_exact':str(lam)} for lam,c in n['children']],
                'compression_error_weighted_squared':record(n['cost']),
                'positive_energy_excess':record(n['energy_cost']),
                'compression_error_dirichlet':record(n['error_dirichlet']),
                'trace':record(n['trace']),'trace_error_squared_upper_bound':record(n['trace_bound'])})
        first_floor=next((r['node_budget'] for r in row_sets['positive_energy']
            if interval_from_record(r['closed_squared_budget'])[1]<nonnegative_floor[0]),None)
        first_zero=next((r['node_budget'] for r in row_sets['positive_energy']
            if interval_from_record(r['positive_energy_excess'])==ZERO),None)
        assert first_floor is not None and first_zero is not None
        assert all(interval_from_record(r['closed_squared_budget'])[0]>=nonnegative_floor[1]
            for r in row_sets['positive_energy'] if r['node_budget']<first_floor)
        assert all(interval_from_record(r['positive_energy_excess'])[0]>0
            for r in row_sets['positive_energy'] if r['node_budget']<first_zero)
        output['roads'][name]={'packet_count':len(nodes),
            'negative_signed_capacity_count':sum(n['u'][1]<0 for n in nodes.values()),
            'negative_root_capacity_count':sum(n['u'][1]<0 for n in roots),
            'baselines':{'old_U':ancestor['roads'][name]['closed_squared_budgets']['U'],
                'old_Z':record(baselineZ),'full_signed_interpolant':record(baselineS),
                'nonnegative_root_floor':record(nonnegative_floor),
                'one_layer_signed_children_nodes':first_layer_count,
                'one_layer_signed_children_budget':record(budget(first_layer))},
            'node_data':node_records,'frontier_dp':row_sets['weighted_error'],
            'energy_frontier_dp':row_sets['positive_energy'],
            'minimum_nodes_to_beat_nonnegative_root_floor':first_floor,
            'minimum_nodes_to_match_full_signed_positive_energy':first_zero,
            'checks':{'all_u_positive_parts_equal_alpha':True,'all_original_packets_retained':True,
                'all_signed_subtree_upper_bound_enclosure_checks':True,
                'all_local_dirichlet_error_identities':True,'all_frontier_disjoint_error_norm_identities':True,
                'all_dp_choices_strictly_certified_or_identical':True,'all_positive_energy_excess_additivity_checks':True,
                'minimum_node_thresholds_certified_on_both_sides':True,
                'full_expansion_equals_fine_interpolant':True,
                'same_original_true_skeleton_remainder_and_endpoints':True,'no_full_arithmetic_road_recomputed':True},
            'dp_comparison_count':checks['comparison_count'],
            'positive_energy_dp_comparison_count':energy_checks['comparison_count']}
    target=OUT/'signed_frontier_certificate.json'
    target.write_text(json.dumps(output,ensure_ascii=False,separators=(',',':'))+'\n')
    for name,r in output['roads'].items():
        print(name,'negative_u',r['negative_signed_capacity_count'],'baselines',
              {k:(v['upper'] if isinstance(v,dict) and 'upper' in v else v) for k,v in r['baselines'].items()})
        print(name,'minimum_nodes_below_nonnegative_floor',r['minimum_nodes_to_beat_nonnegative_root_floor'],
              'minimum_nodes_match_full_signed_energy',r['minimum_nodes_to_match_full_signed_positive_energy'])
        for row in r['energy_frontier_dp']:
            if row['node_budget'] in [5,8,10,12,15,20,25,30,35,38]:
                print(name,row['node_budget'],row['retained_kernel_nodes'],
                      row['error_root']['upper'],row['closed_squared_budget']['upper'],
                      row['with_preexisting_full_Z_intersection_budget']['upper'])
    print('PASS',round(time.perf_counter()-started,3),'seconds',target.stat().st_size,'bytes')


if __name__=='__main__':
    main()
