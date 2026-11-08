#!/usr/bin/env python3
"""PREFIX-611 BRC native-derived marked coin: exact coverage + Blackwell certificate.

Requires only the Python standard library. Uses PREFIX-610's original-native
likelihood result, NOT an independently rerun PREFIX-565 native graph check.
"""
import json
from collections import defaultdict
from fractions import Fraction
from math import comb
from pathlib import Path

SCIENCE_PIN = "f42f2906d77f24085c123f3ccfe9667d41caa96d"
NATIVE_BLOB = "7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41"
DEPENDENCY_COMMIT = "4bdeec79b72e184703390c74bbb020910340b97e"

def one_num(n,d,q):
    """Count q-letter words hitting every one of d special letters at least once."""
    assert 0<=n and 1<=d<=12 and d<=q
    return sum((-1)**j*comb(d,j)*(q-j)**n for j in range(d+1))

def two_num(n,d,q):
    """Count words hitting every special letter at least twice."""
    assert 0<=n and 1<=d<=12 and d<=q
    total=0
    for j in range(d+1):
        subtotal=0
        falling=1
        for a in range(min(j,n)+1):
            if a: falling*=n-a+1
            subtotal+=comb(j,a)*falling*(q-j)**(n-a)
        total+=(-1)**j*comb(d,j)*subtotal
    return total

def direct_dp(n,d,q,cap):
    """Independent integer dynamic program retaining truncated visit counts."""
    state=(0,)*d
    dp={state:1}
    for _ in range(n):
        nxt=defaultdict(int)
        for counts,ways in dp.items():
            nxt[counts]+=ways*(q-d)
            for ell in range(d):
                new=list(counts);new[ell]=min(cap,new[ell]+1)
                nxt[tuple(new)]+=ways
        dp=nxt
    assert sum(dp.values())==q**n
    return dp.get((cap,)*d,0)

def min_n(d,q,num,den,formula):
    assert 0<num<den
    good=lambda n: formula(n,d,q)*den>=num*q**n
    hi=1
    while not good(hi):hi*=2
    lo=0
    while lo+1<hi:
        mid=(lo+hi)//2
        if good(mid):hi=mid
        else:lo=mid
    assert good(hi) and not good(hi-1)
    return hi

def marked(theta,q):
    d=len(theta)
    assert 1<=d<=12 and d<=q and all(abs(t)<Fraction(1,48) for t in theta)
    p={"neutral":Fraction(q-d,q)}
    for ell,t in enumerate(theta):
        for sign in (-1,+1):
            p[(ell,sign)]=Fraction(1,2*q)*(1+48*sign*t)
    assert sum(p.values())==1 and all(x>=0 for x in p.values())
    return p

def thin(p):
    out={"neutral":p["neutral"]}
    for key,val in p.items():
        if key=="neutral":continue
        out[key]=val/2
        out["neutral"]+=val/2
    assert sum(out.values())==1
    return out

def tv(p,p2):
    return sum(abs(p[k]-p2[k]) for k in p)/2

def run():
    checks=0
    for d in (2,4,6,12):
        for q in (12,24):
            for n in range(9):
                value=one_num(n,d,q)
                assert 0<=value<=q**n
                if d<=6:
                    assert value==direct_dp(n,d,q,1)
                    checks+=1
                if n:
                    assert value*q**(n-1)>=one_num(n-1,d,q)*q**n
                checks+=1
    for d in (2,4):
        for q in (12,24):
            for n in range(11):
                assert two_num(n,d,q)==direct_dp(n,d,q,2)
                checks+=1
    threshold_rows=[]
    for d in (2,4,12):
        for q in (12,24):
            for num,den in ((95,100),(99,100)):
                row={"d":d,"q":q,"target":f"{num}/{den}"}
                row["minimum_one_hit"]=min_n(d,q,num,den,one_num)
                row["minimum_two_hits"]=min_n(d,q,num,den,two_num)
                threshold_rows.append(row)
                checks+=4
    tv_rows=[]
    for d in (2,4,12):
        theta=[Fraction((i%3)-1,1000) for i in range(d)]
        theta2=theta.copy();theta2[0]+=Fraction(1,10000)
        a=marked(theta,12);b=marked(theta2,12)
        c=marked(theta,24);e=marked(theta2,24)
        assert thin(a)==c and thin(b)==e
        assert tv(a,b)==2*abs(theta[0]-theta2[0])
        assert tv(c,e)==abs(theta[0]-theta2[0])
        checks+=4
        tv_rows.append({"d":d,"TV_slot0":str(tv(a,b)),"TV_slot1_or_2":str(tv(c,e))})
    assert checks==230
    result={
        "status":"ALL_CHECKS_PASS",
        "scope":"exact derived independent one-step sampling from PREFIX-610 native tagged-endpoint likelihood",
        "science_pin":SCIENCE_PIN,
        "original_native_blob":NATIVE_BLOB,
        "upstream_commit":DEPENDENCY_COMMIT,
        "one_hit":"q^-N * sum_j (-1)^j*C(d,j)*(q-j)^N",
        "two_hits":"q^-N * sum_j (-1)^j*C(d,j)*sum_a C(j,a)*(N)_a*(q-j)^(N-a)",
        "per_fiber_informative_probability":{"slot0":"1/12","slot1":"1/24","slot2":"1/24"},
        "sufficient_experiment":"P(l,sign)=(1+48 sign theta_l)/(2q); P(neutral)=1-d/q",
        "blackwell":"B0 strictly Blackwell dominates B1 and B2 by independent 1/2 deletion of marked signs",
        "TV_one_direction":{"slot0":"2*abs(delta_theta)","slot1":"abs(delta_theta)","slot2":"abs(delta_theta)"},
        "threshold_rows":threshold_rows,"rational_TV_witnesses":tv_rows,
        "checks":checks,"arithmetic":"integer and Fraction exact; separate occupancy DP",
        "native_source_reexecuted":False,
        "status_level":"AUTHOR_PROVED / EXACT_COMBINATORIAL_CHECKED / UNREVIEWED / NOT_ADMITTED"}
    Path(__file__).with_name("PREFIX611_R6_RESULTS.json").write_text(
        json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":result["status"],"checks":checks,"threshold_rows":threshold_rows},indent=2))

if __name__=="__main__":
    run()
