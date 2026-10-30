#!/usr/bin/env python3
"""R416 independent degree-bounded certificate for s=29, standard library only.

For each parity, Delta_{q} = delta_(2m+parity,q) / Cat_(m-1+parity)
for q=28,29,30 is rational in m with denominator dividing a
14-linear-factor common product T(m), so its numerator has degree <= 14.
The normalized Turan rational function consequently has numerator and
 denominator degree <=30. Candidate P/Q from the uploaded certificate has
both degrees <=29, hence their cross difference degree <=59. Testing the
exact equality at 60 distinct values proves an identity over Q(m). The
exact positivity of every P and Q coefficient proves the universal sign.
"""
import json
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
S=29
N=60

def cat(n):
    assert n>=0
    return comb(2*n,n)//(n+1)

def delta(r,s):
    assert r>=s>=1
    n=r-s
    ans=0
    for j in range(n+1):
        k=r-2*j
        plus=comb(2*s,k) if 0<=k<=2*s else 0
        minus=comb(2*s,k-1) if 0<=k-1<=2*s else 0
        ans+=comb(n,j)*(plus-minus)
    return ans

def independent_kernel(r,s):
    assert r>=s>=1
    return sum(comb(s-1,j)*2**(s-1-j)*cat((r-s+j)//2)
               for j in range(s) if (r-s+j)%2==0)

def poly_eval_desc(coeff,x):
    acc=0
    for c in coeff:acc=acc*x+c
    return acc

def check():
    assert S==29
    data=json.loads((HERE/'R416_EVIDENCE.json').read_text())
    assert data['certificate_count']==2 and data['schema']=='ENTERPRISE_MATH_R416_TURAN_FIXED_S29_ONLY_V1'
    total=0
    for parity in (0,1):
        cert=next(c for c in data['certificates'] if c['s']==S and c['parity']==parity)
        assert cert['s']==S and cert['parity']==parity
        ps=cert['numerator_coefficients_desc']; qs=cert['denominator_coefficients_desc']
        assert len(ps)==S+parity and len(qs)==S+parity
        assert min(ps)>0 and min(qs)>0
        m0=(S+2-parity)//2
        # Degree bound: common rational Delta denominator has 14 linear factors.
        # Normalized Turan numerator/denominator degree <= 2*14+2=30.
        # P/Q degree <= 29, so cross difference degree <= 59.
        assert max(len(ps),len(qs))-1+30 <= N-1
        for x in range(N):
            m=x+m0;r=2*m+parity
            dd={q:delta(r,q) for q in (S-1,S,S+1)}
            for q in dd:
                assert dd[q]==independent_kernel(r,q),(parity,x,q)
            h=lambda q:comb(r+q,2*q)*dd[q]
            D=h(S)**2-h(S-1)*h(S+1)
            B=comb(r+S,2*S)
            C=cat(m-1+parity)
            # All integers. Equality for 60 points is a complete rational identity
            # certificate only together with the degree-bound proof above.
            assert poly_eval_desc(qs,x)*D == poly_eval_desc(ps,x)*(B*C)**2,(parity,x)
            assert D>0
            total+=1
        print('R416_DEGREE_CERT_PARITY_PASS',parity,'points',N,
              'num_degree',len(ps)-1,'den_degree',len(qs)-1)
    print('R416_DEGREE_BOUNDED_IDENTITY_PASS',total,
          'exact independent integer Turan checks;',3*total,'Catalan kernel checks')
if __name__=='__main__':check()
