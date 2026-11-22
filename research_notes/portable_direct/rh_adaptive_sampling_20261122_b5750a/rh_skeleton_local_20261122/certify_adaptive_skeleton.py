#!/usr/bin/env python3
"""Minimum true-node skeletons whose positive chord floor costs zero.

Reads the existing full-road triangle certificate. No arithmetic road is
rebuilt. All signs/visibility decisions use outward 10**60 intervals.
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
from certify_joint_energy import (A,B,DIGITS,ZERO,add,sub,scale,mul,positive,
    square,sqrt_interval,isum,record,energy,interval_from_record,intersects)

def tent(p,n):
    L,x,R=p
    if not L<=n<=R:return F(0)
    return F((n-L)*(R-x),R-L) if n<=x else F((x-L)*(R-n),R-L)

def line(values,L,R,n):
    return add(scale(values[L],F(R-n,R-L)),scale(values[R],F(n-L,R-L)))

def interpolate(values,nodes):
    return {n:line(values,L,R,n) for L,R in zip(nodes,nodes[1:]) for n in range(L,R+1)}

def visibility(nodes,q):
    edges={}; certificates=[]
    for i,L in enumerate(nodes[:-1]):
        for j in range(i+1,len(nodes)):
            R=nodes[j];tests=[];reason=None
            if j==i+1:reason='original_fine_edge'
            elif q[L][1]<=0 and q[R][1]<=0:reason='both_true_endpoint_values_nonpositive'
            else:
                chord={n:line(q,L,R,n) for n in nodes[i:j+1]}
                for n in nodes[i+1:j]:tests.append(('fine_node',[n],sub(chord[n],positive(q[n]))))
                for u,v in zip(nodes[i:j],nodes[i+1:j+1]):
                    if q[u][1]<0<q[v][0]:
                        tests.append(('zero_crossing_positive_denominator',[u,v],sub(mul(q[v],chord[u]),mul(q[u],chord[v]))))
                    elif q[v][1]<0<q[u][0]:
                        tests.append(('zero_crossing_positive_denominator',[u,v],sub(mul(q[u],chord[v]),mul(q[v],chord[u]))))
            bad=next((t for t in tests if t[2][0]>0),None)
            if bad:
                ok=False
                witness={'kind':bad[0],'nodes':bad[1],'strict_gap_or_positive_denominator_numerator':record(bad[2])}
                if bad[0]=='fine_node':integer_witness=(bad[1][0],bad[2])
                else:
                    u,v=bad[1];ru,rv=sum(q[u]),sum(q[v]);root=F(u*rv-v*ru,rv-ru)
                    k=root.numerator//root.denominator
                    integer_witness=None
                    for n in range(max(u,k-1),min(v,k+2)+1):
                        gap=sub(line(q,L,R,n),positive(line(q,u,v,n)))
                        if gap[0]>0:integer_witness=(n,gap);break
                assert integer_witness is not None,('continuous and integer visibility need separate graphs',L,R)
                witness['integer_violation_node']=integer_witness[0]
                witness['integer_violation_gap']=record(integer_witness[1])
            else:
                assert reason is not None or all(t[2][1]<=0 for t in tests),(L,R,tests)
                ok=True;witness={'kind':reason or 'all_fine_and_zero_crossing_breakpoints_nonpositive'}
            edges[i,j]=ok
            certificates.append({'L':L,'R':R,'visible_under_positive_fine_interpolant':ok,'witness':witness})
    return edges,certificates

def shortest_path(nodes,edges):
    m=len(nodes);dist=[0]+[10**6]*(m-1);prev=[None]*m
    for j in range(1,m):
        d,i=min((dist[i]+1,i) for i in range(j) if edges[i,j])
        dist[j]=d;prev[j]=i
    path=[m-1]
    while path[-1]!=0:path.append(prev[path[-1]])
    path.reverse()
    return [nodes[i] for i in path], [{'node':n,'minimum_segments_from_left':dist[i],
        'predecessor':None if prev[i] is None else nodes[prev[i]]} for i,n in enumerate(nodes)]

def lower_hull(nodes,q):
    stack=[];comparisons=[]
    for x in nodes:
        while len(stack)>=2:
            a,b=stack[-2:]
            turn=sub(scale(sub(q[x],q[b]),b-a),scale(sub(q[b],q[a]),x-b))
            assert turn[0]>0 or turn[1]<0,('uncertain hull orientation',a,b,x)
            pop=turn[1]<0
            comparisons.append({'a':a,'b':b,'c':x,'orientation':record(turn),'remove_middle':pop})
            if not pop:break
            stack.pop()
        stack.append(x)
    return stack,comparisons

def select(proposals,counter):
    """Compare exact positive edge-cost sums by separated intervals or identity."""
    best=min(proposals,key=lambda p:(p['value'][1],p['value'][0],len(p['nodes']),p['nodes']))
    for p in proposals:
        if p is best:continue
        counter['comparisons']+=1
        if p['signature']==best['signature']:
            assert p['value']==best['value']
            counter['identical_cost_expressions']+=1
        else:
            assert best['value'][1]<p['value'][0],('unresolved comparison',best,p)
            counter['strict_interval_separations']+=1
    return best

def edge_cost_dp(nodes,q,fine,edges,X,counter):
    costs={};records=[]
    for (i,j),visible in edges.items():
        L,R=nodes[i],nodes[j]
        value=ZERO if visible else isum(scale(positive(sub(square(positive(line(q,L,R,n))),square(positive(fine[n])))),F(1,n*n)) for n in range(L+1,R))
        if not visible:assert value[0]>0
        costs[i,j]=value
        records.append({'L':L,'R':R,'positive_energy_excess':record(value),
            'exact_zero_by_visibility':visible})
    dp={(0,0):{'value':ZERO,'signature':(),'nodes':[nodes[0]]}}
    for j in range(1,len(nodes)):
        for k in range(1,j+1):
            choices=[]
            for i in range(j):
                if (i,k-1) not in dp:continue
                old=dp[i,k-1];sig=old['signature']+(() if costs[i,j]==ZERO else (f'{X}:{nodes[i]}:{nodes[j]}',))
                choices.append({'value':add(old['value'],costs[i,j]),'signature':sig,'nodes':old['nodes']+[nodes[j]]})
            dp[j,k]=select(choices,counter)
    end={k-1:dp[len(nodes)-1,k] for k in range(1,len(nodes))}
    return end,records

def main():
    start=time.perf_counter()
    source_path=ROOT/'rh_triangle_certificate_20261122/dyadic_triangle_certificate.json'
    source=json.loads(source_path.read_bytes());assert source['status']=='AUTHOR_STRICT_FINITE_DYADIC_TRIANGLE_CERTIFICATE_PASSED'
    result={'schema':'EM_ADAPTIVE_TRUE_SKELETON_V1','status':'PASS',
        'scope':'Minimum extra skeleton nodes chosen from the fixed true fine samples, preserving all original dyadic endpoints; no coarse-data-only arithmetic estimate.',
        'science_freeze':'9fc068244e4f1117f1e75df5eb0285c6697d21d7',
        'window':source['window'],'arithmetic':{'denominator_power_of_10':DIGITS,'method':'outward integer intervals and rational geometry'},
        'inputs':[{'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [source_path,ROOT/'rh_joint_certificate/certify_joint_energy.py',ROOT/'rh_correlation_rational/certify_matched_nodes.py']],
        'roads':{}}
    for name,road in source['roads'].items():
        samples={r['n']:interval_from_record(r['value']) for r in road['true_dyadic_endpoint_samples']}
        fine_values={};skeleton_values={};blocks=[];block_dp=[]
        counter={'comparisons':0,'strict_interval_separations':0,'identical_cost_expressions':0}
        for rb,mb in zip(road['dyadic_blocks'],source['partition']['dyadic_blocks']):
            X,Y=rb['X'],rb['Y'];nodes=mb['nodes'];packets=[p for level in rb['levels'] for p in level['packets']]
            q={n:add(line(samples,X,Y,n),isum(scale(interval_from_record(p['signed_charge']),tent((p['L'],p['x'],p['R']),n)) for p in packets)) for n in nodes}
            q[X],q[Y]=samples[X],samples[Y]
            fine=interpolate(q,nodes);edges,certs=visibility(nodes,q)
            path,dp=shortest_path(nodes,edges);hull,hchecks=lower_hull(nodes,q)
            cost_dp,cost_records=edge_cost_dp(nodes,q,fine,edges,X,counter)
            block_dp.append(cost_dp)
            assert all(edges[nodes.index(a),nodes.index(b)] for a,b in zip(hull,hull[1:]))
            skeleton=interpolate(q,path)
            # Analytic visibility establishes exact zero. These complete integer
            # evaluations check the interval implementation without asserting
            # that interval overlap proves the exact geometric theorem.
            assert all(skeleton[n][0]<=positive(fine[n])[1] for n in range(X,Y+1))
            fine_values.update(fine);skeleton_values.update(skeleton)
            blocks.append({'X':X,'Y':Y,'fine_nodes':nodes,
                'true_fine_samples':[{'n':n,'value':record(q[n])} for n in nodes],
                'minimum_zero_floor_skeleton':path,'minimum_added_nodes':len(path)-2,
                'lower_convex_hull_skeleton':hull,'lower_hull_added_nodes':len(hull)-2,
                'visibility_edges':certs,'shortest_path_table':dp,'lower_hull_orientation_checks':hchecks,
                'edge_positive_energy_excesses':cost_records,
                'minimum_cost_by_exact_added_nodes':[{'added_nodes':k,'nodes':p['nodes'],'positive_energy_excess':record(p['value']),'nonzero_edge_cost_expression':p['signature']} for k,p in cost_dp.items()]})
        E=energy(fine_values,A+1,B-1,'positive')
        previous=interval_from_record(road['energies']['fine_interpolant_positive_energy']);assert intersects(E,previous)
        R=interval_from_record(road['energies']['fine_local_positive_remainder_energy'])
        endpoints=interval_from_record(road['energies']['true_two_endpoint_direct_energy'])
        budget=add(square(add(sqrt_interval(E),sqrt_interval(R))),endpoints)
        all_new=sorted({n for b in blocks for n in b['minimum_zero_floor_skeleton']})
        global_dp={0:{'value':ZERO,'signature':(),'nodes':[]}}
        for table in block_dp:
            buckets={}
            for old_count,old_state in global_dp.items():
                for add_count,new_state in table.items():
                    count=old_count+add_count
                    buckets.setdefault(count,[]).append({'value':add(old_state['value'],new_state['value']),
                        'signature':old_state['signature']+new_state['signature'],
                        'nodes':sorted(set(old_state['nodes']+new_state['nodes']))})
            global_dp={k:select(v,counter) for k,v in buckets.items()}
        curve=[]
        for k in sorted(global_dp):
            best=select([v for j,v in global_dp.items() if j<=k],counter)
            E_new=add(E,best['value']);b_new=add(square(add(sqrt_interval(E_new),sqrt_interval(R))),endpoints)
            curve.append({'added_nodes_budget':k,'added_nodes_used':len(best['nodes'])-len(source['partition']['backbone']),
                'nodes':best['nodes'],'positive_energy_excess':record(best['value']),
                'optimal_positive_envelope_energy':record(E_new),'closed_squared_budget':record(b_new),
                'nonzero_edge_cost_expression':best['signature']})
        first_zero=next(p['added_nodes_budget'] for p in curve if p['positive_energy_excess']['integer_bounds']==['0','0'])
        assert first_zero==len(all_new)-len(source['partition']['backbone'])
        result['roads'][name]={'original_skeleton_nodes':source['partition']['backbone'],
            'minimum_zero_floor_skeleton_nodes':all_new,'minimum_added_nodes':len(all_new)-len(source['partition']['backbone']),
            'lower_hull_added_nodes':sum(b['lower_hull_added_nodes'] for b in blocks),
            'fine_node_count_unchanged':len(source['partition']['fine_nodes']),
            'optimal_positive_envelope_energy':record(E),'fine_positive_remainder_energy_unchanged':record(R),
            'true_two_endpoint_energy_unchanged':record(endpoints),'closed_zero_floor_budget':record(budget),
            'exact_skeleton_excess_over_fine_positive_energy':0,
            'true_road_skeleton_floor_bound':'b_J(q) <= 2 ||q_+||_w ||P_-||_w + ||P_-||_w^2; actual q floor need not be zero',
            'minimum_budget_by_added_skeleton_nodes':curve,'certified_DP_comparisons':counter,'blocks':blocks,
            'checks':{'all_continuous_invisible_chords_have_integer_witnesses':True,
                'shortest_path_exhausts_all_fine_node_subsets':True,
                'all_old_dyadic_endpoints_retained':True,'no_complete_arithmetic_road_recomputed':True}}
        print(name,'added',result['roads'][name]['minimum_added_nodes'],'nodes',all_new,'budget',record(budget)['upper'])
        for p in curve[:first_zero+1]:print(name,'added_budget',p['added_nodes_budget'],'budget',p['closed_squared_budget']['upper'])
    result['cost']={'wall_seconds':time.perf_counter()-start,'complete_arithmetic_road_recomputations':0}
    target=OUT/'adaptive_skeleton_certificate.json';target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print('PASS',target.stat().st_size)

if __name__=='__main__':main()
