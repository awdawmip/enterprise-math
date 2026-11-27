from fractions import Fraction as Q
from itertools import product,combinations
import json,random,hashlib
from pathlib import Path

def support(f,g,cols,rect,r):
    # Point zonotope columns (F,G); transport convex hull of +/-r corners.
    corners=[(sig*r*u,sig*r*v) for sig in (-1,1) for u in rect[0] for v in rect[1]]
    lines=[(v,-u) for u,v in corners]
    ss={Q(0)}
    for u,v in cols:
        if u: ss.add(v/u)
    for (a,b),(c,d) in combinations(lines,2):
        if b!=d:ss.add((c-a)/(b-d))
    def upper(s):return g-s*f+sum(abs(v-s*u) for u,v in cols)+max(a+b*s for a,b in lines)
    s=min(ss,key=lambda s:(upper(s),s));return upper(s),s

def vertices(f,g,cols,rect,r):
    # Exact independent check: Minkowski sum convex hull of corner sums;
    # intersection F=0 is on a segment between vertices, or a vertex itself.
    p=[]
    for signs in product((-1,1),repeat=len(cols)):
        u=f+sum(z*a for z,(a,b) in zip(signs,cols));v=g+sum(z*b for z,(a,b) in zip(signs,cols))
        for sig in (-1,1):
            for a,b in product(*rect):p.append((u+sig*r*a,v+sig*r*b))
    pos=[(u,v) for u,v in p if u>0];neg=[(u,v) for u,v in p if u<0];out=[v for u,v in p if u==0]
    out.extend((v*w-z*u)/(w-u) for u,v in neg for w,z in pos)
    return max(out) if out else None
rng=random.Random(1125);checked=0
for i in range(120):
    cols=[(Q(rng.randint(-4,4)),Q(rng.randint(-4,4))) for _ in range(3)]
    f=Q(rng.randint(-5,5));g=Q(rng.randint(-4,4));r=Q(rng.randint(1,4),5)
    rect=([Q(-4),Q(-1)],[Q(-2),Q(3)])
    v=vertices(f,g,cols,rect,r)
    if v is not None:
        z,s=support(f,g,cols,rect,r);assert z==v,(z,v,s);checked+=1
# Example with exact shared point constraint; derivative-only choice is -2 when F'=-1.
cols=[(Q(1),Q(3))];rect=([Q(-1),Q(-1)],[Q(-2),Q(-2)]);r=Q(1,10)
up,s=support(Q(0),Q(1,2),cols,rect,r)
lo,sl=support(Q(0),Q(-1,2),[(u,-v) for u,v in cols],(rect[0],[-rect[1][1],-rect[1][0]]),r)
assert (up,-lo,s,sl)==(Q(3,5),Q(2,5),Q(3),Q(-3))
# Frozen derivative transfer alone: exact minimax coefficient vs previous ratio midpoint.
a=json.load(open('root_8800_result.json'));t=json.load(open('tangent_result.json'));D=10**85
fl,fu=(Q(int(v),D) for v in a['F_jets'][1]);gl,gu=map(Q,t['Gp']);old_s=Q(t['s']);rr=Q(t['root_radius'])
assert fl<=fu<0 and 0<gl<=gu
A,B=-fu,-fl;C,D=gl,gu
s0=-(C+D)/(A+B)
mag=lambda s:max(abs(g-s*f) for f,g in product((fl,fu),(gl,gu)))
assert mag(s0)==(B*D-A*C)/(A+B) and mag(s0)<=mag(old_s)
print('exact relaxed-polytope checks',checked,'of 120 feasible instances')
print('example optimized bounds',str(-lo),str(up),'s',s,'vs tangent-only [-1/2,3/2]')
print('frozen derivative minimax old/new transfer',float(rr*mag(old_s)),float(rr*mag(s0)))
print('strict improvement',mag(s0)<mag(old_s))
print('frozen minimax gain minus 1',float(mag(old_s)/mag(s0)-1))
