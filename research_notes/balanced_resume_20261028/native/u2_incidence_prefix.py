#!/usr/bin/env python3
"""Declared-incidence, source-resolved finite U2 prefix using pinned positive BRC.

The scientific kernel and Packet implementation are imported unchanged.
This adapter is a conditional response circuit, not native action admission.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

PACKET_PATH='research_notes/chatgpt_direct/20261007_cell_closure_u2_7f21d8/packet_router.py'
PACKET_BLOB='7465f5aa16cbb8fba61ba4be80f8a6884b879c53'

def git_blob(raw):
    return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()

def load_kernel(repo_root):
    path=Path(repo_root)/PACKET_PATH
    if git_blob(path.read_bytes())!=PACKET_BLOB:
        raise ValueError('packet-router source pin mismatch')
    spec=importlib.util.spec_from_file_location('u2_declared_pinned_router',path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    return module

def validated_families(R, families):
    """Finite anchored families; coherent global-H is not silently assumed."""
    if set(families)!=set(range(12)):
        raise ValueError('each signed incoming port must have an explicit family')
    result={}
    for p in range(12):
        hs=[]
        for h in families[p]:
            if len(h)!=3 or any(type(q) is not int or q not in range(12) for q in h):
                raise ValueError('triples require exactly three integer ports in 0..11')
            h=tuple(sorted(h))
            if p not in h or len({q//2 for q in h})!=3:
                raise ValueError('every triple must contain its incoming port and three axes')
            hs.append(h)
        if not hs or len(hs)!=len(set(hs)):
            raise ValueError('empty or duplicate anchored incidence')
        result[p]=tuple(sorted(hs))
    return result

def transfer_interface(R,families):
    hs=validated_families(R,families)
    columns={p:R.marginals(R.packets(p,R.brc.CWM_ONE,tag=('basis',p),incidence=hs[p])) for p in R.PORTS}
    K=tuple(tuple(columns[p][q].total for p in R.PORTS) for q in R.PORTS)
    W=tuple(tuple(K[q][p] for q in R.PORTS) for p in R.PORTS)
    row=tuple(R.total(columns[p][q] for p in R.PORTS).total for q in R.PORTS)
    for p in R.PORTS:
        assert R.total(columns[p].values()).total==1
        assert K[p][p]==R.Q(1,3) and K[p^1][p]==0
    return {'families':hs,'K_destination_by_source':K,'W_source_by_destination':W,'row_mass':row}

def field_prefix(R,cells,incidence_by_material,depth=2,rho=None,max_leaves=1000000):
    """Retain every finite leaf; raise on resource cap, never drop hidden mass.

    Returns full leaves with source, initial-input, current incoming, Cell and
    ordered packet/edge history, as well as source x material x incoming CWMs.
    All material kernels must be supplied explicitly, including defaults.
    """
    rho=R.Q(1,4) if rho is None else R.Q(rho)
    if type(depth) is not int or depth<0 or not R.Q(0)<rho<R.Q(1):
        raise ValueError('nonnegative integer depth and 0<rho<1 required')
    if type(max_leaves) is not int or max_leaves<1:
        raise ValueError('positive max_leaves required')
    cells=tuple(tuple(z) for z in cells)
    if any(len(z)!=6 or any(type(x) is not int for x in z) for z in cells):
        raise ValueError('six signed raw-chart integer coordinates required')
    if len(cells)!=len(set(cells)) or not cells:
        raise ValueError('nonempty distinct labelled material Cells required')
    if set(incidence_by_material)!=set(range(len(cells))):
        raise ValueError('explicit incidence for every labelled material required')
    interfaces={i:transfer_interface(R,incidence_by_material[i]) for i in range(len(cells))}
    located={z:i for i,z in enumerate(cells)}
    attenuation=R.edge(rho)
    bulk=R.edge(rho/12)
    seed=R.edge(R.Q(1,12))
    layer=[{'source':s,'initial_input':p,'cell':z,'incoming':p,'history':(), 'state':seed}
           for s,z in enumerate(cells) for p in R.PORTS]
    if len(layer)>max_leaves:
        raise ValueError('leaf resource cap exceeded at seed; no truncated result')
    layers=[]
    for n in range(depth+1):
        full_total=R.total(v['state'] for v in layer)
        assert full_total.total==len(cells)*rho**n
        separated={s:{b:{p:R.total(v['state'] for v in layer if v['source']==s and v['cell']==z and v['incoming']==p)
                         for p in R.PORTS} for b,z in enumerate(cells)} for s in range(len(cells))}
        own={s:R.total(separated[s][s].values()) for s in range(len(cells))}
        layers.append({'depth':n,'leaf_count':len(layer),'total':full_total,
                       'source_material_incoming':separated,'own_return':own,'leaves':layer})
        if n==depth:
            break
        nxt=[]
        for parent_index,parent in enumerate(layer):
            z,p,state=parent['cell'],parent['incoming'],parent['state']
            material=located.get(z)
            if material is not None:
                ps=R.packets(p,state,tag=('source',parent['source'],'initial',parent['initial_input'],
                              'depth',n+1,'parent',parent_index,'material',material),born_at=z,
                             incidence=interfaces[material]['families'][p])
                emissions=[(q,R.serial(packet.leg,attenuation),packet.tag) for packet in ps for q in packet.ports]
            else:
                emissions=[(q,R.serial(state,bulk),None) for q in R.PORTS]
            if len(nxt)+len(emissions)>max_leaves:
                raise ValueError('leaf resource cap exceeded; no truncated result')
            for q,weight,tag in emissions:
                target=R.advance(z,q)
                event={'depth':n+1,'from':z,'incoming':p,'packet_tag':tag,'outgoing':q,'to':target}
                nxt.append({'source':parent['source'],'initial_input':parent['initial_input'],
                            'cell':target,'incoming':q^1,'history':parent['history']+(event,),'state':weight})
        layer=nxt
    return {'typed_model':'CONDITIONAL_FIXED_POSITION_POSITIVE_RESPONSE',
            'native_action_occupancy_status':'G1_G2_G3_G4_G5_UNKNOWN',
            'cells':cells,'rho':rho,'depth':depth,'interfaces':interfaces,'layers':layers,
            'omitted_global_total_bound':R.Q(len(cells))*rho**(depth+1)/(1-rho),
            'tail_scope':'total positive response only; no all-depth path-count or joint-state closure'}

def self_test(repo_root, output, full_trace=None):
    R=load_kernel(repo_root)
    H=((0,2,4),(1,3,5),(6,8,10),(7,9,11),(0,6,8))
    irregular={p:tuple(h for h in H if p in h) for p in R.PORTS}
    default={p:R.triples_at(p) for p in R.PORTS}
    cells=(R.ZERO,R.advance(R.ZERO,0))
    cases=[('both_irregular',{0:irregular,1:irregular}),
           ('only_first_irregular',{0:irregular,1:default}),
           ('only_second_irregular',{0:default,1:irregular})]
    summary=[]
    traces=[]
    for name,assigned in cases:
        result=field_prefix(R,cells,assigned,depth=2)
        own=result['layers'][2]['own_return']
        lam=R.Q(1,48)
        expected=[lam**2*(12+3*result['interfaces'][s]['row_mass'][q]) for s,q in [(0,0),(1,1)]]
        assert [own[s].total for s in (0,1)]==expected
        assert result['omitted_global_total_bound']==R.Q(1,24)
        encoded=json.dumps(R.to_json(result),sort_keys=True,separators=(',',':')).encode()
        summary.append({'case':name,'leaf_counts':[L['leaf_count'] for L in result['layers']],
                        'source_labelled_own_returns':R.to_json(own),'expected_totals':R.to_json(expected),
                        'full_trace_sha256':hashlib.sha256(encoded).hexdigest(),
                        'full_trace_utf8_bytes':len(encoded),
                        'first_row_mass':R.to_json(result['interfaces'][0]['row_mass'])})
        traces.append(R.to_json(result))
    # An input that merely reorders one triple is still a duplicate.
    rejected=0
    invalid=[dict(default),dict(default),dict(default)]
    invalid[0][0]=()
    invalid[1][0]=((0,2,4),(4,0,2))
    invalid[2][0]=((0,1,2),)
    for families in invalid:
        try: validated_families(R,families)
        except ValueError: rejected+=1
        else: raise AssertionError('invalid incidence accepted')
    try: field_prefix(R,cells,{0:irregular,1:irregular},depth=2,max_leaves=25)
    except ValueError: rejected+=1
    else: raise AssertionError('silent resource truncation')
    # Correctness of the source-row / destination-row bridge on an actual non-symmetric K.
    I=transfer_interface(R,irregular)
    assert I['K_destination_by_source'][2][0]!=I['W_source_by_destination'][2][0]
    assert I['W_source_by_destination']==tuple(zip(*I['K_destination_by_source']))
    report={'status':'EXACT_PINNED_BRC_ADAPTER_CHECKS_PASS','cases':summary,'invalid_inputs_rejected':rejected,
            'BRC_calls':dict(R.CALLS),'packet_router_blob':PACKET_BLOB,
            'brc_source_blob':R.BLOB,'adapter_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'new_theorem':False,'new_tool_family':False,'native_G1_through_G5':'UNKNOWN',
            'execution':'New targeted adapter checks; old 97/3329/25074 checks not rerun or recounted.'}
    Path(output).write_text(json.dumps(report,indent=2)+'\n')
    if full_trace:
        Path(full_trace).write_text(json.dumps(traces,sort_keys=True,separators=(',',':'))+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='cases'},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--repo-root',required=True)
    parser.add_argument('--output',default=str(Path(__file__).with_name('u2_adapter_validation.json')))
    parser.add_argument('--full-trace')
    args=parser.parse_args()
    self_test(args.repo_root,args.output,args.full_trace)
