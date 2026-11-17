#!/usr/bin/env python3
"""Exact four-read injectivity between q=73 and p=77 in frozen labeled-source observer.
Python 3 and SymPy. Rational resultant/Sturm and Bernstein certificates, no sampling.
Frozen scientific pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
"""
import json
from pathlib import Path
import sympy as s

e,d,u,v=s.symbols('e d u v')
n_max=96
coef=[0]*n_max;coef[0]=1
moment=list(range(n_max)) # first labeled source weight 1
for j,weight in enumerate((1,1,2,3,6)):
    for n in range(weight,n_max):coef[n]+=coef[n-weight]
    if j:
        for n in range(weight,n_max):moment[n]+=moment[n-weight]
C=lambda n:sum(coef[:n])
T=lambda n:sum(moment[:n])
S=lambda n:18*n**4+54*n**3-345*n**2+2070*n-16315
Y=lambda n,ee,dd:s.Integer(n)**3*(T(n)+ee)/(C(n)+dd)-s.Rational(S(n),108)
assert [(C(n),T(n)) for n in (73,77,91,95)]==[(707343,8931013),(906087,12046216),(1978664,30933812),(2422568,39491884)]
x=[];b=[]
for j in range(4):
    a,p=73+6*j,77+6*j
    xx=s.cancel((Y(a,e,d)+s.Rational(S(p),108))/p**3)
    x.append(xx);b.append(s.cancel(xx*C(p)-T(p)))
D=s.factor(s.cancel((b[0]-b[1])/(x[1]-x[0])))
E=s.factor(s.cancel(b[0]+x[0]*D))
F=s.factor(s.cancel((b[0]-b[1])*(x[2]-x[0])-(b[0]-b[2])*(x[1]-x[0])))
R=s.factor(s.cancel(Y(95,E,D)-Y(91,e,d)))
PF=s.fraction(F)[0];QR=s.fraction(R)[0]
resultant=s.resultant(PF,QR,d)
fac=s.factor_list(resultant)[1]
assert [(s.degree(f,e),m) for f,m in fac]==[(1,1),(1,1),(1,1),(5,1)]
elo=s.Rational(3306,10000);ehi=s.Rational(3307,10000)
root_checks=[]
for f,m in fac:
    p=s.Poly(f,e)
    globally=s.count_roots(p,-2,2)
    narrowed=s.count_roots(p,elo,ehi)
    expect=(1 if p.degree()==5 else 0)
    assert globally==narrowed==expect
    root_checks.append({'degree':p.degree(),'multiplicity':m,'roots_in_closed_e_interval':int(globally),'roots_in_bracket':int(narrowed),'factor':str(f)})

# e in [3306/10000,3307/10000]; d in [-2,2] or [-2,-1].
e_box=elo+(ehi-elo)*u
proof_checks=[]
def positive(expr,d_box,label):
    n,h=s.fraction(s.cancel(s.together(expr.subs({e:e_box,d:d_box}))))
    if h.subs({u:s.Rational(1,2),v:s.Rational(1,2)})<0:n,h=-n,-h
    for suffix,P in (('denominator',h),('numerator',n)):
        pp=s.Poly(s.expand(P),u,v);du,dv=pp.degree_list();mon=dict(pp.terms())
        coeffs=[]
        for i in range(du+1):
            for j in range(dv+1):
                beta=sum(mon.get((a,b),0)*s.binomial(i,a)*s.binomial(j,b)/s.binomial(du,a)/s.binomial(dv,b) for a in range(i+1) for b in range(j+1))
                assert beta.is_Rational and beta>0, f'{label}_{suffix}: nonpositive coefficient'
                coeffs.append(beta)
        proof_checks.append({'part':f'{label}_{suffix}','bidegree':[du,dv],'count':len(coeffs),'min_coefficient':str(min(coeffs))})

positive(s.diff(F,d),-2+4*v,'strict_F_increasing_on_full_admissible_d')
positive(F.subs(d,-1),0*v,'F_at_minus_one_strictly_positive')
positive(E-2,-2+v,'alternative_E_exceeds_2_when_d_at_most_minus_one')
positive(x[1]-x[0],-2+4*v,'two_read_inversion_denominator_positive')
assert len(proof_checks)==8 and sum(r['count'] for r in proof_checks)==50

out={'unit':'R749STC','status':'PASS','evidence':'AUTHOR_EXACT_NOT_REVIEWED',
     'frozen_pin':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
     'cutoff_pair':[73,77],'resultant_degree_e':int(s.degree(resultant,e)),
     'resultant_factors':root_checks,'unique_candidate_e_bracket':[str(elo),str(ehi)],
     'four_read_exact_collision_in_allowed_error_box':False,
     'exact_three_read_collision_exists':'R749STA and R749STB',
     'pairwise_minimal_exact_observations':4,
     'positive_bernstein_coefficients':sum(r['count'] for r in proof_checks),
     'bernstein_certificates':proof_checks,
     'proof_scope':'all continuous error parameters in [-2,2] for the fixed pair q73,p77',
     'next':'global minimal horizon 4..11; search four-read alias at large cutoffs; improve noise bounds'}
dest=Path(__file__).with_name('R749STC_FOUR_READ_PAIR_SEPARATION_RESULTS.json')
dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PASS',out['positive_bernstein_coefficients'],'strict Bernstein coefficients; resultant roots isolated; q73/p77 minimal exact horizon 4')
