#!/usr/bin/env python3
"""PREFIX-400: exact finite algebraic feasibility on the P399 singular slice.
Standard library only; rational fractions and square-root signs are decided exactly.
The general five-intensity-noise problem remains a separate open algorithmic task.
"""
from __future__ import annotations
import argparse
import json
from fractions import Fraction as F
from dataclasses import dataclass

N = 75154
K4 = F(300616, 3969)
K5 = F(2638189, 63504)
R = F(59, 63)


def sign(a: F, b: F, d: F) -> int:
    """Sign of a + b*sqrt(d), d>=0, using only rational comparisons."""
    if d < 0:
        raise ValueError("negative radicand")
    if b == 0 or d == 0:
        return (a > 0) - (a < 0)
    if a == 0:
        return (b > 0) - (b < 0)
    if a > 0 and b > 0:
        return 1
    if a < 0 and b < 0:
        return -1
    z = a*a - b*b*d
    s = (z > 0) - (z < 0)
    return s if a > 0 else -s


@dataclass(frozen=True)
class Point:
    tag: str
    ta: F
    tb: F
    sa: F
    sb: F
    rad: F

    def tuple_json(self):
        ca=(245*self.ta+123*self.sa)/N
        cb=(245*self.tb+123*self.sb)/N
        da=(-123*self.ta+245*self.sa)/N
        db=(-123*self.tb+245*self.sb)/N
        return {"tag": self.tag, "T": [str(self.ta),str(self.tb)],
                "sigma": [str(self.sa),str(self.sb)],
                "c": [str(ca),str(cb)], "d": [str(da),str(db)],
                "sqrt_radicand":str(self.rad)}


def circle_line(tag: str, u: F, v: F, w: F, radius_sq: F):
    """Return all intersections of u*T+v*sigma=w with T^2+sigma^2=radius_sq."""
    D = u*u+v*v
    assert D > 0
    rad = D*radius_sq-w*w
    if rad < 0:
        return []
    pairs = [(F(u*w,D),-v/D,F(v*w,D),u/D)]
    if rad > 0:
        pairs.append((F(u*w,D),v/D,F(v*w,D),-u/D))
    return [Point(tag+('+' if i==0 else '-'), *p, rad) for i,p in enumerate(pairs)]


def evaluate(p: Point, lo: F, hi: F, zlo: F, zhi: F):
    za = 245*p.ta+123*p.sa
    zb = 245*p.tb+123*p.sb
    return {
       "T_ge_L":sign(p.ta-lo,p.tb,p.rad),
       "T_le_U":sign(hi-p.ta,-p.tb,p.rad),
       "Z_ge_A":sign(za-zlo,zb,p.rad),
       "Z_le_B":sign(zhi-za,-zb,p.rad),
    }


def solve(k: F, j4: F, xi4: F, j5: F, xi5: F, q: F, eta: F):
    """Fix I1=1,I2=(59/63)^2,Cu=(1+59/63)^2,I3=k exactly.
    J4,J5,Cv have independent closed rational error bands.
    Return YES with exact quadratic witness or NO with exhaustive finite test signs.
    """
    if min(xi4,xi5,eta) < 0:
        raise ValueError("negative error bound")
    if k < 0:
        return {"feasible": False,"reason":"I3_negative"}
    lo = max((j4-xi4-K4-16*k)*F(63,16),
             (j5-xi5-K5-F(53,8)*k)*F(504,61))
    hi = min((j4+xi4-K4-16*k)*F(63,16),
             (j5+xi5-K5-F(53,8)*k)*F(504,61))
    zlo = F(N,2)*(q-eta-1-k)
    zhi = F(N,2)*(q+eta-1-k)
    summary = {"feasible":False, "k":str(k),"T_band":[str(lo),str(hi)],
               "Z_band":[str(zlo),str(zhi)], "tested":[]}
    if lo > hi:
        summary["reason"]="empty_T_band"
        return summary
    radius_sq = N*k
    if radius_sq == 0:
        p = Point('origin',F(0),F(0),F(0),F(0),F(0))
        points = [p]
    else:
        points = [Point('full_circle_anchor',F(0),F(0),F(0),F(1),radius_sq)]
        lines = [('T_lower',F(1),F(0),lo),('T_upper',F(1),F(0),hi),
                 ('Z_lower',F(245),F(123),zlo),('Z_upper',F(245),F(123),zhi)]
        for tag,u,v,w in lines:
            points += circle_line(tag,u,v,w,radius_sq)
    for p in points:
        checks = evaluate(p,lo,hi,zlo,zhi)
        entry = p.tuple_json()|{"constraint_signs":checks}
        summary["tested"].append(entry)
        if all(z >= 0 for z in checks.values()):
            summary["feasible"]=True
            summary["witness"]=entry
            summary["reason"]="exact_algebraic_source_exists"
            return summary
    summary["reason"]="all_boundary_and_anchor_candidates_excluded"
    return summary


