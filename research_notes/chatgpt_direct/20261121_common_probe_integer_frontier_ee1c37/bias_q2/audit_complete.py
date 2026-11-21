"""Audit the complete q2 profile/frame coverage, provenance, and equality threshold."""
from pathlib import Path
import argparse,hashlib,json
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--run',type=Path,required=True);p.add_argument('--plan',type=Path,required=True);p.add_argument('--inheritance',type=Path,required=True);p.add_argument('--source',type=Path,required=True);p.add_argument('--bounds',type=Path,required=True);p.add_argument('--bound-identity',type=Path,required=True);p.add_argument('--uniform-windows',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True);hashfile=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();source=hashfile(a.source);assert source=='12035b70ca89275d7c8ff381436277c535ae44a2682456a35cfe4b892c323ad9';text=a.source.read_text();assert 'if(abs(delta)<108+biasQ*(c-11292))return false;'in text and 'if(bound>biasQ*11292-108)return false;'in text
plan=json.loads(a.plan.read_text());assert plan['q']==2 and plan['cap']==12043 and len(plan['rows'])==775
label=lambda s:','.join(map(str,s));planned={label(P)+'__'+label(E):[P,E,f,B]for P,E,f,B in plan['rows']};assert len(planned)==775
inherit=json.loads(a.inheritance.read_text());jobs={j['key']:j for j in inherit['jobs']};assert jobs.keys()==planned.keys();profiles=json.loads((a.run/'profiles.json').read_text());assert profiles.keys()==jobs.keys()
identity=json.loads((a.run/'input_identity.json').read_text());assert identity['q']==2 and identity['source_sha256']==source and identity['inheritance_sha256']==hashfile(a.inheritance)
completions={f.stem:json.loads(f.read_text())for f in(a.run/'completed').glob('*.json')};assert completions.keys()==jobs.keys()
all_chunks=[];by_profile={k:[]for k in jobs};seen=set();frame_files={};frame_catalogues={}
for path in sorted((a.run/'chunks').glob('*.json')):
 r=json.loads(path.read_text());s=r['spec'];key=s['key'];j=jobs[key];assert s['source_sha256']==source and r['returncode']==0 and r['stdout']==''
 P,E,f,B=planned[key];assert P==j['P']and E==j['E']and f==j['embedded_floor']and B==j['q2_ceiling'];assert s['embedded_floor']==f and s['minimum_cost']==j['minimum_cost']and s['maximum_cost']==B
 assert len(P)+len(E)==11 and sum(P)+sum(E)==125 and E.count(13)<=4 and all(1<=v<=13 for v in P+E)
 first,end=s['first'],s['end'];assert first<end and (key,first,end)not in seen;seen.add((key,first,end));assert path.stem==key+f'__{first}_{end}'
 counts=r['counts'];assert len(counts)==5 and counts==list(map(int,r['stderr'].split()))and counts[0]==end-first and counts[-1]==0
 frame=Path(profiles[key]['frame']);name=f'f{len(E)}_{sum(E)}'
 if name not in frame_files:
  digest=hashfile(frame);rows=[tuple(map(int,line.split()))for line in frame.read_text().splitlines()];assert rows and all(len(row)==len(E)and len(set(row))==len(E)and all(0<=i<250 for i in row)for row in rows);assert len({tuple(sorted(row))for row in rows})==len(rows)
  frame_files[name]=digest;frame_catalogues[name]={'sha256':digest,'canonical_rows':len(rows)}
 assert s['frame_sha256']==frame_files[name]==profiles[key]['frame_sha256'];assert end<=frame_catalogues[name]['canonical_rows']
 by_profile[key].append(r);all_chunks.append(r)
