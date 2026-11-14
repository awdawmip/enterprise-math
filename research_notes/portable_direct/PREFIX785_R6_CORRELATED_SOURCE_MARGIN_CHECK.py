"""PREFIX-785 correlated single-source observer: exact minimax margin, Fraction.
External Gamma-style scalar comparison only; no frozen recurrence/source changes.
"""
from fractions import Fraction as F
from random import Random
import json


def dist_interval(x,lo,hi):return max(lo-x,F(0),x-hi)

def sharp_margin(q):
    assert q>0
    c1=q;c2=2*q-3
    midpoint=(c1+c2)/2
    return abs(c1-c2)/2+dist_interval(midpoint,F(-1),F(1))

def best_t(q):
    midpoint=(3*q-3)/2
    return min(F(1),max(F(-1),midpoint))

def witnessed(q,t):
    assert q>0 and F(-1)<=t<=F(1)
    return [t-q, t+3-2*q, q-t, -t-3+2*q]

assert sharp_margin(F(5,3))==F(2,3)
assert best_t(F(5,3))==F(1)
assert witnessed(F(5,3),F(1))==[F(-2,3),F(2,3),F(2,3),F(-2,3)]
# Exact piecewise lower envelope, each formula is achieved by best_t.
def piecewise(q):
    if q<=F(1,3):return 2-2*q
    if q<=F(5,3):return (3-q)/2
    if q<=3:return q-1
    return 2*q-4

rng=Random(20261114785)
count=0;grid_checks=0
for _ in range(4096):
    q=F(rng.randint(1,100),rng.choice((3,5,7,11,13)))
    t=best_t(q)
    a=witnessed(q,t)
    radius=max(abs(a[0]),abs(a[1]))
    assert radius==sharp_margin(q)==piecewise(q)
    assert sharp_margin(q)>=F(2,3)
    assert a[0]==-a[2] and a[1]==-a[3]
    assert max(a)==radius and min(a)==-radius
    count+=1
    # Independent point probes cannot attain smaller margin.
    for t2 in (F(-1),F(-1,2),F(0),F(1,2),F(1),
               F(rng.randint(-10,10),10)):
        if abs(t2)>1:continue
        assert max(abs(t2-q),abs(t2+3-2*q))>=radius
        grid_checks+=1
# Independent-box relaxation can cancel all four at q=1, although joint t cannot.
q=F(1)
u1=v1=F(1);u2=v2=F(-1)
relaxed=[-q+u1,3-2*q+u2,q-v1,-3+2*q-v2]
assert relaxed==[0,0,0,0]
assert sharp_margin(q)==1
out={'schema':'PREFIX785_R6_CORRELATED_SOURCE_MARGIN_V1',
     'scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
     'model':'a=(t-q, t+3-2q, q-t, -t-3+2q), q>0, t in [-1,1]',
     'coefficients':{'A':['0','3'],'B':['1','2'],'D':'3'},
     'pointwise_sharp_margin':'abs(3-q)/2 + max(0,abs(3q-3)/2-1)',
     'piecewise':['2-2q for 0<q<=1/3','(3-q)/2 for 1/3<=q<=5/3',
                  'q-1 for 5/3<=q<=3','2q-4 for q>=3'],
     'uniform_infimum':'2/3','unique_optimum_q':'5/3','attaining_t':'1',
     'attaining_four_signs':['-2/3','2/3','2/3','-2/3'],
     'independent_box_cancel_q':'1','independent_box_cancel_signs':['0','0','0','0'],
     'rational_regression':{'parameter_cases':count,'independent_t_checks':grid_checks,
                            'arithmetic':'Python fractions.Fraction exact'},
     'scope':'algebraic provenance-linked single-source observer; not native X6 transfer or Gamma recurrence',
     'status':'ALL_CHECKS_PASS PREFIX785 CORRELATED_SOURCE_UNIFORM_MARGIN'}
with open('PREFIX785_R6_CORRELATED_SOURCE_MARGIN_RESULTS.json','w',encoding='utf-8') as f:
    json.dump(out,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps({'status':out['status'],'sharp_margin':out['pointwise_sharp_margin'],
                  'uniform_infimum':out['uniform_infimum'],'tests':out['rational_regression']},indent=2))
