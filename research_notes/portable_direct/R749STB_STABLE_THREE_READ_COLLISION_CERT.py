#!/usr/bin/env python3
"""R749STB: exact bivariate Bernstein certificate of robust three-read aliases.
Frozen pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Python 3 and SymPy; all certification arithmetic rational.
"""
import json
from pathlib import Path
import sympy as sp

e,d,u,v=sp.symbols('e d u v')
weights=(1,1,2,3,6)
limit=96
c=[0]*limit;c[0]=1
for weight in weights:
    for n in range(weight,limit):c[n]+=c[n-weight]
t=list(range(limit)) # first labeled unit-weight source contributes k1=n
for weight in weights[1:]:
    for n in range(weight,limit):t[n]+=t[n-weight]
C=lambda n:sum(c[:n])
T=lambda n:sum(t[:n])
S=lambda n:18*n**4+54*n**3-345*n**2+2070*n-16315

def Y(n,ee,dd):
    return sp.cancel(sp.Integer(n)**3*(T(n)+ee)/(C(n)+dd)-sp.Rational(S(n),108))

x=[];b=[]
for j in range(4):
    a,p=73+6*j,77+6*j
    xx=sp.cancel((Y(a,e,d)+sp.Rational(S(p),108))/p**3)
    x.append(xx)
    b.append(sp.cancel(xx*C(p)-T(p)))
D=sp.factor(sp.cancel((b[0]-b[1])/(x[1]-x[0])))
E=sp.factor(sp.cancel(b[0]+x[0]*D))
F=sp.factor(sp.cancel((b[0]-b[1])*(x[2]-x[0])-(b[0]-b[2])*(x[1]-x[0])))
R=sp.factor(sp.cancel(Y(95,E,D)-Y(91,e,d)))

# Unit square (u,v): e covers [-151/100,-149/100]; d lies in slanted strip.
ebox=-sp.Rational(151,100)+u/50
center=-sp.Rational(183,200)-sp.Rational(183,500)*(ebox+sp.Rational(3,2))
dbox=center+(2*v-1)/1000

def pos_poly(poly,name):
    poly=sp.Poly(sp.expand(poly),u,v)
    a,b=poly.degree_list()
    mon={ab:co for ab,co in poly.terms()}
    coeff=[sp.factor(sum(mon.get((i,j),0)*sp.binomial(s,i)*sp.binomial(t,j)
                         /sp.binomial(a,i)/sp.binomial(b,j)
                         for i in range(s+1) for j in range(t+1)))
           for s in range(a+1) for t in range(b+1)]
    assert all(co>0 for co in coeff), f'{name}: nonpositive Bernstein coefficient'
    return {'part':name,'bidegree':[a,b],'count':len(coeff),
            'min_coefficient':str(min(coeff))}

checks=[]
def pos_rat(expr,name):
    transformed=sp.cancel(sp.together(expr.subs({e:ebox,d:dbox})))
    n,h=sp.fraction(transformed)
    if h.subs({u:sp.Rational(1,2),v:sp.Rational(1,2)})<0:
        n,h=-n,-h
    checks.append(pos_poly(h,name+'_denominator'))
    checks.append(pos_poly(n,name+'_numerator'))

# Strictly opposing endpoint signs for every value of e in its interval.
pos_rat(-F.subs(d,center-sp.Rational(1,1000)),'F_lower_edge')
pos_rat(F.subs(d,center+sp.Rational(1,1000)),'F_upper_edge')
for name,expression in [('E_gt_minus_2',2+E),('E_lt_2',2-E),
                        ('D_gt_minus_2',2+D),('D_lt_2',2-D),
                        ('fourth_residual_gt_1e_minus_5',R-sp.Rational(1,100000)),
                        ('F_strictly_increasing_in_d',sp.diff(F,d))]:
    pos_rat(expression,name)
assert len(checks)==16
assert sum(row['count'] for row in checks)==199

# Independent square-freeness check for predecessor's q73 exact cubic.
F0=sp.fraction(sp.factor(F.subs(e,-sp.Rational(3,2))))[0]
P=sp.Poly(F0,d)
assert P.degree()==3 and sp.gcd(P,P.diff()).degree()==0
assert C(73)==707343 and T(73)==8931013
assert C(77)==906087 and T(77)==12046216

result={
 'unit':'R749STB','status':'PASS','evidence':'AUTHOR_EXACT_NOT_REVIEWED',
 'frozen_pin':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
 'candidates':[73,77],'e_interval':['-151/100','-149/100'],
 'd_center':'-183/200-(183/500)*(e+3/2)',
 'd_strip_halfwidth':'1/1000','all_parameters_strictly_interior':True,
 'F_increasing_in_d_on_strip':True,'fourth_residual_lower_bound':'1/100000',
 'three_read_collision':'unique analytic d(e) on the stated strip',
 'observer_only_next_read_minimax_error_strictly_above':'1/200000',
 'bernstein_positive_coefficients':199,'checks':checks,
 'dependence':'R749STA for all-q qualitative robust corollary',
 'next':'four-read separation on all q and phase classes; quantitative noise margins'
}
path=Path(__file__).with_name('R749STB_STABLE_THREE_READ_COLLISION_RESULTS.json')
path.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('PASS',result['bernstein_positive_coefficients'],'strict Bernstein coefficients', 'unique analytic collision curve', 'fourth gap > 1e-5')
