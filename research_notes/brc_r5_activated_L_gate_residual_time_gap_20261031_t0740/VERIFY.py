"""Exact R5 added L stop gate: time-hull gap and inherited four-observer gap."""
from fractions import Fraction as F
from itertools import product

R = (F(1), F(3, 2), F(2), F(3))

def kernel(ell):
    return (F(1, 4), ell, F(1, 2)-3*ell/2, F(1, 4)+ell/2)

def full(bits, a, b):
    x0,x1,u0,u1,ub,z0,z1,v0,v1 = bits
    x,z=F(x0+x1,2),F(z0+z1,2)
    w=F(x0*u0+x1*u1,2)
    s=F(ub,4)+w/16
    E=a*x0*v0+b*x1*v1
    return (F(1,8)+F(ub,8)+(1-z)/8,
            F(1,8)+F(ub,8)+(1-z)/4,
            F(3,2)+x+z/2-s+3*E/16,
            F(3,2)+x/2+z-s+E/8)

def lr(bits, a, b):
    x,u,z,v=bits
    return full((x,x,u,u,u,z,z,v,v),a,b)

def hull(points):
    points=sorted(set(points))
    if len(points)<2: return points
    def cross(o,a,b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lower,upper=[],[]
    for p in points:
        while len(lower)>1 and cross(lower[-2],lower[-1],p)<=0: lower.pop()
        lower.append(p)
    for p in reversed(points):
        while len(upper)>1 and cross(upper[-2],upper[-1],p)<=0: upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]

pairs=((F(1,12),F(1,6)),(F(1,12),F(1,12)),
       (F(1,10),F(1,5)),(F(1,100),F(3,10)))
for a,b in pairs:
    for ell in (a,b):
        k=kernel(ell)
        assert all(t>0 for t in k)
        assert sum(k)==1 and sum(t*r for t,r in zip(k,R))==2
        assert sum(k[i]*R[i]/2 for i in range(4))==1
    Fv=[full(bits,a,b) for bits in product((0,1),repeat=9)]
    Lv=[lr(bits,a,b) for bits in product((0,1),repeat=4)]
    assert len(Fv)==512 and len(Lv)==16
    theta=(a+b)/2
    A,B=4+2*theta,8+3*theta
    gain=lambda V:-A*V[2]+B*V[3]
    baseline=12+F(7,2)*theta
    ff,ll=max(map(gain,Fv)),max(map(gain,Lv))
    assert ff==baseline+abs(a-b)/8 and ll==baseline
    old=lambda V:14*V[0]-19*V[1]+2*V[2]-4*V[3]
    assert max(map(old,Fv))==-F(13,2)
    assert max(map(old,Lv))==-F(53,8)
    HF=hull([v[2:] for v in Fv])
    HL=hull([v[2:] for v in Lv])
    assert (HF==HL)==(a==b)
    print(f"ell=({a},{b}) FULL={len(Fv)} LR={len(Lv)} time_hull_equal={HF==HL} time_gap={ff-ll} four_gap={F(1,8)}")

a,b=F(1,12),F(1,6)
witness=full((0,1,0,0,0,1,1,0,1),a,b)
assert witness==(F(1,8),F(1,8),F(81,32),F(133,48))
assert -34*witness[2]+67*witness[3]==F(1195,12)
assert max(-34*v[2]+67*v[3] for v in
    (lr(bits,a,b) for bits in product((0,1),repeat=4)))==F(199,2)
print("witness",tuple(map(str,witness)),"integer_support_gap=1/12","Linf_lower_bound=1/1212")
print("PASS_EXACT_R5_ACTIVATED_L_GATE_RESIDUAL_TO_TIME_GAP")
