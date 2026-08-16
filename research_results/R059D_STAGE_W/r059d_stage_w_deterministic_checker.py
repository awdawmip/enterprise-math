#!/usr/bin/env python3
from pathlib import Path
import json,itertools,re,hashlib
R=Path(__file__).resolve().parent
RID='EM-R059D-9C6B2A';TASK='ce0c98cb2e729d8773443b1f3ebdf8fb4328365b';PAR='a9929a5bd666e621cb1bd77adb464df0d35db399'
C=[]
def ck(n,x):
 C.append(n)
 if not x: raise AssertionError(n)
def L(n): return json.loads((R/n).read_text())
D={'+u':(1,0,0),'-u':(-1,0,0),'+v':(0,1,0),'-v':(0,-1,0),'+w':(0,0,1),'-w':(0,0,-1)}
S={'+u':(1,-1,-1),'-u':(-1,1,1),'+v':(-1,1,-1),'-v':(1,-1,1),'+w':(-1,-1,1),'-w':(1,1,-1)}
ORDER=list(D)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def co(p): a,b,c=p; return (a-b-c,-a+b-c,-a-b+c)
def parse(w): return re.findall(r'[+-][uvw]',w)
def evalw(w):
 i=(0,0,0);q=(0,0,0)
 for d in parse(w): i=add(i,D[d]);q=add(q,S[d])
 return i,q
req=['INTEGER_CELL_COORDINATE_PROTOCOL','ORIGIN_FIRST_SHELL_ATLAS','RADIUS2_CELL_ATLAS','RADIUS3_CELL_ATLAS','MULTI_PATH_COORDINATE_CONSISTENCY','ROOT_ORDER_CANDIDATE_REGISTRY','ROOT_PRECOLLAPSE_TABLE','COLLAPSE_BRANCH_CONSISTENCY_LEDGER','FIVE_TO_FOUR_OR_NINE_CONTROL','MODEL_REJECTION_LEDGER','SIMPLE_RULE_EXTRACTION','TRIVIALITY_LEAKAGE_LEDGER']
for x in req:
 o=L('R059D_STAGE_W_'+x+'.json'); ck('meta-'+x,o['researcher_id']==RID and o['taskbook_source']==TASK and o['frozen_parent']==PAR)
p=L('R059D_STAGE_W_INTEGER_CELL_COORDINATE_PROTOCOL.json');ck('integer-only',p['cell_coordinate_semantics']['CELL_COORDINATES_ARE_INTEGER_ONLY'] is True)
f=L('R059D_STAGE_W_ORIGIN_FIRST_SHELL_ATLAS.json');ck('shell1-counts',f['shell_counts']=={'0':1,'1':6});ck('u1',f['first_step_control_check']['+u']==[1,-1,-1])
for rad,count,shells in [(2,25,{'0':1,'1':6,'2':18}),(3,63,{'0':1,'1':6,'2':18,'3':38})]:
 a=L(f'R059D_STAGE_W_RADIUS{rad}_CELL_ATLAS.json');ck(f'r{rad}-count',a['cell_count']==count);ck(f'r{rad}-shells',a['shell_counts']==shells)
 seen={}
 for row in a['rows']:
  cell,idx,sh,q,short,nonshort,neigh=row;idx=tuple(idx);q=tuple(q)
  ck(f'int-{rad}-{cell}',all(isinstance(x,int) for x in q));ck(f'coord-{rad}-{cell}',q==co(idx));ck(f'shell-{rad}-{cell}',sh==sum(abs(x) for x in idx));ck(f'neighn-{rad}-{cell}',len(neigh)==6)
  ck(f'inj-{rad}-{cell}',q not in seen or seen[q]==cell);seen[q]=cell
  for w in short+nonshort:
   ii,qq=evalw(w);ck(f'pathidx-{rad}-{cell}-{w}',ii==idx);ck(f'pathcoord-{rad}-{cell}-{w}',qq==q)
 ck(f'distinct-{rad}',len(seen)==count)
m=L('R059D_STAGE_W_MULTI_PATH_COORDINATE_CONSISTENCY.json');ck('det',m['determinant']==-4);ck('inject63',m['radius3_coordinate_injectivity']['pass'] and m['radius3_coordinate_injectivity']['distinct_coordinates']==63);ck('inverse',m['inverse_transition_checks']==378)
t=L('R059D_STAGE_W_ROOT_PRECOLLAPSE_TABLE.json')
for ps,rows in t['p_tables'].items():
 p=int(ps);ck(f'rootrows-{p}',len(rows)==37)
 for n,alg,lo,hi,perf in rows:
  k=0
  while (k+1)**p<=n:k+=1
  ck(f'rootlo-{p}-{n}',lo==k);ck(f'rootperf-{p}-{n}',perf==(k**p==n));ck(f'roothi-{p}-{n}',hi==(k if perf else k+1))
b=L('R059D_STAGE_W_COLLAPSE_BRANCH_CONSISTENCY_LEDGER.json')
for row in b['ledger']:
 p=row['p'];n=row['n'];cl=row['classification']
 if p==1: ck(f'p1-{n}',cl=='EXACT_MATCH')
 elif n==2: ck(f'pn2-{p}',cl=='FORCED_UPPER_BY_ATLAS')
 elif n==3: ck(f'pn3-{p}',cl=='NEITHER_SELF_CONSISTENT')
r=L('R059D_STAGE_W_MODEL_REJECTION_LEDGER.json');ck('sqrt-reject',r['square_root']=='SQUARE_ROOT_PRECOLLAPSE_REJECTED');ck('p1-only',r['root_models'][0]['classification']=='UNIQUE_SURVIVOR_WITHIN_TESTED_ROOT_ORDER_REGISTRY_AND_RADIUS3');ck('offaxis',r['off_axis_control_used'].startswith('C[1,1,0]'))
five=L('R059D_STAGE_W_FIVE_TO_FOUR_OR_NINE_CONTROL.json');ck('five-gate',five['status']=='INAPPLICABLE_AFTER_EARLY_MODEL_REJECTION' and not five['five_to_four_forced'] and not five['five_to_nine_forced'])
s=L('R059D_STAGE_W_SIMPLE_RULE_EXTRACTION.json');ck('simple-det',s['matrix_determinant']==-4);ck('no-universal',s['universal_brc_law']=='NOT_ESTABLISHED')
q=L('R059D_STAGE_W_TRIVIALITY_LEAKAGE_LEDGER.json');ck('parent',q['status']=='PASS' and q['gates']['stage_u_and_earlier_immutable']=='PASS_BY_GITHUB_COMPARE_PRE_MANIFEST')
for k,v in q['gates'].items():
 if k not in ('CELL_COORDINATES_ARE_INTEGER_ONLY','stage_u_and_earlier_immutable'): ck('fw-'+k,v is False)
dig=hashlib.sha256('\n'.join(C).encode()).hexdigest()
out={'schema':'R059D_STAGE_W_DETERMINISTIC_CHECKER_OUTPUT_V1','status':'PASS','researcher_id':RID,'taskbook_source':TASK,'frozen_parent':PAR,'checks_total':len(C),'checks_passed':len(C),'checks_failed':0,'checks_digest_sha256':dig,'parent_immutability':'PASS_BY_GITHUB_COMPARE_PRE_MANIFEST','methods':{'proof_core':'exact integer adjacency atlas, determinant injectivity, exact path evaluation, integer-power interval comparisons','enumeration':'finite radius-3 cell/path and p=1..6,n=0..36 oracle only'}}
(R/'R059D_STAGE_W_DETERMINISTIC_CHECKER_OUTPUT.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
print(json.dumps(out,indent=2))
