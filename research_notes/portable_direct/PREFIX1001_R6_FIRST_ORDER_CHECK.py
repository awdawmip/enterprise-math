"""PREFIX-1001: exact-rational finite-size correction checks for Stage46 BRC.
The all-length proof is analytic; this verifies the published PREFIX-1000
collision formula at larger exact integer inputs without endpoint storage.
"""
from fractions import Fraction
from decimal import Decimal, localcontext
from pathlib import Path
import json
from PREFIX1000_R6_POSITIVE_TERMINAL_SCALAR_CHECK import collisions, scalar_components

INDEX=(24,40,70,100,180,200,300)

def decimal_rational(x, places=12):
    with localcontext() as ctx:
        ctx.prec = 42
        return format(Decimal(x.numerator)/Decimal(x.denominator), f'.{places}f')


def check():
    A=collisions(max(INDEX))
    result={}
    for n in INDEX:
        p,m=scalar_components(n,A)
        ratio=Fraction(p+m,6*A[n-1])
        scaled=(n-2)*(ratio-Fraction(35,4))
        assert ratio>Fraction(35,4)
        assert scaled>Fraction(15,2)
        result[str(n)]={
          'ratio_exact':str(ratio),
          'ratio_display_12':decimal_rational(ratio),
          'scaled_gap_exact':str(scaled),
          'scaled_gap_display_12':decimal_rational(scaled)
        }
    assert result['24']['ratio_display_12']=='9.110596760695'
    assert result['300']['scaled_gap_display_12']=='7.520577228340'
    return {'schema':'PREFIX1001_R6_FINITE_SIZE_CERTIFICATE_V1',
            'model':'Stage46 signed X6 BRC, exact three-collision scalar identity',
            'frozen_p000':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
            'sampled_n':list(INDEX),
            'asserted_numeric_inequalities':'ratio>35/4 and (n-2)*(ratio-35/4)>15/2 at sampled n only',
            'status':'EXACT_RATIONAL_SAMPLES_PASSED; ASYMPTOTIC_PROOF_IN_MD',
            'samples':result}

if __name__=='__main__':
    x=check()
    with (Path(__file__).parent/'PREFIX1001_R6_EXACT_RESULTS.json').open('w',encoding='utf-8') as f:
        json.dump(x,f,ensure_ascii=False,indent=2)
    for n,v in x['samples'].items():
        print(n,v['ratio_display_12'],v['scaled_gap_display_12'])
    print('PASS PREFIX-1001 exact-rational finite samples')
