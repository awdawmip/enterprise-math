#!/usr/bin/env python3
"""R398: a complete rational Bernstein certificate of the corank-26 PF2 phase.
Input polynomial source is r398_symbolic.py from original signed K/J recurrence.
All interval signs and endpoint comparisons exact Fraction; floating point only in display.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import comb
import hashlib,json
from pathlib import Path
from r398_symbolic import eval_poly
HERE=Path(__file__).resolve().parent
DATA=json.loads((HERE/'R398_POLYNOMIALS.json').read_text())
assert DATA['schema']=='EM_R398_CORANK26_SIGNED_K3_POLYNOMIALS_V1'
C=[tuple(map(int,x)) for x in DATA['C_ascending']]
T=[tuple(map(int,x)) for x in DATA['T_ascending']]
assert len(C)==53 and len(T)==51
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

def auto_cover(left,right):
    """Adaptive exact compact negative-witness cover: every accepted leaf has one p<0."""
    candidates=[('c'+str(j),p) for j,p in enumerate(C)]+[('T'+str(j),p) for j,p in enumerate(T,1)]
    todo=[(F(left),F(right),0)]
    leaves=[]
    while todo:
        a,b,d=todo.pop()
        mid=(a+b)/2
        useful=[]
        for label,p in candidates:
            if eval_poly(p,a)<0 and eval_poly(p,mid)<0 and eval_poly(p,b)<0:
                useful.append((len(p),label,p))
        useful.sort(key=lambda x:x[0])
        witness=None
        for _,label,p in useful:
            v=bern([-z for z in p],a,b)
            COUNTS['checked']+=1
            if all(z>0 for z in v):
                witness=(label,v); break
        if witness:
            label,v=witness
            leaves.append((a,b,label,d,len(v)))
            COUNTS['strict_positive_coeff']+=len(v)
            COUNTS['max_depth']=max(COUNTS['max_depth'],d)
            for z in v:
                H.update(f'{label}/-1/{a}/{b}/{z.numerator}/{z.denominator}\n'.encode())
        else:
            assert d < 20, ('negative cover gap',a,b)
            m=(a+b)/2
            todo.extend([(m,b,d+1),(a,m,d+1)])
    leaves.sort(key=lambda x:x[0])
    assert leaves[0][0]==F(left) and leaves[-1][1]==F(right)
    assert all(leaves[j][1]==leaves[j+1][0] for j in range(len(leaves)-1))
    LOG.append({'object':'negative_cover','sign':-1,'range':[str(F(left)),str(F(right))],
        'segments':[[str(a),str(b),label,d,n] for a,b,label,d,n in leaves]})
    print('NEGATIVE_COVER',len(leaves),flush=True)
    return leaves

def run():
    a,b=F(1869091,1000000),F(1869092,1000000)
    assert eval_poly(T[26],a)>0>eval_poly(T[26],b)
    for j,p in enumerate(C): cert('c'+str(j),p,F(-1),b)
    for j,p in enumerate(T,1): cert('T'+str(j),p,F(-1),a if j==27 else b)
    derivative=tuple(i*T[26][i] for i in range(1,len(T[26])))
    cert('-T27_prime',derivative,a,b,-1)
    # A second, isolated simple T27 crossing lies above the primary threshold.
    a2,b2=F(1880946,1000000),F(1880947,1000000)
    assert eval_poly(T[26],a2)<0<eval_poly(T[26],b2)
    cert('T27_secondary_prime_positive',derivative,a2,b2,+1)
    cert('c27_negative_secondary_window',C[27],a2,b2,-1)
    # Exact vanishing orders at the K3-degenerate point for every top coefficient.
    q=F(15,8)
    def vanishing_order(poly):
        f=tuple(poly)
        order=0
        while f and eval_poly(f,q)==0:
            order+=1
            f=tuple(j*f[j] for j in range(1,len(f)))
        assert f and eval_poly(f,q)!=0
        return order
    coeff_orders={str(j):vanishing_order(C[j]) for j in range(27,53)}
    turan_orders={str(j):vanishing_order(T[j-1]) for j in range(27,52)}
    assert all(coeff_orders[str(j)]==(3 if j==27 else 2*(j-26)) for j in range(27,53))
    assert all(turan_orders[str(j)]==4*(j-26) for j in range(27,52))
    assert vanishing_order(T[26])==4
    assert eval_poly(C[25],q)>0 and eval_poly(C[26],q)>0
    assert eval_poly(T[23],q)<0 and eval_poly(T[24],q)<0
    leaves=auto_cover(b,4)
    tail=shift(tuple(-z for z in C[0]),F(4))
    assert all(z>0 for z in tail)
    for z in tail:H.update(f'-c0_shift4:{z.numerator}/{z.denominator}\n'.encode())
    lo,hi=a,b
    for _ in range(85):
        mid=(lo+hi)/2
        if eval_poly(T[26],mid)>0:lo=mid
        else:hi=mid
    assert eval_poly(T[26],lo)>0>eval_poly(T[26],hi)
    from r398_exact import eval_at
    tests=['0','1/2','1','93/50','1869/1000','1870/1000','15/8']
    total=0
    for x in tests:
        raw=eval_at(F(x))
        for y,p in zip(raw['coeff'],C):assert y==eval_poly(p,F(x));total+=1
        for y,p in zip(raw['turan'],T):assert y==eval_poly(p,F(x));total+=1
    assert total==728
    collapse={'zero':[j for j,p in enumerate(C) if eval_poly(p,q)==0],
              'negative':[j for j,p in enumerate(C) if eval_poly(p,q)<0]}
    assert collapse['zero']==list(range(27,53))
    assert not collapse['negative']
    record={'schema':'EM_R398_CORANK26_GLOBAL_PF2_CERTIFICATE_V1','r':26,
            'status':'R398_EXACT_PASS','source_polynomial_sha256':DATA['polynomial_sha256'],
            'statement':'53-entry finite raw-D signed K3 corank-26 Newton sequence PF2 iff -1<theta<=eta26',
            'eta26':'unique zero of T27 on (1869091/1000000,1869092/1000000)',
            'root_bracket':[str(lo),str(hi)],'approx_display':str(float((lo+hi)/2)),
            'T27_value_at_15_8':str(eval_poly(T[26],q)),
            'coefficient_orders_at_15_8':coeff_orders,'turan_orders_at_15_8':turan_orders,
            'T27_secondary_root_bracket':[str(a2),str(b2)],
            'T27_secondary_root_simple':True,
            'c27_negative_secondary_window':True,
            'positive_C25_C26_and_negative_T24_T25_at_15_8':True,
            'bracket_signs':[str(eval_poly(T[26],a)),str(eval_poly(T[26],b))],
            'negative_cover':[[str(l),str(r),w] for l,r,w,_,_ in leaves]+[['c0','4','infinity']],
            'tail_shift4_c0_neg_coeff_ascending':[str(z) for z in tail],
            'certificate_count':len(LOG),'subinterval_count':sum(len(z['segments']) for z in LOG),
            'bernstein_calls':COUNTS['checked'],'bernstein_positive_coefficients':COUNTS['strict_positive_coeff'],
            'max_subdivision_depth':COUNTS['max_depth'],'certificate_sha256':H.hexdigest(),
            'independent_point_crosscheck_count':total,'theta_sample_parameters':tests,
            'degeneration_15_8':collapse,'certificates':LOG,
            'bounds':'finite raw D corank 26; no inference to global Q, all D TP2, native X6 or admission',
            'author_status':'UNREVIEWED / NOT_ADMITTED'}
    path=HERE/'R398_EVIDENCE.json';path.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    print('R398_EXACT_PASS', 'eta26≈', record['approx_display'], 'certificates',len(LOG),
      'segments',record['subinterval_count'], 'bernstein',COUNTS,'cross',total,'collapse',collapse)
    print('EVIDENCE_SHA256',hashlib.sha256(path.read_bytes()).hexdigest())
    return record
if __name__=='__main__':run()
