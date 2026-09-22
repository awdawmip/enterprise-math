"""Non-author exact consumption of all other order-one proof trees."""
import contextlib,hashlib,io,json
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
 import root_certificate_review as prior
Q=prior.Q;qr=prior.qr;product=prior.product;BASE=Path(__file__).resolve().parent
raw=(BASE/'remaining_inputs.json').read_bytes();cert_raw=(BASE/'remaining_certificates.json').read_bytes()
inputs=json.loads(raw);cert=json.loads(cert_raw)
assert hashlib.sha256(raw).hexdigest()==cert['remaining_input_sha256']
assert inputs['common_input_sha256']==cert['common_input_sha256']==hashlib.sha256(prior.data_bytes).hexdigest()
assert cert['all_15_completed'] is True
input_map={int(case['residue']):case for case in inputs['cases']}
case_map={int(case['residue']):case for case in cert['cases']}
assert set(input_map)==set(case_map)==set(range(2,17)) and len(cert['cases'])==15
results=[];brc_before=prior.trace_count
for residue in range(2,17):
 p=input_map[residue];c=case_map[residue];assert c['input']==p
 vertical=17*(17+residue);mass=vertical-1;positive=2331-mass;radius=positive**2+2331**2
 assert int(p['vertical_denominator'])==vertical and int(p['vertical_mass'])==mass
 assert int(p['positive_q0_budget'])==positive and p['negative_q0_budget']=='2331'
 assert int(p['radius_squared'])==radius and all(d.above(radius) for d in prior.D)
 u=list(map(int,p['particular_q0']));x=list(map(int,p['weighted_particular']))
 assert x==[a*b for a,b in zip(u,prior.w)]
 for k in range(1,7):
  powers=[j**k for j in range(1,17)]
  coefficients=[(17+residue)**k*product(powers[:j]+powers[j+1:]) for j in range(16)]
  assert qr(sum(a*b for a,b in zip(u,coefficients))+product(powers),17**k)[1]==0
 centers=[Q(*a) for a in p['centers']]
 for i in range(16):
  assert sum(prior.M[i][k]*prior.D[k]*centers[k] for k in range(i+1)).eq(sum(a*b for a,b in zip(x,prior.B[i])))
 assert sum(prior.D[k]*centers[k]*centers[k] for k in range(16)).eq(sum(a*a for a in x))
 nodes={n['id']:n for n in c['nodes']};assert len(nodes)==len(c['nodes'])==c['node_count']
 visited=set();chosen=[0]*16;pruned=[0]
 def audit(ident,level,partial):
  assert ident not in visited;visited.add(ident);node=nodes[ident];assert node['level']==level
  center=centers[level]+sum(chosen[j]*prior.M[j][level] for j in range(level+1,16))
  recorded=Q(*node['center']);assert center.eq(recorded) and partial.eq(Q(*node['partial_before']))
  quotient,remainder=qr(recorded.n,recorded.d)
  assert [int(a['coefficient']) for a in node['options']]==[-quotient-1,-quotient]
  for option in node['options']:
   z=int(option['coefficient']);chosen[level]=z;error=center+z
   total=partial+prior.D[level]*error*error;assert total.eq(Q(*option['partial_after']))
   if total.above(radius):
    assert option['decision']=='PRUNE_EXACT_SQUARED_NORM' and 'child' not in option;pruned[0]+=1
   else:
    assert level>0 and option['decision']=='DESCEND';audit(option['child'],level-1,total)
 audit(0,15,Q());assert visited==set(nodes) and c['kernel'] is None and c['status']=='AFFINE_CLASS_EMPTY'
 results.append({'residue':residue,'nodes':len(visited),'pruned_edges':pruned[0],'status':'VERIFIED_EMPTY_RELAXED_AFFINE_CLASS'})
receipt={'schema':'T6_P17_ORDER1_NONAUTHOR_REVIEW_V1','status':'PASS_ALL_16_ORDER1_RESIDUES',
 'reviewer':'root agent; separate authoring process, source-exposed, not formal Driver acceptance',
 'common_input_sha256':hashlib.sha256(prior.data_bytes).hexdigest(),
 'remaining_inputs_sha256':hashlib.sha256(raw).hexdigest(),'remaining_certificates_sha256':hashlib.sha256(cert_raw).hexdigest(),
 'review_code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'r1_review':'ROOT_REVIEW.json','additional_cases':results,
 'total_classes':16,'total_nodes':8+sum(r['nodes'] for r in results),'total_pruned_edges':9+sum(r['pruned_edges'] for r in results),
 'additional_brc_materializations':prior.trace_count-brc_before,
 'scope':'All p17 order-one single-positive-vertical-atom relaxed residue classes; sign reversal covers a negative unique vertical atom. No order-two or full T6 conclusion.'}
(BASE/'ROOT_ORDER1_REVIEW.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(receipt))
