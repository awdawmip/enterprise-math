#!/usr/bin/env python3
"""Deterministic checks for the P022 q=3r-1 Franel boundary reduction."""
from __future__ import annotations
import argparse, hashlib, json, math, subprocess, tempfile
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "research_artifacts" / "P022_OBSERVATION_HISTORY_ARITHMETIC_CORE"
CPP = ART / "p022_franel_boundary_scan.cpp"
SUMMARY = ART / "scan_summary.json"
EXPECTED_CPP_SHA256 = "3527a151f9d92bc1a1fd58c1ff1bc0ff10acaee3e119694d2e25d9b9b04c0ca2"
EXPECTED_DEEP_STDOUT_SHA256 = "0e0e51f1470c6ba6070b4bf95df7927ed0a5a0fa34bba0ca346517211db6db74"

def franel_exact(n):
    return sum(math.comb(n,k)**3 for k in range(n+1))

def poch(a,k):
    z=Fraction(1,1)
    for j in range(k): z*=a+j
    return z

def whipple_half_exact(m):
    s=Fraction(0,1)
    for k in range(m+1):
        s += poch(Fraction(-m,1),k)*poch(Fraction(1,2)-m,k)*poch(Fraction(2*m+1,1),k)/(math.factorial(k)**3)
    return 4**m*s

def is_prime(n):
    if n<2:return False
    if n%2==0:return n==2
    d=3
    while d*d<=n:
        if n%d==0:return False
        d+=2
    return True

def franel_mod(n,p):
    c=1; total=1
    for k in range(n):
        c=c*(n-k)%p*pow(k+1,-1,p)%p
        total=(total+c*c%p*c)%p
    return total

def half_binomial_mod(m,q):
    s=0
    for k in range(m+1):
        t=math.comb(m,k)%q
        t=t*(math.comb(2*m+k-1,k)%q)%q
        t=t*(math.comb(2*m+k,k)%q)%q
        s=(s-t if k&1 else s+t)%q
    return s

def poch_mod(num,den,k,p):
    a=num*pow(den,-1,p)%p; z=1
    for j in range(k): z=z*((a+j)%p)%p
    return z

def half_pochhammer_mod(m,q):
    s=0; fact=1
    for k in range(m+1):
        if k: fact=fact*k%q
        b=poch_mod(1,3,k,q)
        t=(3*k+1)*poch_mod(-1,6,k,q)%q*b%q*b%q
        s=(s+t*pow(pow(fact,3,q),-1,q))%q
    return s

def candidate_rows(max_r):
    rows=[]
    for r in range(6,max_r+1,6):
        q=3*r-1
        if q%72 not in (17,35): continue
        if is_prime(2*r-1) and is_prime(2*r+1) and is_prime(q):
            rows.append((r,q,q%72,franel_mod(r,q)))
    return rows

def symbolic_checks():
    for m in range(1,13):
        rhs=whipple_half_exact(m)
        assert rhs.denominator==1 and rhs.numerator==franel_exact(2*m)
    for m in range(1,80):
        q=6*m-1
        if not is_prime(q): continue
        f=franel_mod(2*m,q); b=half_binomial_mod(m,q); h=half_pochhammer_mod(m,q)
        assert f==pow(4,m,q)*b%q and b==h
    q=149; m=25
    assert q==6*m-1 and q%72==5
    assert franel_mod(2*m,q)==0 and half_binomial_mod(m,q)==0
    assert all(franel_mod(n,q)!=0 for n in range(1,2*m))
    def vp(x,p):
        v=0
        while x%p==0:
            x//=p; v+=1
        return v
    assert vp(franel_exact(50),149)==1
    assert vp(franel_exact(98),149)==1

def shallow_pressure():
    rows=candidate_rows(20_000)
    assert len(rows)==53
    assert all(z!=0 for *_,z in rows)
    assert sum(c==17 for _,_,c,_ in rows)==25
    assert sum(c==35 for _,_,c,_ in rows)==28
    for r,q,c,_ in rows:
        m=r//2
        if c==17:
            assert m%12==3 and (2*r+1)%8==5 and (2*r+1-1)//2==r
        else:
            assert m%12==6 and (2*r-1)%8==7 and (2*r-1-1)//2==r-1

def summary_checks():
    data=json.loads(SUMMARY.read_text())
    assert data["max_r"]==1_000_000
    assert data["candidate_count"]==891
    assert data["class_17_count"]==435
    assert data["class_35_count"]==456
    assert data["zero_residue_count"]==0
    assert data["scanner_sha256"]=="sha256:"+EXPECTED_CPP_SHA256
    assert data["stdout_tsv_sha256"]=="sha256:"+EXPECTED_DEEP_STDOUT_SHA256
    assert hashlib.sha256(CPP.read_bytes()).hexdigest()==EXPECTED_CPP_SHA256

def deep_reproduce():
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/"scan"
        subprocess.run(["g++","-O3","-std=c++17",str(CPP),"-o",str(exe)],check=True)
        p=subprocess.run([str(exe),"1000000"],check=True,capture_output=True,text=True)
        assert hashlib.sha256(p.stdout.encode()).hexdigest()==EXPECTED_DEEP_STDOUT_SHA256
        for token in ("candidates=891","class17=435","class35=456","zero_residues=0"):
            assert token in p.stderr

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--deep",action="store_true"); args=ap.parse_args()
    symbolic_checks(); shallow_pressure(); summary_checks()
    if args.deep: deep_reproduce()
    print("P022 boundary Franel reduction checks: PASS"+(" (deep)" if args.deep else ""))

if __name__=="__main__": main()
