"""Symbolic B2 identity and exact finite branch-certificate arithmetic."""
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as s
from certify_six_branch_gap import q_interval

A,d=s.symbols('A d',positive=True)
m=s.Rational(7,16)*A**4*d
u=m/(1+m)
v=m*A/(1+m*A)
h=1/(A-1)+5-4*u-5*v
q=A/(A-1)**2+16*u*(1-u)+25*v*(1-v)
assert s.factor(A*s.diff(h,A)+q)==0
logder=s.Rational(19,5)+A/(A-1)-4*m/(1+m)-5*m*A/(1+m*A)
assert s.factor(logder-h+s.Rational(1,5))==0
B1overG=-s.Rational(15,4)*logder-s.Rational(3,4)
assert s.factor(B1overG+s.Rational(15,4)*h)==0
B2overG=-(s.Rational(15,4)*A*s.diff(B1overG,A)
           +B1overG*(s.Rational(15,4)*logder+s.Rational(7,4)))
assert s.factor(B2overG-s.Rational(225,16)*(h*h-q)-s.Rational(15,4)*h)==0
hs=s.series(h,A,0,5).removeO().expand()
qs=s.series(q,A,0,5).removeO().expand()
assert s.expand(hs-(4-A-A**2-A**3-A**4*(1+s.Rational(7,4)*d)))==0
assert s.expand(qs-(A+2*A**2+3*A**3+A**4*(4+7*d)))==0
dp=s.symbols('dp',positive=True)
Ap=A-s.Rational(7,4)*A**4*(dp-d)
qdiff=s.series(qs.subs({A:Ap,d:dp},simultaneous=True)-qs,A,0,5).removeO().expand()
assert s.expand(qdiff-s.Rational(21,4)*A**4*(dp-d))==0
assert F(19,5)+4==F(39,5)
assert F(5,39)*F(8,15)==F(8,117)
assert F(3,2)*F(8,117)==F(4,39)

path=Path(__file__).with_name('six_branch_gap_certificate.json')
record=json.loads(path.read_text())
r=record['target_rectangle']
for row in r['roots']:
    a,A=map(F,row['A_interval'])
    d,D=map(F,row['d_interval'])
    lo,hi=q_interval(a,A,d,D)
    qlo,qhi=map(F,row['q_interval'])
    assert qlo<=lo<=hi<=qhi
    assert a>F(3,4) and d>F(1,3) and qhi<17
    assert min(abs(d-1),abs(D-1))>F(1,50)
intervals=sorted(tuple(map(F,row['q_interval'])) for row in r['roots'])
gap=min(y[0]-x[1] for x,y in zip(intervals,intervals[1:]))
assert gap==F(r['q_gap_lower'])>F(3,40)
Hlo,Hhi=map(F,r['h_interval'])
ulo,uhi=map(F,r['G_over_C_interval'])
assert F(r['B2_gap_lower'])==F(225,16)*2*ulo*F(3,40)>F(1,128)
assert F(r['source_mass_lower'])==6*F(2,135)*(Hhi-Hlo)*(uhi-ulo)/7

# Exact scale sequence c=2^(12n), b=2^(4n+6), p=25n-3.
for n in range(1,10):
    assert 3*(4*n+6)-12*n==18  # beta^3=2^18.
    assert 4*(25*n-3)-7*(12*n)-2*((12*n)-(4*n+6))==0

result={'symbolic_identities':['q=-A*h_A','A*d_A(log G)=h-1/5',
                               'B1/G=-15h/4','B2/G=225(h^2-q)/16+15h/4'],
        'boundary_series':{'h':str(hs),'q':str(qs),'same_h_q_difference':str(qdiff),
                           'gap_A_exponent':'39/5','source_tail_exponent':'8/117',
                           'beta_tail_exponent':'4/39'},
        'root_boxes_checked':6,'q_gap_lower':str(gap),
        'B2_gap_lower':r['B2_gap_lower'],'source_mass_lower':r['source_mass_lower'],
        'exact_scale_sequences_checked':9,'assertions_passed':True,
        'scope':'Identity and saved interval arithmetic; root isolation is recomputed by certify_six_branch_gap.py.'}
Path(__file__).with_name('branch_identity_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
