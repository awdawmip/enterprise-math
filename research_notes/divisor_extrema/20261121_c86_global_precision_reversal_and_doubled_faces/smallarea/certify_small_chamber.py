"""Exact radical certificate for the full origin chamber."""
from fractions import Fraction as F
from pathlib import Path
import json

def root(q,n=20,bits=100):
    q=F(q);scale=1<<bits
    lo=0;hi=scale*max(1,q.numerator//q.denominator+1)
    while hi-lo>1:
        m=(lo+hi)//2
        if m**n*q.denominator<=q.numerator*scale**n:lo=m
        else:hi=m
    a,b=F(lo,scale),F(hi,scale)
    assert a**n<=q<b**n
    return a,b

def powers(q):
    a,b=root(q);return q*q*a,q*q*b

def run():
    terms=[(F(12),F(1,6)),(-F(9),F(1,3)),(-F(16),F(1,2)),
           (F(6),F(2,3)),(F(4),F(3,2)),(-F(4),F(2))]
    lo=hi=F(7)
    for c,q in terms:
        a,b=powers(q)
        lo+=c*(a if c>0 else b);hi+=c*(b if c>0 else a)
    a,b=root(F(3));coef=F(41*21,400)
    lo+=coef*a;hi+=coef*b
    assert lo>F(7,4000)
    result={'status':'PASS','scope':'Strict positive constant for every0<s<=r<=1/3',
            'lower':str(lo),'upper':str(hi),'strict_lower':'7/4000',
            'display_approx':[float(lo),float(hi)],'arithmetic':'Fraction, exact20th-power comparisons'}
    Path(__file__).with_name('small_chamber_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':run()
