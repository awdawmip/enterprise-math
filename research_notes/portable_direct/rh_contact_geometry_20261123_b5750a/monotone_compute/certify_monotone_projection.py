#!/usr/bin/env python3
"""Reciprocal-measure PAVA of the complete-road flux projection.

Only the auxiliary Lambda prefix is evaluated. Every reported actual-road
quantity pays the full thickness error. No actual D array is constructed.
All non-timing arithmetic uses fractions or outward fixed-point intervals.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import isqrt, factorial, prod
import argparse
import hashlib
import importlib.util
import json
import sys
import time

sys.dont_write_bytecode = True


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def weight(u, v):
    return Q(1, u) - Q(1, v)


def mean(q, u, v):
    return (u*q[v]-v*q[u])/(v-u)


def secant(q, l, x, r):
    return (q[x]-q[l])/(x-l)-(q[r]-q[x])/(r-x)


def isqrt_interval(m, z):
    lo = isqrt(max(0, z[0])*m.S)
    hi0 = max(0, z[1])*m.S
    hi = isqrt(hi0)
    return lo, hi+(hi*hi != hi0)


def perturb_square(m, centre_square, error_square):
    d = isqrt_interval(m, centre_square)
    e = isqrt_interval(m, error_square)[1]
    return m.square((max(0, d[0]-e), d[1]+e))


def iabs_upper(z):
    return max(abs(z[0]), abs(z[1]))


def imean(m, q, u, v):
    return m.qmul(m.sub(m.qmul(q[v], u), m.qmul(q[u], v)), 1, v-u)


def itriangle(m, q, l, x, r):
    return m.sub(m.qmul(m.sub(q[x], q[l]), 1, x-l),
                 m.qmul(m.sub(q[r], q[x]), 1, r-x))


def balanced_packets(nodes):
    if len(nodes) <= 2:
        return []
    i = (len(nodes)-1)//2
    return [{'L': nodes[0], 'x': nodes[i], 'R': nodes[-1]}] + \
        balanced_packets(nodes[:i+1]) + balanced_packets(nodes[i:])


def pava(nodes, q):
    """Exact weighted PAVA; equal means are never merged just for equality."""
    cells = [(u, v, weight(u, v), mean(q, u, v))
             for u, v in zip(nodes, nodes[1:])]
    pools = []
    for i in range(len(cells)):
        pools.append([i, i+1, cells[i][3]])
        while len(pools) >= 2 and pools[-2][2] > pools[-1][2]:
            left, right = pools[-2][0], pools[-1][1]
            pools[-2:] = [[left, right, mean(q, nodes[left], nodes[right])]]
    fit = [Q(0)]*len(cells)
    for first, last, value in pools:
        fit[first:last] = [value]*(last-first)
    assert all(fit[i] <= fit[i+1] for i in range(len(fit)-1))
    cumulative = Q(0)
    contacts = [0]
    residual_q = {nodes[0]: Q(0)}
    for i, (u, v, w, z) in enumerate(cells):
        cumulative += w*(z-fit[i])
        assert cumulative >= 0
        residual_q[v] = v*cumulative
        if cumulative == 0:
            contacts.append(i+1)
    assert cumulative == 0 and contacts[-1] == len(cells)
    # Every fine-node contact is retained, including interior zero contacts
    # inside a fitted constant segment.
    contact_pools = []
    for i, j in zip(contacts, contacts[1:]):
        d2 = sum((cells[t][2]*(cells[t][3]-fit[t])**2 for t in range(i,j)), Q(0))
        direct = sum(((residual_q[cells[t][1]]-residual_q[cells[t][0]])**2/
                      (cells[t][1]-cells[t][0]) for t in range(i,j)), Q(0))
        assert d2 == direct
        contact_pools.append({'first':i,'last':j,'L':nodes[i],'R':nodes[j],'d2':d2})
    d2 = sum((w*(z-fit[i])**2 for i, (_,_,w,z) in enumerate(cells)), Q(0))
    assert d2 == sum((p['d2'] for p in contact_pools), Q(0))
    g = {n:q[n]-residual_q[n] for n in nodes}
    assert g[nodes[0]] == q[nodes[0]] and g[nodes[-1]] == q[nodes[-1]]
    assert all(mean(g,u,v) == fit[i] for i,(u,v,_,_) in enumerate(cells))
    return cells, fit, contacts, contact_pools, residual_q, g, d2


def linear_energy(m, first, last, a, b):
    if first > last:
        return m.ZERO
    h0,h20 = m.harmonics(first-1)
    h1,h21 = m.harmonics(last)
    return m.positive(m.total([m.rat(a*a*(last-first+1)),
        m.qmul(m.sub(h1,h0), 2*a*b), m.qmul(m.sub(h21,h20), b*b)]))


def piecewise_energy(m, nodes, q, positive=False):
    first = max(q[nodes[0]], Q(0)) if positive else q[nodes[0]]
    out = m.rat(first*first/nodes[0]**2)
    for u,v in zip(nodes,nodes[1:]):
        a = (q[v]-q[u])/(v-u)
        b = q[u]-u*a
        lo,hi = u+1,v
        if positive:
            if a > 0:
                lo = max(lo, (-b/a).__floor__()+1)
            elif a < 0:
                hi = min(hi, (-b/a).__ceil__()-1)
            elif b <= 0:
                continue
        out = m.add(out, linear_energy(m,lo,hi,a,b))
    return out


def green_trace(m, l, r):
    h = r-l
    if h <= 1:
        return m.ZERO
    h0,h20 = m.harmonics(l)
    h1,h21 = m.harmonics(r-1)
    return m.positive(m.qmul(m.total([
        m.qmul(m.sub(h1,h0), l+r), m.rat(-(h-1)),
        m.qmul(m.sub(h21,h20), -l*r)]),1,h))


def stream_reference(m, old, family, all_nodes, blocks):
    """Full auxiliary flux moments and full positive error prefix, no D."""
    a,b = all_nodes[0],all_nodes[-1]
    coef = prod(map(Q,family['nodes']))/factorial(len(family['nodes'])+1)
    k = len(family['nodes'])+1
    assert m.log_int(b)[1] <= k*m.S
    qstar,_,_,_,oracle_cost = old.point_oracle(m,all_nodes,family)
    qcentre = {n:Q(sum(z),2*m.S) for n,z in qstar.items()}
    events=[]
    for p in old.primes_upto(b):
        power=p
        while power<=b:
            events.append((power,p));power*=p
    events.sort()
    event_index=0
    psi=m.ZERO
    eta0=[0]*(b+1)
    eta1=[m.ZERO]*(b+1)
    integrated_radius=[m.ZERO]*(b+1)
    selected=set(all_nodes)
    e_points={}
    summaries={}
    ranges=blocks+[(a,b)]
    for u,v in ranges:
        summaries[(u,v)]={'mass':m.ZERO,'square':m.ZERO,'global_error2':m.ZERO,'local_error2':m.ZERO}
    for n in range(1,b+1):
        if n>=2:
            en=m.qmul(old.interval_power(m,m.log_int(n),k),coef)[1]
            eta0[n]=eta0[n-1]+en
            eta1[n]=m.add(eta1[n-1],m.qmul((en,en),1,n))
        while event_index<len(events) and events[event_index][0]==n:
            psi=m.add(psi,m.log_int(events[event_index][1]));event_index+=1
        if n<b:
            integrated_radius[n+1]=m.add(integrated_radius[n],
                m.qmul((eta0[n],eta0[n]),1,n*(n+1)))
        if n<a:
            continue
        kap=m.qmul(m.sub(m.log_int(n+1),m.log_int(n)),n*(n+1))
        en=m.sub(psi,kap)
        if n in selected:
            e_points[n]={'reference':en,'radius':eta0[n]}
        if n==b:
            continue
        for u,v in ranges:
            if u<=n<v:
                row=summaries[(u,v)]
                row['mass']=m.add(row['mass'],m.qmul(en,1,n*(n+1)))
                row['square']=m.add(row['square'],m.qmul(m.square(en),1,n*(n+1)))
                for key,radius in [('global_error2',eta0[n]),('local_error2',eta0[n]-eta0[u])]:
                    row[key]=m.add(row[key],m.qmul(m.square((radius,radius)),1,n*(n+1)))
    full=[]
    for u,v in ranges:
        row=summaries[(u,v)];w=weight(u,v)
        variance=m.positive(m.sub(row['square'],m.qmul(m.square(row['mass']),1/w)))
        mass_expected=m.sub(m.qmul(qstar[v],1,v),m.qmul(qstar[u],1,u))
        assert m.overlap(row['mass'],mass_expected)
        full.append({'L':u,'R':v,'reference_variance':m.record(variance),
            'complete_error_square_norm':m.record(row['global_error2']),
            'constant_shift_removed_error_square_norm':m.record(row['local_error2']),
            'actual_variance':m.record(perturb_square(m,variance,row['local_error2']))})
    closed_e=m.qmul(m.qmul(old.interval_power(m,m.log_int(b),k),coef),Q(b+1,2)-Q(1,b))
    assert eta0[b] <= closed_e[1]
    return {'qstar':qstar,'qcentre':qcentre,'eta0':eta0,'eta1':eta1,
            'integrated_radius':integrated_radius,'e_points':e_points,
            'full_variances':full,'oracle_cost':oracle_cost,
            'closed_E_error_at_B':closed_e}


def hat_error(m, data, l, x, r):
    e0,e1=data['eta0'],data['eta1']
    a,b=x-l,r-x
    left=m.qmul(m.sub((e0[x]-e0[l],)*2,
                     m.qmul(m.sub(e1[x],e1[l]),l)),1,a)
    right=m.qmul(m.sub(m.qmul(m.sub(e1[r-1],e1[x]),r),
                      (e0[r-1]-e0[x],)*2),1,b)
    return m.positive(m.add(left,right))[1]


def analyze_region(m,data,nodes,packets,label):
    l,r=nodes[0],nodes[-1]
    qc,qs=data['qcentre'],data['qstar']
    cells,fit,contacts,pools,residual,g,d2=pava(nodes,qc)
    overall=mean(qc,l,r)
    variance=sum((w*(z-overall)**2 for _,_,w,z in cells),Q(0))
    complete_error2=m.ZERO
    local_error2=m.ZERO
    cell_rows=[]
    for i,(u,v,w,z) in enumerate(cells):
        numerr=iabs_upper(m.sub(imean(m,qs,u,v),m.rat(z)))
        avg_radius=m.qmul(m.sub(data['integrated_radius'][v],
                               data['integrated_radius'][u]),1/w)
        rho=max(0,avg_radius[1])+numerr
        localrho=max(0,avg_radius[1]-data['eta0'][l])+numerr
        complete_error2=m.add(complete_error2,m.qmul(m.square((rho,rho)),w))
        local_error2=m.add(local_error2,m.qmul(m.square((localrho,localrho)),w))
        cell_rows.append({'L':u,'R':v,'weight':str(w),'reference_midpoint_mean':str(z),
             'fitted_mean':str(fit[i]),'actual_mean':m.record((m.rat(z)[0]-rho,m.rat(z)[1]+rho)),
             'complete_matching_radius_integer':str(rho),
             'error_after_unknown_constant_shift_integer':str(localrho)})
    rawsum=Q(0);possum=Q(0);level_rows={};packet_rows=[]
    for p in packets:
        u,x,v=p['L'],p['x'],p['R']
        t=secant(qc,u,x,v)
        tau=Q((x-u)*(v-x),v-u)
        raw=tau*t*t;pos=tau*max(t,Q(0))**2
        rawsum+=raw;possum+=pos
        er=hat_error(m,data,u,x,v)+iabs_upper(m.sub(itriangle(m,qs,u,x,v),m.rat(t)))
        ti=m.rat(t);actual_t=(ti[0]-er,ti[1]+er)
        actual_pos=m.qmul(m.square(m.positive(actual_t)),tau)
        weighted=m.qmul(m.square(m.positive(actual_t)),(v-u)**3)
        depth=sum(1 for a in packets if a['L']<=u and v<=a['R'] and (a['L'],a['R'])!=(u,v))
        row=level_rows.setdefault(depth,{'count':0,'raw':Q(0),'positive':Q(0),
                                          'actual_positive':m.ZERO,'actual_scaled':m.ZERO})
        row['count']+=1;row['raw']+=raw;row['positive']+=pos
        row['actual_positive']=m.add(row['actual_positive'],actual_pos)
        row['actual_scaled']=m.add(row['actual_scaled'],weighted)
        packet_rows.append({'L':u,'x':x,'R':v,'root_depth':depth,
            'reference_triangle_moment':str(t),'actual_triangle_moment':m.record(actual_t),
            'actual_directed_haar_energy':m.record(actual_pos),
            'old_elimination_level':p.get('old_elimination_level')})
    assert rawsum==variance and len(packets)==len(nodes)-2
    assert possum<=d2<=variance
    b0=m.ZERO;simple_b0=m.ZERO;pool_rows=[]
    for p in pools:
        u,v=p['L'],p['R'];d=p['d2']
        trace=green_trace(m,u,v)
        bound=m.qmul(trace,d)
        simple=Q((v-u)**2-1,6*u*u)*d
        b0=m.add(b0,bound);simple_b0=m.add(simple_b0,m.rat(simple))
        pool_rows.append({'L':u,'R':v,'cell_count':p['last']-p['first'],
                         'dirichlet_residual_exact':str(d),
                         'green_trace':m.record(trace),'trace_budget':m.record(bound)})
    observed_gap_energy=piecewise_energy(m,nodes,residual)
    assert observed_gap_energy[0]<=b0[1]
    q_radius={}
    for n in nodes:
        qm=m.positive(m.sub(m.qmul(data['eta1'][n],n),(data['eta0'][n],)*2))[1]
        qm+=iabs_upper(m.sub(qs[n],m.rat(qc[n])))
        q_radius[n]=Q(qm,m.S)
    qerror_energy=piecewise_energy(m,nodes,q_radius)
    fpositive=piecewise_energy(m,nodes,{n:qc[n] for n in nodes},True)
    gpositive=piecewise_energy(m,nodes,g,True)
    roots=m.add(m.add(isqrt_interval(m,gpositive),isqrt_interval(m,b0)),
                isqrt_interval(m,qerror_energy))
    layers=[{'root_depth':d,'packet_count':z['count'],
        'reference_unsigned':m.record(m.rat(z['raw'])),
        'reference_directed':m.record(m.rat(z['positive'])),
        'actual_directed':m.record(z['actual_positive']),
        'actual_width_weighted_over_L2':m.record(m.qmul(z['actual_scaled'],1,l*l))}
        for d,z in sorted(level_rows.items())]
    actual_var=perturb_square(m,m.rat(variance),local_error2)
    actual_distance=perturb_square(m,m.rat(d2),local_error2)
    actual_directed=m.total(z['actual_positive'] for z in level_rows.values())
    assert actual_var[0]>0 and actual_distance[0]>actual_directed[1]
    ratio=(m.rat(Q(actual_distance[0],actual_var[1]))[0],
           m.rat(Q(actual_distance[1],actual_var[0]))[1])
    return {'label':label,'L':l,'R':r,'node_count':len(nodes),'cell_count':len(cells),
        'reference_projected_variance':m.record(m.rat(variance)),
        'reference_directed_haar_sum':m.record(m.rat(possum)),
        'reference_monotone_cone_distance_square':m.record(m.rat(d2)),
        'actual_projected_variance':m.record(actual_var),
        'actual_monotone_cone_distance_square':m.record(actual_distance),
        'actual_directed_haar_sum':m.record(actual_directed),
        'actual_distance_over_variance':m.record(ratio),
        'strict_actual_distance_exceeds_directed_haar_sum':True,
        'complete_error_square_norm':m.record(complete_error2),
        'constant_shift_removed_error_square_norm':m.record(local_error2),
        'all_fine_node_contacts':[nodes[i] for i in contacts],
        'positive_contact_pool_count':sum(p['d2']>0 for p in pools),
        'contact_pools':pool_rows,'reference_contact_trace_budget':m.record(b0),
        'reference_simple_contact_trace_budget':m.record(simple_b0),
        'reference_exact_F_minus_G_square_energy':m.record(observed_gap_energy),
        'reference_F_positive_energy':m.record(fpositive),
        'reference_G_positive_energy':m.record(gpositive),
        'actual_F_error_square_energy':m.record(qerror_energy),
        'actual_fine_interpolant_positive_energy_upper_from_G_and_pool':m.record(m.square(roots)),
        'layers':layers,'cells':cell_rows,'packets':packet_rows}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--harmonic-module',type=Path,required=True)
    ap.add_argument('--oracle-module',type=Path,required=True)
    ap.add_argument('--family',type=Path,required=True)
    ap.add_argument('--geometry',type=Path,required=True)
    args=ap.parse_args()
    started=time.perf_counter()
    m=load(args.harmonic_module,'monotone_harmonic')
    old=load(args.oracle_module,'monotone_oracle')
    family=json.loads(args.family.read_text())
    geo=json.loads(args.geometry.read_text())
    original=geo['original44']
    blockranges=[(x['L'],x['R']) for x in original]
    allnodes=sorted(set(geo['dense1270_nodes'])|{n for b in original for n in b['nodes']})
    data=stream_reference(m,old,family,allnodes,blockranges)
    prefix_seconds=time.perf_counter()-started
    results=[]
    for grid in ['original44','dense1270']:
        gridnodes=sorted({n for b in original for n in b['nodes']}) if grid=='original44' else geo['dense1270_nodes']
        forest=[]
        for block in original:
            l,r=block['L'],block['R']
            nodes=[n for n in gridnodes if l<=n<=r]
            packets=block['packets'] if grid=='original44' else balanced_packets(nodes)
            forest+=packets
            results.append(analyze_region(m,data,nodes,packets,grid+':dyadic'))
        anchors=[b['L'] for b in original]+[original[-1]['R']]
        results.append(analyze_region(m,data,gridnodes,forest+balanced_packets(anchors),grid+':whole'))
    b=allnodes[-1]
    nodes_out=[]
    for n in allnodes:
        e=data['e_points'][n]
        qr=m.positive(m.sub(m.qmul(data['eta1'][n],n),(data['eta0'][n],)*2))[1]
        nodes_out.append({'n':n,'E_reference_integer_bounds':list(map(str,e['reference'])),
            'complete_E_error_integer_upper':str(e['radius']),
            'actual_E_integer_bounds':[str(e['reference'][0]-e['radius']),str(e['reference'][1]+e['radius'])],
            'q_reference_integer_bounds':list(map(str,data['qstar'][n])),
            'complete_q_matching_radius_integer_upper':str(qr),
            'certified_q_lower_integer':str(data['qstar'][n][0]-qr),
            'certified_q_upper_integer':str(data['qstar'][n][1]+qr)})
    out={'schema':'RH_MONOTONE_FLUX_PROJECTION_V1','status':'PASS',
        'scope':'Author finite computation; all actual-road errors paid; midpoint PAVA topology not asserted stable.',
        'input_files':[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
                       for p in [args.harmonic_module,args.oracle_module,args.family,args.geometry]],
        'arithmetic':{'denominator_power_of_10':m.DIGITS,'PAVA':'exact rational midpoint data; strict decrease merges; all zero integral contacts retained'},
        'window':geo['window'],'point_union_count':len(allnodes),
        'no_actual_D_q_c_array_created':True,
        'complete_E_error_at_B':m.record((data['eta0'][b],)*2),
        'closed_form_E_error_at_B':m.record(data['closed_E_error_at_B']),
        'full_flux_variances':data['full_variances'],'projected_analyses':results,
        'selected_flux_points':nodes_out,
        'cost':{'prefix_seconds':prefix_seconds,'total_seconds':time.perf_counter()-started,
                'auxiliary_flux_integer_edges':b-allnodes[0],
                'all_integer_error_terms':b-1,'thickness_exponential_calls':0}}
    target=Path(__file__).with_name('monotone_projection_certificate.json')
    target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    compact={'status':out['status'],'E_error_B':out['complete_E_error_at_B'],
        'full_variances':out['full_flux_variances'],'rows':[
            {k:r[k] for k in ['label','L','R','cell_count','reference_projected_variance',
              'reference_directed_haar_sum','reference_monotone_cone_distance_square',
              'actual_monotone_cone_distance_square','positive_contact_pool_count',
              'reference_contact_trace_budget','reference_exact_F_minus_G_square_energy']}
            for r in results],'cost':out['cost']}
    Path(__file__).with_name('summary.json').write_text(json.dumps(compact,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'cost':out['cost'],'rows':len(results),'points':len(nodes_out)}))


if __name__=='__main__':
    main()
