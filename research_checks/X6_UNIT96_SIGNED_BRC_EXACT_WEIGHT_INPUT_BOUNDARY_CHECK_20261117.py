#!/usr/bin/env python3
"""Unit96: real-source signed BRC exact-weight boundary and opt-in repair.

Run from a complete enterprise-math repo checkout. Uses the pinned frozen
signed_brc.py and an opt-in new signed_brc_strict_v2.py; preserves original.
Pure positive-rational branch mass; signs label step direction, not amplitude.
"""
from __future__ import annotations

from collections import defaultdict
from decimal import Decimal
from fractions import Fraction
from hashlib import sha1, sha256
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
MOD = ROOT / 'experiments/x6_signed_native_spatial_v16_20260905'
ORIGINAL = MOD / 'signed_brc.py'
STRICT = MOD / 'signed_brc_strict_v2.py'
ORIGINAL_BLOB = '300a96e3dc24bf6fff73743037a0347a8bc83176'

def require(cond, detail='check failed'):
    if not cond:
        raise RuntimeError(str(detail))

def git_blob(path):
    b=path.read_bytes()
    return sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

require(git_blob(ORIGINAL)==ORIGINAL_BLOB, 'original frozen BRC mismatch')
sys.path.insert(0,str(MOD))
import signed_brc as original  # noqa: E402
import signed_brc_strict_v2 as strict  # noqa: E402

ZERO=(0,)*6
U0=(1,0,0,0,0,0)
ONE=(1,)*6

# These are accepted by the ORIGINAL module although outside its annotated
# exact int/Fraction input type. They must not be accepted by the strict module.
invalid=[('bool_true', True), ('float_0_1', 0.1),
         ('string_fraction', '1/10'), ('decimal_0_1', Decimal('0.1'))]
observed={}
for label,value in invalid:
    wp=[1]*6; wp[0]=value
    original_value=original.endpoint_weight(1,U0,wp,ONE)
    require(original_value==Fraction(value),(label,'old acceptance',str(original_value)))
    try:
        strict.endpoint_weight(1,U0,wp,ONE)
    except TypeError:
        pass
    else:
        raise RuntimeError('strict accepted '+label)
    observed[label]={'original_accepted_fraction':str(original_value), 'strict_rejected':True}
require(Fraction(0.1)==Fraction(3602879701896397,36028797018963968))
observed['float_0_1']['difference_from_declared_one_tenth']=str(Fraction(0.1)-Fraction(1,10))

# Independently accumulate all labeled native signed words by exact Fraction
# arithmetic: each of twelve named directions carries its own positive weight.
profiles=[
    ((Fraction(1,2),Fraction(2,3),Fraction(3,4),Fraction(4,5),Fraction(5,6),Fraction(6,7)),
     (Fraction(7,6),Fraction(6,5),Fraction(5,4),Fraction(4,3),Fraction(3,2),Fraction(2,1))),
    ((1,2,3,4,5,6),(6,5,4,3,2,1)),
    ((Fraction(2,7),Fraction(1,3),Fraction(5,8),Fraction(3,5),Fraction(7,4),Fraction(1,11)),
     (Fraction(3,7),Fraction(4,9),Fraction(2,5),Fraction(11,6),Fraction(1,13),Fraction(5,2))),
]
profiles_out=[]
for positive,negative in profiles:
    state={ZERO:Fraction(1)}
    tested=0
    states_per_length=[]
    for n in range(6):
        require(sum(state.values())==(sum(map(Fraction,positive))+sum(map(Fraction,negative)))**n,
                ('total mass',n))
        for z,expected in state.items():
            got=strict.endpoint_weight(n,z,positive,negative)
            old=original.endpoint_weight(n,z,positive,negative)
            require(expected==got==old,('weighted endpoint',n,z,str(expected),str(got),str(old)))
            require(got>0)
            tested+=1
        states_per_length.append(len(state))
        if n<5:
            nxt=defaultdict(Fraction)
            for z,mass in state.items():
                for axis in range(6):
                    for sign,w in ((1,positive[axis]),(-1,negative[axis])):
                        zz=list(z);zz[axis]+=sign
                        nxt[tuple(zz)]+=mass*Fraction(w)
            state=dict(nxt)
    profiles_out.append({'compared_native_endpoints':tested,'endpoint_counts_n0_to_n5':states_per_length})

# One concrete named signed-native path, preserving exact weight and direction.
require(strict.endpoint_weight(1,U0,[Fraction(1,10)]+[1]*5,ONE)==Fraction(1,10))
require(original.endpoint_weight(1,U0,[0.1]+[1]*5,ONE)!=Fraction(1,10))
require(strict.endpoint_multiplicity(6,ZERO)==original.endpoint_multiplicity(6,ZERO)==19920)

result={
  'schema':'EM_X6_UNIT96_EXACT_SIGNED_BRC_WEIGHT_SOURCE_CHECK_V1',
  'source_blob_sha1':ORIGINAL_BLOB,
  'strict_blob_sha1':git_blob(STRICT),
  'status':'AUTHOR_EXECUTED_UNREVIEWED_NOT_ADMITTED',
  'original_input_coercion_examples':observed,
  'original_signed_brc_unchanged':True,
  'positive_rational_profiles':profiles_out,
  'total_exact_weight_endpoint_comparisons':sum(x['compared_native_endpoints'] for x in profiles_out),
  'signed_zero_return_length6':19920,
  'native_benchmark_r063_helly_executed':False,
  'actual_current_bad_consumer_proved':False,
}
print(json.dumps(result,ensure_ascii=False,sort_keys=True,separators=(',',':')))

if __name__=='__main__':
    pass
