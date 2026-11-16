#!/usr/bin/env python3
"""EC49FQZ: dependency-free exact 47-node class-16943 BRC continuum verifier.
Uses 45 inherited certified prices from PR #2587 plus seam-only certified
73/32 and 191/64. Exact rational area; certified rational sqrt bounds.
"""
from fractions import Fraction as F
from math import isqrt
from decimal import Decimal, localcontext

old = sorted({
    F(1),F(13,12),F(7,6),F(5,4),F(4,3),F(17,12),
    F(3,2),F(13,8),F(7,4),F(15,8),F(2),F(17,8),F(9,4),
    F(19,8),F(5,2),F(31,12),F(8,3),F(11,4),F(17,6),
    F(23,8),F(3),F(47,16),F(39,16),F(35,16),F(37,16),
    *(F(n,16) for n in (25,27,29,31,33)),
    *(F(n,24) for n in (61,63,65,67)),
    F(11,8),F(35,24),F(25,24),F(9,8),F(29,24),F(31,24),
    *(F(n,32) for n in (79,93,95)),
    F(75,32),F(77,32)
})
assert len(old)==45
added=[F(73,32),F(191,64)]
assert all(c not in old for c in added)
grid=sorted(old+added)
assert len(grid)==47 and grid[0]==1 and grid[-1]==3

K=lambda x:F(7557)-169*x
G=lambda x:310*(3-x)/K(x)
beta=F(620,3299)
assert [G(c) for c in added]==[F(7130,229487),F(310,451369)]
assert all(0<=G(c)<beta for c in grid)

area=lambda g:sum(((b-a)*(G(a)-G(b)) for a,b in zip(g,g[1:])),F(0))
before,after=area(old),area(grid)
assert before==F(162317745998378463895,39951040674583873370736)
assert after==F(5959469197718386554712955,1505500161665693064580080288)
assert 1-after/2==F(3005040854133667742605447621,3011000323331386129160160576)
assert after<before
for a,b in zip(grid,grid[1:]):
    assert K(a)>K(b)>0
    assert G(a)-G(b)==F(2185500)*(b-a)/(K(a)*K(b))

gains=[]
for c in added:
    a=max(y for y in old if y<c)
    b=min(y for y in old if y>c)
    gain=(b-a)*(G(a)-G(b))-(c-a)*(G(a)-G(c))-(b-c)*(G(c)-G(b))
    expected=F(2185500)*(c-a)*(b-c)/K(c)*(1/K(a)+1/K(b))
    assert gain==expected>0
    gains.append(gain)
assert gains==[F(182125,2194343942),F(155,7224608)]
assert sum(gains)==before-after==F(827952521505,7926637399062368)

scale=10**20
def rootbracket(z):
    n=isqrt((z.numerator*scale*scale)//z.denominator)
    a,b=F(n,scale),F(n+1,scale)
    assert a*a<=z<b*b
    return a,b

def regret_bracket(a,b):
    a0,a1=rootbracket(K(a))
    b0,b1=rootbracket(K(b))
    return F(50)*(b-a)/(a1+b1)**2,F(50)*(b-a)/(a0+b0)**2

bounds=[(a,b,*regret_bracket(a,b)) for a,b in zip(grid,grid[1:])]
winner=max(bounds,key=lambda z:z[2])
assert winner[0:2]==(F(35,16),F(9,4))
assert all(winner[2]>z[3] for z in bounds if z is not winner)
assert winner[3]<max(regret_bracket(a,b)[1] for a,b in zip(old,old[1:]))

with localcontext() as ctx:
    ctx.prec=60
    D=lambda v:Decimal(v.numerator)/Decimal(v.denominator)
    def regret(a,b):
        return 50*D(b-a)/(D(K(a)).sqrt()+D(K(b)).sqrt())**2
    print("CERTIFIED_PERCENT",100*D(1-after/2))
    print("UNCERTIFIED_CONTAINING_STRIP_AREA",str(after))
    print("AREA_GAIN",str(before-after))
    print("REGRET_LEADER",str(winner[0]),str(winner[1]))
    print("REGRET_CERTIFICATE_PER_t",regret(winner[0],winner[1]))
    print("PREVIOUS_REGRET_CERTIFICATE_PER_t",max(regret(a,b) for a,b in zip(old,old[1:])))
print("EC49FQZ_47NODE_EXACT_PASS")
