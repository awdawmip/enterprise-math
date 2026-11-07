#!/usr/bin/env python3
"""R426 exact signed-BRC Newton obstruction checker; Python standard library."""
import argparse
import json
from fractions import Fraction
from math import comb
from pathlib import Path


def c(n, j):
    return comb(n, j) if 0 <= j <= n else 0


def cat(k):
    return comb(2 * k, k) // (k + 1)


def delta_raw(r, s):
    # Keep the negative contribution of the original factor (1-t).
    return sum(comb(r - s, i) * (c(2*s, r-2*i) - c(2*s, r-2*i-1))
               for i in range(r-s+1))


def h_raw(r, s):
    return comb(r+s, 2*s) * delta_raw(r, s)


def delta_catalan(r, s):
    # [z^(r-1)] (1+2z)^(s-1) C(z^2)
    return sum(c(s-1,j) * 2**j * cat((r-1-j)//2)
               for j in range(min(r-1,s-1)+1) if (r-1-j)%2==0)


def q1(r):
    return (r-3)*h_raw(r,3)**2-2*(r-2)*h_raw(r,2)*h_raw(r,4)


def run(rmax):
    assert rmax >= 9
    checks = dict(raw_to_catalan=0, parity_formulas=0, ratio_identities=0,
                  newton_failures=0, full_coefficient_checks=0)
    witnesses={}
    for r in range(4,rmax+1):
        k=r//2
        a,b,d=[h_raw(r,s) for s in (2,3,4)]
        assert min(a,b,d)>0
        if r%2==0:
            u=Fraction(k,2*(2*k-3))
            expected=(2*cat(k-1),4*cat(k-1),(6+8*u)*cat(k-1))
            ratio=Fraction(112*(k-1)*(2*k+3),15*(k+2)*(8*k-9))
            threshold=Fraction(4*(k-1),2*k-3)
            assert 8*k*k+105*k-18>0
        else:
            u=Fraction(k+1,2*(2*k-1))
            expected=(cat(k),(1+4*u)*cat(k),(1+12*u)*cat(k))
            ratio=Fraction(28*(k+2)*(4*k+1)**2,
                           15*(k-1)*(2*k+5)*(8*k+5))
            threshold=Fraction(2*k-1,k-1)
            if k>=3:
                assert 32*k**3+140*k*k-476*k-431>0
        observed=tuple(delta_raw(r,s) for s in (2,3,4))
        assert observed==tuple(expected),(r,observed,expected)
        checks['parity_formulas']+=3
        assert Fraction(b*b,a*d)==ratio
        checks['ratio_identities']+=1
        if r!=5:
            assert ratio<threshold and q1(r)<0
            checks['newton_failures']+=1
        else:
            assert q1(5)==3528
        if r<=48:
            for s in range(2,r+1):
                assert delta_raw(r,s)==delta_catalan(r,s)>0
                checks['raw_to_catalan']+=1
                checks['full_coefficient_checks']+=1
        if r in (4,5,6,7,rmax):
            witnesses[str(r)]={
                "H2_H3_H4":[a,b,d], "j1_N":q1(r),
                "j1_ratio":f"{ratio.numerator}/{ratio.denominator}",
                "j1_required":f"{threshold.numerator}/{threshold.denominator}"
            }
    coeffs=[h_raw(5,s) for s in range(2,6)]
    assert coeffs==[70,168,126,42]
    q2=2*coeffs[2]**2-6*coeffs[1]*coeffs[3]
    assert q2==-10584
    checks['newton_failures']+=1
    witnesses["5"]["j2_N"]=q2
    assert [h_raw(4,s) for s in (2,3,4)]==[30,28,14]
    minor=28*(28*28-14*30)-14*(30*28)
    assert minor==-1568
    return {
        "schema":"R426_SIGNED_BRC_NEWTON_OBSTRUCTION_V1",
        "arithmetic":"exact Python integers and Fraction",
        "r_interval_checked":[4,rmax],
        "checks":checks, "r5_coefficients":coeffs,
        "r4_three_by_three_toeplitz_minor":minor,
        "witnesses":witnesses,
        "infinite_proof":"R426_PROOF.zh-CN.md algebraic parity inequalities",
        "status":"AUTHOR_SIDE_EXACT_CHECKED_NOT_ADMITTED"
    }


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--rmax",type=int,default=256)
    p.add_argument("--out",default="R426_EVIDENCE.json")
    args=p.parse_args()
    result=run(args.rmax)
    Path(args.out).write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("R426_EXACT_PASS",args.rmax,*result["checks"].values(),
          "r4_pf3",result["r4_three_by_three_toeplitz_minor"])


if __name__=="__main__":
    main()
