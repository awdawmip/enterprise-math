#!/usr/bin/env python3
"""R386 exact regression for the signed-BRC Sheffer-type identity and half-degree theorem.

Formal proof is in R386_PROOF.zh-CN.md; these finite checks do NOT certify
all-corank universality. Inputs are the original signed R384 K/J -> B -> D
recurrence, with K_3[t^2]=-8(1+theta), and no native-X6 simulation.

Run in the repository sibling research directory, or alongside R384_verify.py
in a standalone research package. Outputs local JSON evidence and summary.
"""
from __future__ import annotations

import hashlib
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
SIBLING = HERE.parent / 'r384_universal_signed_k3_catalan_top_20261029_emr3'
if (SIBLING / 'R384_verify.py').is_file():
    sys.path.insert(0, str(SIBLING))
else:
    sys.path.insert(0, str(HERE))

from R384_verify import build  # type: ignore[import-not-found]
try:
    from R384_verify import differences  # type: ignore[import-not-found]
except ImportError:
    from R384_verify import difference as differences  # type: ignore[import-not-found]

PARAMS = ['-1/2', '0', '1/2', '1', '15/8']
MAX_R = 16
MAX_U = 5

def convolution_truncated(a, b, n):
    return [sum((a[i]*b[k-i] for i in range(k+1)), F(0)) for k in range(n+1)]

def inverse_mult(a, b, n):
    """Find C such that A*C=B modulo s^(n+1), assuming A[0]=1."""
    assert a[0] == 1
    c=[]
    for k in range(n+1):
        c.append(b[k] - sum((a[i]*c[k-i] for i in range(1,k+1)),F(0)))
    return c

def run():
    observations=[]
    sheffer_nontrivial=0
    degeneracy_checks=0
    for param in PARAMS:
        theta=F(param)
        H,Q=build(theta,MAX_R)
        rows=[[H(r,u) for r in range(MAX_R+1)] for u in range(MAX_U+1)]
        a=rows[0]
        b=inverse_mult(a,rows[1],MAX_R)
        expected_b1=F(30-16*theta,5)
        expected_b2=F(216-96*theta,5)
        expected_b3=F(1808-832*theta,5)
        assert a[:4] == [1,6,32,160-64*theta], (theta,'A low jet',a[:4])
        assert b[:4] == [1,expected_b1,expected_b2,expected_b3], (theta,'B low jet',b[:4])
        power=[F(1)]+[F(0)]*MAX_R
        for u in range(1,MAX_U+1):
            power=convolution_truncated(power,b,MAX_R)
            predicted=convolution_truncated(a,power,MAX_R)
            if u>=2:
                for r,(got,exp) in enumerate(zip(rows[u],predicted)):
                    assert got==exp,(param,u,r,got,exp)
                    sheffer_nontrivial+=1
        row={'theta':param,'a_jet_0_3':[str(x) for x in a[:4]],
             'b_jet_0_3':[str(x) for x in b[:4]],
             'nontrivial_sheffer_u_range':[2,MAX_U],
             'nontrivial_sheffer_r_range':[0,MAX_R]}
        if theta==F(15,8):
            assert b[1]==0 and b[2]==F(36,5) and b[3]==F(248,5)
            deg_rows=[]
            for r in range(1,MAX_R+1):
                hd=differences([H(r,u) for u in range(r+1)])
                qd=differences(Q(r))
                degree_h=max((i for i,v in enumerate(hd) if v),default=-1)
                degree_q=max((i for i,v in enumerate(qd) if v),default=-1)
                assert degree_h==r//2,(r,'H degree',degree_h)
                assert degree_q==r,(r,'Q degree',degree_q)
                expected=(-1)**r*math.comb(r,r//2)*180**r
                assert qd[r]==expected,(r,'Newton c_r',qd[r],expected)
                # c_j =0 for all j>r, check complete finite tail.
                assert all(qd[i]==0 for i in range(r+1,2*r+1))
                degeneracy_checks+=4
                deg_rows.append({'r':r,'degree_H':degree_h,'degree_Q':degree_q,
                                 'c_r':str(qd[r]),'expected':str(expected)})
            row['degenerate_observations']=deg_rows
        observations.append(row)
    assert sheffer_nontrivial==len(PARAMS)*4*(MAX_R+1)==340
    assert degeneracy_checks==16*4==64
    evidence={'schema':'R386_SIGNED_BRC_SHEFFER_FINITE_AUDIT_V1',
              'source':'R384_verify.py original signed R346 K/J -> B -> D branch model; theta>-1',
              'source_model':'Auxiliary signed combinatorial BRC model; not native X6',
              'method':'Exact rational series multiplication and finite Newton differences, no floating point',
              'parameter_values':PARAMS,
              'r_range':[0,MAX_R],'u_range':[0,MAX_U],
              'independent_nontrivial_sheffer_coeff_checks':sheffer_nontrivial,
              'degeneracy_exact_assertions':degeneracy_checks,
              'observations':observations,
              'scope':'Finite implementation verification only; global theorem from residue proof'}
    ev_path=HERE/'R386_EVIDENCE.json'
    ev_path.write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    summary={'schema':'R386_SUMMARY_V1',
             'status':'R386_EXACT_PASS',
             'parameters':len(PARAMS),'r_max':MAX_R,'u_max':MAX_U,
             'nontrivial_sheffer_coeff_checks':sheffer_nontrivial,
             'degenerate_degree_and_tail_assertions':degeneracy_checks,
             'theta_star':'15/8',
             'theta_star_B_jet':['1','0','36/5','248/5'],
             'global_proof_status':'AUTHOR_SIDE_RESIDUE_PROOF_UNREVIEWED',
             'evidence_sha256':hashlib.sha256(ev_path.read_bytes()).hexdigest()}
    (HERE/'R386_SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('R386_EXACT_PASS',json.dumps(summary,ensure_ascii=False))

if __name__=='__main__':
    run()
