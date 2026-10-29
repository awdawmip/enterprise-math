#!/usr/bin/env python3
"""R378: exact complete signed K3, raw-D corank-10 PF2 phase certificate.

Run after `python R378_compute.py`. No numerical sampling is used to infer a sign.
All finite intervals use exact rational Bernstein basis positivity; infinite tail
uses positive coefficients of shifted polynomial. Source R346 original K/J and
R369 B->L independent point-route are bundled in this project PR.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
from functools import reduce
from math import comb
import json, hashlib
HERE=Path(__file__).resolve().parent
X=json.loads((HERE/'R378_COEFFICIENTS.json').read_text())
assert X['r']==10 and X['joint_digest']=='a5fa8566861e5259d1a714df1c62661001657c94925fc6789fe730e110ac9915'
C=[[int(z) for z in p] for p in X['c_desc']]
T=[[int(z) for z in p] for p in X['T_desc']]
assert len(C)==21 and len(T)==19

def bernstein(desc,l,r):
    """Bernstein coefficients of exact p(l+(r-l)u) on u in [0,1]."""
    h=r-l
    asc=[]
    for z in desc:
        nxt=[F(0)]*(len(asc)+1)
        for i,v in enumerate(asc):
            nxt[i]+=v*l; nxt[i+1]+=v*h
        nxt[0]+=z
        asc=nxt
    n=len(asc)-1
    return [sum(asc[i]*F(comb(k,i),comb(n,i)) for i in range(k+1)) for k in range(n+1)]

def value(desc,x):
    return reduce(lambda a,z:a*x+z,desc,F(0))

N_CHECK=0;N_POS=0;MAX_DEPTH=0
LOG=[];HASH=hashlib.sha256()
def certified_intervals(label,p,l,r,sign=1,limit=20):
    """For each of finitely many dyadic segments all Bernstein coefficients >0."""
    global N_CHECK,N_POS,MAX_DEPTH
    stack=[(F(l),F(r),0)]
    ok=[]
    while stack:
        a,b,depth=stack.pop()
        q=bernstein([sign*z for z in p],a,b)
        N_CHECK+=1
        if all(z>0 for z in q):
            N_POS+=len(q);MAX_DEPTH=max(MAX_DEPTH,depth)
            ok.append((a,b,depth,len(q)))
            for z in q: HASH.update(f'{label}:{sign}:{a}:{b}:{z.numerator}/{z.denominator}\n'.encode())
        else:
            if depth>=limit:
                raise AssertionError(f'Cannot certify {label} sign={sign} on [{a},{b}] depth={depth}')
            m=(a+b)/2
            stack.append((m,b,depth+1));stack.append((a,m,depth+1))
    ok.sort(key=lambda p:p[0]);assert ok[0][0]==l and ok[-1][1]==r
    assert all(ok[i][1]==ok[i+1][0] for i in range(len(ok)-1))
    LOG.append({'object':label,'sign':sign,'domain':[str(l),str(r)],'segments':[[str(a),str(b),d,k] for a,b,d,k in ok]})
    return len(ok)

def verify():
    from sympy import Symbol, expand, binomial
    th=Symbol('theta')
    # Root in (a,b) of exact polynomial T11; no floats in proof.
    a=F(1844956,1000000)
    b=F(1844957,1000000)
    assert value(T[10],a)>0 and value(T[10],b)<0
    print('root signs passed',flush=True)
    # Prove positivity from -1 through root, even if a Bernstein interval
    # needs subdivision. This gives global positive support and all other
    # adjacent Turan defects in their required ranges.
    for j,p in enumerate(C):certified_intervals('c'+str(j),p,F(-1),b,1)
    for j,p in enumerate(T,1):certified_intervals('T'+str(j),p,F(-1),a if j==11 else b,1)
    d=[p*(len(T[10])-1-i) for i,p in enumerate(T[10][:-1])]
    certified_intervals('-T11_derivative',d,a,b,-1)
    # Negative witnesses cover (eta10, +infinity) without gaps.
    certified_intervals('T11',T[10],b,F(18749,10000),-1)
    certified_intervals('T9',T[8],F(18749,10000),F(188,100),-1)
    certified_intervals('c11',C[11],F(188,100),F(21,10),-1)
    certified_intervals('c5',C[5],F(21,10),F(13,5),-1)
    certified_intervals('c0',C[0],F(13,5),F(3),-1)
    # For theta >=3, -c0(3+y) has strictly positive coefficients.
    asc=[]
    for z in [-v for v in C[0]]:
        nx=[F(0)]*(len(asc)+1)
        for k,v in enumerate(asc):nx[k]+=3*v;nx[k+1]+=v
        nx[0]+=z;asc=nx
    assert len(asc)==8 and all(z>0 for z in asc)
    for q in asc:HASH.update(f'-c0_tail_shift_3:{q.numerator}/{q.denominator}\n'.encode())
    # Exact ten-degree collapse at theta=15/8; T9 remains negative.
    th_collapse=F(15,8)
    assert all(value(C[j],th_collapse)>0 for j in range(11))
    assert all(value(C[j],th_collapse)==0 for j in range(11,21))
    assert value(T[8],th_collapse)<0 and value(T[10],th_collapse)==0
    # Exact Catalan highest coefficient, follows R369 pattern.
    assert expand(sum(z*th**i for i,z in enumerate(reversed(C[-1]))) - int(binomial(20,10)/11)*(30-16*th)**20)==0
    # Independent original signed K/J -> B -> L numeric rational route.
    import sys
    sys.path.insert(0,str(HERE.parent/'r369_signed_k3_branch_top_catalan_20261029_emr3'))
    from R369_check import compute_rows
    point_count=0
    for t in (F(-1,2),F(0),F(1)):
        rows,_=compute_rows(t,10)
        assert len(rows[10])==21
        for j,z in enumerate(rows[10]):
            assert z==value(C[j],t),(t,j)
            point_count+=1
    assert point_count==63
    left,right=a,b
    for _ in range(70):
        middle=(left+right)/2
        if value(T[10],middle)>0:left=middle
        elif value(T[10],middle)<0:right=middle
        else:left=right=middle;break
    assert value(T[10],left)>=0 and value(T[10],right)<=0
    out={'schema':'R378_SIGNED_K3_CORANK10_GLOBAL_PF2_V1',
         'status':'R378_EXACT_PASS','source_joint_digest':X['joint_digest'],
         'r':10,'model':'Original R346 12 signed K/J, only K3[t2]=-8(1+theta)',
         'theta_domain':'theta>-1',
         'theorem':'finite 21 raw-D Newton observations PF2 iff -1<theta<=eta10',
         'eta10':'unique real root T11 on (1844956/1e6,1844957/1e6)',
         'root_sign_at_bracket':[str(value(T[10],a)),str(value(T[10],b))],
         'eta10_refined_bracket':[str(left),str(right)],
         'root_uniqueness':'-T11 prime strict positive on bracket; T11 positive before a',
         'negative_cover':[['T11',str(b),'18749/10000'],['T9','18749/10000','188/100'],['c11','188/100','21/10'],['c5','21/10','13/5'],['c0','13/5','3'],['c0','3','+infinity']],
         'tail_shifted_minus_c0_coeffs_ascending':[str(q) for q in asc],
         'interval_objects':len(LOG),'verified_bernstein_segments':sum(len(t['segments']) for t in LOG),
         'tested_bernstein_intervals':N_CHECK,'positive_bernstein_coefficients':N_POS,
         'max_depth':MAX_DEPTH,'exact_bernstein_digest':HASH.hexdigest(),
         'independent_r369_three_point_equalities':point_count,
         'collapse_at_15_over_8':'c0..c10>0, c11..c20=0, T9<0, T11=0',
         'certificates':LOG,
         'scope':'Finite raw D minors, not global D TP2, not all-index Q, not native X6, author-side UNREVIEWED NOT_ADMITTED'}
    (HERE/'R378_EVIDENCE.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print('R378_EXACT_PASS','root≈',f'{float((left+right)/2):.13f}',
          'segments',out['verified_bernstein_segments'],
          'rational signs',N_POS,'independent',point_count,flush=True)
    return out

if __name__=='__main__':verify()
