#!/usr/bin/env python3
"""Independent exact 2nd-order jet audit at all 125 padded box centers.

Directly differentiates the frozen positive rational branch products, without
using C291's log-Hessian identities; compares against outer-rounded enclosures.
"""
from fractions import Fraction as F
import C275_STANDALONE_EXACT_REPLAY as s
import C288_ISOLATING_BOXES_EXACT as c288
import C290_PADDED_CHART_EXACT as c290
import C291_HESSIAN_EXACT as cert

N=4
Z=F(0)
class Jet:
    __slots__=('v','g','h')
    def __init__(self,v,g=None,h=None):
        if isinstance(v,Jet):self.v,self.g,self.h=v.v,v.g,v.h;return
        self.v=F(v)
        self.g=tuple(g) if g is not None else (Z,)*N
        self.h=tuple(tuple(row) for row in h) if h is not None else ((Z,)*N,)*N
    def __add__(self,o):
        o=Jet(o)
        return Jet(self.v+o.v,[self.g[i]+o.g[i] for i in range(N)],
                   [[self.h[i][j]+o.h[i][j] for j in range(N)] for i in range(N)])
    __radd__=__add__
    def __neg__(self):return Jet(-self.v,[-x for x in self.g],[[-x for x in row] for row in self.h])
    def __sub__(self,o):return self+-Jet(o)
    def __rsub__(self,o):return Jet(o)-self
    def __mul__(self,o):
        o=Jet(o)
        return Jet(self.v*o.v,
            [self.g[i]*o.v+self.v*o.g[i] for i in range(N)],
            [[self.h[i][j]*o.v+self.v*o.h[i][j]+self.g[i]*o.g[j]+o.g[i]*self.g[j]
              for j in range(N)] for i in range(N)])
    __rmul__=__mul__
    def inverse(self):
        assert self.v!=0
        v=self.v
        return Jet(1/v,[-g/v**2 for g in self.g],
                [[2*self.g[i]*self.g[j]/v**3-self.h[i][j]/v**2
                    for j in range(N)] for i in range(N)])
    def __truediv__(self,o):return self*Jet(o).inverse()
    def __rtruediv__(self,o):return Jet(o)*self.inverse()
    def __abs__(self):
        assert self.v
        return self if self.v>0 else -self
    def __pow__(self,n):
        assert isinstance(n,int)
        if n==0:return Jet(1)
        if n<0:return self.inverse()**(-n)
        result=Jet(1); x=self
        while n:
            if n&1:result=result*x
            n//=2
            if n:x=x*x
        return result

def direct_jet(coords,W):
    x=[]
    for i,v in enumerate(coords):
        g=[Z]*4;g[i]=F(1)
        x.append(Jet(v,g))
    out=Jet(0)
    for j in s.J:
        m=Jet(W[j])
        for k,v in enumerate(x):
            m=m*(s.Z-v)/(s.Z-s.U[s.I[k]])*abs(s.U[j]-s.U[s.I[k]])/abs(s.U[j]-v)
        out+=m
    for i,j in enumerate(s.I):
        p=x[i]
        m=(s.Q*s.A/s.H)/(((2-p*p)*(3-p*p))**3)
        for h in s.J:m=m*(s.Z-s.U[h])/abs(p-s.U[h])
        for k,v in enumerate(x):
            if k!=i:m=m*(s.Z-v)/abs(p-v)
        out+=m
    return out

def run():
    paths,_=c288.build_paths();W,_=s.floor_fixed_masses()
    assert len(paths)==125
    for idx in range(0,len(paths),8):
        p=paths[idx]
        B=tuple((lo-c290.PAD,hi+c290.PAD) for lo,hi in p['box'])
        mid=tuple((lo+hi)/2 for lo,hi in B)
        direct=direct_jet(mid,W)
        H,rho=cert.Hessian_interval(B,W)
        assert direct.v==s.original_F(mid,W),(idx,'mass mismatch')
        for a in range(4):
            for b in range(4):
                assert direct.h[a][b]==direct.h[b][a]
                assert H[a][b][0] <= direct.h[a][b]/s.Q <= H[a][b][1],(idx,a,b,'Hessian escape')
    print('C291_INDEPENDENT_SECOND_JET_PASS 16 selected exact centers, 256 ordered Hessian entries')
if __name__=='__main__':run()
