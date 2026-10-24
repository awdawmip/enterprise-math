#!/usr/bin/env python3
"""Independent exact four-variable dual-number audit of C290 center gradients.
Computes original product branches directly; does not use log-gradient formulas.
"""
from fractions import Fraction as R
import C275_STANDALONE_EXACT_REPLAY as s
import C288_ISOLATING_BOXES_EXACT as c288
import C290_PADDED_CHART_EXACT as cert

N=4
ZERO=R(0)
class Dual:
    __slots__=('v','d')
    def __init__(self,v,d=None):
        if isinstance(v,Dual):self.v,self.d=v.v,v.d;return
        self.v=R(v);self.d=(ZERO,)*N if d is None else tuple(map(R,d))
    def __add__(self,x):
        x=Dual(x)
        return Dual(self.v+x.v,(a+b for a,b in zip(self.d,x.d)))
    __radd__=__add__
    def __neg__(self):return Dual(-self.v,(-a for a in self.d))
    def __sub__(self,x):return self+(-Dual(x))
    def __rsub__(self,x):return Dual(x)-self
    def __mul__(self,x):
        x=Dual(x)
        return Dual(self.v*x.v,(a*x.v+self.v*b for a,b in zip(self.d,x.d)))
    __rmul__=__mul__
    def inverse(self):
        assert self.v!=0
        return Dual(1/self.v,(-a/(self.v*self.v) for a in self.d))
    def __truediv__(self,x):return self*Dual(x).inverse()
    def __rtruediv__(self,x):return Dual(x)*self.inverse()
    def __abs__(self):
        assert self.v!=0
        return self if self.v>0 else -self
    def __pow__(self,n):
        assert isinstance(n,int)
        if n==0:return Dual(1)
        if n<0:return (self.inverse())**(-n)
        res=Dual(1);a=self
        while n:
            if n&1:res=res*a
            a=a*a;n//=2
        return res

def evaluate_dual(coords,weights):
    x=[]
    for k,v in enumerate(coords):
        g=[ZERO]*4;g[k]=R(1)
        x.append(Dual(v,g))
    tot=Dual(0)
    for j in s.J:
        m=Dual(weights[j])
        for k,p in enumerate(x):
            m=m*(s.Z-p)/(s.Z-s.U[s.I[k]]) * abs(s.U[j]-s.U[s.I[k]])/abs(s.U[j]-p)
        tot+=m
    for i,j in enumerate(s.I):
        p=x[i]
        m=(s.Q*s.A/s.H)/(((2-p*p)*(3-p*p))**3)
        for h in s.J:
            m=m*(s.Z-s.U[h])/abs(p-s.U[h])
        for k,y in enumerate(x):
            if i!=k:m=m*(s.Z-y)/abs(p-y)
        tot+=m
    return tot

def check():
    paths,_=c288.build_paths();W,_=s.floor_fixed_masses()
    for idx,p in enumerate(paths):
        B=tuple((lo-cert.PAD,hi+cert.PAD) for lo,hi in p['box'])
        mid=tuple((lo+hi)/2 for lo,hi in B)
        a=evaluate_dual(mid,W)
        assert a.v==s.original_F(mid,W),(idx,'mass sum mismatch')
        grads,_=cert.partial_interval(B,W)
        for k in range(4):
            assert grads[k][0]<=a.d[k]<=grads[k][1],(idx,k,'derivative escaped rational interval')
        assert a.d[2]>R(6,5)*s.Q,(idx,'normal derivative not positive')
    print('C290_INDEPENDENT_PRODUCT_DUAL_GRADIENT_PASS',len(paths),'centers,',4*len(paths),'derivative enclosures')
if __name__=='__main__':check()
