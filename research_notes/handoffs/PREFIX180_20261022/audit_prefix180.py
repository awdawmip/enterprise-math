"""Exact author-side audit of PREFIX-180 full two-solver census and symmetry orbit."""
from pathlib import Path
from itertools import combinations
from hashlib import sha256
from collections import Counter
import contextlib, importlib.util, io, json, re
H=Path(__file__).resolve().parent
p=H/'REFERENCE_PREFIX179/EM_PREFIX179_HANDOFF_20261022/audit_prefix179.py'
spec=importlib.util.spec_from_file_location('prefix179_certified_source',p)
a=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(a)
prior=a.combined
assert len(prior)==2061662
ref=a.a.a.a
assert len(ref.maps)==4
Q0={0,1,2,3,4,51,64,71,74};D={1,2,64}; O=sorted(set(range(84))-Q0)
F='distance3_remove1264_180.bin'; raw=(H/F).read_bytes()
assert len(raw)==67525*27
pat=re.compile(re.escape(F)+r' row=(\d+) Q=([0-9,]+) base_uncovered=(\d+) K=(\d+) answer=(YES|NO|UNKNOWN) nodes=(\d+) W=(.*)')
c=Counter(); nodes=0; minnodes=10**9; maxnodes=0; lo=10**9; hi=0
with (H/'primary_180.log').open() as f:
 for i,add in enumerate(combinations(O,3)):
  q=tuple(sorted((Q0-D)|set(add)))
  r=raw[i*27:(i+1)*27]
  assert tuple(r[:9])==q and r[9:]==bytes(18),(i,'input')
  line=f.readline().rstrip('\n'); match=pat.fullmatch(line)
  assert match,(i,line)
  j,ids,bu,k,answer,n,w=match.groups()
  assert int(j)==i and tuple(map(int,ids.strip(',').split(',')))==q and int(k)==11
  assert answer=='NO' and w==''
  n=int(n);bu=int(bu)
  assert 0<n<=200000
  c[answer]+=1;nodes+=n;minnodes=min(minnodes,n);maxnodes=max(maxnodes,n);lo=min(lo,bu);hi=max(hi,bu)
 assert f.readline()==''
assert c=={'NO':67525}
second=(H/'second_180.log').read_text().strip()
sm=re.fullmatch(r'INDEPENDENT_PREFIX178_DONE rows=(\d+) feasible11=(\d+) impossible11=(\d+) total_nodes=(\d+) max_nodes=(\d+) distinctQ=(\d+)',second)
assert sm,second
n,yes,no,second_nodes,second_max,distinct=map(int,sm.groups())
assert n==no==distinct==67525 and yes==0
for fn in ['primary_time_180.txt','second_time_180.txt']:
 assert 'exit=0' in (H/fn).read_text()
orbits=[ref.fam(D,mp) for mp in ref.maps]
orbit=set.union(*orbits)
inter=orbit&prior
joint=prior|orbit
pairwise={f'{i}-{j}':len(orbits[i]&orbits[j]) for i,j in combinations(range(4),2)}
S=ref.R+[ref.X3[j]for j in sorted(Q0)]+[ref.X4[j]for j in [0,4,8,10,11,14,19,22,25,26,29,34]]
assert len(set(S))==len(S)==66
sums={tuple(x[j]+y[j]for j in range(4))for i,x in enumerate(S)for y in S[i:]}
assert sums==set(ref.T) and len(sums)==969
report={
 'schema':'EM_PREFIX180_AUTHOR_CHECKED_FINITE_CENSUS_V1',
 'date':'2026-10-22','global_knowledge_main':'4a635ff6dd2f430d2fe18ab45d78e321b28b42c6',
 'enterprise_math_main':'dd31d08d4aeed7c69db45fad7438dcc55a311318',
 'model':'BOOLEAN_BRC_AUXILIARY_FOUR_INTEGER_COORDINATES_NOT_P000_NATIVE_X6',
 'question':'Does a size <= 11 X4 completion exist for D={1,2,64} replaced by any outside 3-subset?',
 'Q0':sorted(Q0),'deletion':sorted(D),'R_size':45,'Q_size':9,'required_W_lower_bound':12,
 'input_rows':n,'input_bytes':len(raw),'input_sha256':sha256(raw).hexdigest(),
 'primary':{'YES':0,'NO':c['NO'],'UNKNOWN':0,'nodes_total':nodes,'min_nodes':minnodes,'max_nodes':maxnodes,'base_uncovered_range':[lo,hi],'exit_code':0,'log_sha256':sha256((H/'primary_180.log').read_bytes()).hexdigest()},
 'second':{'YES':yes,'NO':no,'nodes_total':second_nodes,'max_nodes':second_max,'exit_code':0,'log_sha256':sha256((H/'second_180.log').read_bytes()).hexdigest()},
 'symmetry':{'group_order':4,'orbit_size':len(orbit),'pairwise_intersections':pairwise,'old_union':len(prior),'overlap':len(inter),'new_configurations':len(orbit)-len(inter),'new_union':len(joint)},
 'witness':{'Q0':sorted(Q0),'W0':[0,4,8,10,11,14,19,22,25,26,29,34],'S_size':66,'targets':969},
 'scope':'AUTHOR_CHECKED_COMPUTER_ASSISTED_FINITE_PROOF; global beta_4(8) lower bound NOT proved; per-Q exact 66 NOT proved; P000 native six-axis/slice lift NOT proved',
 'BRC':'Boolean support only; no multiplicity, weight, path or phase preservation',
 'authority':'Owner/CLAIM unknown; actual gateway em_control_tasks CONTROL_QUOTA; Gateway status research_authority_granted=false; remote Source admission not asserted.'
}
(H/'CERTIFICATE_PREFIX180.json').write_text(json.dumps(report,ensure_ascii=False,indent=2,sort_keys=True)+'\n')
print('PREFIX180_FULL_AUTHOR_FINITE_AUDIT_PASS')
print(json.dumps({'primary':report['primary'],'second':report['second'],'symmetry':report['symmetry'],'witness':report['witness']},ensure_ascii=False,indent=2))
