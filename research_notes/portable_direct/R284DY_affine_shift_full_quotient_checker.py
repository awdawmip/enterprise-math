#!/usr/bin/env python3
"""R284DY: full frozen Port quotient by a 9-bit fixed shift, exact integers.

Run next to R284DX_six_bit_full_quotient_checker.py (immutable parent).
Reuses the pinned R284CO determinant and the independently checked R284DX
64-class table; the new 9-bit identity is also rechecked on all 65,536 states.
"""
import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path
from R284DX_six_bit_full_quotient_checker import (
    P, FROZEN_SHA, CORE, Q_TABLE, det,
)

COEFFS = (55152, -19198, -19411, 52)
SHIFT = 9
THRESHOLD = 2879 * P


def core_data(lower):
    u1, a, x, y, u2, w, b, z, u3, g, h, r = lower
    t, s = 6 - a, 13 - b
    u = t*s - x*w
    p1, p2 = s*u1 + x*u2, t*u2 + w*u1
    return (u,p1,p2)


def core_quotient(lower):
    u, p1, p2 = core_data(lower)
    A, B, C, K = COEFFS
    return (A*u + B*p1 + C*p2 + K) // (1<<SHIFT)


def index_key(lower):
    return sum((lower[pos]-1)<<bit for bit,pos in enumerate(CORE))


def main():
    # Exact 64-class identity; the other lower bits do not occur in core_data.
    margins=[]
    for key in range(64):
        lower=[1]*12
        for bit,pos in enumerate(CORE):
            lower[pos]=1+((key>>bit)&1)
        u,p1,p2=core_data(lower)
        numerator=COEFFS[0]*u+COEFFS[1]*p1+COEFFS[2]*p2+COEFFS[3]
        q=Q_TABLE[key]
        margins.append((numerator-(q<<SHIFT),((q+1)<<SHIFT)-numerator))
        assert min(margins[-1])>=1
        assert numerator//(1<<SHIFT)==q
    # Independent exhaustive check against T//P and frozen Port codeword hash.
    sha=hashlib.sha256()
    quotients_by_class=[Counter() for _ in range(64)]
    extremal_correction=[]
    fullstate_quots=[None]*65536
    for upper in itertools.product((1,2),repeat=4):
        top=sum((v-1)<<bit for bit,v in enumerate(upper))
        for lower in itertools.product((1,2), repeat=12):
            key=index_key(lower)
            T=det(lower, top)
            qcore=core_quotient(lower)
            assert qcore==Q_TABLE[key]
            correct=int(key==63 and T<THRESHOLD)
            quotient=qcore-correct
            residue=T-quotient*P
            assert quotient==T//P and 0<=residue<P and residue==T%P
            sha.update(residue.to_bytes(8,'big'))
            quotients_by_class[key][quotient]+=1
            if correct and len(extremal_correction)<5:
                extremal_correction.append({'upper_mask':top,'lower':list(lower),'T':T})
            index=(top<<12)+sum((value-1)<<bit for bit,value in enumerate(lower))
            fullstate_quots[index]=quotient
    assert sha.hexdigest()==FROZEN_SHA
    assert all(c==Counter({Q_TABLE[k]:1024}) for k,c in enumerate(quotients_by_class[:63]))
    assert quotients_by_class[63]==Counter({2878:446,2879:578})
    # Full-domain fourth upper bit invariance; parent checker also certifies it.
    assert all(fullstate_quots[i]==fullstate_quots[i^(1<<15)] for i in range(65536))
    return {
       'schema':'R284DY_AFFINE_NINE_BIT_PORT_QUOTIENT_V1',
       'scientific_status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
       'frozen_source':'awdawmip/enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py',
       'frozen_git_blob_sha1':'b46e0f682b58e47c27094b4bea6fa4e55119a3ee',
       'frozen_codeword_sha256':FROZEN_SHA,
       'parent_provenance':'R284DX full 65536-state quotient certificate at enterprise-math main@1161b7f25d79af64a0ff5911434dcd173e0f3d1a',
       'P':P,'states_checked':65536,'core_classes_checked':64,
       'core_features':['u=(6-a)*(13-b)-x*w','p1=(13-b)*u1+x*u2','p2=(6-a)*u2+w*u1'],
       'numerator_coefficients':{'u':COEFFS[0],'p1':COEFFS[1],'p2':COEFFS[2],'constant':COEFFS[3]},
       'floor_divisor':1<<SHIFT,'shift_bits':SHIFT,
       'core_numerator_floor_margins_min':[min(m[0] for m in margins), min(m[1] for m in margins)],
       'core_class_quotients_equal_R284DX_Q_table':True,
       'exceptional_key':63,'exception_threshold':THRESHOLD,'exceptional_lower_quotient_count':446,'exceptional_upper_quotient_count':578,
       'correction_examples':extremal_correction,
       'full_state_quotients_match_exact_division':True,
       'all_residues_match_exact_modulo':True,
       'upper_mask_bit3_flip_quotient_invariant':True,
       'ordered_residue_sha256':sha.hexdigest(),
       'all_exact_checks_passed':True,'independent_review':'NOT_REVIEWED',
    }

if __name__=='__main__':
    certificate=main()
    path=Path(__file__).with_name('R284DY_affine_shift_full_quotient_certificate.json')
    path.write_text(json.dumps(certificate,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:certificate[k] for k in ('states_checked','core_classes_checked','numerator_coefficients','floor_divisor','core_numerator_floor_margins_min','exceptional_lower_quotient_count','exceptional_upper_quotient_count','ordered_residue_sha256','all_exact_checks_passed')},ensure_ascii=False,indent=2))
