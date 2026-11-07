#!/usr/bin/env python3
"""Exact Bernstein certificate: 23-term raw signed-BRC K3 corank-11 PF2 phase.

Run python R379_compute.py first. Uses exact integer/Fraction signs, never
floating-point sampling for universal inequalities.
"""
from __future__ import annotations
import json, hashlib
from fractions import Fraction as F
from pathlib import Path
from math import comb
from functools import reduce
HERE=Path(__file__).resolve().parent
Z=json.loads((HERE/'R379_COEFFICIENTS.json').read_text())
assert Z['schema']=='EM_R379_CORANK11_RAW_SIGNED_K3_V1'
assert Z['r']==11 and Z['joint_digest']=='6b710854cad0b921ff82e8ac47ad66f7649ec9db9833b0dfe178d31c143b2e1e'
C=[[int(q) for q in p] for p in Z['c_desc']]
T=[[int(q) for q in p] for p in Z['T_desc']]
assert len(C)==23 and len(T)==21

def evalp(p,x):
    return reduce(lambda a,z:a*x+z,p,F(0))

def bern(p,l,r):
    assert r>l
    asc=[]
    for val in p:
        out=[F(0)]*(len(asc)+1)
        for i,a in enumerate(asc):out[i]+=a*l;out[i+1]+=a*(r-l)
        out[0]+=val;asc=out
    n=len(asc)-1
    return [sum(asc[i]*F(comb(k,i),comb(n,i)) for i in range(k+1)) for k in range(n+1)]

LOG=[];TOTAL_CHECKS=0;TOTAL_POS=0;MAX_DEPTH=0;SEGHASH=hashlib.sha256()
def cert(label,p,l,r,sign=1,depth_limit=22):
    global TOTAL_CHECKS,TOTAL_POS,MAX_DEPTH
    l,r=F(l),F(r);assert r>l
    stack=[(l,r,0)];passseg=[]
    while stack:
        a,b,d=stack.pop()
        qs=bern([sign*z for z in p],a,b)
        TOTAL_CHECKS+=1
        if all(x>0 for x in qs):
            passseg.append((a,b,d,len(qs)))
            TOTAL_POS+=len(qs);MAX_DEPTH=max(MAX_DEPTH,d)
            for x in qs:SEGHASH.update(f'{label}:{sign}:{a}:{b}:{x.numerator}/{x.denominator}\n'.encode())
        else:
            if d>=depth_limit:
                raise AssertionError(f'NONSTRICT_SIGN {label} [{a},{b}] {sign} depth {d}')
            m=(a+b)/2;stack.append((m,b,d+1));stack.append((a,m,d+1))
    passseg.sort(key=lambda z:z[0]);assert passseg and passseg[0][0]==l and passseg[-1][1]==r
    assert all(passseg[i][1]==passseg[i+1][0] for i in range(len(passseg)-1))
    LOG.append({'object':label,'sign':sign,'domain':[str(l),str(r)],'segments':[[str(a),str(b),depth,n] for a,b,depth,n in passseg]})
    print('CERTIFIED',label,sign,str(l),str(r),'segments',len(passseg),flush=True)

