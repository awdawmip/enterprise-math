#!/usr/bin/env python3
"""Exact/regression checker for the inert finite-Clausen derivative bridge.

This checker verifies finite identities and bounded prime regression only.
It is not a proof of the all-prime target.
"""
from __future__ import annotations
import argparse, json
from math import comb, factorial
from pathlib import Path

def primes_upto(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    if n >= 0: sieve[0:1] = b"\x00"
    if n >= 1: sieve[1:2] = b"\x00"
    for q in range(2, int(n**0.5) + 1):
        if sieve[q]:
            sieve[q*q:n+1:q] = b"\x00" * (((n-q*q)//q)+1)
    return [i for i in range(2, n+1) if sieve[i]]

def inv(a: int, m: int) -> int:
    return pow(a % m, -1, m)

def chi3(p: int) -> int:
    return 1 if p % 3 == 1 else -1

def vp_int(x: int, p: int, cap: int = 99) -> int:
    if x == 0:
        return cap
    v = 0
    while x % p == 0:
        x //= p
        v += 1
    return v

def b_list(p: int, power: int = 3) -> list[int]:
    """B_k=(1/6)_k(1/3)_k/(k!)^2 * 2^-k modulo p^power."""
    M = p**power
    out = [1]
    for k in range(p-1):
        num = (6*k+1)*(3*k+1)
        den = 36*(k+1)*(k+1)
        out.append(out[-1] * (num % M) * inv(den, M) % M)
    return out

def a3_list(p: int, power: int = 3) -> list[int]:
    """a_k=binom(2k,k)^2 binom(3k,k)/216^k modulo p^power."""
    M = p**power
    out = [1]
    for k in range(p-1):
        num = (2*k+1)*(3*k+1)*(3*k+2)
        den = 36*(k+1)**3
        out.append(out[-1] * (num % M) * inv(den, M) % M)
    return out

def target_sum(p: int) -> int:
    M = p**3
    a = a3_list(p, 3)
    return sum((6*k+1)*a[k] for k in range(p)) % M

def finite_clausen_data(p: int) -> dict:
    M = p**3
    B = b_list(p, 3)
    G = sum(B) % M
    H = sum((12*k+1)*B[k] for k in range(p)) % M
    T = 0
    U = 0
    for i in range(p):
        for j in range(p):
            if i+j >= p:
                U = (U + B[i]*B[j]) % M
                T = (T + (1+6*(i+j))*B[i]*B[j]) % M
    S = (G*H-T) % M
    return {"G":G, "H":H, "T":T, "U":U, "S_from_GH_T":S}

def predicted_b_valuation(p: int, k: int) -> int:
    if p % 6 == 1:
        m=(p-1)//6
        if k <= m: return 0
        if k <= 2*m: return 1
        return 2
    m=(p-5)//6
    if k <= 4*m+3: return 0
    if k <= 5*m+4: return 1
    return 2

def C_reflect(p: int, r: int) -> int:
    """For p=6m+1: B_{p-r}/p^2 mod p."""
    num = pow(2, r-1, p) * (factorial(r-1) % p)**2 % p
    den = 18 % p
    i6 = inv(6,p); i3=inv(3,p)
    for s in range(r):
        den = den * ((6*s+5)*i6 % p) % p
        den = den * ((3*s+2)*i3 % p) % p
    return num * inv(den,p) % p

def reduced_tail_plus(p: int) -> int:
    """p=6m+1 coefficient R_p with T_p = p^2 R_p (mod p^3)."""
    assert p % 6 == 1
    m=(p-1)//6
    Bp=b_list(p,1)
    R=0
    for i in range(1,m+1):
        inner=0
        for r in range(1,i+1):
            inner=(inner+(1+6*(i-r))*C_reflect(p,r))%p
        R=(R+2*Bp[i]*inner)%p
    return R

def block_tail_minus(p: int) -> dict:
    """p=6m+5 tail block decomposition modulo p^3."""
    assert p % 6 == 5
    M=p**3; B=b_list(p,3); m=(p-5)//6
    I0=range(0,4*m+4); I1=range(4*m+4,5*m+5); I2=range(5*m+5,p)
    sets=[set(I0),set(I1),set(I2)]
    acc=[[0]*3 for _ in range(3)]
    for i in range(p):
        bi=0 if i in sets[0] else (1 if i in sets[1] else 2)
        for j in range(p):
            if i+j < p: continue
            bj=0 if j in sets[0] else (1 if j in sets[1] else 2)
            acc[bi][bj]=(acc[bi][bj]+(1+6*(i+j))*B[i]*B[j])%M
    return {
        "T00":acc[0][0],
        "T01_twosided":(acc[0][1]+acc[1][0])%M,
        "T02_twosided":(acc[0][2]+acc[2][0])%M,
        "T11":acc[1][1],
        "T12_twosided":(acc[1][2]+acc[2][1])%M,
        "T22":acc[2][2],
        "total":sum(sum(row) for row in acc)%M,
    }

def run(target_bound: int, tail_bound: int) -> dict:
    inert=[p for p in primes_upto(target_bound) if p>3 and p%24 in (13,17,19,23)]
    target_fail=[]
    for p in inert:
        want=(p*chi3(p))%(p**3)
        got=target_sum(p)
        if got!=want:
            target_fail.append({"p":p,"got":got,"want":want})

    tail_primes=[p for p in inert if p<=tail_bound]
    tail_fail=[]; plus_rows=[]; minus_rows=[]
    for p in tail_primes:
        M=p**3
        B=b_list(p,3)
        for k,b in enumerate(B):
            pred=predicted_b_valuation(p,k)
            got=vp_int(b,p)
            if min(got,3)!=pred:
                tail_fail.append({"kind":"B_VAL","p":p,"k":k,"got":got,"pred":pred})
                break
        d=finite_clausen_data(p)
        s0=target_sum(p)
        if d["S_from_GH_T"]!=s0:
            tail_fail.append({"kind":"FINITE_CLAUSEN","p":p,"lhs":d["S_from_GH_T"],"rhs":s0})
        if p%6==1:
            m=(p-1)//6
            support_bad=0
            for i in range(p):
                for j in range(p):
                    if i+j<p: continue
                    vi=predicted_b_valuation(p,i); vj=predicted_b_valuation(p,j)
                    survives=(vi+vj<3)
                    expected=((i<=m and j>=2*m+1) or (j<=m and i>=2*m+1))
                    if survives!=expected:
                        support_bad+=1
            R=reduced_tail_plus(p)
            if d["T"]!=(p*p*R)%M:
                tail_fail.append({"kind":"REFLECTION_TAIL","p":p,"T":d["T"],"R":R})
            plus_rows.append({"p":p,"T_mod_p3":d["T"],"T_over_p2_mod_p":R,"support_bad":support_bad})
        else:
            blocks=block_tail_minus(p)
            if blocks["total"]!=d["T"]:
                tail_fail.append({"kind":"BLOCK_TOTAL","p":p})
            if blocks["T12_twosided"]%M or blocks["T22"]%M:
                tail_fail.append({"kind":"HIGH_BLOCK_NONZERO","p":p,"blocks":blocks})
            minus_rows.append({
                "p":p,
                **blocks,
                "vp_T00":vp_int(blocks["T00"],p),
                "vp_T01_twosided":vp_int(blocks["T01_twosided"],p),
                "vp_T02_twosided":vp_int(blocks["T02_twosided"],p),
                "vp_T11":vp_int(blocks["T11"],p),
            })

    return {
        "schema":"ENTERPRISE_BRC_HALF_COUPLING_INERT_FINITE_CLAUSEN_REGRESSION_V1",
        "target_bound":target_bound,
        "tail_bound":tail_bound,
        "inert_prime_count":len(inert),
        "tail_prime_count":len(tail_primes),
        "target_failures":target_fail,
        "tail_identity_failures":tail_fail,
        "plus_class_rows":plus_rows,
        "minus_class_rows":minus_rows,
        "status":"PASS" if not target_fail and not tail_fail else "FAIL",
        "proof_status":"FINITE_REGRESSION_ONLY_NOT_A_PROOF",
    }

def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument("--target-bound",type=int,default=10000)
    ap.add_argument("--tail-bound",type=int,default=250)
    ap.add_argument("--json-out")
    args=ap.parse_args()
    data=run(args.target_bound,args.tail_bound)
    text=json.dumps(data,ensure_ascii=False,indent=2)
    if args.json_out:
        Path(args.json_out).write_text(text+"\n",encoding="utf-8")
    print(text)
    return 0 if data["status"]=="PASS" else 1

if __name__=="__main__":
    raise SystemExit(main())
