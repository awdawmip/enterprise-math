"""Exact finite phase integration and algebraic moment check for Z^2."""
from fractions import Fraction as F
from pathlib import Path
import json
from certify_half_area import root_fraction_bounds,encoded


def exact_phase_average(sigma,theta):
    bound=(sigma.denominator+sigma.numerator-1)//sigma.numerator
    ints=range(-bound,bound+1)
    cuts={F(0),F(1)}
    for m in ints:
        for x in (-sigma*m,1-sigma*m):
            if 0<x<1:cuts.add(x)
    cuts=sorted(cuts)
    answer=F(0);cells=0;maxvectors=0
    for xl,xr in zip(cuts,cuts[1:]):
        x=(xl+xr)/2
        xs=[m for m in ints if 0<x+sigma*m<1]
        for yl,yr in zip(cuts,cuts[1:]):
            y=(yl+yr)/2
            ys=[n for n in ints if 0<y+sigma*n<1]
            positive=negative=F(1)
            zero=False;vectors=0
            for m in xs:
                for n in ys:
                    if m==n==0:continue
                    vectors+=1
                    z=sigma*((1-theta)*m+theta*n)
                    if z==0:zero=True
                    elif z>0:positive=min(positive,z)
                    else:negative=min(negative,-z)
            unique=F(0) if zero else max(F(0),positive+negative-1)
            answer+=(xr-xl)*(yr-yl)*unique
            cells+=1;maxvectors=max(maxvectors,vectors)
    return answer,cells,maxvectors


def formula(sigma,theta):
    t=min(theta,1-theta)
    if sigma<=F(1,2):return 2*t*sigma**3
    if sigma<=1:
        p=1-sigma;q=2*sigma-1
        return q*q+2*p*q*sigma+2*p*p*t*sigma
    return F(1)


def main():
    cases=[]
    for sigma in [F(1,9),F(1,5),F(1,3),F(1,2),F(3,5),F(2,3),F(4,5),F(1)]:
        for theta in [F(1,5),F(1,4),F(1,3),F(1,2),F(3,4),F(4,5)]:
            actual,cells,mx=exact_phase_average(sigma,theta)
            expected=formula(sigma,theta)
            assert actual==expected,(sigma,theta,actual,expected)
            cases.append({'sigma':str(sigma),'theta':str(theta),'probability':str(actual),
                          'endpoint_cells':cells,'max_eligible_nonzero_vectors':mx})
    gamma=F(1,10);t=F(1,4)
    factor=(1-2*t)*gamma/((gamma+1)*(gamma+2))
    assert factor*2/(gamma+3)==F(100,7161)
    assert factor/2==F(5,462)
    zl,zu=root_fraction_bounds(10,2)
    lo=F(100,7161)-F(5,462)*zu
    hi=F(100,7161)-F(5,462)*zl
    assert lo>F(38667704448956047,10**19)
    data={'status':'exact_checks_passed','finite_phase_cases':len(cases),
          'formula':'I_quarter-I_mid=100/7161-(5/462)*2^(-1/10)',
          'moment_difference':encoded(lo,hi,21),'cases':cases,
          'coverage':'Exact rational endpoint partition and all eligible integer pairs in each case; universal proof in SQUARE_LATTICE_OBSTRUCTION.md'}
    Path(__file__).with_name('square_lattice_certificate.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'cases_passed':len(cases),'moment_difference':data['moment_difference']['outward_decimal']}))


if __name__=='__main__':main()