def verify():
    a=F(1843323,1000000);b=F(1843324,1000000)
    assert evalp(T[10],a)>0 and evalp(T[10],b)<0
    for j,p in enumerate(C):cert(f'c{j}',p,-1,b)
    for j,p in enumerate(T,1):cert(f'T{j}',p,-1,a if j==11 else b)
    degree=len(T[10])-1
    der=[coef*(degree-i) for i,coef in enumerate(T[10][:-1])]
    cert('-T11_prime',der,a,b,-1)
    cert('-T11',T[10],b,F(1856,1000),-1)
    cert('-c11',C[11],F(1856,1000),F(198,100),-1)
    cert('-c5',C[5],F(198,100),F(23,10),-1)
    cert('-c4',C[4],F(23,10),F(31,10),-1)
    cert('-c0',C[0],F(31,10),F(4),-1)
    asc=[]
    for z in [-q for q in C[0]]:
        nv=[F(0)]*(len(asc)+1)
        for i,v in enumerate(asc):nv[i]+=4*v;nv[i+1]+=v
        nv[0]+=z;asc=nv
    assert len(asc)==8 and all(t>0 for t in asc)
    for x in asc:SEGHASH.update(f'-c0_tail_shift_4:{x.numerator}/{x.denominator}\n'.encode())
    import sys
    sys.path.insert(0,str(HERE.parent/'r369_signed_k3_branch_top_catalan_20261029_emr3'))
    from R369_check import compute_rows
    cross=0
    for th in (F(-1,2), F(0), F(1)):
        rows,_=compute_rows(th,11)
        assert len(rows[11])==23
        for j,v in enumerate(rows[11]):
            assert v==evalp(C[j],th),(th,j)
            cross+=1
    assert cross==69
    from sympy import symbols, expand
    th=symbols('theta')
    assert expand(sum(z*th**i for i,z in enumerate(reversed(C[-1]))) - 58786*(30-16*th)**22)==0
    th0=F(15,8)
    collapse={'zero':[j for j,p in enumerate(C) if evalp(p,th0)==0],
              'negative':[j for j,p in enumerate(C) if evalp(p,th0)<0]}
    assert collapse=={'zero':list(range(12,23)),'negative':[10,11]}
    lo,hi=a,b
    for _ in range(75):
        mid=(lo+hi)/2
        if evalp(T[10],mid)>0:lo=mid
        elif evalp(T[10],mid)<0:hi=mid
        else:lo=hi=mid;break
    assert evalp(T[10],lo)>=0>=evalp(T[10],hi)
    out={'schema':'R379_SIGNED_K3_CORANK11_GLOBAL_PF2_V1','r':11,
         'status':'R379_EXACT_PASS','source_joint_digest':Z['joint_digest'],
         'model':'original R346 signed 12 K/J branches, only K3[t2]=-8(1+theta)',
         'statement':'The finite 23-entry raw-D corank11 Newton observation has PF2 iff -1<theta<=eta11',
         'theta_domain':'>-1','eta11':'unique root of T11 in (1843323/1e6,1843324/1e6)',
         'bracket_signs':[str(evalp(T[10],a)),str(evalp(T[10],b))],
         'refined_root_bracket':[str(lo),str(hi)],
         'root_approx_display':str(float((lo+hi)/2)),
         'negative_cover':[['-T11',str(b),str(F(1856,1000))],['-c11',str(F(1856,1000)),str(F(198,100))],
                           ['-c5',str(F(198,100)),str(F(23,10))],['-c4',str(F(23,10)),str(F(31,10))],
                           ['-c0',str(F(31,10)),str(F(4))],['-c0','4','infinity']],
         'tail_shift_4_minus_c0_coefficients_ascending':[str(x) for x in asc],
         'interval_objects':len(LOG),'certified_segments':sum(len(z['segments']) for z in LOG),
         'bernstein_checks':TOTAL_CHECKS,'bernstein_positive_coefficients':TOTAL_POS,
         'max_subdivision_depth':MAX_DEPTH,'certificate_sha256':SEGHASH.hexdigest(),
         'independent_r369_point_equalities':cross,'collapse_at_15_8':collapse,'certificates':LOG,
         'scope':'finite 23 signed-raw-D observations; NOT global Q, original D TP2, native X6 or mathematical admission',
         'author_status':'UNREVIEWED / NOT_ADMITTED'}
    assert len(LOG)==50 and out['certified_segments']==53 and TOTAL_CHECKS==56 and TOTAL_POS==1465
    assert MAX_DEPTH==3 and SEGHASH.hexdigest()=='171a70128cfdc84c306c5fa8c20d001a64091fde0093188bf6db2927e1ee5f5e'
    (HERE/'R379_EVIDENCE.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print('R379_EXACT_PASS','eta11≈',f'{float((lo+hi)/2):.14f}',
          'segments',out['certified_segments'],'positive_bernstein',TOTAL_POS,'cross',cross,'collapse',collapse,flush=True)
    return out
if __name__=='__main__':verify()
