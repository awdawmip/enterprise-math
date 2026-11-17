#!/usr/bin/env python3
"""R749STN: exact, reproducible two-time separation certificates.
The model and frozen pin are inherited without modification from R749STM.
Python 3 + SymPy; all arithmetic is rational/integer. No sampled real grid.
"""
import hashlib
import json
from functools import lru_cache
from itertools import product
from math import comb, factorial
from pathlib import Path
import sympy as s

N=s.Symbol('N'); J=s.Symbol('J'); e,d,E,D=s.symbols('e d E D')
PARAMS=(e,d,E,D)
WEIGHTS=(1,1,2,3,6)
def conv(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):z[i+j]+=v*w
    return z
def block(ws):
    z=[1]
    for w in ws:z=conv(z,[int(k%w==0) for k in range(7-w)])
    return z
QC=block((*WEIGHTS,1))
QT=conv([0,1],block((1,1,1,1,2,3,6)))
def falling(t,k):return s.prod(t-i for i in range(k))/factorial(k)
@lru_cache(None)
def quasi(r):
    C=s.Poly(s.expand(sum(a*falling((N-1-i)/6+5,5) for i,a in enumerate(QC) if (r-1-i)%6==0)),N)
    T=s.Poly(s.expand(sum(a*falling((N-1-i)/6+6,6) for i,a in enumerate(QT) if (r-1-i)%6==0)),N)
    return C,T
@lru_cache(None)
def CT(n):
    C,T=quasi(n%6)
    return s.Integer(C.eval(n)),s.Integer(T.eval(n))
def S(n):return 18*n**4+54*n**3-345*n**2+2070*n-16315

def numerator(q,h,j,formal=False):
    """108*den*(a*(Yqj-Ypj)+b*(Yq2j-Yp2j)), times 6*j if formal.
    den=(Cq1+d)*(Cq2+d)*(Cp1+D)*(Cp2+D)>0.
    """
    p=q+6*h
    q1,q2,p1,p2=q+6*j,q+12*j,p+6*j,p+12*j
    if formal:
        def at(v):
            c,t=quasi(q%6)
            return s.Poly(c.as_expr().subs(N,v),J),s.Poly(t.as_expr().subs(N,v),J)
        c1,t1=at(q1);c2,t2=at(q2);c3,t3=at(p1);c4,t4=at(p2)
        # multiplying by 6*j clears rational a,b coefficients
        a=s.Poly(12*J-(q+27),J)
        b=s.Poly(-24*J+4*(q+27),J)
    else:
        c1,t1=CT(q1);c2,t2=CT(q2);c3,t3=CT(p1);c4,t4=CT(p2)
        x=s.Rational(1,6*j)
        a=2-(q+27)*x; b=-4+4*(q+27)*x
    Q1,Q2,P1,P2=c1+d,c2+d,c3+D,c4+D
    total=Q1*Q2*P1*P2
    expression=(a*(108*q1**3*(t1+e)*Q2*P1*P2-108*p1**3*(t3+E)*Q1*Q2*P2-(S(q1)-S(p1))*total)
              +b*(108*q2**3*(t2+e)*Q1*P1*P2-108*p2**3*(t4+E)*Q1*Q2*P1-(S(q2)-S(p2))*total))
    return s.Poly(expression,J,*PARAMS) if formal else s.Poly(expression,*PARAMS)

def bernstein_rows(poly,j_origin=None):
    """For P(J,e,d,E,D), J=j_origin+t (t>=0), [-2,2]^4 -> [0,1]^4.
    For P(e,d,E,D), produce the single row for a fixed J.
    Rows are t-power coefficients, and columns are exact tensor Bernstein coefficients.
    """
    deg=tuple(poly.degree(v) for v in PARAMS)
    tdeg=poly.degree(J) if j_origin is not None else 0
    from collections import defaultdict
    power=defaultdict(lambda:s.Integer(0))
    for exps,coeff in poly.terms():
        pj=exps[0] if j_origin is not None else 0
        pp=exps[1:] if j_origin is not None else exps
        for t in range(pj+1):
            base=coeff*comb(pj,t)*(j_origin**(pj-t) if j_origin is not None else 1)
            for sub in product(*(range(v+1) for v in pp)):
                val=base
                for k,i in zip(pp,sub):val*=comb(k,i)*4**i*(-2)**(k-i)
                power[(t,*sub)]+=val
    rows=[]
    for t in range(tdeg+1):
        row=[]
        for idx in product(*(range(v+1) for v in deg)):
            val=0
            for sub in product(*(range(v+1) for v in idx)):
                x=power[(t,*sub)]
                for k,i,m in zip(idx,sub,deg):x*=s.Rational(comb(k,i),comb(m,i))
                val+=x
            row.append(val)
        rows.append(row)
    return deg,rows

def digest(rows):
    return hashlib.sha256(('\n'.join(','.join(str(c) for c in row) for row in rows)+'\n').encode('ascii')).hexdigest()

def exact_Y(n,ee,dd):
    C,T=CT(n)
    return n**3*(T+ee)/(C+dd)-s.Rational(S(n),108)

