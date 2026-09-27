"""Bounded full-native certificates, reuse, failed witnesses and replay controls."""
from pathlib import Path
from fractions import Fraction as F
from copy import deepcopy
from dataclasses import FrozenInstanceError
from time import perf_counter
import gzip
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parents[1]
sys.path.insert(0,str(BASE/'sep26-shor-general/optimization/collision_analysis'))
from check_gram_sampler import load_bank, LazyStreamingProgram, ExactCarrierCodec, verify_vendor
from word_certificates import (WordCertificateBank,CertificateReplayError,CompleteNativeWord,
                               CALLS,strict_bytes,digest)


def main():
    paths = (Path(__file__),ROOT/'word_certificates.py')
    hashes = {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    first,t0 = len(CALLS),perf_counter()
    kernel = verify_vendor()
    bank,binding = load_bank()
    initial_end = len(CALLS)
    programs = [LazyStreamingProgram(N,a,4,bank,61,codec=ExactCarrierCodec(61,tuple(range(6))))
                for N,a in ((21,2),(21,4),(65,3),(15,2))]
    p = programs[0]
    program_setup_end = len(CALLS)
    certified = WordCertificateBank(p)
    assert all(certified.get(m).accepted for m in (2,3,4))
    reuse_start = len(CALLS)
    for _ in range(3):
        for program in programs:
            certified.check(program)
            for m in (2,3,4):
                assert certified.get(m).s >= 0
    reuse = {'checks':12,'lookups':36,'actual_core_calls':len(CALLS)-reuse_start,
        'N_a_variations':[[x.N,x.a] for x in programs],
        'same_phase_codec_binding':True,'scientific_setup_repeated':False}
    assert reuse['actual_core_calls']==0
    serialized = certified.evidence()
    restored = WordCertificateBank.restore(p,strict_bytes(serialized))
    assert restored.binding_sha256 == certified.binding_sha256
    full = LazyStreamingProgram(21,2,4,bank,61)
    full_certified = WordCertificateBank(full)
    assert all(full_certified.get(m).s==certified.get(m).s and full_certified.get(m).accepted
               for m in (2,3,4))
    rejected=[]
    def reject(label,thunk):
        start = len(CALLS)
        try: thunk()
        except (ValueError,FrozenInstanceError,AttributeError,KeyError) as error:
            rejected.append({'case':label,'rejected':True,'type':type(error).__name__,
                'reason':str(error),'call_interval':[start,len(CALLS)],
                'fresh_replay_evidence':getattr(error,'evidence',None)})
        else:raise AssertionError(label+' was accepted')
    reject('codec_mismatch',lambda:certified.check(full))
    reject('immutable_record',lambda:setattr(certified.get(3),'s',F(0)))
    reject('immutable_bank',lambda:setattr(certified,'binding_sha256','0'*64))
    reject('bool_phase',lambda:certified.get(True))
    def mutate_program_field():
        old = p.bank[3]
        p.bank[3] = p.bank[4]
        try:certified.check(p)
        finally:p.bank[3] = old
    reject('replaced_phase',mutate_program_field)
    detached = certified.evidence()
    detached['logical']['words']['3']['s']='0'
    assert certified.evidence()['logical']['words']['3']['s'] != '0'
    reject('changed_s_unrehashed',lambda:WordCertificateBank.restore(p,detached))
    for label,change in (
        ('changed_s_rehashed',lambda x:x['words']['3'].update(s='0')),
        ('changed_full_column_rehashed',lambda x:x['words']['4']['complete_forward_columns'][60].__setitem__(60,0)),
        ('changed_residual_entry_rehashed',lambda x:x['words']['3']['full_matrices']['B_squared_minus_sB'][60].__setitem__(60,'1')),
        ('changed_observer_rehashed',lambda x:x['words']['3']['observer_operations'][0].update(signed_observation='7')),
        ('boolean_acceptance_replaced_by_int',lambda x:x['words']['3'].update(accepted=1)),
        ('codec_claim_rehashed',lambda x:x['codec_binding'].update(encoded_dim=5))):
        bad=deepcopy(serialized);change(bad['logical']);bad['binding_sha256']=digest(bad['logical'])
        reject(label,lambda:WordCertificateBank.restore(p,bad))
    # A complete native reflection is orthogonal but this rank-two witness
    # must fail: B has one nonzero eigenvalue and s=tr(B)/2 is insufficient.
    reflection = CompleteNativeWord((('neg',0),),61)
    failed_program = LazyStreamingProgram(21,2,2,{2:reflection},61,
                         codec=ExactCarrierCodec(61,tuple(range(6))))
    failed = WordCertificateBank(failed_program)
    assert not failed.get(2).accepted and failed.get(2).s == 2
    assert failed.evidence()['logical']['words']['2']['failed_entries']==[[0,0,'8']]
    identity = CompleteNativeWord((),61)
    identity_program = LazyStreamingProgram(21,2,2,{2:identity},61)
    identity_cert = WordCertificateBank(identity_program)
    assert identity_cert.get(2).accepted and identity_cert.get(2).s==0
    assert hashes=={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    payload = {'status':'BOUNDED_ACTUAL_NATIVE_FULL_CARRIER_CHECKS_PASSED',
        'source_hashes':hashes,'kernel':kernel,'source_bank':binding,
        'initial_bank_admission_call_interval':[first,initial_end],
        'program_setup_call_interval':[initial_end,program_setup_end],
        'program_admission_receipts':[{'N':x.N,'a':x.a,'phase_bindings':x.phase_bindings,
            'codec_binding':x.codec_binding,'H4_binding':x.h4_binding,
            'lazy_verifications':x.lazy_permutation_verifications,
            'tables':[table.export_certificate() for table in x.lazy_factory.tables.values()]}
            for x in programs+[full,failed_program,identity_program]],
        'encoded_bank':certified.evidence(),'restored_bank':restored.evidence(),
        'full61_bank':full_certified.evidence(),'cross_program_reuse':reuse,
        'negative_controls':rejected,'failed_reflection_witness':failed.evidence(),
        'zero_identity_witness':identity_cert.evidence(),
        'actual_core_calls':CALLS[first:],'core_call_count':len(CALLS)-first,
        'elapsed_seconds':perf_counter()-t0,
        'scope':'shared-author bounded actual execution; no ideal-angle or complexity claim'}
    from certified_word_compiler import packed
    raw = packed(payload)
    out=ROOT/'WORD_CERTIFICATE_RESULTS.json.gz'
    out.write_bytes(gzip.compress(raw,mtime=0))
    summary={'status':payload['status'],'source_hashes':hashes,
        'payload_sha256':hashlib.sha256(raw).hexdigest(),'payload_bytes':len(raw),
        'gzip_bytes':out.stat().st_size,'gzip_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
        'core_call_count':payload['core_call_count'],'elapsed_seconds':payload['elapsed_seconds'],
        'binding_sha256':certified.binding_sha256,
        'words':[{'m':m,'s':str(certified.get(m).s),'accepted':certified.get(m).accepted,
            'certificate_sha256':certified.get(m).certificate_sha256,
            'unique_observer_expressions':certified.evidence()['logical']['words'][str(m)]['actual_unique_observer_expressions']}
            for m in (2,3,4)],
        'encoded_cold_setup':{k:v for k,v in certified.evidence()['setup'].items() if k!='actual_core_calls'},
        'cross_program_reuse':reuse,'negative_controls':len(rejected),
        'reflection_witness_status':'REJECTED_WITH_FULL_RESIDUAL_8',
        'identity_s_zero_passed':True,'full61_vs_encoded6_s_and_acceptance_equal':True}
    (ROOT/'WORD_CERTIFICATE_SUMMARY.json').write_bytes(packed(summary))
    print(json.dumps(summary,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
