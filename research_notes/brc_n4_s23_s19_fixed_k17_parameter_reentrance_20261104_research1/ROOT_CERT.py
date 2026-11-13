from runpy import run_path
from pathlib import Path
from fractions import Fraction as F
v=run_path(str(Path(__file__).with_name('VERIFY.py')))
model=v['model']; sub=v['sub'];mul=v['mul'];iv=v['iv']

def g(n):
    s=F(1,9)+F(n,10**12)
    ct,cb,*_=model(s)
    return sub(mul(iv(9),ct),mul(iv(17),cb))
lo,hi=10**6,10**7
assert g(lo)[0]>0 and g(hi)[1]<0
while hi-lo>1:
    md=(lo+hi)//2
    r=g(md)
    if r[0]>0:lo=md
    elif r[1]<0:hi=md
    else: raise ArithmeticError(f'bound too weak at {md}')
# Uniform analytic exclusion of all mixed m=1..8 on the certified bracket.
s_lo=F(1,9)+F(lo,10**12)
s_hi=F(1,9)+F(hi,10**12)
CTlo, CBlo, *_=model(s_lo)
CThi, CBhi, *_=model(s_hi)
# C_B(s) increases with s by Bernoulli thinning (data processing); C_T(s)
# increases by its explicit logarithm formula. c(s)=2-s decreases.
E_uniform_upper=CThi[1]-(2-s_hi)*CBlo[0]
assert CBlo[0]>F(1,10**5)
assert 8*E_uniform_upper < CBlo[0]/10
for m in range(1,9):
    assert F(1,10) < F(m,9)+m*F(lo,10**12)
    assert F(m,9)+m*F(hi,10**12) < 1
for n in [lo,hi]:
    a,b=g(n)
    print('epsilon_num',n,'epsilon',F(n,10**12),'s',F(1,9)+F(n,10**12),'g_enclosure=',float(a),float(b))
print('PASS_S23_K17_TRANSITION_EXISTENCE_1E12_GRID_20261104')
