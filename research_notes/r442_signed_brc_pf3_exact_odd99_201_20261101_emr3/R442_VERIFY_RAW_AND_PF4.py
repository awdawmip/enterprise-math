#!/usr/bin/env python3
"""Independent raw signed-convolution input audit and exact PF4 negative witnesses."""
from math import comb,gcd
from itertools import permutations
from functools import reduce
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parent

def B(n,k): return comb(n,k) if 0<=k<=n else 0

def h_signed(r,s):
    return B(r+s,2*s)*sum(B(r-s,q)*(B(2*s,r-2*q)-B(2*s,r-2*q-1)) for q in range(r-s+1))

def perm_det(matrix):
    n=len(matrix)
    tot=0
    for p in permutations(range(n)):
        neg=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))%2
        v=1
        for i,j in enumerate(p):v*=matrix[i][j]
        tot+=(-1 if neg else 1)*v
    return tot

rows=[];tested=0;negatives=0;witness_bytes=[]
lines=(ROOT/'R442_INPUTS.txt').read_text().strip().splitlines()
for line in lines:
    words=line.split(); r=int(words[0]); n=int(words[1]); a=list(map(int,words[2:])); assert n==r-1==len(a)
    raw=[h_signed(r,r-i) for i in range(n)]
    assert all(v>0 for v in raw)
    g=reduce(gcd,raw)
    assert a==[v//g for v in raw],r
    tested+=n
    start=r-3
    mat=[[a[h] if 0<=h<n else 0 for h in (start+j-i for j in range(4))] for i in range(4)]
    d=perm_det(mat)
    assert d<0,r
    negatives+=1
    witness_line=f'{r} {start},{start+1},{start+2},{start+3} {d}'
    witness_bytes.append(witness_line)
    rows.append({'r':r,'raw_coefficient_checks':n,'gcd':str(g),'pf4_contiguous_columns':[start+i for i in range(4)],'pf4_det_sign':-1,'pf4_negative_det_decimal':str(d),'pf4_abs_bits':(-d).bit_length()})
output='\n'.join(witness_bytes)+'\n'
(ROOT/'R442_PF4_NEGATIVE_WITNESSES.txt').write_text(output)
summary={'verified':True,'rows':len(rows),'raw_signed_coefficient_equalities':tested,'negative_pf4_witnesses':negatives,'pf4_witness_sha256':hashlib.sha256(output.encode()).hexdigest(),'first_row':rows[0],'last_row':rows[-1], 'witnesses':rows}
(ROOT/'R442_RAW_AND_PF4_EVIDENCE.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print('R442_RAW_AND_PF4_PASS',len(rows),tested,negatives,summary['pf4_witness_sha256'])
print('r99_PF4',str(rows[0]['pf4_negative_det_decimal'])[:150], 'bits',rows[0]['pf4_abs_bits'])
print('r201_PF4',str(rows[-1]['pf4_negative_det_decimal'])[:150],'bits',rows[-1]['pf4_abs_bits'])
