"""Certified fixed-point Gaussian lattice sums. No third-party packages."""
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt
import json

G = 10**50
N = 14


def ceildiv(a,b):
    return -((-a)//b)


@dataclass(frozen=True)
class Ball:
    lo: int
    hi: int

    @classmethod
    def bracket(cls,lo,hi):
        lo,hi=F(lo)*G,F(hi)*G
        return cls(lo.numerator//lo.denominator,ceildiv(hi.numerator,hi.denominator))

    def __add__(self,other):
        other=asball(other)
        return Ball(self.lo+other.lo,self.hi+other.hi)

    __radd__=__add__

    def __neg__(self):
        return Ball(-self.hi,-self.lo)

    def __sub__(self,other):
        return self+(-asball(other))

    def __rsub__(self,other):
        return asball(other)+(-self)

    def __mul__(self,other):
        other=asball(other)
        v=[x*y for x in (self.lo,self.hi) for y in (other.lo,other.hi)]
        return Ball(min(v)//G,ceildiv(max(v),G))

    __rmul__=__mul__

    def __pow__(self,k):
        result=asball(1)
        x=self
        while k:
            if k%2:
                result=result*x
            x=x*x
            k//=2
        return result

    def sqrt(self):
        assert self.lo>0
        return Ball(isqrt(self.lo*G),isqrt(self.hi*G-1)+1)

    def overlap(self,other):
        return max(self.lo,other.lo)<=min(self.hi,other.hi)

    def text(self):
        # Report a 16-place outward decimal interval, after all full-precision comparisons.
        s=10**16
        def fmt(n):
            return ('-' if n<0 else '')+str(abs(n)//s)+'.'+str(abs(n)%s).zfill(16)
        return [fmt((self.lo*s)//G),fmt(ceildiv(self.hi*s,G))]


def asball(x):
    return x if isinstance(x,Ball) else Ball.bracket(x,x)


def atan_reciprocal(m):
    z=F(1,m)
    p=sum((-1)**j*z**(2*j+1)/(2*j+1) for j in range(45))
    return Ball.bracket(p-z**91/91,p)


PI=16*atan_reciprocal(5)-4*atan_reciprocal(239)


def exp_neg(x):
    # Scale to [0,1] so signs of the alternating Taylor error give both endpoints.
    y=x*F(1,16)
    assert 0 <= y.lo <= y.hi <= G
    def bound(r):
        t=v=F(1)
        for j in range(1,39):
            t=-t*r/j
            v+=t
        return v-t*r/39,v
    low=bound(F(y.hi,G))[0]
    high=bound(F(y.lo,G))[1]
    return Ball.bracket(low,high)**16


def moment(q,k,mask=lambda n: True,cut=N):
    total=asball(int(k==0 and mask(0)))
    for n in range(1,cut+1):
        if mask(n):
            total=total+2*n**k*q**(n*n)
    # Ratio after the first omitted term is at most this, including unfiltered terms.
    ratio=F(cut+2,cut+1)**k*(q**(2*cut+3))
    assert ratio.hi < G//2
    tail=4*(cut+1)**k*q**((cut+1)**2)
    return total+Ball(0,tail.hi)


def row(alpha):
    s=PI*alpha
    q=exp_neg(s)
    r=exp_neg(PI*(1/alpha))
    V=[moment(q,j) for j in (0,2,4)]
    W=[moment(r,j) for j in (0,2)]
    theta,m2,m4=V
    odd=lambda n: n%2==1
    oq,orr=moment(q,0,odd),moment(r,0,odd)
    scale=asball(1/alpha).sqrt()
    square=theta*theta-1
    hx=4*s*s*m2*m2-2*s*m2*theta
    hu=2*(s*s*m4*theta-s*m2*theta-s*s*m2*m2)
    hx_p=-4*PI*PI*scale*m2*W[1]
    assert hx.overlap(hx_p) and hx.hi<0<hu.lo
    escape=2*oq*(2*s*theta-4*s*s*m2)
    assert escape.overlap(8*PI*PI*scale*oq*W[1]) and escape.lo>0
    # At horizontal period 1 and vertical spacing 1, phi=1/2 changes just odd rows.
    # Direct half-integer row count, separately from the Poisson frequencies above.
    half=moment(exp_neg(s*F(1,4)),0,odd,cut=30)
    drop_direct=oq*(theta-half)
    drop_poisson=2*scale*oq*orr
    assert drop_direct.overlap(drop_poisson) and drop_direct.lo>0
    return {'square_energy':square,'bravais_shear_hessian':hx,'rectangle_logheight_hessian':hu,
            'half_offset_energy_drop':drop_direct,'two_row_positive_escape_rate':escape}


def vacancy_check():
    # Squared lengths in the triangular basis are (2/sqrt(3))*(a^2+ab+b^2).
    def norm(x):
        a,b=x
        return a*a+a*b+b*b
    def pair_hist(points):
        return Counter(norm((a-c,b-d)) for a,b in points for c,d in points if (a,b)!=(c,d))
    output=[]
    for cutoff in (1,3,7,12,19):
        bound=2*isqrt(cutoff)+2
        points=[(a,b) for a in range(-bound,bound+1) for b in range(-bound,bound+1)
                if norm((a,b))<=cutoff]
        rest=[p for p in points if p!=(0,0)]
        full,missing=pair_hist(points),pair_hist(rest)
        radial=Counter(norm(p) for p in rest)
        assert all(full[l]-missing[l]==2*radial[l] for l in set(full)|set(radial))
        target=(1,0)
        force={}
        for v in rest:
            if v==target:
                continue
            key=norm(v)
            a,b=force.get(key,(0,0))
            force[key]=(a+v[0],b+v[1])
        assert force.get(1)==(-1,0) and all(x==(0,0) for l,x in force.items() if l!=1)
        output.append(dict(norm_bound=cutoff,sites_before=len(points),sites_after=len(rest),
                           incident_ordered_pairs_removed=2*len(rest)))
    return output


def main():
    alphas=[F(1,4),F(1,2),F(1),F(2),F(4)]
    rows={a:row(a) for a in alphas}
    for a,r in rows.items():
        for key in ('bravais_shear_hessian','rectangle_logheight_hessian','half_offset_energy_drop'):
            assert r[key].overlap(rows[1/a][key]*(1/a))
        assert (r['square_energy']+1).overlap((rows[1/a]['square_energy']+1)*(1/a))
    print(json.dumps({'alphas':{str(a):{k:v.text() for k,v in r.items()} for a,r in rows.items()},
                      'interval_precision_decimal_places':50,'reported_decimal_places':16,
                      'integer_row_cutoff':N,'half_integer_odd_index_cutoff':30,
                      'pi_machin_interval':PI.text(),'finite_triangular_vacancy_tests':vacancy_check(),
                      'checks':['all five Hessian signs','real and Poisson shear/optical Hessians',
                                'real and Poisson half-offset drop','Bravais reciprocal scales']},
                     indent=2))
if __name__=='__main__':
    main()