def observations_for_kT(k: F, T: F):
    return (K4+16*k+F(16,63)*T,
            K5+F(53,8)*k+F(61,504)*T)


def self_test():
    k=F(2); T=F(122); j4,j5=observations_for_kT(k,T)
    cvplus=F(5); cvminus=F(97357,37577)
    mid=(cvplus+cvminus)/2
    test_data=[
        ("exact_plus",(k,j4,F(0),j5,F(0),cvplus,F(0)),True),
        ("exact_minus",(k,j4,F(0),j5,F(0),cvminus,F(0)),True),
        ("exact_midpoint_impossible",(k,j4,F(0),j5,F(0),mid,F(1,100)),False),
        ("joint_noise_plus",(k,j4,F(1,10),j5,F(1,10),cvplus,F(1)),True),
        ("joint_noise_midpoint_impossible",(k,j4,F(1,10),j5,F(1,10),mid,F(1)),False),
        ("conflicting_port_strips",(k,j4,F(1,100),observations_for_kT(k,F(0))[1],F(1,100),F(1),F(100)),False),
        ("zero_k_yes",(F(0),K4,F(0),K5,F(0),F(1),F(0)),True),
        ("zero_k_no",(F(0),K4,F(0),K5,F(0),F(2),F(0)),False),
    ]
    output=[]
    for name,args,expected in test_data:
        result=solve(*args)
        assert result["feasible"] is expected, (name,result)
        output.append({"case":name, **result})
    delta=F(63,160)
    lip=F(2,N)*(F(245)+F(123*123,367))*delta
    gap=F(90528,37577)
    uniform_gap=gap-2*lip
    assert F(2*N)-(F(123)**2)>F(367)**2
    assert uniform_gap>2
    assert uniform_gap-2 == F(111190717,275815180)
    print('PASS_PREFIX400_EXACT_CIRCLE_LINE_BOUNDARY_FEASIBILITY 8_CASES')
    print('PASS_PREFIX400_UNIFORM_NOISY_SINGULAR_TWO_BRANCH_CV_SEPARATION')
    return {"cases":output,"nominal_cv_gap":str(gap),"T_max_deviation":str(delta),
            "per_branch_Cv_drift_bound":str(lip),"interbranch_gap_lower":str(uniform_gap),
            "post_eta1_margin":str(uniform_gap-2),
            "scope":"fixed exact I1,I2,Cu,I3; independent bounded I4,I5,Cv"}


def main():
    a=argparse.ArgumentParser()
    a.add_argument('--input',help='JSON with keys k,J4,xi4,J5,xi5,q,eta as rational strings')
    a.add_argument('--output',help='JSON output path')
    args=a.parse_args()
    if args.input:
        with open(args.input,encoding='utf-8') as f:
            v=json.load(f)
        result=solve(*(F(v[name]) for name in ('k','J4','xi4','J5','xi5','q','eta')))
    else:
        result=self_test()
    serialized=json.dumps(result,ensure_ascii=False,indent=2)
    if args.output:
        with open(args.output,'w',encoding='utf-8') as f:
            f.write(serialized+'\n')
    else:
        print(serialized)

if __name__=='__main__':
    main()
