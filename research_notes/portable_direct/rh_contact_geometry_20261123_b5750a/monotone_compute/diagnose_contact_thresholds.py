#!/usr/bin/env python3
"""Five fixed contact thresholds for certified upper endpoint interpolants."""
from fractions import Fraction as Q
from pathlib import Path
from bisect import bisect_right
import argparse
import hashlib
import importlib.util
import json
import sys

sys.dont_write_bytecode=True


def load(p,name):
    s=importlib.util.spec_from_file_location(name,p)
    m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m


def at(nodes,values,n):
    if n in values:
        return values[n]
    i=bisect_right(nodes,n)-1
    u,v=nodes[i:i+2]
    return (values[u]*(v-n)+values[v]*(n-u))/(v-u)


def positive_components(nodes,values,tau):
    pieces=[]
    for u,v in zip(nodes,nodes[1:]):
        a=(values[v]-values[u])/(v-u)-tau
        b=values[u]-u*(a+tau)
        lo,hi=u+1,v
        if a>0:
            lo=max(lo,(-b/a).__floor__()+1)
        elif a<0:
            hi=min(hi,(-b/a).__ceil__()-1)
        elif b<=0:
            continue
        if lo<=hi:
            if pieces and lo<=pieces[-1][1]+1:
                pieces[-1][1]=max(pieces[-1][1],hi)
            else:
                pieces.append([lo,hi])
    return pieces


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--main-module',type=Path,required=True)
    ap.add_argument('--harmonic-module',type=Path,required=True)
    ap.add_argument('--certificate',type=Path,required=True)
    ap.add_argument('--geometry',type=Path,required=True)
    args=ap.parse_args()
    base=load(args.main_module,'contact_main');m=load(args.harmonic_module,'contact_harmonic')
    cert=json.loads(args.certificate.read_text());geo=json.loads(args.geometry.read_text())
    assert cert['status']=='PASS'
    q={r['n']:Q(int(r['certified_q_upper_integer']),m.S) for r in cert['selected_flux_points']}
    thresholds=[Q(0),Q(1,100000),Q(3,100000),Q(1,10000),Q(3,10000)]
    rows=[];grid_summaries=[]
    for grid in ['original44','dense1270']:
        fullnodes=sorted({n for b in geo['original44'] for n in b['nodes']}) if grid=='original44' else geo['dense1270_nodes']
        selected_bounds=[];zero_bounds=[];selected_taus=[]
        for block in geo['original44']:
            l,r=block['L'],block['R'];nodes=[n for n in fullnodes if l<=n<=r]
            cells,fit,contacts,pools,residual,g,d2=base.pava(nodes,q)
            true_upper_interpolant_energy=base.piecewise_energy(m,nodes,q,True)
            diagnostics=[]
            for tau in thresholds:
                components=positive_components(nodes,residual,tau)
                budget=m.ZERO;component_rows=[]
                for lo,hi in components:
                    u,v=lo-1,hi+1
                    assert l<=u<v<=r
                    qu,qv=at(nodes,residual,u),at(nodes,residual,v)
                    assert qu<=tau*u and qv<=tau*v
                    cuts=[u]+[n for n in nodes if u<n<v]+[v]
                    slope=(qv-qu)/(v-u)
                    energy=sum(((at(nodes,residual,b)-at(nodes,residual,a))/(b-a)-slope)**2*(b-a)
                               for a,b in zip(cuts,cuts[1:]))
                    term=m.qmul(base.green_trace(m,u,v),energy)
                    budget=m.add(budget,term)
                    component_rows.append({'L':u,'R':v,'positive_integer_support':[lo,hi],
                        'local_chord_removed_dirichlet_energy':str(energy),'trace_budget':m.record(term)})
                gshift={n:g[n]+tau*n for n in nodes}
                genergy=base.piecewise_energy(m,nodes,gshift,True)
                budget_energy=m.square(m.add(base.isqrt_interval(m,genergy),base.isqrt_interval(m,budget)))
                exact_uenergy=base.piecewise_energy(m,nodes,{n:residual[n]-tau*n for n in nodes},True)
                assert exact_uenergy[0]<=budget[1]
                assert true_upper_interpolant_energy[0]<=budget_energy[1]
                diagnostics.append({'tau':str(tau),'component_count':len(components),
                    'max_component_width':max((z['R']-z['L'] for z in component_rows),default=0),
                    'background_positive_energy':m.record(genergy),'trace_budget':m.record(budget),
                    'exact_positive_remainder_energy':m.record(exact_uenergy),
                    'fine_interpolant_positive_energy_bound_expression':m.record(budget_energy),
                    'components':component_rows})
            best=min(diagnostics,key=lambda d:int(d['fine_interpolant_positive_energy_bound_expression']['integer_bounds'][1]))
            selected_taus.append(best['tau'])
            selected_bounds.append(tuple(map(int,best['fine_interpolant_positive_energy_bound_expression']['integer_bounds'])))
            zero_bounds.append(tuple(map(int,diagnostics[0]['fine_interpolant_positive_energy_bound_expression']['integer_bounds'])))
            rows.append({'grid':grid,'L':l,'R':r,'node_count':len(nodes),
                'exact_upper_interpolant_positive_energy':m.record(true_upper_interpolant_energy),
                'all_fine_node_contacts':[nodes[i] for i in contacts],
                'thresholds':diagnostics,'best_of_five_tau':best['tau']})
        shared=[b['L'] for b in geo['original44'][1:]]
        duplicated=sum((max(q[n],Q(0))**2/n**2 for n in shared),Q(0))
        direct=base.piecewise_energy(m,fullnodes,q,True)
        best_bound=m.sub(m.total(selected_bounds),m.rat(duplicated))
        zero_bound=m.sub(m.total(zero_bounds),m.rat(duplicated))
        assert direct[0]<=best_bound[1]
        grid_summaries.append({'grid':grid,'chosen_taus_by_block':selected_taus,
            'actual_fine_interpolant_positive_energy_upper_via_strict_node_majorant':m.record(direct),
            'zero_threshold_blockwise_bound_expression':m.record(zero_bound),
            'best_of_five_blockwise_bound_expression':m.record(best_bound),
            'shared_endpoint_positive_energy_removed_exact':str(duplicated)})
    out={'schema':'RH_CONTACT_THRESHOLD_DIAGNOSTIC_V1','status':'PASS',
        'scope':'Five fixed thresholds on certified q upper endpoint interpolants; bounds concern fine interpolation, not the unsampled full road.',
        'no_actual_contact_topology_assumed':True,'thresholds':list(map(str,thresholds)),
        'input_files':[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
            for p in [args.main_module,args.harmonic_module,args.certificate,args.geometry]],
        'grid_summaries':grid_summaries,'blocks':rows}
    Path(__file__).with_name('contact_threshold_certificate.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':'PASS','grid_summaries':grid_summaries},ensure_ascii=False))


if __name__=='__main__':
    main()
