"""Low-memory geometric profile envelope; q2 outputs are plans, not exclusions."""
from pathlib import Path
from itertools import product
import argparse,hashlib,json,subprocess,sys,time
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--baseline',type=Path,required=True);p.add_argument('--q3-proof',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--cap',type=int,default=11793);a=p.parse_args();h=Path(__file__).resolve().parent;out=a.output.resolve();out.mkdir(parents=True,exist_ok=True);sys.path.insert(0,str(a.baseline.resolve()/'bias'))
from plan_extended import catalog,minimum,partitions,mod,checksum
cap=a.cap;rows=[];start=time.time()
for sizes in partitions(125,11):
 full=sizes.count(13)
 if full>=5 or sum(min(minimum.get((s,e),10000)for e in (0,1))for s in sizes)>cap:continue
 levels=sorted(set(sizes));choices=[(0,)if s in (1,13)else range(sizes.count(s)+1)for s in levels]
 for counts in product(*choices):
  P=tuple(s for s,n in zip(levels,counts)for _ in range(n));E=tuple(s for s,n in zip(levels,counts)for _ in range(sizes.count(s)-n))
  if len(P)<4 or (len(P)==4 and sum(P)<42):continue
  if any(sum(E[-k:])>mod.bias.MOTHER_UNIONS[k]for k in range(1,len(E)+1)):continue
  large=E.count(12)+full
  if large>6:continue
  slots=[(s,0)for s in P]+[(s,1)for s in E]
  if large==6:slots[slots.index((12,1))]=(12,2)
  floor=sum(minimum[x]for x in slots);first=max(floor,11301,11365 if full==4 else 0)
  if first>cap:continue
  embedded_floor=sum(minimum[s,1]for s in E)+12*max(large-5,0)
  rows.append({'P':P,'E':E,'floor':floor,'embedded_floor':embedded_floor,'first':first,'slots':[3*s+e for s,e in sorted(slots,reverse=True)]})
text=f'{len(catalog)} {len(rows)} {cap}\n'
for (s,e),values in sorted(catalog.items()):text+=f'{3*s+e} {minimum[s,e]} {len(values)}\n'+''.join(f'{c} {d}\n'for c,d in sorted(values.items()))
for row in rows:text+=str(row['floor'])+' '+str(row['first'])+' '+' '.join(map(str,row['slots']))+'\n'
fi=out/'input.txt';fi.write_text(text);exe=out/'trie_envelope';subprocess.run(['c++','-std=c++20','-O3',str(h/'trie_envelope.cpp'),'-o',str(exe)],check=True);run=subprocess.run([str(exe),str(fi)],capture_output=True,text=True,check=True)
risks={2:[],3:[]};boundary=[];seen=set();bounds={}
for line in run.stdout.splitlines():
 tag,*vals=line.split();v=list(map(int,vals))
 if tag=='profile':
  i,q2,q3=v;assert i not in seen;seen.add(i);row=rows[i]
  for q,c in [(2,q2),(3,q3)]:
   if c>=0:risks[q].append([row['P'],row['E'],row['embedded_floor'],c])
 elif tag=='bound':c,d,i=v;bounds[c]=d
 elif tag=='boundary':i,d=v;boundary.append({'profile':rows[i],'spectrum_upper_A':d})
 else:raise AssertionError(tag)
assert seen==set(range(len(rows)))
canon=lambda xs:sorted(json.dumps(x,separators=(',',':'))for x in xs)
old=json.loads((a.q3_proof/'profiles_q3.json').read_text())['rows'];assert cap>=11793 and canon(risks[3])==canon(old)
assert len(boundary)==1 and list(boundary[0]['profile']['P'])==[9,10,10,11,11,11,11] and list(boundary[0]['profile']['E'])==[13]*4
failed=[]
for P,E,f,c in risks[2]:
 if not(13*(len(E)-1)<sum(E)and sum(E[:2])>13 and min(P)>mod.bias.MOTHER_UNIONS[len(E)]-sum(E)):failed.append([P,E,f,c])
result={'cost_cap':cap,'geometric_profiles':len(rows),'single_class_catalog_sha256':checksum,'input_sha256':hashlib.sha256(text.encode()).hexdigest(),'q3_exact_match_profiles':len(risks[3]),'q3_exact_match_to_completed_plan':True,'q2_risk_profiles_within_this_cap':len(risks[2]),'q2_plan_complete':cap>=12043,'q2_geometric_exclusions_completed':False,'q2_native_precondition_failures':failed,'boundary_profiles_at_C11594_A_at_least_1012':boundary,'engine_statistics':run.stderr.strip(),'elapsed_seconds':time.time()-start,'scope':'All feasible P/E profiles within this cost cap under inherited unconditional geometry; scalar difference upper bounds only. No search exclusion is inferred from the q2 plan.'}
(out/'summary.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');(out/'profiles_q2.json').write_text(json.dumps({'q':2,'cap':cap,'rows':risks[2]},indent=2)+'\n');(out/'difference_by_cost.json').write_text(json.dumps(bounds,indent=2,sort_keys=True)+'\n');print(json.dumps(result,indent=2),flush=True)
