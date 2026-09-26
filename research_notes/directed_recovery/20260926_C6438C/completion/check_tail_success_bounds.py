"""Observe fixed-grid identity-tail success bounds through actual BRC paths."""
from pathlib import Path
from fractions import Fraction as F
import gzip, hashlib, json, sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'phases'))
from closed_phase_bank import truncated_error_certificate
from stage45.brc_loop_recheck import core_power,verify_vendor,CALLS

verify_vendor()
raw=gzip.decompress((ROOT.parent/'phases'/'bank_t34.json.gz').read_bytes())
payload=json.loads(raw)
intervals={int(m):{k:F(v) for k,v in row.items()} for m,row in payload['phase_intervals'].items()}

def positive_product(*weights):
    g=[[F(0) for _ in range(len(weights)+1)] for _ in range(len(weights)+1)]
    for i,w in enumerate(weights):g[i][i+1]=F(w)
    return core_power(tuple(map(tuple,g)),len(weights))[0][-1]

def threshold(coefficient,strict):
    rows=[]
    def accepts(n):
        t=2*n
        error=truncated_error_certificate(t,intervals,33)['telescoping_sum']
        affine=F(185*t-3225,2**32)+F(8,2**(32+t-32))
        assert error==affine
        observed=positive_product(coefficient,n,error)
        accepted=observed<1 if strict else observed<=1
        rows.append({'n':n,'t':t,'actual_certificate_error':str(error),
                     'BRC_product':str(observed),'accepted':accepted})
        return accepted
    lo,hi=17,4096
    assert accepts(lo) and not accepts(hi)
    while hi-lo>1:
        mid=(lo+hi)//2
        if accepts(mid):lo=mid
        else:hi=mid
    assert accepts(lo) and not accepts(hi)
    return {'coefficient':coefficient,'strict':strict,'maximum_certified_n':lo,
            'first_n_not_certified':hi,'observations':rows}

report={'schema':'BRC_SHOR_IDENTITY_TAIL_SUCCESS_THRESHOLD_V1',
        'researcher':'EM-DIRECT-C6438C','activity':'RA-CAAAC604CB513AEA8BBC1DFC',
        'source_bank_uncompressed_sha256':hashlib.sha256(raw).hexdigest(),
        'identity_tail_from_m':33,'target_bits':32,'vector_bits':64,
        'scope':'changed full-D identity-tail algorithm; no word equality with closed-bank tail asserted',
        'retry_budget_16ns':threshold(16,False),
        'strictly_positive_success_bound':threshold(8,True),
        'actual_BRC_calls':CALLS,'no_new_bank_or_reference_execution':True}
(ROOT/'TAIL_SUCCESS_CHECKS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'retry_max_n':report['retry_budget_16ns']['maximum_certified_n'],
    'positive_max_n':report['strictly_positive_success_bound']['maximum_certified_n'],
    'BRC_calls':len(CALLS)}))
