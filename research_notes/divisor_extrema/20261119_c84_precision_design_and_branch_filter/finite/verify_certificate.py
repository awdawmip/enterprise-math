"""Independent exact arithmetic checks and a fresh coarse certificate."""
from fractions import Fraction as F
from pathlib import Path
import json
import certify_one_third as C

checks=[]
def includes(interval,x):
    return F(interval.lo,C.SCALE)<=x<=F(interval.hi,C.SCALE)

def frac_log(x,terms=120):
    x=F(x);k=0
    while x<1:x*=2;k-=1
    while x>2:x/=2;k+=1
    def base(x):
        w=(x-1)/(x+1);ss=sum(w**(2*j+1)/F(2*j+1) for j in range(terms))*2
        tail=2*w**(2*terms+1)/(F(2*terms+1)*(1-w*w))
        return ss,ss+tail
    a,b=base(x);l,h=base(F(2))
    return (a+k*l,b+k*h) if k>=0 else (a+k*h,b+k*l)

cases=[F(-7,3),F(-1,8),F(0),F(1,17),F(1,2),F(9,4)]
for a in cases:
    for b in cases:
        ia,ib=C.lift(a),C.lift(b)
        assert includes(ia+ib,a+b) and includes(ia-ib,a-b) and includes(ia*ib,a*b)
        if b:assert includes(ia/ib,a/b)
checks.append({'name':'fraction_arithmetic','passed':True,'rational_pairs':len(cases)**2})
for x in [F(0),F(1,17),F(1,4),F(2),F(19,3)]:
    a=C.positive_sqrt(C.lift(x))
    assert F(a.lo,C.SCALE)**2<=x<=F(a.hi,C.SCALE)**2
checks.append({'name':'integer_sqrt_bounds','passed':True,'cases':5})
for x in [F(1,64),F(1,4),F(3,4),F(1),F(2),F(5),F(7)]:
    a=C.ilog(C.lift(x));l,h=frac_log(x)
    assert F(a.lo,C.SCALE)<=l<=h<=F(a.hi,C.SCALE)
checks.append({'name':'log_vs_independent_fraction_series','passed':True,'cases':7,'fraction_terms':120})
for x in [F(0),F(1,239),F(1,5),F(1,3),F(1,2)]:
    aa=sum((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(120));bb=aa+x**241/241
    a=C.iatan(C.lift(x))
    assert F(a.lo,C.SCALE)<=aa<=bb<=F(a.hi,C.SCALE)
checks.append({'name':'atan_vs_independent_fraction_series','passed':True,'cases':5,'fraction_terms':120})
x=C.D2.variable(C.lift(F(1,4)))
f=C.log(x)+C.atan(x)+C.sqrt(x)
assert includes(f.d,F(101,17)) and includes(f.dd,-F(5330,289))
checks.append({'name':'second_derivative_rules','passed':True,'exact_first':'101/17','exact_second':'-5330/289'})
root=Path(__file__).parent
stored=json.loads((root/'one_third_certificate.json').read_text())
lo,hi=[F(stored['F3_interval'][key]) for key in ['lower','upper']]
assert hi-lo<F(1,10**6)
short=list(map(F,stored['F3_interval']['outward_decimal_9']))
assert short[0]<lo<hi<short[1]
checks.append({'name':'stored_exact_enclosure_and_outward_decimals','passed':True,'grid_recomputed':False})
coarse,_,_=C.f3_certificate(8)
assert F(coarse.lo,C.SCALE)<lo<hi<F(coarse.hi,C.SCALE)
checks.append({'name':'fresh_coarse_certificate','passed':True,'grid_per_branch':8,'fine_grid_recomputed':False})
result={'scope':'Exact elementary interval arithmetic checks and fresh coarse quadrature; the saved 2048-grid certificate was executed separately, not regenerated here.','passed':len(checks),'failed':0,'checks':checks}
(root/'certificate_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