counts_total=[0]*5
for key,pieces in by_profile.items():
 pieces.sort(key=lambda r:r['spec']['first']);cursor=0;counts=[0]*5;ranges=[]
 for r in pieces:
  s=r['spec'];assert s['first']==cursor;cursor=s['end'];ranges.append([s['first'],s['end']]);counts=[u+v for u,v in zip(counts,r['counts'])]
 c=completions[key];assert cursor==profiles[key]['total_frames']==counts[0]and ranges==c['ranges']==profiles[key]['ranges'];assert counts==c['counts']and c['source_sha256']==source and c['complete_profile_exclusion']is True and c['job']==jobs[key]
 counts_total=[u+v for u,v in zip(counts_total,counts)]
assert len(all_chunks)==2029 and counts_total[0]==7758668 and counts_total[-1]==0
summary=json.loads((a.run/'summary.json').read_text());assert summary['complete_exclusion']is True and summary['completed_profiles']==775 and summary['completed_frame_chunks']==2029 and summary['completed_profile_frames']==counts_total[0]and summary['completed_profile_search_nodes']==counts_total[1]and not summary['witnesses']
bounds=json.loads(a.bounds.read_text());bound_id=json.loads(a.bound_identity.read_text());assert bounds['complete_bound_verification']is True and bounds['profiles']==775 and set(bounds['records'])==set(jobs);assert bound_id['same_bound_fragment']is True and bound_id['active_source_sha256']==source and bound_id['verified_source_sha256']==bounds['search_source_sha256'];assert bounds['typed_catalog_sha256']==identity['typed_catalog_sha256']
start=text.index(' // Complete single-class spectrum, typed as proper (0), embedded (1),');end=text.index(' bool assign(',start);assert hashlib.sha256(text[start:end].encode()).hexdigest()==bound_id['fragment_sha256']
for key,b in bounds['records'].items():
 assert b['verified']is True and b['q']==2 and b['total_cost_window']==[jobs[key]['minimum_cost'],jobs[key]['q2_ceiling']]and b['catalog_sha256']==identity['typed_catalog_sha256']
u=json.loads(a.uniform_windows.read_text());assert u['verified']is True and u['profiles']==13 and u['q']==0 and u['source_sha256']=='a1e464d51aaf83b276663fcb85443b7d842b7483121f38aa685f5e8e112c33ac';uniform={v['key']:v for v in u['records']};assert set(uniform)=={k for k,j in jobs.items()if 'uniform_excluded_through'in j}
for key,v in uniform.items():assert v['uniform_excluded_through']==jobs[key]['uniform_excluded_through']and v['q']==0 and v['counts'][-1]==0
result={'complete_exclusion':True,'q':2,'weighted_radius':'1/2','closed_p_interval':['1/4','3/4'],'profiles':775,'complete_frame_chunks':2029,'family_profile_placements':counts_total[0],'search_nodes':counts_total[1],'class_emissions':counts_total[2],'settlement_calls':counts_total[3],'competing_or_new_tied_tables':counts_total[4],'source_sha256':source,'input_identity':identity,'canonical_frame_catalogues':frame_catalogues,'uniform_inherited_windows_direct_q0_recheck':{'profiles':13,'frames':u['total_frames'],'nodes':u['search_nodes'],'bias_objective_disabled':True},'complete_bound_verification':{'profiles':775,'bellman_inequalities':bounds['total_bellman_inequalities'],'cost_window_queries':bounds['total_cost_window_queries']},'forced_outer_twelve_profiles':sum(sum(s>=12 for s in j['E'])==6 for j in jobs.values()),'candidate_test_includes_equality':True,'all_bound_pruning_strict':True,'outside_uniform_family_gap_probability':'(9-17*abs(2*p-1))/31250','endpoint_gap_at_least':'1/62500','unlabelled_optimal_table_count_at_center':8000,'unlabelled_optimal_table_count_at_every_other_point_in_closed_interval':4000,'maximal_stability_interval_proved':False}
(a.output/'completed_q2.json').write_text(json.dumps(completions,indent=2,sort_keys=True)+'\n');(a.output/'frame_chunks_q2.json').write_text(json.dumps(all_chunks,indent=2,sort_keys=True)+'\n');(a.output/'result_q2.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in result.items()if k not in('input_identity','canonical_frame_catalogues')},indent=2),flush=True)
