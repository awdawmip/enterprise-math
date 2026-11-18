#!/usr/bin/env python3
"""Recompute PREFIX-903 using the exact GitHub-pinned PREFIX-900 C++17 classifier.
Usage: python3 PREFIX903_R6_FOURTH_PANEL_CHECK.py SOURCE_CPP CERTIFICATE_CSV
Canonical C++ Git blob: 175aabe087718cc48ecc8e2f7492cef6731fc5ca.
"""
import csv
import hashlib
import json
import math
import pathlib
import subprocess
import sys
import tempfile

N, T = 1 << 32, 33 * (1 << 32)
Q = range(262145, 524288, 2)
S = {262147,280001,300001,320003,340007,360007,380003,400009,420001,
     440003,460001,480007,500383,510007,520001,524285}
U = S | set(range(400011,400522,2)) | set(range(480011,480522,2))
U |= {q for q in Q if any(((1<<h)-1)%q==0 or ((1<<h)+1)%q==0 for h in range(1,32))}
assert len(U) == 552

def E(a,b):
    return (a*b < T or a in U or b in U or
            a//math.gcd(a,b)*b < N or
            33*((N+a-1)//a)>b or 33*((N+b-1)//b)>a)

def witness(a,b,w):
    x,y,i,j=(w[k] for k in ('x','y','i','j'))
    assert 0<=x<N and 0<=y<N and 0<=i<32 and 0<=j<32
    assert (x,i)!=(y,j)
    assert x%a==y%a and (x^(1<<i))%b==(y^(1<<j))%b

def main():
    src=pathlib.Path(sys.argv[1]).read_bytes()
    blob=hashlib.sha1(f'blob {len(src)}\0'.encode()+src).hexdigest()
    assert blob=='175aabe087718cc48ecc8e2f7492cef6731fc5ca',blob
    with open(sys.argv[2], newline='') as f:
        rows=list(csv.DictReader(f))
    P=[510001+194*j for j in range(64)]+[510003+194*j for j in range(64)]
    P += [510005+194*j for j in range(64)]
    B=[510009+194*j for j in range(64)]
    P += B
    assert len(rows)==64 and len(set(P))==256 and not(set(P)&U)
    with tempfile.TemporaryDirectory() as d:
        exe=str(pathlib.Path(d)/'prefix900')
        subprocess.run(['g++','-O3','-std=c++17',sys.argv[1],'-o',exe],check=True)
        observed=[]
        for idx,a in enumerate(B):
            r=json.loads(subprocess.check_output([exe,str(a)]))
            cert=rows[idx]
            assert int(cert['q1'])==a==r['q1']
            for k in ('old_four_family','zf_new','anchored_ff_new','general_ff_new','unresolved'):
                assert int(cert[k])==r[k],(a,k,cert[k],r[k])
            assert r['unresolved']==0
            assert sum(r[k] for k in ('old_four_family','zf_new','anchored_ff_new','general_ff_new'))==len(Q)
            assert len(r['general_witnesses'])==r['general_ff_new']
            for w in r['general_witnesses']+r['anchored_examples']:
                witness(a,w['q2'],w)
            assert sum(E(a,b) for b in Q)==r['old_four_family']
            observed.append(r)
    EB=sum(r['old_four_family'] for r in observed)
    EP=507393+506797+505972
    EPP=sum(E(a,b) for a in P for b in P)
    EBP=sum(E(a,b) for a in B for b in P[:192])
    EBB=sum(E(a,b) for a in B for b in B)
    base=7567620214
    prior=7614875038
    after=base+2*(len(P)*len(Q)-EP-EB)-(len(P)**2-EPP)
    delta=2*(len(B)*len(Q)-EB-(len(B)*192-EBP))-(len(B)**2-EBB)
    assert EPP==594 and EBP==83 and EBB==64
    assert EB==505808 and after==7630612196 and delta==15737158
    assert after-prior==delta
    print(json.dumps({'panel_rows':len(rows),'all_resolved':True,'general_witnesses_checked':sum(r['general_ff_new'] for r in observed),
                      'old_B':EB,'E_PP':EPP,'E_BP':EBP,'E_BB':EBB,
                      'prior':prior,'delta':delta,'union':after,'uncovered':len(Q)**2-after},sort_keys=True))

if __name__=='__main__':
    main()
