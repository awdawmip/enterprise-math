#!/usr/bin/env python3
"""EC49FOP 341-way exact finite native observer classifier.
Place the source export EC49FOP_2KEY_PROFILES_ALL.csv alongside this program.
Produces EC49FOP_341_PAIRS.csv and EC49FOP_341_RESULTS.json.
"""
import csv,itertools,json
E={5:(5,7),7:(6,7),13:(6,7),15:(3,5,7),17:(3,6,7),19:(3,5,7),21:(3,6,7)}
R=(3,5,6,7);D={};meta={}
with open('EC49FOP_2KEY_PROFILES_ALL.csv',newline='') as fh:
 for row in csv.DictReader(fh):
  e=tuple(int(row[x]) for x in ('out1','out2','in1','in2'))
  r=int(row['root']);m=int(row['subset']);c=int(row['cost'])
  must=int(row['must']);opt=int(row['opt'])
  if(e,r) in meta:assert meta[e,r]==(must,opt)
  else:meta[e,r]=(must,opt)
  d=D.setdefault((e,r),{})
  assert m not in d
  d[m]=c
base=(-1,-1,-1,-1)
assert len(D)==342*4
for e,r in D:
 assert meta[e,r]==meta[base,r]
 assert D[e,r].keys()==D[base,r].keys()
legal=[]
for cc in itertools.product(*E.values()):
 masks={r:0 for r in R}
 for l,r in zip(E,cc):masks[r]|=1<<l
 legal.append(masks)
assert len(legal)==648
result=[]
for e in sorted({x for x,r in D if x!=base}):
 diff={r:sum(D[e,r][m]!=D[base,r][m] for m in D[base,r]) for r in R}
 delta=[sum(D[e,r][m[r]]-D[base,r][m[r]] for r in R) for m in legal]
 canc=sum(d==0 and any(D[e,r][m[r]]!=D[base,r][m[r]] for r in R) for d,m in zip(delta,legal))
 result.append(dict(out1=e[0],out2=e[1],in1=e[2],in2=e[3],
                    changed_03=diff[3],changed_05=diff[5],
                    changed_06=diff[6],changed_07=diff[7],
                    changed_terminals=sum(d!=0 for d in delta),
                    min_delta=min(delta),max_delta=max(delta),
                    compensated_assignments=canc))
assert len(result)==341
out={'schema':'EC49FOP_341_EXACT_V1',
 'swaps':len(result),'common_domain':len(result),
 'root_entries':341*168,'terminal_observations':341*648,
 'terminal_equal':sum(x['changed_terminals']==0 for x in result),
 'profiles_equal':sum(sum(x['changed_'+str(r).zfill(2)] for r in R)==0 for x in result),
 'terminal_equal_profile_changed':sum(x['changed_terminals']==0 and sum(x['changed_'+str(r).zfill(2)] for r in R)>0 for x in result),
 'different_terminal':sum(x['changed_terminals']>0 for x in result),
 'local_cancel_swaps':sum(x['compensated_assignments']>0 for x in result),
 'local_cancel_assignments':sum(x['compensated_assignments'] for x in result),
 'total_changed_terminal_assignments':sum(x['changed_terminals'] for x in result),
 'nonempty_root_changes':sum(any(x['changed_'+str(r).zfill(2)] for r in R) for x in result),
 'first_local_cancel':next((x for x in result if x['compensated_assignments']),None),
 'max_local_cancel':max(result,key=lambda x:x['compensated_assignments']),
 'first_equal_but_nonzero_profile':next((x for x in result if x['changed_terminals']==0 and sum(x['changed_'+str(r).zfill(2)] for r in R)>0),None),
 'by_removed':{','.join(map(str,part)):sum((x['out1'],x['out2'])==part for x in result) for part in sorted(set((x['out1'],x['out2']) for x in result))},
 'review':'NOT_REVIEWED'}
assert (out['terminal_equal'],out['different_terminal'],out['local_cancel_swaps'],out['local_cancel_assignments'],out['total_changed_terminal_assignments'])==(0,341,99,4728,204300)
with open('EC49FOP_341_RESULTS.json','w') as fh:json.dump(out,fh,indent=2);fh.write('\n')
with open('EC49FOP_341_PAIRS.csv','w',newline='') as fh:
 w=csv.DictWriter(fh,fieldnames=list(result[0]));w.writeheader();w.writerows(result)
print(json.dumps(out,indent=2))
