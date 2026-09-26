"""Exact proof-observer budgets from the actual frozen-grid BRC certificate."""
import gzip,hashlib,json
from fractions import Fraction as F
from closed_phase_bank import ROOT,optimize_tail_certificate,truncated_error_certificate
from stage79.phase_compiler import encode

raw=gzip.decompress((ROOT/'bank_t34.json.gz').read_bytes());saved=json.loads(raw)
intv={int(m):{k:F(v) for k,v in r.items()} for m,r in saved['phase_intervals'].items()}
examples={t:optimize_tail_certificate(t,intv) for t in (12,34,38,40,64,100,1000,2000)}
bound=lambda t:optimize_tail_certificate(t,intv)['chosen']['telescoping_sum']
t=2
while bound(t+2)<=F(1,1000000):t+=2
n=2
while bound(2*(n+1))<=F(1,16*(n+1)):n+=1
cutoff=33;delta=F(1,1<<32)
slope=sum((intv[m]['gate_error']+4*delta for m in range(3,cutoff)),F(0))+4*intv[cutoff]['upper']
intercept=sum(((1-m)*(intv[m]['gate_error']+4*delta) for m in range(3,cutoff)),F(0))-4*cutoff*intv[cutoff]['upper']
for width in (34,40,100,1000):
    value=slope*width+intercept+F(4*intv[cutoff]['upper'],1<<(width-cutoff+1))
    assert value==truncated_error_certificate(width,intv,cutoff)['telescoping_sum']
report={'schema':'BRC_SHOR_TAIL_CUTOFF_CERTIFICATE_SELECTION_V1',
  'activity':saved['activity'],'status':'PROVED_CERTIFICATE_OPTIMIZATION_NOT_NEW_FULL_CIRCUIT_RUN',
  'bank_payload_sha256':hashlib.sha256(raw).hexdigest(),
  'examples':examples,'tolerance':F(1,1000000),'max_even_t':t,
  'at_tolerance_frontier':optimize_tail_certificate(t,intv)['chosen'],
  'next_even':optimize_tail_certificate(t+2,intv)['chosen'],
  'success_budget_condition':'E_(2n) <= 1/(16n), theorem assumptions are separate',
  'max_n_for_this_success_budget':n,'at_n':optimize_tail_certificate(2*n,intv)['chosen'],
  'next_n':optimize_tail_certificate(2*(n+1),intv)['chosen'],
  'fixed_cutoff_33_affine_part':{'slope':slope,'intercept':intercept,
    'remaining_term':'4*u33/2^(t-32), u33=2^-31, t>=33'},
  'actual_BRC_core_calls_new':0,
  'typed_reuse':'telescoping and algebraic-root monotonicity applied to actual full-word and interval certificate',
  'source_parameters_unchanged':True,'no_scientific_propagator_executed':True}
(ROOT/'tail_optimization.json').write_text(json.dumps(encode(report),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(encode({k:report[k] for k in ('max_even_t','max_n_for_this_success_budget','fixed_cutoff_33_affine_part')})))
