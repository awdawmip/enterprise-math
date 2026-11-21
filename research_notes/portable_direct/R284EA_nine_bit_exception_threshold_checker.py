#!/usr/bin/env python3
"""R284EA: exact nine-bit correction classifier and integer dual proof.

Run beside R284DX_six_bit_full_quotient_checker.py on the frozen R284CO
source. Python standard library only; all checks use exact integers.
"""
from itertools import product
from hashlib import sha256
from pathlib import Path
import json
from R284DX_six_bit_full_quotient_checker import P, FROZEN_SHA, CORE, det

BITS=("Y","Z","U","G","H","R","B0","B1","B2")
WEIGHTS=(13,6,28,25,11,12,26,17,6)
POS=(
 ((0,0,1,0,0,0,1,1,1),25),
 ((0,1,0,1,1,1,0,1,1),23),
 ((0,1,1,1,0,1,0,0,1),45),
 ((1,0,1,1,1,0,0,0,0),51),
)
NEG=(
 ((0,0,1,1,0,0,0,1,1),36),
 ((0,0,1,1,1,1,0,0,0),41),
 ((0,1,1,1,0,0,0,1,0),11),
 ((0,1,1,1,1,0,0,0,1),6),
 ((1,1,0,1,0,0,1,0,1),24),
 ((1,1,1,0,1,1,0,0,1),26),
)

def score(bits):
    return sum(w*b for w,b in zip(WEIGHTS,bits))

def bits_of(lower,top):
    return (lower[3]-1,lower[7]-1,lower[8]-1,lower[9]-1,
            lower[10]-1,lower[11]-1,top&1,(top>>1)&1,(top>>2)&1)

def core_key(lower):
    return sum((lower[p]-1)<<j for j,p in enumerate(CORE))

def quotient(lower,top):
    u1,a,x,y,u2,w,b,z,u3,g,h,r=lower
    t,s=6-a,13-b
    u=t*s-x*w
    p1=s*u1+x*u2
    p2=t*u2+w*u1
    qcore=(13788*u-4799*p1-4854*p2+14)//128
    return qcore-int(core_key(lower)==63 and score(bits_of(lower,top))>=77)

def make_core63(bits):
    Y,Z,U,G,H,R,B0,B1,B2=bits
    return (2,2,2,1+Y,2,2,2,1+Z,1+U,1+G,1+H,1+R), B0+2*B1+4*B2

def main():
    truth={}
    min_true_score,max_false_score=1000,-1
    max_true_delta,min_false_delta=-10**100,10**100
    for bits in product((0,1),repeat=9):
        lower,top=make_core63(bits)
        delta=det(lower,top)-2879*P
        actual=delta<0
        assert actual==(score(bits)>=77)
        assert (det(lower,top|8)<2879*P)==actual
        truth[bits]=actual
        if actual:
            min_true_score=min(min_true_score,score(bits))
            max_true_delta=max(max_true_delta,delta)
        else:
            max_false_score=max(max_false_score,score(bits))
            min_false_delta=min(min_false_delta,delta)
    assert sum(truth.values())==223
    assert (min_true_score,max_false_score)==(77,76)
    assert (max_true_delta,min_false_delta)==(-27577,41823)
    assert all(truth[b] and score(b)==77 for b,m in POS)
    assert all(not truth[b] and score(b)==76 for b,m in NEG)
    assert sum(m for b,m in POS)==sum(m for b,m in NEG)==144
    dual=tuple(sum(m*b[j] for b,m in POS)-sum(m*b[j] for b,m in NEG)
               for j in range(9))
    assert dual==(1,)*9 and sum(WEIGHTS)==144
    influences=tuple(sum(truth[b]!=truth[b[:j]+(1-b[j],)+b[j+1:]]
                         for b in truth)//2 for j in range(9))
    assert influences==(45,21,111,95,41,43,103,61,21)
    ordered=sha256()
    exception_count=0
    for upper in product((1,2),repeat=4):
        top=sum((x-1)<<j for j,x in enumerate(upper))
        for lower in product((1,2),repeat=12):
            T=det(lower,top)
            q=quotient(lower,top)
            assert q==T//P
            residue=T-q*P
            assert 0<=residue<P and residue==T%P
            ordered.update(residue.to_bytes(8,"big"))
            exception_count+=int(core_key(lower)==63 and score(bits_of(lower,top))>=77)
    assert exception_count==446 and ordered.hexdigest()==FROZEN_SHA
    return {
      "schema":"R284EA_SHARP_NINE_BIT_EXCEPTION_THRESHOLD_V1",
      "date":"2026-11-22",
      "scientific_status":"AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED",
      "frozen_source":"awdawmip/enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py",
      "frozen_source_blob":"b46e0f682b58e47c27094b4bea6fa4e55119a3ee",
      "original_codeword_sha256":FROZEN_SHA,
      "bit_order":BITS,"weights":WEIGHTS,"threshold":77,
      "nine_bit_assignments_checked":512,"exception_true_nine_bit_assignments":223,
      "upper_bit3_repetitions_checked":512,
      "full_frozen_states_checked":65536,"exception_true_full_states":446,
      "score_boundary":{"true_min":min_true_score,"false_max":max_false_score},
      "determinant_margin":{"true_nearest_delta":max_true_delta,"false_nearest_delta":min_false_delta},
      "bit_influence_edges":dict(zip(BITS,influences)),
      "sharp_total_integer_weight":144,
      "exact_dual_certificate":{
         "true_witness_multiplicities":[{"bits":b,"count":m} for b,m in POS],
         "false_witness_multiplicities":[{"bits":b,"count":m} for b,m in NEG],
         "total_multiplicity_each_side":144,
         "weighted_true_minus_false_coordinate_vector":dual,
         "implied_weight_sum_lower_bound":144
      },
      "full_quotient_and_residue_equal_frozen":True,
      "ordered_residue_sha256":ordered.hexdigest(),
      "review":"NOT_REVIEWED"
    }

if __name__=="__main__":
    certificate=main()
    path=Path(__file__).with_name("R284EA_nine_bit_exception_threshold_certificate.json")
    path.write_text(json.dumps(certificate,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({"state_count":certificate["full_frozen_states_checked"],
                      "exception_count":certificate["exception_true_full_states"],
                      "sharp_weight":certificate["sharp_total_integer_weight"],
                      "frozen_digest":certificate["ordered_residue_sha256"]},indent=2))
