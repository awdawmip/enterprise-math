"""Exact lower envelope of affine numerator-budget margins, including parameter switches.
Integer polynomial Sturm isolation covers all real critical points and crossings.
"""
import sympy as s
from itertools import product,combinations
from mixed_region import run as check_plane
v,u=s.symbols('v u')
h=(1+v)**5
a=(1+u)*(1+v)**3
b=-4*(v**5-121*v**4+70*v**3*u+381*v**3-365*v**2*u-121*v**2+185*v*u+v-5*u)
c=(20*(a-h)+b)/120
g=[2*a-h,2*c+h,2*a-h-2*c,a-2*c]
# For a fixed v, both ends of the u interval suffice, since g is affine in u.
# Each endpoint produces 8 constraints (4 margins times +/-u). Flag inactive
# constraints with positive slope, which do not reduce the budget.
P0=6*v**5-96*v**4+441*v**3-41*v**2+56*v+15
cut=s.Rational(19,100)
def poly(f):
    return s.Poly(f,v).primitive()[1]
def roots(f,lo=0,hi=cut):
    p=poly(f)
    return [(l,r) for (l,r),m in p.intervals(inf=lo,sup=hi,eps=s.Rational(1,10**15))]
fun={}
for j,sgn_v in product(range(4),(-1,1)):
    f=s.cancel(g[j].subs(v,sgn_v*v))
    c0=f.subs(u,0)
    c1=f.diff(u)
    for sgn_u in (-1,1):
        key=j,sgn_u,sgn_v
        z=s.cancel(-c0/(sgn_u*c1))
        fun[key]=z
# At a fixed denominator budget V take the smaller radius over v=+V and
# v=-V. The active signed radius is strictly decreasing, so the full
# interval -V<=v<=V has the same critical radius as its endpoints.
def winner(x):
    candidates={key:rat.subs(v,x) for key,rat in fun.items() if rat.as_numer_denom()[1].subs(v,x) != 0}
    pos={key:f for key,f in candidates.items() if f>=0}
    val=min(pos.values())
    return val,tuple(k for k in pos if pos[k]==val)
def unique_intervals(intervals):
    out=[]
    for l,r in sorted(intervals):
        if out and l<=out[-1][1]:
            assert max(l,out[-1][0])<=min(r,out[-1][1])
            out[-1]=(max(l,out[-1][0]),min(r,out[-1][1]))
        else:out.append((l,r))
    return out

def main():
    assert check_plane()==524
    art=[(s.Integer(0),s.Integer(0)),(cut,cut)]
    # The origin is strictly safe on both denominator rays prior to Vcrit.
    # P0(-v) is the first such zero, verified below against all four margins.
    # Partition at all pairwise equality roots, all poles, zeros and
    # stationary points. The winning ratio is constant in identity in a cell.
    clipped=[roots(P0.subs(v,-v))[0]]
    art+=clipped
    for f in g:
        for direction in (-1,1):
            center=s.cancel(f.subs({u:0,v:direction*v},simultaneous=True))
            assert center.subs(v,0)>0
            assert not roots(center,0,clipped[0][0])
    for key,f in fun.items():
        n,d=f.as_numer_denom()
        art.extend(roots(n));art.extend(roots(d));art.extend(roots(s.cancel(s.diff(f,v)).as_numer_denom()[0]))
    for k1,k2 in combinations(fun,2):
        f=s.cancel(fun[k1]-fun[k2]).as_numer_denom()[0]
        if f: art.extend(roots(f))
    cuts=unique_intervals(art)
    breaks=[]
    pre=None
    for left,right in zip(cuts,cuts[1:]):
        if left[0]>=clipped[0][0]:break
        sample=(left[1]+right[0])/2
        val,keys=winner(sample)
        # The winning single-endpoint ratio decreases strictly on the whole
        # open cell, since all derivative zeros already index the partition.
        for key in keys: assert s.diff(fun[key],v).subs(v,sample)<0
        # Certify that alpha remains below 2 for every point in the rectangle:
        # if the envelope is R(v), (1+R(v))/(1-v)^2<2. Prove on entire
        # interval [0,.19] by isolating roots of each branch's bound below.
        if keys!=pre:
            breaks.append((left,keys));pre=keys
    for idx,(left,keys) in enumerate(breaks):
        right=breaks[idx+1][0] if idx+1<len(breaks) else clipped[0]
        rat=fun[keys[0]]
        M=s.cancel(2*(1-v)**2-(1+rat))
        numerator,denominator=M.as_numer_denom()
        assert M.subs(v,(left[1]+right[0])/2)>0
        for f in [numerator,denominator]:assert not roots(f,left[0],right[1])
        if idx:
            p=s.factor(s.cancel(rat-fun[breaks[idx-1][1][0]]).as_numer_denom()[0])
        else:p=0
        print('start',float((left[0]+left[1])/2),'corner',keys,'switch',p,'radius',s.factor(rat))
    print('end V',float(sum(clipped[0])/2),'arrangement roots',len(cuts))
    return breaks,clipped
if __name__=='__main__':main()
