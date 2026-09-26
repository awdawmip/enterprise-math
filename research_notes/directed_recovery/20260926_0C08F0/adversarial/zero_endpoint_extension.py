"""Extend the frozen BRC dyadic-root interval interface at p=0 only.

Precision stays at the existing target_bits=32.  This is not a new root solver,
new native phase gate, higher-precision reference, or full Shor execution.
"""
from __future__ import annotations
import argparse
import json
import os
import sys
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parent
SOURCE=Path(os.environ.get('BRC_STAGE87_SOURCE',str(ROOT.parent/'stage87-source'))).resolve()
sys.path.insert(0,str(SOURCE))
from stage45.brc_loop_recheck import CALLS, verify_vendor
from stage79.phase_compiler import root_bracket, polynomial_probe, encode


def closed_root_bracket(p,bits):
    p=F(p)
    if p==0:
        # Same actual positive BRC observer: 0*x*x+2*x-0 = 2*x.
        assert polynomial_probe(p,F(0))==0
        assert polynomial_probe(p,F(1,1<<bits))==F(2,1<<bits)
        return F(0),F(0)
    return root_bracket(p,bits)


def closed_dyadic_parameters(max_m,bits=32):
    if max_m<2 or bits<3:
        raise ValueError('max_m>=2, bits>=3 required')
    lo=hi=F(1)
    out={2:{'lower':lo,'upper':hi,'parameter':F(1),'gate_error':F(0)}}
    for m in range(3,max_m+1):
        lo,_=closed_root_bracket(lo,bits)
        _,hi=closed_root_bracket(hi,bits)
        assert 0<=lo<=hi<1
        assert 0<=hi-lo<=F(4,1<<bits)
        midpoint=(lo+hi)/2
        assert 0<midpoint<=1
        out[m]={'lower':lo,'upper':hi,'parameter':midpoint,
                'gate_error':hi-lo}
    return out


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',required=True)
    ap.add_argument('--activity',required=True)
    args=ap.parse_args()
    source=verify_vendor()
    before=len(CALLS)
    t=34; bits=32; vector_bits=64
    intervals=closed_dyadic_parameters(t,bits)
    # No new fixed bank or Shor state is run here; this computes the inherited
    # certificate from actual frozen-grid brackets and unchanged B=64 theorem.
    L=(t-1)*(t-2)//2
    target=sum((t-m+1)*v['gate_error'] for m,v in intervals.items())
    dilation=F(4*L,1<<(vector_bits//2))
    assert target+dilation<F(1,1000000)
    report={'schema':'SHOR_ZERO_ENDPOINT_BRC_INTERVAL_EXTENSION_V1',
            'status':'AUTHOR_EXACT_BOUNDARY_EXTENSION_NOT_ADMITTED',
            'activity':args.activity,
            'source_head':'0852cad130c1d877174d235687cf60c19f318c58',
            'kernel':source,'target_bits':bits,'vector_bits':vector_bits,
            'highest_phase':t,'intervals':intervals,
            'target_error_bound':target,
            'fixed_word_dilation_bound_CONDITIONAL_NOT_EXECUTED':dilation,
            'combined_bound_CONDITIONAL_NOT_EXECUTED':target+dilation,
            'actual_BRC_core_calls':len(CALLS)-before,
            'full_ShOR_state_run':False,'new_fixed_phase_bank_run':False,
            'higher_precision':False,'arithmetic':'ACTUAL_TYPED_BRC_ONLY',
            'scope':'actual same-32-bit interval extension through m=34; '
                    'B64 fixed-word existence/error theorem reused symbolically; '
                    'no assertion that an extended fixed bank or circuit ran'}
    Path(args.output).write_text(json.dumps(encode(report),ensure_ascii=False,
                                           indent=2)+'\n',encoding='utf-8')
    print(json.dumps(encode({k:report[k] for k in ['highest_phase',
          'target_error_bound','combined_bound_CONDITIONAL_NOT_EXECUTED',
          'actual_BRC_core_calls']}),ensure_ascii=False))

if __name__=='__main__':
    main()
