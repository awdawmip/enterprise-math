#!/usr/bin/env python3
"""PREFIX-629: exact signed Bernstein bound, BRC two-direction variance exclusion.
Science pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
Run beside SOURCE-published PREFIX621_R6_stochastic_tail_certificate.py.
Only Python standard library and exact Fraction arithmetic.
"""
import contextlib
import hashlib
import io
import json
from decimal import Decimal, localcontext
from fractions import Fraction as Q
from math import comb
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    import PREFIX621_R6_stochastic_tail_certificate as old

N=189
D=N-2
rows=old.rows[:N]
assert old.first==25 and old.surv[N]==0

def survivor(p):
    a,b=p.numerator,p.denominator
    return [Q(sum(v*a**k*(b-a)**(n-k) for k,v in row.items()),b**n)
            for n,row in enumerate(rows)]

sa=survivor(Q(37,256))
sb=survivor(Q(39,256))
alpha_b=[]
beta_a=[]
for n in range(N):
    alpha_b.append(1-sum((Q(comb(n+m,n),2**(n+m+1))*sb[m]
                          for m in range(N) if sb[m]),Q(0)))
    beta_a.append((n+1)-sum((Q((n+m+1)*comb(n+m,n),2**(n+m+2))*sa[m]
                            for m in range(N) if sa[m]),Q(0)))
assert all(0<=x<=1 for x in alpha_b)
assert all(0<=x<=n+1 for n,x in enumerate(beta_a))

c=[]
for n,row in enumerate(rows):
    v=[0]*(n+1)
    for k,A in row.items():
        for j in range(k,n+1):
            v[j]+=(-1 if (j-k)%2 else 1)*A*comb(n-k,j-k)
    assert v[0]==row.get(0,0) and sum(v)==row.get(n,0)
    c.append(v)

# F(p)=J(p,a)-87 U(p,b). Power coefficients in the polynomial p.
f=[(j+1)*sum(((beta_a[n]-87*alpha_b[n])*c[n][j+1]
               for n in range(j+1,N)),Q(0)) for j in range(D+1)]
# Exact Bernstein coefficient identity for G_h(x)=F(h*x), 0<=x<=1:
# b_k(h)=sum_(j=0)^k f_j*h^j*C(k,j)/C(D,j)

def bernstein_coefficients(hden):
    return [sum((f[j]*Q(comb(k,j),comb(D,j)*hden**j)
                 for j in range(k+1)),Q(0)) for k in range(D+1)]

out=[]
for den,margin in [(16,188),(14,18)]:
    bs=bernstein_coefficients(den)
    assert len(bs)==188
    assert all(x < -margin for x in bs)
    assert bs[0]==f[0]
    assert bs[-1]==sum((f[j]*Q(1,den**j) for j in range(D+1)),Q(0))
    maxb=max(bs)
    with localcontext() as ctx:
        ctx.prec=30
        display=str(Decimal(maxb.numerator)/Decimal(maxb.denominator))
    out.append({'p1_max':f'1/{den}', 'bernstein_degree':D,
                'coefficients_certified':len(bs),'max_bernstein_coefficient_display':display,
                'strict_upper_bound_for_F':f'-{margin}',
                'proven_dV_dp1_upper_bound':f'-{2*margin}*q^2',
                'max_coefficient_fraction_sha256':hashlib.sha256(str(maxb).encode()).hexdigest(),
                'result':'PASS'})

res={'schema':'PREFIX629_R6_BERNSTEIN_SIGNED_INTERVAL_V1',
     'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
     'd':2,'q':'all real q>=2','p2_range':['37/256','39/256'],
     'source':'PREFIX621 exact first-passage counts and PREFIX624 monotonicity; PREFIX622 independent Poissonized moments; PREFIX626 edge witnesses',
     'certificate':'188 exact rational Bernstein control points at each of two intervals',
     'results':out,'verification':'ALL_CHECKS_PASS',
     'status':'AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED'}
Path(__file__).with_name('PREFIX629_R6_RESULTS.json').write_text(json.dumps(res,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('ALL_CHECKS_PASS')
for row in out:print(row['p1_max'],row['strict_upper_bound_for_F'],row['max_bernstein_coefficient_display'])
