"""Python audit of complete K<=12 census on the support-viable rows."""
from pathlib import Path
from itertools import combinations_with_replacement
from hashlib import sha256
import re,json
H=Path(__file__).resolve().parent
b=(H/'eligible_no_support_obstruction_180.bin').read_bytes()
original=(H/'distance3_remove1264_180.bin').read_bytes()
row_ids=list(map(int,(H/'eligible_original_row_numbers_180.txt').read_text().splitlines()))
assert len(b)==646*27 and len(row_ids)==646
for i,ori in enumerate(row_ids):
 assert b[27*i:27*i+27] == original[27*ori:27*ori+27]
P=re.compile(r'eligible_no_support_obstruction_180\.bin row=(\d+) Q=([0-9,]+) base_uncovered=(\d+) K=(\d+) answer=(YES|NO|UNKNOWN) nodes=(\d+) W=(.*)')
counts={'YES':0,'NO':0,'UNKNOWN':0}; solutions=[]; nodes=0; maxnodes=0
with (H/'eligible_k12_results_180.log').open() as f:
 for i in range(646):
  s=f.readline().rstrip('\n');m=P.fullmatch(s)
  assert m,(i,s)
  j,q,uncovered,K,ans,n,w=m.groups()
  assert int(j)==i and int(K)==12 and int(n)>0 and int(n)<=200000
  q_ids=tuple(map(int,q.strip(',').split(',')))
  assert tuple(b[27*i:27*i+9])==q_ids
  counts[ans]+=1; nodes+=int(n);maxnodes=max(maxnodes,int(n))
  if ans=='YES':
   w_ids=tuple(map(int,w.strip(',').split(',')))
   assert len(w_ids)==len(set(w_ids))==12 and len(q_ids)==9
   solutions.append({'eligible_row':i,'original_row':row_ids[i],'Q':list(q_ids),'W':list(w_ids),'nodes':int(n)})
 assert f.readline()==''
assert counts=={'YES':1,'NO':645,'UNKNOWN':0}
second=(H/'independent_k12_180.log').read_text().splitlines()
assert len(second)==2 and second[0].startswith('YES Qindex=439 W=')
assert second[1].startswith('INDEPENDENT_PREFIX178_DONE rows=646 feasible12=1 impossible12=645 ')
assert solutions[0]['eligible_row']==439 and solutions[0]['original_row']==62090
assert ','.join(map(str,solutions[0]['W'])) in second[0]
assert 'exit=0' in (H/'eligible_k12_time_180.txt').read_text()
assert 'exit=0' in (H/'independent_k12_time_180.txt').read_text()
# independent exact Python integer lattice/witness computation
simplex=lambda n:[(a,b,c,n-a-b-c)for a in range(n+1)for b in range(n-a+1)for c in range(n-a-b+1)]
sup=lambda x:sum(bool(a)for a in x)
X=simplex(8);T=set(simplex(16));R=[x for x in X if sup(x)<=2 and x!=(4,4,0,0)];X3=[x for x in X if sup(x)==3];X4=[x for x in X if sup(x)==4]
q=solutions[0]['Q'];w=solutions[0]['W'];S=R+[X3[j] for j in q]+[X4[j] for j in w]
assert len(S)==66 and len(set(S))==66
S2={tuple(x[k]+y[k] for k in range(4)) for x,y in combinations_with_replacement(S,2)}
assert len(S2)==len(T)==969 and S2==T
report={'schema':'EM_PREFIX180_EXACT_K12_CLASSIFICATION_V1','eligible_source_count':646,'source_total':67525,
 'primary':{'YES':1,'NO':645,'UNKNOWN':0,'nodes_total':nodes,'max_nodes':maxnodes,'exit_code':0,'log_sha256':sha256((H/'eligible_k12_results_180.log').read_bytes()).hexdigest()},
 'second':{'YES':1,'NO':645,'exit_code':0,'log_sha256':sha256((H/'independent_k12_180.log').read_bytes()).hexdigest()},
 'unique_Q_achieving_66_states_in_new_direct_family':solutions[0],
 'positive_witness':{'state_count':66,'target_count':969,'exact_sumset_equality':True},
 'quantifier_warning':'Unique nine-source Q in this direct 67525 family admitting <=12 W, not a claim that W witness is unique.',
 'theorem':'66879 impossible even with full X4; remaining 646 are completable using full X4; 645 require >=13 W, exactly one Q has min W=12.'}
(H/'EXACT_K12_CERTIFICATE_PREFIX180.json').write_text(json.dumps(report,sort_keys=True,ensure_ascii=False,indent=2)+'\n')
print('PREFIX180_K12_UNIQUENESS_AND_NEW_WITNESS_PASS')
print(json.dumps(report,ensure_ascii=False,indent=2))