def verify_counts():
    max_n=7955
    part=[0]*(max_n+1);part[0]=1
    for w in WEIGHTS:
        for m in range(w,max_n+1):part[m]+=part[m-w]
    counts=[0]*(max_n+1);totals=[0]*(max_n+1)
    for m in range(1,max_n+1):
        counts[m]=counts[m-1]+part[m-1]
        totals[m]=totals[m-1]+counts[m-1]
    sample=set(range(29,241))
    for q,h,j in ((73,32,37),(77,1297,8)):
        sample.update((q+6*j,q+12*j,q+6*h+6*j,q+6*h+12*j))
    for j in range(1,8):sample.update((77+6*j,77+12*j,7859+6*j,7859+12*j))
    assert all(CT(i)==(counts[i],totals[i]) for i in sample)
    return len(sample)

def run():
    result={'unit':'R749STN','source_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'evidence':'AUTHOR_EXACT_NOT_REVIEWED','model_weights':WEIGHTS,
        'count_crosschecks':verify_counts(),'family_certificates':[]}
    total_positive=0
    for q,h,cut,small,eta in [(73,32,37,(),s.Rational(1,120)),(77,1297,8,range(1,8),s.Rational(1,20))]:
        deg,rows=bernstein_rows(numerator(q,h,J,formal=True),cut)
        assert deg==(1,2,1,2) and len(rows)==20 and all(len(r)==36 for r in rows)
        assert all(x>0 for row in rows for x in row)
        total_positive+=sum(len(r) for r in rows)
        extras=[]
        for j in small:
            sd,rs=bernstein_rows(numerator(q,h,j))
            assert sd==deg and len(rs)==1 and len(rs[0])==36
            assert all(v>0 for v in rs[0]);total_positive+=36
            extras+=rs
        # At the indicated first time, all parameter choices have Jhat>=L>0.
        static_deg,static_rows=bernstein_rows(numerator(q,h,cut))
        assert static_deg==deg and all(v>0 for v in static_rows[0])
        four=(q+6*cut,q+12*cut,q+6*h+6*cut,q+6*h+12*cut)
        den_max=s.prod(CT(n)[0]+2 for n in four)
        L=min(static_rows[0])*cut**2/(12960*den_max)
        x=s.Rational(1,6*cut);a=2-(q+27)*x;b=-4+4*(q+27)*x
        noise=2*eta*(abs(a)+abs(b))/(4320*x*x)
        assert L>noise>0
        # Check exact numerator identity against raw Y observations at sample parameters.
        probe=(s.Rational(1,2),-1,s.Rational(3,2),2)
        ev,dv,Ev,Dv=probe
        F1=exact_Y(four[0],ev,dv)-exact_Y(four[2],Ev,Dv)
        F2=exact_Y(four[1],ev,dv)-exact_Y(four[3],Ev,Dv)
        den=s.prod(CT(v)[0]+(dv if i<2 else Dv) for i,v in enumerate(four))
        direct=numerator(q,h,cut).eval(dict(zip(PARAMS,probe)))
        assert direct==108*den*(a*F1+b*F2)
        result['family_certificates'].append({
          'pair':[q,q+6*h],'all_j_from':cut,'smaller_j_covered':list(small),
          'halfline_t_degree':19,'nuisance_bernstein_degree':deg,
          'halfline_positive_coefficients':len(rows)*36,
          'finite_positive_coefficients':len(extras)*36,
          'all_positive_exact':True,'halfline_coefficient_sha256':digest(rows),
          'finite_coefficient_sha256':digest(extras) if extras else None,
          'Jhat_lower_at_start':str(L),'L_gt': '83/100' if q==73 else '34/100',
          'raw_readout_noise_eta_allowed_at_start':str(eta),
          'numerator_identity_test':'EXACT_PASS'})
        assert L > (s.Rational(83,100) if q==73 else s.Rational(34,100))
    negative_zero=[]
    for j in range(1,37):
        P=numerator(73,32,j)
        neg=P.eval({e:-2,d:2,E:2,D:-2})
        pos=P.eval({e:2,d:-2,E:-2,D:2})
        assert neg<0<pos
        negative_zero.append(j)
    result['early_separator_sign_change_j']=negative_zero
    result['positive_Bernstein_coefficients_total']=total_positive
    assert total_positive==1692
    # Not a proof that both individual readouts collide at earlier indices.
    result['scope_note']='Positivity proves strict separation for the specified two-time linear statistic; early sign changes concern this statistic only.'
    dest=Path(__file__).with_name('R749STN_TWO_READ_BERNSTEIN_RESULTS.json')
    dest.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print('PASS positive coefficients',total_positive,'crosschecks',result['count_crosschecks'])
    for v in result['family_certificates']:
        print(v['pair'],'j>=',v['all_j_from'],'L=',v['Jhat_lower_at_start'][:35],
          'eta=',v['raw_readout_noise_eta_allowed_at_start'])
    print('PASS early stat sign changes: 36/36; JSON bytes:',dest.stat().st_size)
if __name__=='__main__':run()
