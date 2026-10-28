#!/usr/bin/env python3
"""Small independent exact checks for coupled cuts and U2 adapter semantics."""
from pathlib import Path
from fractions import Fraction
import hashlib, importlib.util, json, sys

ROOT=Path(__file__).resolve().parent.parent

# Independently evaluate each proved finite maximization; no completion census.
def smooth(a):
    for p in (2,3,5,7,11,13):
        while a%p==0:a//=p
    return a==1
rows=[]
expected=[('1/6',[3,4]),('1/18',[3]),('1/54',[3]),('1/162',[3]),('1/486',[3]),('1/1458',[3]),('10/147',[7]),('3/250',[5]),('1/384',[4]),('1/1536',[4]),('1/6144',[4]),('5/132',[12]),('15/3584',[8]),('1/1620',[6]),('1/9720',[6]),('910/37179',[18]),('1512/805255',[11]),('35/177147',[9]),('7315/423936',[24]),('1485/1529437',[14]),('26719875/2080374784',[32])]
for h in range(1,7):
    for k in range(7-h):
        A=((h+k+1)*(h+1)+k)//(k+1)
        assert smooth(A)
        values={}
        for a in range(2,A+1):
            if not smooth(a):continue
            v=Fraction(1,a**k*(a-1))
            for b in range(2,h+2):v*=1-Fraction(b,a)
            assert v>=0
            values[a]=v
        cap=max(values.values());args=[a for a,v in values.items() if v==cap]
        assert (str(cap),args)==expected[len(rows)]
        rows.append({'h':h,'k':k,'proved_cutoff':A,'cap':str(cap),'maximizers':args})

# Inspect a different, nonsymmetric family with three material labels.
path=ROOT/'native/u2_incidence_prefix.py'
adapter_sha=hashlib.sha256(path.read_bytes()).hexdigest()
spec=importlib.util.spec_from_file_location('review_u2',path)
module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module;spec.loader.exec_module(module)
R=module.load_kernel('/workspace/enterprise-math')
cells=(R.ZERO,R.advance(R.ZERO,0),R.advance(R.ZERO,2))
# Use the next two cyclic axes, with material-dependent signs.
families={s:{p:(tuple(sorted((p,2*((p//2+1)%6)+(s%2),2*((p//2+2)%6)+((s+1)%2)))),) for p in R.PORTS} for s in range(3)}
result=module.field_prefix(R,cells,families,depth=2,max_leaves=10000)
checked=0
for layer in result['layers']:
    for leaf in layer['leaves']:
        assert len(leaf['history'])==layer['depth']
        position=cells[leaf['source']]
        incoming=leaf['initial_input']
        for event in leaf['history']:
            assert tuple(event['from'])==position and event['incoming']==incoming
            assert tuple(event['to'])==R.advance(position,event['outgoing'])
            if position in cells:
                material=cells.index(position)
                assert event['packet_tag'] is not None
                triple=event['packet_tag'][-1]
                assert tuple(triple)==families[material][incoming][0]
                assert event['outgoing'] in triple
            else:assert event['packet_tag'] is None
            position=tuple(event['to']);incoming=event['outgoing']^1
        assert position==tuple(leaf['cell']) and incoming==leaf['incoming']
        checked+=1
    for source in range(3):
        for target,z in enumerate(cells):
            for p in R.PORTS:
                direct=sum((v['state'].total for v in layer['leaves'] if v['source']==source and v['cell']==z and v['incoming']==p),R.Q(0))
                assert direct==layer['source_material_incoming'][source][target][p].total
try:module.field_prefix(R,cells,{0:families[0],1:families[1]},depth=0)
except ValueError:pass
else:raise AssertionError('missing material silently defaulted')
report={'reviewer':'EM-REVIEW-58D6A2','status':'EXACT_TARGETED_CHECKS_PASS','t6':{'rows':rows,'completion_enumeration':False},'u2':{'adapter_sha256':adapter_sha,'materials':3,'leaf_counts':[v['leaf_count'] for v in result['layers']],'history_and_source_checked_leaves':checked,'missing_material_rejected':True,'native_G1_through_G5':'UNKNOWN'},'formal_kernel_proof':False,'old_scientific_runs_repeated':False}
Path(__file__).with_name('second_round_checks_result.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':report['status'],'t6_rows':len(rows),'u2':report['u2']},indent=2))
