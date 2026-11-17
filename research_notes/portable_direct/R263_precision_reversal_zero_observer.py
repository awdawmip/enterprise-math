"""Exact R263 one-mask mod-169 zero-only witness after R262 mod-13 minimum four."""
import json
from fractions import Fraction
from pathlib import Path
from R260_labelled_modular_quotient import reconstruct, sequence

def run():
    s=Fraction(67,169)
    c,q=reconstruct(s,1184397599,989553240,3805974000)
    m,p,P=57,169,78
    d=len(q[m])
    assert d==5
    a=sequence(c[m],q[m],p,P+d)
    assert [v%p for v in c[m]]==[0,0,104,166,2,1]
    assert a[:d]==[54,58,150,4,156]
    assert a[:d]==a[P:P+d]
    assert all(v for v in a[:P])
    assert not any(P%h==0 and a[:d]==a[h:h+d] for h in range(1,P))
    assert a[(1093-3)%P]==a[(2185-3)%P]==156
    cert={'schema':'EM_R263_PRECISION_REVERSAL_ZERO_ONLY_V1','frozen_science_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
        'parameter':'67/169','modulus':169,'selected_original_mask':57,
        'characteristic_ascending_mod169':[v%169 for v in c[m]],
        'initial_window':[v%169 for v in q[m]],
        'shifted_period_taps_verified':d,'minimal_output_period':P,
        'period_values':a[:P],'zero_count':0,
        'value_at_k_1093_and_2185_mod169':156,
        'minimal_zero_only_label_count':1,'proof':'monic recurrence plus full 78-period nonzero certificate'}
    path=Path(__file__).with_name('R263_verification.json')
    path.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
    print('R263 PASS: period=78, nonzero-all, minimal mask=57, zero-only labels=1')
if __name__=='__main__':run()
