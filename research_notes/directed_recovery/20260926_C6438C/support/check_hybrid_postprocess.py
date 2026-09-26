"""Actual typed-BRC checks of the explicit after-readout enhancement."""
from copy import deepcopy
from pathlib import Path
import gzip,hashlib,json
from hybrid_postprocess import hybrid_classical_postprocess,verify_hybrid_postprocess,modular_source_certificates
from sparse_modular import sparse_classical_postprocess,digest
from stage45.brc_loop_recheck import verify_vendor,CALLS

ROOT=Path(__file__).resolve().parent

def main():
    vendor=verify_vendor();CALLS.clear();cases=[];source_certificates={}
    fixtures=[(15,2,8,0,[3,5]),(21,2,10,0,[3,7]),(35,2,12,0,[5,7]),
      (15,14,8,0,[]),(9,2,8,0,[]),(7,3,6,0,[]),
      (15,2,4,4,[3,5]),(21,2,6,1,[3,7])]
    for N,a,t,k,expected in fixtures:
        result=hybrid_classical_postprocess(N,a,t,k)
        primary=sparse_classical_postprocess(N,a,t,k)
        assert result['primary_postprocessing']==primary
        assert result['factors']==expected
        assert result['hybrid']['minimal_order_claimed'] is False
        if primary['factors']:
            assert all(result[key]==value for key,value in primary.items())
            assert result['factor_source']=='ORIGINAL_CF' and not result['hybrid']['attempts']
        elif expected:
            assert result['factor_source']=='LOW_ODD_PART_RETURNING_EXPONENT_FALLBACK'
            assert result['hybrid']['attempts'] and result['minimal_order_claimed'] is False
        else:
            assert result['status']==primary['status']
            assert result['hybrid']['coverage_complete'] and result['hybrid']['status']=='CANDIDATES_EXHAUSTED_NO_FACTOR'
        if k==0:assert primary['status']=='ZERO_PHASE_RETRY' and result['hybrid']['attempts']
        replay=verify_hybrid_postprocess(result)
        source_certificates.update(modular_source_certificates(result))
        cases.append({'N':N,'a':a,'t':t,'k':k,'result':result,'replay':replay})
        print(json.dumps({'N':N,'a':a,'t':t,'k':k,'factors':result['factors'],
          'source':result['factor_source'],'candidate_attempts':len(result['hybrid']['attempts']),
          'coverage_complete':result['hybrid']['coverage_complete']}),flush=True)
    rejected=[]
    def mutation(label,change):
        specimen=deepcopy(cases[0]['result']);change(specimen)
        try:verify_hybrid_postprocess(specimen)
        except ValueError:rejected.append(label)
        else:raise AssertionError('corrupted hybrid record accepted: '+label)
    mutation('wrong_factor',lambda r:r['factors'].__setitem__(0,2))
    mutation('deleted_primary_zero_reason',lambda r:r['primary_postprocessing'].__setitem__('status','OMITTED'))
    mutation('false_minimal_order',lambda r:r['hybrid'].__setitem__('minimal_order_claimed',True))
    mutation('missing_candidate',lambda r:r['hybrid']['attempts'].pop(0))
    mutation('truncated_candidate_scope',lambda r:r['hybrid']['candidate_contract'].__setitem__('odd_part_max',31))
    for label,args in [('nonunit_base',(15,3,8,0)),('invalid_readout',(15,2,8,256)),
      ('odd_control_width',(15,2,7,0)),('boolean_input',(True,2,8,0))]:
        try:hybrid_classical_postprocess(*args)
        except ValueError:rejected.append(label)
        else:raise AssertionError('invalid public input accepted: '+label)
    payload={'schema':'BRC_HYBRID_POSTPROCESS_CHECKS_V1',
      'researcher':'EM-DIRECT-C6438C','activity':'RA-CAAAC604CB513AEA8BBC1DFC',
      'status':'AUTHOR_EXECUTED_SHARED_CONTEXT_UNREVIEWED_NOT_ADMITTED',
      'vendor':vendor,'cases':cases,'modular_source_certificates':source_certificates,
      'negative_controls':rejected,'actual_BRC_calls':CALLS,
      'scope':'declared completed-readout arithmetic fixtures; not sampled output frequencies or ideal reference',
      'algorithm_change':'original CF followed after failure by public even low-odd-part exponent candidates'}
    data=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
    (ROOT/'HYBRID_POSTPROCESS_RESULTS.json.gz').write_bytes(gzip.compress(data,mtime=0))
    brief={key:value for key,value in payload.items() if key not in ('cases','modular_source_certificates','actual_BRC_calls')}
    brief.update(full_payload_sha256=hashlib.sha256(data).hexdigest(),full_payload_bytes=len(data),
      actual_BRC_call_count=len(CALLS),modular_source_certificate_count=len(source_certificates),
      cases=[{'N':r['N'],'a':r['a'],'t':r['t'],'k':r['k'],'factors':r['result']['factors'],
        'factor_source':r['result']['factor_source'],'primary_status':r['result']['primary_postprocessing']['status'],
        'fallback_status':r['result']['hybrid']['status'],'candidate_attempts':len(r['result']['hybrid']['attempts']),
        'coverage_complete':r['result']['hybrid']['coverage_complete'],'replay':r['replay']} for r in cases])
    (ROOT/'HYBRID_POSTPROCESS_SUMMARY.json').write_text(json.dumps(brief,indent=2)+'\n',encoding='utf-8')
    manifest={}
    for name in ('hybrid_postprocess.py','check_hybrid_postprocess.py','HYBRID_POSTPROCESS_NOTE.md',
      'HYBRID_POSTPROCESS_RESULTS.json.gz','HYBRID_POSTPROCESS_SUMMARY.json'):
        path=ROOT/name
        if path.exists():
            raw=path.read_bytes();manifest[name]={'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
              'git_blob':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()}
    (ROOT/'HYBRID_POSTPROCESS_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'completed_cases':len(cases),'negative_controls':len(rejected),
      'native_calls':len(CALLS),'full_trace_bytes':len(data),'modular_certificates':len(source_certificates)}),flush=True)

if __name__=='__main__':main()
