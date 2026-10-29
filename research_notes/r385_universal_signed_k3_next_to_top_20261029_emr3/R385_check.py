#!/usr/bin/env python3
"""R385 exact finite regression against the original signed twelve-branch BRC recurrence.
The neighboring R384 directory is a required existing dependency in PR #1592.
"""
from __future__ import annotations
import hashlib
import json
import math
import sys
from pathlib import Path
from fractions import Fraction as F

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'r384_universal_signed_k3_catalan_top_20261029_emr3'))
from R384_verify import build,differences as difference

PARAMS=['-1/2','0','1/2','901/1000','902/1000','1','15/8','2']
MAX_R=16

def claimed_coefficients(r, theta):
    t=F(theta)
    lam=F(30-16*t,25)
    F_r=(35*r+25-32*r*t+32*t)/50
    G=(-384*t*t+760*t+105)/625
    top=F(5**r,math.factorial(r))*lam**r
    second=F(5**r,math.factorial(r-1)) * (lam**(r-1)*F_r + (r-1)*lam**(r-2)*G if r>=2 else F_r)
    return top,second

def run():
    obs=[]
    for param in PARAMS:
        theta=F(param); H,_=build(theta,R=MAX_R)
        for r in range(1,MAX_R+1):
            diffs=difference([H(r,u) for u in range(r+1)])
            top=diffs[r]/math.factorial(r)
            second=(diffs[r-1]-F(r-1,2)*diffs[r])/math.factorial(r-1)
            expected_top,expected_second=claimed_coefficients(r,theta)
            assert (top,second)==(expected_top,expected_second),(param,r,top,expected_top,second,expected_second)
            if theta==F(15,8) and r>=3:
                assert top==second==0,(param,r,'degree not <= r-2')
            obs.append({'theta':param,'r':r,'top':str(top),'second':str(second)})
    data={'schema':'R385_SIGNED_K3_NEXT_TO_TOP_EXACT_V1','arithmetic':'exact Fraction from original signed K/J-B-D recurrence','parameters':PARAMS,'r_range':[1,MAX_R],'checks':len(obs)*2,'observations':obs,'limitations':'Finite crosscheck; universal theorem uses algebraic proof in R385_PROOF.zh-CN.md'}
    out=HERE/'R385_EVIDENCE.json'
    out.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    sha=hashlib.sha256(out.read_bytes()).hexdigest()
    summary={'schema':'R385_SUMMARY_V1','checks':len(obs)*2,'parameter_count':len(PARAMS),'coranks_count':MAX_R,'evidence_sha256':sha,'theta15over8_degree_bound':'deg H_r <= r-2 for r>=3 (universal via proof)','status':'R385_EXACT_PASS'}
    (HERE/'R385_SUMMARY.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('R385_EXACT_PASS '+json.dumps(summary,ensure_ascii=False))

if __name__=='__main__':run()
