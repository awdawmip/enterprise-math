"""Bank-only bounded native checks. Run only after source review authorization."""
from copy import deepcopy
from dataclasses import FrozenInstanceError,replace
from fractions import Fraction as F
from pathlib import Path
from time import perf_counter
import gzip
import hashlib
import json
import sys
import traceback
from uuid import uuid4

ROOT=Path(__file__).resolve().parent
BASE=ROOT.parents[1]
sys.path.insert(0,str(BASE/'sep26-shor-general/optimization/collision_analysis'))
from check_gram_sampler import load_bank,LazyStreamingProgram,ExactCarrierCodec,verify_vendor
from so_trace_certificates import (SOTraceBank,TraceReplayError,CompleteNativeWord,
    strict_bytes,digest,packed,CALLS)

EXECUTION_CONTEXT={'stage':'not_started'}


def hashes():
    return {p.name:hashlib.sha256(p.read_bytes()).hexdigest()
        for p in (Path(__file__),ROOT/'so_trace_certificates.py')}


def main():
    EXECUTION_CONTEXT['stage']='validate_guard_and_output_absence'
    out=ROOT/'SO_TRACE_BANK_RESULTS.json.gz'
    if out.exists():raise ValueError('refusing to overwrite execution evidence')
    guard=json.loads((ROOT.parent/'STARTUP_GUARD.json').read_bytes())
    assert guard['activity_allowed'] and guard['persistence_allowed'] and not guard['sync_debt_events']
    source=hashes();first,start=len(CALLS),perf_counter()
    EXECUTION_CONTEXT['stage']='existing_native_bank_admission'
    vendor=verify_vendor();bank,bank_binding=load_bank()
    native_bank_admission_end=len(CALLS)
    EXECUTION_CONTEXT['stage']='complete_and_encoded_program_admission'
    encoded=LazyStreamingProgram(21,2,4,bank,61,codec=ExactCarrierCodec(61,tuple(range(6))))
    complete=LazyStreamingProgram(21,2,4,bank,61)
    programs=[encoded,complete]
    program_admission_end=len(CALLS)
    EXECUTION_CONTEXT['stage']='encoded_cold_trace_bank'
    new=SOTraceBank(encoded)
    EXECUTION_CONTEXT['stage']='complete_cold_trace_bank'
    full=SOTraceBank(complete)
    records=[]
    prior_raw=gzip.decompress((BASE/'sep27-qft-uniform/word_certificates/WORD_CERTIFICATE_RESULTS.json.gz').read_bytes())
    prior_sha=hashlib.sha256(prior_raw).hexdigest()
    assert prior_sha=='c4a88c9bd19b9ac6c3b96ac9f42f339f436a48c32fdcb6a5230d37cb3a666e44'
    prior=json.loads(prior_raw)['encoded_bank']['logical']['words']
    EXECUTION_CONTEXT['stage']='existing_word_scalar_and_inverse_checks'
    for m in (2,3,4):
        r=new.get(m);word=new.evidence()['logical']['words'][str(m)]
        assert r.bound_valid and r.bound_method=='SO_HALF_TRACE_BOUND'
        assert r.s==full.get(m).s==F(prior[str(m)]['s'])
        assert word['complete_forward_columns']==prior[str(m)]['complete_forward_columns']
        assert word['denominator']==prior[str(m)]['denominator']
        assert new.get(m,inverse=True) is r
        assert word['expression_reference_count']==122
        assert all(op['states']<=5 and op['depth']==2 for op in word['observer_operations'])
        columns=word['complete_forward_columns'];inverse=word['complete_inverse_columns']
        assert all(columns[j][i]==inverse[i][j] for i in range(61) for j in range(61))
        records.append({'m':m,'s':str(r.s),'bound_method':r.bound_method,
            'bound_is_exact':r.bound_is_exact,'full61_and_codec_s_equal':True,
            'prior_actual_rank_two_bound_equal':True,'inverse_bound_record_shared':True,
            'actual_unique_observer_expressions':word['actual_unique_observer_expressions']})
    EXECUTION_CONTEXT['stage']='warm_reuse_checks'
    before=len(CALLS)
    for _ in range(3):
        new.check(encoded)
        for m in (2,3,4):new.get(m);new.get(m,inverse=True)
    reuse={'checks':3,'lookups':18,'actual_core_calls':len(CALLS)-before,
        'host_metadata_cost_not_free':True}
    assert reuse['actual_core_calls']==0
    serialized=new.evidence()
    EXECUTION_CONTEXT['stage']='serialized_positive_restore'
    restored=SOTraceBank.restore(encoded,strict_bytes(serialized))
    assert restored.binding_sha256==new.binding_sha256
    fixtures=[]
    for name,word,expected,method,exact in (
        ('identity',(),F(0),'SO_HALF_TRACE_BOUND',True),
        ('reflection',(('neg',0),),F(4),'DET_MINUS_ONE_EXACT',True),
        ('double_quarter',(('swap',0,1),('neg',1),('swap',2,3),('neg',3)),
            F(4),'SO_HALF_TRACE_BOUND',False)):
        EXECUTION_CONTEXT['stage']='special_word:'+name
        actual=CompleteNativeWord(word,61)
        p=LazyStreamingProgram(21,2,2,{2:actual},61)
        programs.append(p);cert=SOTraceBank(p);record=cert.get(2)
        assert (record.s,record.bound_method,record.bound_is_exact)==(expected,method,exact)
        assert record.bound_valid and cert.get(2,inverse=True) is record
        fixtures.append({'case':name,'bank':cert.evidence(),
            'inverse_same_bound':True,'no_phase_target_accuracy_claim':True})
    reflection_program=programs[-2]
    reflection_evidence=fixtures[1]['bank']
    rejected=[]
    def reject(label,call,*,zero=False):
        EXECUTION_CONTEXT['stage']='negative_control:'+label
        before=len(CALLS)
        try:call()
        except (ValueError,FrozenInstanceError,AttributeError,KeyError) as error:
            evidence=deepcopy(getattr(error,'evidence',None))
            delta=len(CALLS)-before
            if zero:assert delta==0
            rejected.append({'case':label,'rejected':True,'type':type(error).__name__,
                'reason':str(error),'call_interval':[before,len(CALLS)],
                'actual_core_calls':delta,'failed_fresh_replay_evidence':evidence})
        else:raise AssertionError(label+' was accepted')
    reject('bool_phase',lambda:new.get(True),zero=True)
    reject('nonbool_inverse',lambda:new.get(2,inverse=1),zero=True)
    reject('immutable_record',lambda:setattr(new.get(3),'s',F(0)),zero=True)
    reject('immutable_bank',lambda:setattr(new,'binding_sha256','0'*64),zero=True)
    reject('wrong_codec',lambda:new.check(complete),zero=True)
    def altered_metadata():
        saved=encoded.phase_bindings['3']['all_columns_orthonormal']
        encoded.phase_bindings['3']['all_columns_orthonormal']=1
        try:new.check(encoded)
        finally:encoded.phase_bindings['3']['all_columns_orthonormal']=saved
    reject('warm_metadata_bool_to_int',altered_metadata,zero=True)
    def altered_column_type():
        gate=encoded.bank[2];cols=[list(col) for col in gate.columns]
        j,i=next((j,i) for j,col in enumerate(cols) for i,value in enumerate(col) if value==1)
        cols[j][i]=True
        encoded.bank[2]=replace(gate,columns=tuple(tuple(col) for col in cols))
        try:new.check(encoded)
        finally:encoded.bank[2]=gate
    reject('warm_column_int_to_bool',altered_column_type,zero=True)
    reject('illegal_bool_coordinate',lambda:CompleteNativeWord((('neg',True),),61),zero=True)
    reject('duplicate_gate_coordinate',lambda:CompleteNativeWord((('swap',0,0),),61),zero=True)
    detached=deepcopy(serialized);detached['logical']['words']['3']['s']='0'
    reject('unrehashed_scalar',lambda:SOTraceBank.restore(encoded,detached),zero=True)
    changes=(
        ('scalar',lambda l:l['words']['3'].update(s='0')),
        ('parity',lambda l:l['words']['3']['orientation'].update(negative_letter_parity=1)),
        ('primitive',lambda l:l['primitive_orientation']['primitive_determinants'].update(h4=-1)),
        ('trace_node',lambda l:l['words']['3']['trace_nodes'][0].update(value='7')),
        ('clipping_branch',lambda l:l['words']['3'].update(clipping_branch='UNIVERSAL_FOUR')),
        ('valid_bool_to_int',lambda l:l['words']['3'].update(bound_valid=1)),
        ('residual_column',lambda l:l['words']['3']['complete_forward_columns'][60].__setitem__(60,0)),
        ('codec_claim',lambda l:l['codec_binding'].update(encoded_dim=5)),
        ('inverse_claim',lambda l:l['words']['3'].update(inverse_uses_same_bound=False)),
        ('source',lambda l:l['source'].update(trace_bank_sha256='0'*64)),
    )
    for label,change in changes:
        bad=deepcopy(serialized);change(bad['logical']);bad['binding_sha256']=digest(bad['logical'])
        reject('rehashed_'+label,lambda:SOTraceBank.restore(encoded,bad))
    bad=deepcopy(reflection_evidence)
    bad['logical']['words']['2']['s']='2';bad['binding_sha256']=digest(bad['logical'])
    reject('reflection_false_half_trace_two',lambda:SOTraceBank.restore(reflection_program,bad))
    old=json.loads(prior_raw)['encoded_bank']
    reject('old_bank_schema',lambda:SOTraceBank.restore(encoded,old),zero=True)
    reject('duplicate_json_key',lambda:SOTraceBank.restore(encoded,'{"logical":{},"logical":{}}'),zero=True)
    EXECUTION_CONTEXT['stage']='assemble_and_write_success_evidence'
    assert hashes()==source
    payload={'schema':'BRC_SO_TRACE_BANK_BOUNDED_EXECUTION_V1','status':'PASSED',
        'source_hashes':source,'vendor':vendor,'source_bank':bank_binding,
        'initial_native_bank_admission_call_interval':[first,native_bank_admission_end],
        'initial_program_admission_call_interval':[native_bank_admission_end,program_admission_end],
        'prior_rank_two_comparison_raw_sha256':prior_sha,'records':records,
        'encoded_bank':new.evidence(),'complete_bank':full.evidence(),
        'restored_bank':restored.evidence(),'warm_reuse':reuse,'special_words':fixtures,
        'negative_controls':rejected,
        'program_admissions':[{'N':p.N,'a':p.a,'t':p.t,'phase_bindings':p.phase_bindings,
            'codec_binding':p.codec_binding,'H4_binding':p.h4_binding,
            'permutation_verifications':p.lazy_permutation_verifications,
            'factory_tables':[t.export_certificate() for t in p.lazy_factory.tables.values()]}
            for p in programs],
        'actual_core_calls':CALLS[first:],'core_call_count':len(CALLS)-first,
        'elapsed_seconds':perf_counter()-start,
        'scope':'AUTHOR_SHARED_CONTEXT_BANK_ONLY; NO_POLICY_OR_IDEAL_REFERENCE_EXECUTION'}
    raw=packed(payload);out.write_bytes(gzip.compress(raw,mtime=0))
    summary={'status':payload['status'],'source_hashes':source,'records':records,
        'special_cases':[{'case':x['case'],'s':x['bank']['logical']['words']['2']['s'],
            'method':x['bank']['logical']['words']['2']['bound_method']}
            for x in fixtures],
        'negative_controls':len(rejected),'core_call_count':payload['core_call_count'],
        'elapsed_seconds':payload['elapsed_seconds'],'warm_reuse':reuse,
        'encoded_cold_setup':{k:v for k,v in new.evidence()['setup'].items() if k!='actual_core_calls'},
        'raw_sha256':hashlib.sha256(raw).hexdigest(),'raw_bytes':len(raw),
        'gzip_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'gzip_bytes':out.stat().st_size,
        'scope':payload['scope']}
    (ROOT/'SO_TRACE_BANK_SUMMARY.json').write_bytes(packed(summary))
    print(packed(summary).decode(),flush=True)
    EXECUTION_CONTEXT['stage']='complete'


if __name__=='__main__':
    execution_first=len(CALLS)
    execution_sources=hashes()
    try:
        main()
    except BaseException as error:
        # Unexpected execution failure is a separate artifact, never a PASS.
        # Raw constructor failures need not carry TraceReplayError.evidence;
        # the complete core-call interval still survives here.
        failed={'schema':'BRC_SO_TRACE_BANK_FAILED_EXECUTION_V1','status':'FAILED',
            'source_hashes_at_start':execution_sources,'source_hashes_at_failure':hashes(),
            'known_context':dict(EXECUTION_CONTEXT),'exception_type':type(error).__name__,
            'exception_message':str(error),'traceback':traceback.format_exc(),
            'attached_exception_evidence':getattr(error,'evidence',None),
            'call_interval':[execution_first,len(CALLS)],
            'actual_core_calls':CALLS[execution_first:],'core_call_count':len(CALLS)-execution_first}
        raw=packed(failed)
        path=ROOT/('FAILED_EXECUTION_'+uuid4().hex+'.json.gz')
        with path.open('xb') as handle:handle.write(gzip.compress(raw,mtime=0))
        print('FAILED execution evidence saved: '+str(path),file=sys.stderr,flush=True)
        raise
