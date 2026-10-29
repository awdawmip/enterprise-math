#!/usr/bin/env python3
"""R382: a complete rational Bernstein certificate of the corank-14 PF2 phase.
Input polynomial source is r382_symbolic.py from original signed K/J recurrence.
All interval signs and endpoint comparisons exact Fraction; floating point only in display.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import comb
import hashlib,json
from pathlib import Path
from r382_symbolic import eval_poly
HERE=Path(__file__).resolve().parent
DATA=json.loads((HERE/'R382_POLYNOMIALS.json').read_text())
assert DATA['schema']=='EM_R382_CORANK14_SIGNED_K3_POLYNOMIALS_V1'
C=[tuple(map(int,x)) for x in DATA['C_ascending']]
T=[tuple(map(int,x)) for x in DATA['T_ascending']]
assert len(C)==29 and len(T)==27
LOG=[]
COUNTS={'checked':0,'strict_positive_coeff':0,'max_depth':0}
H=hashlib.sha256()

def bern(p,l,r):
    """Exact p(l+(r-l)t) in Bernstein(n) control point values."""
    assert r>l
    asc=[]
    for val in reversed(p):
        o=[F(0)]*(len(asc)+1)
        for i,a in enumerate(asc):
            o[i]+=a*l;o[i+1]+=a*(r-l)
        o[0]+=val; asc=o
    n=len(asc)-1
    return [sum(asc[i]*F(comb(k,i),comb(n,i)) for i in range(k+1)) for k in range(n+1)]

def cert(label,p,left,right,sign=1,depth_limit=18):
    left,right=F(left),F(right)
    assert left<right
    stk=[(left,right,0)]; segments=[]
    while stk:
        a,b,d=stk.pop()
        bs=bern([sign*x for x in p],a,b)
        COUNTS['checked']+=1
        if all(x>0 for x in bs):
            segments.append((a,b,d,len(bs)))
            COUNTS['strict_positive_coeff']+=len(bs)
            COUNTS['max_depth']=max(COUNTS['max_depth'],d)
            for x in bs:
                H.update(f'{label}/{sign}/{a}/{b}/{x.numerator}/{x.denominator}\n'.encode())
        else:
            if d>=depth_limit:raise AssertionError(f'failed {label} sign={sign} on [{a},{b}] at depth {d}')
            m=(a+b)/2; stk.extend([(m,b,d+1),(a,m,d+1)])
    segments.sort(key=lambda p:p[0])
    assert segments[0][0]==left and segments[-1][1]==right
    assert all(segments[i][1]==segments[i+1][0] for i in range(len(segments)-1))
    LOG.append({'object':label,'sign':sign,'range':[str(left),str(right)],'segments':[[str(a),str(b),d,n] for a,b,d,n in segments]})
    print('CERT',label,sign,'segments',len(segments),flush=True)

def shift(poly,s):
    # p(s+u), ascending powers u
    out=[]
    for val in reversed(poly):
        z=[F(0)]*(len(out)+1)
        for i,v in enumerate(out):z[i]+=s*v;z[i+1]+=v
        z[0]+=val;out=z
    return out

def run():
    a,b=F(1858090,1000000),F(1858091,1000000)
    assert eval_poly(T[14],a)>0>eval_poly(T[14],b)
    for j,p in enumerate(C):cert('c'+str(j),p,F(-1),b)
    for j,p in enumerate(T,1):cert('T'+str(j),p,F(-1),a if j==15 else b)
    d=tuple((i)*T[14][i] for i in range(1,len(T[14])))
    cert('-T15_prime',d,a,b,-1)
    neg=[
      ('T15',T[14],b,F(187,100)),
      ('T13',T[12],F(187,100),F(188,100)),
      ('c15',C[15],F(188,100),F(202,100)),
      ('c7',C[7],F(202,100),F(21,10)),
      ('c2',C[2],F(21,10),F(222,100)),
      ('c1',C[1],F(222,100),F(4))]
    for name,p,l,r in neg:cert('-'+name,p,l,r,-1)
    tail=shift(tuple(-z for z in C[1]),F(4))
    assert all(z>0 for z in tail)
    for x in tail:H.update(f'-c1_tail_shift_4:{x.numerator}/{x.denominator}\n'.encode())
    lo,hi=a,b
    for _ in range(80):
        mid=(lo+hi)/2
        if eval_poly(T[14],mid)>0:lo=mid
        else:hi=mid
    assert eval_poly(T[14],lo)>0>eval_poly(T[14],hi)
    # independent rational direct path over 7 sample parameters
    from r382_exact import eval_at
    tests=['0','1/2','9/10','901/1000','902/1000','1','15/8']
    total=0
    for x in tests:
        raw=eval_at(F(x))
        for y,poly in zip(raw['coeff'],C):assert y==eval_poly(poly,F(x));total+=1
        for y,poly in zip(raw['turan'],T):assert y==eval_poly(poly,F(x));total+=1
    assert total==392
    q=F(15,8)
    collapse={'zero':[j for j,p in enumerate(C) if eval_poly(p,q)==0],
              'negative':[j for j,p in enumerate(C) if eval_poly(p,q)<0],
              'negative_turan':[j+1 for j,p in enumerate(T) if eval_poly(p,q)<0]}
    assert collapse['zero']==list(range(15,29))
    assert 13 in collapse['negative_turan']
    record={'schema':'EM_R382_CORANK14_GLOBAL_PF2_CERTIFICATE_V1','r':14,
            'status':'R382_EXACT_PASS','source_polynomial_sha256':DATA['polynomial_sha256'],
            'statement':'29-entry finite raw-D signed K3 corank-14 Newton sequence PF2 iff -1<theta<=eta14',
            'eta14':'unique zero of T15 on (1858090/1000000,1858091/1000000)',
            'root_bracket':[str(lo),str(hi)],'approx_display':str(float((lo+hi)/2)),
            'bracket_signs':[str(eval_poly(T[14],a)),str(eval_poly(T[14],b))],
            'negative_cover':[[n,str(l),str(r)] for n,p,l,r in neg]+[['c1','4','infinity']],
            'tail_shift4_c1_neg_coeff_ascending':[str(z) for z in tail],
            'certificate_count':len(LOG),'subinterval_count':sum(len(z['segments']) for z in LOG),
            'bernstein_calls':COUNTS['checked'],'bernstein_positive_coefficients':COUNTS['strict_positive_coeff'],
            'max_subdivision_depth':COUNTS['max_depth'],'certificate_sha256':H.hexdigest(),
            'independent_point_crosscheck_count':total,'theta_sample_parameters':tests,
            'degeneration_15_8':collapse,'certificates':LOG,
            'bounds':'finite raw D corank 14; no inference to global Q, all D TP2, native X6 or admission',
            'author_status':'UNREVIEWED / NOT_ADMITTED'}
    path=HERE/'R382_EVIDENCE.json'; path.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    print('R382_EXACT_PASS', 'eta14≈', record['approx_display'], 'certificates',len(LOG), 'segments',record['subinterval_count'], 'bernstein',COUNTS, 'cross',total, 'collapse', collapse)
    print('EVIDENCE_SHA256',hashlib.sha256(path.read_bytes()).hexdigest())
    return record
if __name__=='__main__':run()
