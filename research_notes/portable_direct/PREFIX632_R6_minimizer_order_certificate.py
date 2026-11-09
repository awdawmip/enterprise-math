#!/usr/bin/env python3
"""PREFIX632: exact rational signed-BRC valley-order witnesses.
Science pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
Run beside SOURCE PREFIX621_R6_stochastic_tail_certificate.py.
"""
import contextlib, io, json
from fractions import Fraction as F
from math import comb
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
    import PREFIX621_R6_stochastic_tail_certificate as old
N=189
rows=old.rows[:N]
assert old.first==25 and old.surv[N]==0
def survivor_derivative(p):
    a,b=p.numerator,p.denominator
    s=[];d=[]
    for n,row in enumerate(rows):
        v=sum(t*a**k*(b-a)**(n-k) for k,t in row.items())
        s.append(F(v,b**n))
        if n:
            dv=sum(t*a**k*(b-a)**(n-k)*(b*k-n*a)
                   for k,t in row.items())
            d.append(F(dv,a*(b-a)*b**(n-1)))
        else:d.append(F(0))
    return s,d
p2=F(19,128)
s2,_=survivor_derivative(p2)
alpha=[];beta=[]
for n in range(N):
    alpha.append(1-sum((F(comb(n+m,n),2**(n+m+1))*s2[m]
                     for m in range(N) if s2[m]), F(0)))
    beta.append(n+1-sum((F((n+m+1)*comb(n+m,n),2**(n+m+2))*s2[m]
                     for m in range(N) if s2[m]), F(0)))
assert all(0<a<=1 for a in alpha)
assert all(0<b<=n+1 for n,b in enumerate(beta))
def gradient(p1,q):
    s,d=survivor_derivative(p1)
    mu=sum(s2,F(0))+sum((x*y for x,y in zip(s,alpha)),F(0))
    U=sum((x*y for x,y in zip(d,alpha)),F(0))
    J=sum((x*y for x,y in zip(d,beta)),F(0))
    assert U>0
    return 2*(J-mu*U)-U/q, U
points=((F(4,25),24,-1),(F(401,2500),24,1),
        (F(401,2500),12,-1),(F(161,1000),12,1))
results=[]
for p1,q,sign in points:
    value,U=gradient(p1,q)
    assert (value<0 if sign<0 else value>0)
    results.append({'p1':str(p1),'p2':str(p2),'q':q,
      'sign':'NEGATIVE' if sign<0 else 'POSITIVE',
      'g_over_q2_display':format(float(value),'.12f'),
      'U_display':format(float(U),'.12f'),
      'verification':'exact Fraction sign'})
out={'schema':'PREFIX632_R6_MINIMIZER_ORDER_V1',
     'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
     'general_theorem':'For fixed p2 in [37/256,39/256], 12<=q1<q2, all interval-I minimizers b for q2 and a for q1 satisfy b<a, mu(b)<mu(a), W(b)<W(a); I=[3/20,1/6].',
     'rational_witness':'At p2=19/128 there exist local minima V24 in (4/25,401/2500) and V12 in (401/2500,161/1000).',
     'results':results,
     'checks':{'first_stopping_level':25,'last_stopping_level':189,
               'positive_alpha_coefficients':N,'positive_beta_coefficients':N,
               'exact_gradient_signs':len(points)},
     'verification':'ALL_CHECKS_PASS',
     'status':'AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED'}
Path(__file__).with_name('PREFIX632_R6_RESULTS.json').write_text(
    json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('ALL_CHECKS_PASS',[(x['p1'],x['q'],x['sign']) for x in results])
