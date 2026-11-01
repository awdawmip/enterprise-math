"""Exact quadratic-field audit of BRC N4/S23 two-endpoint (a upper, c lower) theorem.

No floating point; all comparisons in Q(sqrt(D)) via rational squared signs.
The full real-continuum theorem is proved in PROOF.md, not inferred from this grid.
"""
from fractions import Fraction as F
from itertools import product
import json

class K:
    __slots__ = ('a', 'b', 'd')
    def __init__(self, a=0, b=0, d=0):
        self.a = F(a); self.b = F(b); self.d = F(d)
    def coerce(self, x):
        if isinstance(x, K):
            assert x.d == self.d
            return x
        return K(x, 0, self.d)
    def __add__(self, x):
        x = self.coerce(x)
        return K(self.a+x.a, self.b+x.b, self.d)
    __radd__ = __add__
    def __neg__(self):
        return K(-self.a,-self.b,self.d)
    def __sub__(self, x):
        return self+-self.coerce(x)
    def __rsub__(self, x):
        return self.coerce(x)+-self
    def __mul__(self, x):
        x = self.coerce(x)
        return K(self.a*x.a+self.b*x.b*self.d, self.a*x.b+self.b*x.a, self.d)
    __rmul__ = __mul__
    def __truediv__(self, x):
        x = self.coerce(x)
        den = x.a*x.a-x.b*x.b*self.d
        assert den
        return K((self.a*x.a-self.b*x.b*self.d)/den,
                 (self.b*x.a-self.a*x.b)/den, self.d)
    def __rtruediv__(self, x):
        return self.coerce(x)/self
    def sign(self):
        a,b,d = self.a,self.b,self.d
        assert d > 0
        if b == 0: return (a>0)-(a<0)
        if b > 0:
            if a >= 0: return 1
            return (b*b*d > a*a)-(b*b*d < a*a)
        if a <= 0: return -1
        return (a*a > b*b*d)-(a*a < b*b*d)
    def __eq__(self, x):
        return (self-self.coerce(x)).sign() == 0
    def __lt__(self, x):
        return (self-self.coerce(x)).sign() < 0
    def __le__(self, x):
        return (self-self.coerce(x)).sign() <= 0
    def __gt__(self, x):
        return (self-self.coerce(x)).sign() > 0
    def __ge__(self, x):
        return (self-self.coerce(x)).sign() >= 0
    def __abs__(self):
        return -self if self.sign() < 0 else self
    def __repr__(self):
        return f'({self.a})+({self.b})*sqrt({self.d})'

M20 = ((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
       (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))

def audit(h,t):
    p = F(1,8)-h
    disc = 43-16*h+16*h*h
    C = lambda v=0: K(v,0,disc)
    root = K(h/2-F(5,8), F(1,8), disc)
    H1 = C(F(3,16)+h/2)
    H2 = C(F(3,16)+h/3+t/6)
    rh = max(H1,H2)
    rl = max(rh,root)
    assert 32*root*root+(40-32*h)*root-(9+12*h)==0
    assert C(F(3,16))<=rh<=C(F(1,4))
    assert C(F(3,16))<=rl<=C(F(1,4))
    U=C(F(7,8)+h); L=C(F(1,2))
    B0=C(F(1,8)); B1=C(F(1,2))
    Z0=C(F(1,2)-t); Z1=C(F(7,8))
    sH=C(p)+rh
    zH=(C(F(7,16))-rh)/sH
    sL=C(p)+rl
    xL=U-rl
    yL=C(F(1,2))-4*rl/3
    zL=(C(F(7,16))-rl)/sL
    assert Z0<=zH<=Z1 and Z0<=zL<=Z1
    assert L<=xL<=U and B0<=yL<=B1
    dA=C(F(3,8)+h)
    alpha=rh/dA
    beta=C(F(1,3))
    w2=(C(1)-4*C(p)-2*rh)/(6*dA)
    w1=alpha-w2
    w4=beta-w2
    w3=C(1)-alpha-beta+w2
    w=(w1,w2,w3,w4)
    assert sum(w,C())==1 and all(C()<=v<=C(1) for v in w)
    def F4(a,b,c):
        return (a,(1-a)*b,(1-a)*(1-b)*c,(1-a)*(1-b)*(1-c))
    def obs(a,b,c):
        src = (F4(a,b,C(F(1,2))), F4(a,b,C(F(1,2))), F4(a,C(),c),
               F4(C(F(1,4)),b,C(F(1,2))), F4(C(F(1,4)),b,C(F(1,2))),
               F4(C(F(1,4)),C(F(1,3)),C(F(1,2))))
        return tuple(tuple(sum((src[j][k]*M20[i][j] for j in range(6)),C())/20
                           for k in range(4)) for i in range(6))
    joint = (obs(L,B0,zH),obs(L,B1,zH),obs(U,B0,zH),obs(U,B1,zH))
    ch = tuple(tuple(sum((w[m]*joint[m][i][j] for m in range(4)),C())
                     for j in range(4)) for i in range(6))
    cl = obs(xL,yL,zL)
    assert ch[0][1]==C(F(1,16)) and ch[3][1]==C(F(3,16))
    assert ch[2][2]==C(F(7,16))-rh and cl[2][2]==C(F(7,16))-rl
    def tv(row,centre):
        return sum((abs(x-y) for x,y in zip(row,centre)),C())/2
    n=0
    for a,b,c in product((L,U),(B0,B1),(Z0,Z1)):
        v=obs(a,b,c)
        for i in range(6):
            assert sum(v[i],C())==1
            assert tv(v[i],ch[i])<=rh, (h,t,'hull',i,a,b,c)
            assert tv(v[i],cl[i])<=rl, (h,t,'lawful',i,a,b,c)
            n+=2
    assert abs(obs(U,B0,Z0)[2][0]-ch[2][0])==rh
    assert abs(obs(U,B0,Z0)[2][0]-cl[2][0])==rl
    return n, int(root>rh), int(root==rh), int(root<rh)

samples=[F(i,512) for i in (0,4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64)]
special=[(F(1,25),F(6,125)),(F(1,25),F(47,1000)),
         (F(1,25),F(49,1000)),(F(1,50),F(9,200)),
         (F(1,100),F(43,1000))]
counts=[0,0,0,0,0]
for h,t in list(product(samples,samples))+special:
    out=audit(h,t)
    counts=[counts[i]+([1]+list(out))[i] for i in range(5)]
print(json.dumps({
    'status':'PASS_BRC_N4_S23_A_UPPER_C_LOWER_2D_EXACT_PHASE_20261102',
    'domain':'h,tau rational sample in [0,1/8]; universal proof resides in PROOF.md',
    'sample_boxes':counts[0],
    'original_four_atom_six_row_vertex_comparisons':counts[1],
    'strict_gap_samples':counts[2],
    'zero_gap_boundary_samples':counts[3],
    'zero_gap_interior_samples':counts[4],
    'arithmetic':'Fraction exact field Q(sqrt(43-16h+16h^2)); symbolic sign by rational squares',
    'mixing':'full original 6x6 M20, same four-vertex weights for all rows',
},ensure_ascii=False,indent=2))
