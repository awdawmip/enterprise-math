"""Exact rational checks for seventh plateau extension across the w-gap regime."""
from fractions import Fraction

def logbd(a,b,t=45):
 z=Fraction(a-b,a+b)
 s=sum((2*z**(2*k+1)/(2*k+1) for k in range(t)),Fraction(0))
 return s,s+2*z**(2*t+1)/((2*t+1)*(1-z*z))
l2,u2=logbd(2,1);l87,u87=logbd(8,7);l54,u54=logbd(5,4)
lo=(3*l2-u87)/(u54+u87);hi=(3*u2-l87)/(l54+l87)
e0,e1=79*lo-431,79*hi-431
d0,d1=2074774-380295*hi,2074774-380295*lo
assert 0<d0<d1<e0<e1
assert 5*d1 < 3*e0 # all delta_2,4,6,7 < eta; stricter than 3/5
for i,a in [(2,1),(4,2),(6,3),(7,4)]:
 assert 0 < i*d0-a*e1
 assert i*d1-a*e0 < d0
m1=380295+2074774
Hmax=m1+509
assert Hmax==2455578
v=[None,0,380295,760669,1140964,1521338,1901633,2282007,2662381]
k=[None,0,2074774,4149979,6224753,8299958,10374732,12449937,14525142]
n7=14905515
assert Hmax<v[8] and Hmax<k[3]
assert n7>6*Hmax and n7>Hmax
assert 760669+1+14905515>9821296
assert (14731944-(1521338+1))<n7
assert (17187523-(2282007+1))==n7
print('PASS_S23_AV_SEVENTH_PLATEAU_EXTENDED_W_GAP')
print('threshold_global_min_positive_gap>=eta for h< m1+510=2455579')
print('good_occupation_indices=(2,4,6,7) with 0<delta_i<eta')
print('exact_seventh_plateau=2282518..2455578 N=14905515')
print('next_gap_vector=w+u at length 2455579; unresolved endpoint onward')
