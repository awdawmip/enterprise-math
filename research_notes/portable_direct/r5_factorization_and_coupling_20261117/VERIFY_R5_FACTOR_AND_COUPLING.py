#!/usr/bin/env python3
"""R5 exact count-factor and multiplicative-coupling certificate.

Default regenerates frozen predecessor's 101-budget coefficients from the GitHub
repository checkout. For independent postprocessing of an already certified
output, pass --coefficients path/to/compact_stdout.json.

Scientific input pin: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Derived one-dimensional indexed-event observer; not native X6/BRC.
"""
import argparse
from hashlib import sha256
import json
from math import gcd
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
PREDECESSOR = (HERE.parent / 'r5_all_budget_cohort_hierarchy_20261116'
               / 'VERIFY_R5_BUDGET_INTERACTION_HIERARCHY.py')


def load_coefficients(path):
    if path is None:
        raw = subprocess.check_output([sys.executable, str(PREDECESSOR)])
        source = str(PREDECESSOR)
    else:
        raw = Path(path).read_bytes()
        source = str(path)
    data = json.loads(raw)
    assert data['status'] == 'PASS_R5_101_BUDGET_INTERACTION_HIERARCHY'
    assert data['scientific_input'] == '435e77af0d180eac32bd1f9c4c464bc4010b7551'
    assert data['budgets'] == [214,314]
    coeffs = {int(k): {int(mask): int(n) for mask, n in v.items()}
              for k, v in data['all_budget_coefficients'].items()}
    assert list(sorted(coeffs)) == list(range(214, 315))
    assert all(v > 0 and mask in range(256) for d in coeffs.values() for mask, v in d.items())
    return coeffs, sha256(raw).hexdigest(), source


def factor_cut_27(coeffs):
    # Bit 7 is U[7] = original effective gap cut 27.
    for k in range(214, 223):
        d = coeffs[k]
        bottom = {mask: val for mask, val in d.items() if not mask & 128}
        top = {mask ^ 128: val for mask, val in d.items() if mask & 128}
        assert set(bottom) == set(top), (k, set(bottom)^set(top))
        assert all(9 * top[mask] == 4 * bottom[mask]
                   for mask in bottom), k
    return {'budgets':[214,222], 'cut':27, 'coefficient_ratio':'4/9',
            'closed_to_open_count_ratio':'13/9',
            'checked_coefficient_pairs':sum(len(coeffs[k])//2 for k in range(214,223))}


def exact_coupling(coeffs, first, last, bit1, bit2):
    signs = {}; witnesses = {}; zeros = []
    for k in range(first, last+1):
        d = coeffs[k]
        assert set(d) == {0, bit1, bit2, bit1 | bit2}, (k,list(d))
        a, b, c, h = (d[i] for i in (0,bit1,bit2,bit1|bit2))
        # N(0,0)=a, N(1,0)=a+b, N(0,1)=a+c, N(1,1)=a+b+c+h.
        # Thus N00*N11-N10*N01 = a*h-b*c exactly.
        det = a*h-b*c
        tag = 'positive' if det>0 else 'negative' if det<0 else 'zero'
        signs.setdefault(tag,[]).append(k)
        if k in (first,first+1,256,257,298,299,301,302,last):
            g = gcd(gcd(a,b),gcd(c,h))
            A,B,C,H=a//g,b//g,c//g,h//g
            witnesses[str(k)]={'normalized_coefficients':[str(A),str(B),str(C),str(H)],
                               'normalization_gcd':str(g),
                               'normalized_determinant':str(A*H-B*C),
                               'sign':tag}
        if det == 0: zeros.append(k)
        assert h>0
    runs=[]
    for k in range(first,last+1):
        d=coeffs[k];det=d[0]*d[bit1|bit2]-d[bit1]*d[bit2]
        tag='positive' if det>0 else 'negative' if det<0 else 'zero'
        if runs and runs[-1][0]==tag and runs[-1][2]==k-1:runs[-1][2]=k
        else:runs.append([tag,k,k])
    return {'budget_range':[first,last], 'bit_masks':[bit1,bit2],
            'sign_intervals':runs,
            'zero_budgets':zeros, 'selected_exact_witnesses':witnesses}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--coefficients',type=Path)
    args=parser.parse_args()
    coeffs,digest,source=load_coefficients(args.coefficients)
    sep=factor_cut_27(coeffs)
    # U = (3,8,9,10,15,17,25,27)
    first=exact_coupling(coeffs,223,290,64,128)
    second=exact_coupling(coeffs,294,313,16,32)
    assert first['sign_intervals']==[['positive',223,256],['negative',257,290]]
    assert second['sign_intervals']==[['negative',294,298],['positive',299,301],['negative',302,313]]
    neg2=[k for k in range(294,314)
          if coeffs[k][0]*coeffs[k][48]-coeffs[k][16]*coeffs[k][32]<0]
    pos2=[k for k in range(294,314)
          if coeffs[k][0]*coeffs[k][48]-coeffs[k][16]*coeffs[k][32]>0]
    assert neg2 == list(range(294,299))+list(range(302,314)),neg2
    assert pos2 == [299,300,301],pos2
    assert set(coeffs[292])=={0}
    assert set(coeffs[291])=={0,64,128}
    assert set(coeffs[293])=={0,16,32}
    out={'status':'PASS_R5_101_BUDGET_FACTOR_AND_COUPLING',
         'scientific_input':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
         'scope':'frozen 954-event derived indexed-center observer; no native transfer',
         'upstream_coefficient_stdout_sha256':digest,
         'upstream_coefficient_source':source,
         'cut27_factorization':sep,
         'joint_25_27':first,
         'joint_15_17':second,
         'joint_15_17_exact_sign_runs':[['negative',294,298],['positive',299,301],['negative',302,313]],
         'strictly_positive_mixed_coefficients':88,
         'interpretation':'additive mixed difference positive throughout active 2-bit windows, while multiplicative association changes sign'}
    # Fresh finite check for every strictly positive pairwise cohort coefficient
    assert all(coeffs[k][192]>0 for k in range(223,291))
    assert all(coeffs[k][48]>0 for k in range(294,314))
    assert 88 == (290-223+1)+(313-294+1)
    print(json.dumps(out,sort_keys=True,ensure_ascii=False,separators=(',',':')))


if __name__=='__main__':main()
