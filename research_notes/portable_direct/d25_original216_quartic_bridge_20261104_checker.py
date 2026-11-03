#!/usr/bin/env python3
"""D25 author-side exact p^3 two-family bridge/valuation-band checker.
Guo--Zudilin quartic theorem: see Zhi-Hong Sun, AIMS Math 7 (2022),
Remark 5.4; computation does not prove the cross-family bridge.
No native H0/B0 experiment is attempted.
"""
import json
from math import comb
from pathlib import Path

def primes_upto(n):
    sieve=bytearray(b"\x01")*(n+1)
    sieve[:2]=b"\x00\x00"
    for i in range(2,int(n**.5)+1):
        if sieve[i]:
            sieve[i*i:n+1:i]=b"\x00"*(((n-i*i)//i)+1)
    return [k for k in range(5,n+1) if sieve[k]]

def coefficient_bands(p):
    m=p**3
    a=b=1
    A=[0,0,0,0]
    B=[0,0,0,0]
    for k in range(p):
        alpha=2*k//p + 3*k//p
        beta=4*k//p
        A[min(alpha,3)]=(A[min(alpha,3)]+(6*k+1)*a)%m
        B[min(beta,3)]=(B[min(beta,3)]+(8*k+1)*b)%m
        if k<p-1:
            d1=36*(k+1)**3
            d2=2304*(k+1)**4
            a=a*(2*k+1)*(3*k+1)*(3*k+2)*pow(d1,-1,m)%m
            b=b*(4*k+1)*(4*k+2)*(4*k+3)*(4*k+4)*pow(d2,-1,m)%m
    assert A[3]==B[3]==0
    return A[:3],B[:3]

def direct_sum(p,flavor):
    mod=p**3
    a=0
    for k in range(p):
        if flavor=="W":
            num=comb(2*k,k)**2*comb(3*k,k)
            den=216
            weight=6*k+1
        elif flavor=="V":
            num=comb(2*k,k)**2*comb(4*k,2*k)
            den=2304
            weight=8*k+1
        else: raise ValueError(flavor)
        a=(a+weight*num*pow(den,-k,mod))%mod
    return a

def main():
    pp=primes_upto(2000)
    stats={x:0 for x in ("full_bridge_equal","V_guo_zudilin","B2_zero","A2_nonzero",
                         "layer0_distinct","layer1_distinct","layer0_same_mod_p")}
    samples={}
    checked=[5,7,11,13,19,37,73,373]
    for p in pp:
        A,B=coefficient_bands(p)
        mod=p**3
        chi=1 if p%3==1 else -1
        results={
          "full_bridge_equal":sum(A)%mod==sum(B)%mod,
          "V_guo_zudilin":sum(B)%mod==(chi*p)%mod,
          "B2_zero":B[2]==0,
          "A2_nonzero":A[2]!=0,
          "layer0_distinct":A[0]!=B[0],
          "layer1_distinct":A[1]!=B[1],
          "layer0_same_mod_p":A[0]%p==B[0]%p
        }
        for key,val in results.items(): stats[key]+=int(val)
        assert results["full_bridge_equal"] and results["V_guo_zudilin"]
        if p in checked:
            directA=direct_sum(p,"W")
            directB=direct_sum(p,"V")
            assert directA==sum(A)%mod and directB==sum(B)%mod
            samples[str(p)]={
              "modulus":mod,"W_val_0_1_2":A,"V_val_0_1_2":B,
              "W_minus_V_by_port":[(A[j]-B[j])%mod for j in range(3)],
              "W_direct":directA,"V_direct":directB,
              "A2_quotient_mod_p":A[2]//(p*p)
            }
    result={
      "status":"AUTHOR_DERIVED_EXACT_SCOPED_LEMMA_AND_FINITE_EXPERIMENT_UNREVIEWED_NOT_ADMITTED",
      "prime_domain":"all 301 primes 5<=p<=2000",
      "count":len(pp),
      "stats":stats,"samples":samples,
      "arithmetic":"exact modular integer recurrence and independent binomial crosscheck",
      "mathematical_target_not_proven":"W_(p-1) == V_(p-1) mod p^3 for all primes p>=5",
      "native_H0_B0_experiment":"NOT_EXECUTED"
    }
    path=Path(__file__).with_name("d25_original216_quartic_bridge_20261104_results.json")
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"count":len(pp),"stats":stats,"samples":samples},indent=2))

if __name__=="__main__":main()
