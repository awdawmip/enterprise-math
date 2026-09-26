"""Compare every original CF result field on bounded actual BRC readouts."""
from pathlib import Path
import gzip,hashlib,json
import lazy_modular as lazy
from lazy_postprocess import lazy_classical_postprocess,lazy_classical_postprocess_trace
from stage45.brc_loop_recheck import CALLS

ROOT=Path(__file__).resolve().parent
cases=[]
for N,a,t in [(15,2,4),(21,2,4),(35,2,4)]:
    for k in range(1<<t):
        old=lazy.sparse.sparse_classical_postprocess(N,a,t,k)
        new=lazy_classical_postprocess(N,a,t,k)
        assert new==old
        cases.append({'N':N,'a':a,'t':t,'k':k,'old_actual':old,'lazy_actual':new})

# A direct guard makes any accidental eager modular-table fallback visible.
def forbidden(*args,**kwargs):
    raise AssertionError('eager full-domain compiler entered lazy postprocessing')
lazy.sparse.compile_modular_permutation=forbidden
lazy.sparse.sparse_modular_columns=forbidden
guarded=lazy_classical_postprocess_trace(21,2,6,11)
assert guarded['result']['status']=='FACTORS'
zero=lazy_classical_postprocess_trace(21,2,6,0)
assert zero['result']['status']=='ZERO_PHASE_RETRY' and zero['lazy_tables']==[]
out={'status':'AUTHOR_ACTUAL_BOUNDED_SHARED_CONTEXT_NOT_ADMITTED','cases':cases,
     'all_original_result_fields_equal':True,'full_domain_fallback_guard_passed':True,
     'guarded_factor_trace':guarded,'zero_readout_trace':zero,
     'native_core_calls':CALLS,'actual_core_call_count':len(CALLS),
     'ordinary_modular_reference_used':False,'source':lazy.source_binding()}
raw=json.dumps(out,sort_keys=True,separators=(',',':')).encode()
(ROOT/'LAZY_POSTPROCESS_RESULTS.json.gz').write_bytes(gzip.compress(raw,mtime=0))
summary={k:v for k,v in out.items() if k not in ('cases','guarded_factor_trace','zero_readout_trace','native_core_calls')}
summary['compared_readouts']=len(cases)
summary['guarded_factor_result']=guarded['result']
summary['guarded_table_count']=len(guarded['lazy_tables'])
summary['guarded_requested_columns']=sum(len(x['queried_columns']) for x in guarded['lazy_tables'])
summary['payload_sha256']=hashlib.sha256(raw).hexdigest()
(ROOT/'LAZY_POSTPROCESS_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary))
