"""Exact one-dimensional Q_P formula and directed midpoint enclosure.

The geometric reduction and analytic antiderivatives are documented in
DOUBLED_FACE_INTEGRAL.md. D2 carries the first two derivatives with respect
to u; its interval output bounds the whole cell's second derivative.
"""
from fractions import Fraction as F
from functools import lru_cache
import c84_interval_kernel as k

I=k.I

class D2:
    def __init__(self,v,d=0,dd=0):self.v,self.d,self.dd=map(I.cv,(v,d,dd))
    @staticmethod
    def cv(x):return x if isinstance(x,D2)else D2(x)
    def __add__(self,x):
        x=D2.cv(x);return D2(self.v+x.v,self.d+x.d,self.dd+x.dd)
    __radd__=__add__
    def __neg__(self):return D2(-self.v,-self.d,-self.dd)
    def __sub__(self,x):return self+-D2.cv(x)
    def __rsub__(self,x):return D2.cv(x)+-self
    def __mul__(self,x):
        x=D2.cv(x)
        return D2(self.v*x.v,self.d*x.v+self.v*x.d,
                  self.dd*x.v+2*self.d*x.d+self.v*x.dd)
    __rmul__=__mul__
    def inverse(self):
        z=1/self.v
        return D2(z,-self.d*z*z,2*self.d*self.d*z**3-self.dd*z*z)
    def __truediv__(self,x):return self*D2.cv(x).inverse()
    def __rtruediv__(self,x):return D2.cv(x)*self.inverse()
    def __pow__(self,n):
        assert isinstance(n,int)and n>=0
        ans=D2(1)
        for _ in range(n):ans=ans*self
        return ans
    def log(self):return D2(k.log(self.v),self.d/self.v,
                           self.dd/self.v-(self.d/self.v)**2)

def angular_integral(u,r,upper_piece):
    """Integral over t of the positive source/chord convolution numerator."""
    inv=1/u;M=r-u;H=M-inv;L=u-H
    # 2u+1/u>=2sqrt(2) keeps log's true positive argument visible even
    # when the natural interval expression loses the cancellation.
    lower=2*I.rat(2).sqrt()-r.v
    L.v=I(max(L.v.lo,lower.lo),L.v.hi)
    ans=(H**3*(M/u).log()+L**3*(L/u).log()
         +(3*M-inv)*inv**2*(inv/M).log()
         +H*(M**2+u**2+inv**2-F(5,2)*H*u))
    if upper_piece:
        ans+=u**3/2-3*u+F(3,2)*inv+inv**3+6*inv*u.log()
    return ans

@lru_cache(None)
def doubled_parallelogram(a,mesh=64):
    """112-bit full-cell enclosure of Q_P(A), 2<=A<4."""
    a=F(a);assert 2<=a<4 and mesh>0
    if a==2:return I.rat(0)
    r=(2*I.cv(a)).sqrt()
    bottom=(r-(2*I.cv(a)-4).sqrt())/2
    middle=I.rat(1);top=r/2
    total=I.rat(0)
    for left,right,upper in [(bottom,middle,False),(middle,top,True)]:
        width=(right-left)/mesh
        for j in range(mesh):
            l=left+(right-left)*F(j,mesh)
            h=left+(right-left)*F(j+1,mesh)
            midpoint=(l+h)/2
            val=angular_integral(D2(midpoint),D2(r),upper).v
            whole=angular_integral(D2(I(l.lo,h.hi),1,0),D2(r),upper)
            m=I(max(abs(whole.dd.lo),abs(whole.dd.hi)))
            error=(m*width**3/24).hi
            total+=val*width+I(-error,error)
    total=total/k.ZETA
    return I(max(0,total.lo),total.hi)

if __name__=='__main__':
    for a in [F(9,4),F(5,2),F(3),F(7,2),F(255,64)]:
        print(str(a),doubled_parallelogram(a).json())
