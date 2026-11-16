#!/usr/bin/env python3
"""R749SST exact all-cutoff 11-read identifiability certificate (Python 3 + SymPy).
Runs entirely in exact integer/rational arithmetic.
"""
import json
from pathlib import Path
import sympy as s

x,h,e,d,E,D,z=s.symbols('x h e d E D z')
W=(1,1,2,3,6); M=100
coeff=[0]*(M+1); coeff[0]=1
for w in W:
    for k in range(w,M+1): coeff[k]+=coeff[k-w]
C=[0]*(M+1); T=[0]*(M+1)
for k in range(1,M+1):
    C[k]=C[k-1]+coeff[k-1]
    T[k]=T[k-1]+C[k-1]
assert C[6]>2 and all(C[k+1]>=C[k] for k in range(6,M))

# Check marking of the first distinct unit-weight source by direct enumeration.
for k in range(1,25):
    cc=tt=0
    for n5 in range((k-1)//6+1):
        for n4 in range((k-1-6*n5)//3+1):
            for n3 in range((k-1-6*n5-3*n4)//2+1):
                u=k-1-6*n5-3*n4-2*n3
                cc+=(u+1)*(u+2)//2
                tt+=u*(u+1)*(u+2)//6
    assert (cc,tt)==(C[k],T[k])

# Exact phase-polynomial generating-function degrees and early-index identities.
v=sum(z**j for j in range(6))
assert s.degree(z*v**3*(1+z**2+z**4)*(1+z**3),z)==23
assert s.degree(z**2*v**4*(1+z**2+z**4)*(1+z**3),z)==29
for degree,maxj in ((5,3),(6,4)):
    for j in range(maxj+1):
        for n in range(j):
            assert s.prod(n-j+degree-k for k in range(degree))==0

S=lambda a:18*a**4+54*a**3-345*a**2+2070*a-16315
jets={}
for r in range(6):
    samples=[r+6*k for k in range(1,9)]
    cr=s.Poly(s.interpolate([(q,C[q]) for q in samples[:6]],x),x)
    tr=s.Poly(s.interpolate([(q,T[q]) for q in samples[:7]],x),x)
    assert (cr.degree(),tr.degree())==(5,6)
    assert all(cr.eval(q)==C[q] and tr.eval(q)==T[q] for q in samples)
    den=s.Poly(cr.as_expr()+d,x)
    nu=s.Poly(s.expand(x**3*(tr.as_expr()+e)-S(x)*den.as_expr()/108),x)
    assert (den.degree(),nu.degree())==(5,5)
    aa=[nu.nth(5-i)/den.nth(5) for i in range(6)]
    bb=[den.nth(5-i)/den.nth(5) for i in range(6)]
    out=[]
    for k in range(6):
        out.append(s.expand(aa[k]-sum(bb[j]*out[k-j] for j in range(1,k+1))))
    jets[r]=out
limits=[s.Rational(455,36),-s.Rational(295,36),-s.Rational(25,36),
        s.Rational(185,36),-s.Rational(25,36),-s.Rational(295,36)]
assert all(jets[r][0]==limits[r] for r in range(6))

def shifted(coeffs,k):
    if k==0: return coeffs[0]
    return s.expand(sum(coeffs[j]*(-1)**(k-j)*s.binomial(k-1,k-j)*h**(k-j)
                        for j in range(1,k+1)))

same_factors={
0:1150*h*(258213*h**2+6816674)/(9*(3*h**2+1445)),
1:100*h*(10664979*h**2+243694783)/(27*(3*h**2+1445)),
2:10*h*(100428693*h**2+2357398450)/(27*(3*h**2+1445)),
3:20*h*(15902457*h**2+394064185)/(9*(3*h**2+1445)),
4:10*h*(100279653*h**2+2405588050)/(27*(3*h**2+1445)),
5:100*h*(10679883*h**2+238875823)/(27*(3*h**2+1445))
}
cross_factors={
(1,5):-100*(414*h**4-10672431*h**3+276630*h**2-241285303*h+1201140)/(27*(3*h**2+1445)),
(5,1):100*(414*h**4+10672431*h**3+276630*h**2+241285303*h+1201140)/(27*(3*h**2+1445)),
(2,4):10*(4140*h**4+100354173*h**3+2756580*h**2+2381493250*h+7329600)/(27*(3*h**2+1445)),
(4,2):-10*(4140*h**4-100354173*h**3+2756580*h**2-2381493250*h+7329600)/(27*(3*h**2+1445))
}
matched=[]
for r,t in [(r,r) for r in range(6)]+list(cross_factors):
    difference=[s.expand(jets[r][k]-shifted(jets[t],k).subs({e:E,d:D}))
                for k in range(6)]
    assert difference[0]==0
    matrix,vector=s.linear_eq_to_matrix(difference[1:5],[d,e,D,E])
    assert s.factor(matrix.det())==3224862720000*h**2*(3*h**2+1445)
    solution=matrix.inv()*vector
    fifth=s.factor(difference[5].subs(dict(zip((d,e,D,E),solution))))
    expected=same_factors[r] if r==t else cross_factors[(r,t)]
    assert s.factor(fifth-expected)==0
    if r==t:
        pol=s.Poly(s.cancel(fifth/h*(3*h**2+1445)),h)
        assert pol.degree()==2
        assert pol.coeff_monomial(1)>0 and pol.coeff_monomial(h**2)>0
    else:
        factor=(-100 if (r,t)==(1,5) else 100 if (r,t)==(5,1)
                else 10 if (r,t)==(2,4) else -10)
        base=s.cancel(expected*(27*(3*h**2+1445)))
        reduced=s.Poly(s.cancel(base/factor),h,modulus=3)
        assert reduced.degree()==1 and reduced.eval(0)==0 and reduced.eval(1)!=0
        assert (t-r)%3!=0
    matched.append({'phases':[r,t], 'fifth_after_four_matches':str(fifth),
                    'rational_identity_for_compatible_nonzero_integer_shift':False})
assert set((r,t) for r in range(6) for t in range(6) if limits[r]==limits[t])==set(
    [(r,r) for r in range(6)]+list(cross_factors))

# Supplement: previously proven R749SSJ X(q+6)>X(q) on [-2,2]^2.
for q in range(6,71):
    for ee in (-2,0,2):
        for dd in (-2,0,2):
            xx0=s.Rational(T[q]+ee,C[q]+dd)
            xx1=s.Rational(T[q+6]+ee,C[q+6]+dd)
            assert xx1>xx0

out={'research_unit':'R749SST','status':'PASS',
     'evidence_class':'AUTHOR_EXACT_NOT_REVIEWED',
     'frozen_scientific_pin':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
     'weights':list(W), 'cutoff_domain':'q>=6 integer',
     'error_domain':'e,d real in [-2,2], shared across six-step reads of each candidate',
     'uniform_full_state_read_upper_bound':11,
     'same_phase_limit_read_upper_bound':10,
     'rational_difference_numerator_degree_bound':10,
     'equal_limit_numerator_degree_bound':9,
     'jet_matrix_determinant':'3224862720000*h^2*(3*h^2+1445)',
     'ten_matching_phase_cases':matched,
     'verification':'Exact 10 symbolic matching-jet obstructions + 24 labeled enumerations + 585 supplemental samples.',
     'open':'Sharp minimum horizon, minimax cutoff-dependent noise, native observer-fibre transfer.'}
Path(__file__).with_name('R749SST_UNIFORM_ELEVEN_READ_RESULTS.json').write_text(
    json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('PASS: global 11-read full triple identifiability and same-limit 10-read bound')
