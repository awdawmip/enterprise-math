"""Exact finite checks for the complete-integer cumulative-field obstruction."""
from fractions import Fraction as F
from pathlib import Path
import json


def case(s):
    X, h, d = s**4, s**3, s**2
    def q(n):
        if n <= X or n >= 2*X:
            return F(0)
        r=(n-X)%h
        return F(r*r*(h-r)**2, X*h*h)
    def E(n):
        return n*q(n+1)-(n+1)*q(n)
    for n in range(X-1,2*X+2):
        a=q(n+1)-2*q(n)+q(n-1)
        assert abs(a)<=F(4,n)
        assert E(n)-E(n-1)==n*a
    energy=sum((q(n)/n)**2 for n in range(X,2*X+1))
    hardy=sum((min(E(n),F(0))/n)**2 for n in range(X,2*X))
    assert F(81,524288)<=energy<=F(1,256)
    assert F(9*s*s,32768)<=hardy<=F(81*s*s,256)
    for L in range(X,2*X,h):
        assert sum(E(n)/F(n*(n+1)) for n in range(L,L+h))==0
    remainder=F(0)
    for L in range(X,2*X,d):
        for n in range(L,L+d):
            interp=((L+d-n)*q(L)+(n-L)*q(L+d))/d
            remainder+=((q(n)-interp)/n)**2
    assert remainder<=F(2,15*s**4)
    def show(x):
        scale=10**35
        lo=x.numerator*scale//x.denominator
        hi=-((-x.numerator*scale)//x.denominator)
        def decimal(n):
            return str(n//scale)+'.'+str(n%scale).zfill(35)
        return {'lower':decimal(lo),'upper':decimal(hi),
                'integer_bounds':[str(lo),str(hi)],'denominator_power_of_10':35}
    return {'s':s,'X':X,'h':h,'fine_step':d,
            'S':show(energy),'negative_cumulative_square':show(hardy),
            'ratio':show(hardy/energy),'fine_remainder_square':show(remainder),
            'source_check_integer_count':X+3,'status':'PASS'}


if __name__=='__main__':
    out={'status':'PASS','scope':'General full-integer source family, not actual arithmetic q.',
         'arithmetic':'exact Fraction; displayed decimal intervals are rounded outward',
         'cases':[case(s) for s in (2,4,8)]}
    Path(__file__).with_name('obstruction_certificate.json').write_text(
        json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'cases':[
        {k:c[k] for k in ('s','X','S','negative_cumulative_square','ratio','fine_remainder_square')}
        for c in out['cases']]},ensure_ascii=False))
