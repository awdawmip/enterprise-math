"""Separate q3 geometric/cost exclusions from q3 objective-dependent exclusions."""
from pathlib import Path
import argparse,hashlib,json,sys
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--baseline',type=Path,required=True);p.add_argument('--q3-proof',type=Path,required=True);p.add_argument('--plan',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();sys.path.insert(0,str(a.baseline.resolve()/'bias'));from plan_extended import catalog
q2=json.loads(a.plan.read_text())['rows'];old=json.loads((a.q3_proof/'completed_q3.json').read_text());label=lambda s:','.join(map(str,s));jobs=[];stats={'q2_profiles':len(q2),'common_profiles':0,'new_profiles':0,'same_budget_common':0,'expanded_budget_common':0,'q3_zero_emission_uniform_exclusions':0,'entire_q2_profiles_inherited':0,'only_expanded_cost_window_needed':0,'must_recheck_old_objective_band':0,'root_weight_inequalities_verified':0}
for P,E,floor,ceiling in q2:
 key=label(P)+'__'+label(E);lo=max(11301,11365 if E.count(13)==4 else 0,sum(min(catalog[s,0])for s in P)+floor);job={'key':key,'P':P,'E':E,'embedded_floor':floor,'q2_ceiling':ceiling,'minimum_cost':lo,'status':'pending'}
 if key not in old:stats['new_profiles']+=1;job['provenance']='new_q2_profile'
 else:
  stats['common_profiles']+=1;receipt=old[key];v=receipt['result'];oldceiling,oldfloor=v[:2];assert floor==oldfloor and ceiling>=oldceiling
  stats['same_budget_common'if ceiling==oldceiling else'expanded_budget_common']+=1
  root_weight=sum(min(3*c-d for c,d in catalog[s,1].items())for s in E)+3*(floor-sum(min(catalog[s,1])for s in E))+sum(min(3*c-d for c,d in catalog[s,0].items())for s in P)
  assert root_weight<=3*11292-108;stats['root_weight_inequalities_verified']+=1
  job.update({'q3_ceiling':oldceiling,'q3_search_nodes':v[3],'q3_class_emissions':v[4],'q3_root_weight':root_weight})
  if v[4]==0:
   assert v[-1]==0 and v[5]==0;stats['q3_zero_emission_uniform_exclusions']+=1;job['uniform_excluded_through']=oldceiling;job['minimum_cost']=max(lo,oldceiling+1)
   if ceiling==oldceiling:stats['entire_q2_profiles_inherited']+=1;job['status']='inherited_complete_uniform_exclusion';job['provenance']='zero proper-class emissions, root q3 weighted test passes; all failures are geometric or uniform cost'
   else:stats['only_expanded_cost_window_needed']+=1;job['provenance']='old cost window is uniformly impossible; search the expanded cost window'
  else:stats['must_recheck_old_objective_band']+=1;job['provenance']='q3 exclusion depends potentially on its stricter difference threshold; recheck the old cost window as well'
 jobs.append(job)
assert stats['common_profiles']==530 and stats['new_profiles']==245
out={'statistics':stats,'source_native_sha256':hashlib.sha256((a.baseline/'bias/weighted_native.cpp').read_bytes()).hexdigest(),'criterion':'If the q3 root weighted lower bound passes and the completed search has zero emitted proper classes, no weighted recursive call occurs. All failed branches are pure geometry, legality or uniform cost. Thus its full old cost window can be inherited independently of the action-bias objective.','caution':'q3 found=0, even with the same cost budget, is otherwise insufficient for a q2 exclusion; the two difference thresholds differ.','jobs':jobs}
a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(stats,indent=2),flush=True)
