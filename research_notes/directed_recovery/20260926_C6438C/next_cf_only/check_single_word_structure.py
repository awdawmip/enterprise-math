"""Bounded native-word structure check; no ideal/reference propagation."""
from __future__ import annotations
import argparse,hashlib,json,sys
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'phases'))
from closed_phase_bank import load_certified_bank
from stage80.fixed_phase import square_probe
from stage45.brc_loop_recheck import CALLS,verify_vendor
from stage79.phase_compiler import encode

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--activity',required=True);args=ap.parse_args()
    vendor=verify_vendor();before=len(CALLS)
    bank,intervals,dim,certificate=load_certified_bank(34,
      expected_payload_sha256='feecbc02808991f6d7b1e2c3179c8da2018b76901ef34c26ef0d28b65729dd5c')
    delta=F(1,1<<32)
    assert sum((intervals[m]['gate_error']+4*delta for m in range(3,33)),F(0))==177*delta
    rows=[]
    for m in range(3,33):
        v=bank[m];S=v.scale;z=v.z;S2=v.den
        # Two ACTUAL positive BRC square comparison observers per word.
        lower=square_probe(F(4),F(z[0],S),F(3))
        upper=square_probe(F(1),F(z[0],S),F(1))
        assert lower>0 and upper<0
        active_pair_trace=F(4*z[0]*z[0]-2*S2,S2)
        assert 1<active_pair_trace<2
        remaining_square=S2-z[0]*z[0]-z[1]*z[1]
        assert remaining_square>0
        composed_pair_trace=F(-(4*z[0]*z[1]+2*remaining_square),S2)
        if m==3:assert -2<composed_pair_trace<-1
        else:assert -1<composed_pair_trace<0
        # Read exact diagonal columns from the full-word-certified quotient,
        # and compose the actually native quarter turn. This is not a new
        # desired matrix or a numerical eigenvalue calculation.
        diagonal_trace=F(0)
        quarter_trace=F(0)
        for j in range(dim):
            basis=[int(i==j) for i in range(dim)]
            actual=v.apply_numer(basis)
            diagonal_trace+=F(actual[j],S2)
            composed=bank[2].apply_numer(actual)
            quarter_trace+=F(composed[j],S2)
        assert diagonal_trace==dim-2+active_pair_trace
        assert quarter_trace==dim-2+composed_pair_trace
        rows.append({'m':m,'residual_nonzero_coordinates':sum(x!=0 for x in z[2:]),
          'p0_square_lower_BRC_probe':lower,'p0_square_upper_BRC_probe':upper,
          'single_word_nontrivial_pair_trace':active_pair_trace,
          'quarter_then_single_word_pair_trace':composed_pair_trace,
          'diagonal_columns_checked_each':dim,
          'interpretation':'pair traces strictly between consecutive integers, hence nontrivial pair is not a root of unity'})
    payload={'schema':'BRC_SINGLE_WORD_CYCLOTOMIC_STRUCTURE_V1','activity':args.activity,
      'status':'AUTHOR_EXECUTED_BOUNDED_STRUCTURE_CHECK_NOT_ALL_SUBSET_PRODUCTS',
      'phase_bank':certificate,'vendor':vendor,'rows':rows,
      'eta_actual_certificate_sum':177*delta,
      'single_nonexact_words_checked':30,'quarter_compositions_checked':30,
      'actual_BRC_core_calls':len(CALLS)-before,'call_receipts':CALLS[before:],
      'classical_reference_run':False,'eigenvalue_solver_used':False,
      'all_two_or_more_nonexact_word_products_checked':False,
      'scope':'zero or one nonexact phase occurrence, optionally with exact quarter turn'}
    raw=json.dumps(encode(payload),sort_keys=True,separators=(',',':')).encode()
    (ROOT/'SINGLE_WORD_STRUCTURE.json').write_bytes(raw+b'\n')
    print(json.dumps({'single_words':30,'quarter_compositions':30,'eta':str(177*delta),
      'actual_BRC_core_calls':len(CALLS)-before,'payload_sha256':hashlib.sha256(raw).hexdigest()}),flush=True)

if __name__=='__main__':main()
