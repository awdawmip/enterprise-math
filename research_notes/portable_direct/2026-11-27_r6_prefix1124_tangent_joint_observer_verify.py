from fractions import Fraction as F
import json, hashlib
from pathlib import Path
class I:
    def __init__(self,a,b=None): self.a,self.b=F(a),F(a if b is None else b);assert self.a<=self.b
    @staticmethod
    def cast(x):return x if isinstance(x,I) else I(x)
    def __add__(self,x):x=I.cast(x);return I(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self):return I(-self.b,-self.a)
    def __sub__(self,x):return self+-I.cast(x)
    def __rsub__(self,x):return I.cast(x)+-self
    def __mul__(self,x):
        x=I.cast(x);v=[a*b for a in (self.a,self.b) for b in (x.a,x.b)];return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,x):x=I.cast(x);assert x.a*x.b>0;return self*I(1/x.b,1/x.a)
    def __rtruediv__(self,x):return I.cast(x)/self
    def __pow__(self,n):
        v=I(1)
        for _ in range(n):v=v*self
        return v
    def mag(self):return max(abs(self.a),abs(self.b))
    def mid(self):return (self.a+self.b)/2
    def out(self):return [str(self.a),str(self.b)]
G=10**85
old=json.load(open('root_8800_result.json'));new=json.load(open('root_9200_only.json'))
assert hashlib.sha256(Path('root_8800_result.json').read_bytes()).hexdigest()=='367ed5c982ef92405623cfe6633aa29ce1449bfa2e1cb2e355fd8692d84355a9'
assert hashlib.sha256(Path('root_9200_only.json').read_bytes()).hexdigest()=='b17b098179d915eabbdefc8f6050a8d401e06731a59e7f130350ce6aaab1948f'
def box(x):return I(*(F(int(y),G) for y in x))
t=box(new['t']);told=box(old['t']);assert told.a<=t.a<=t.b<=told.b
f1,f2,f3=(box(old['F_jets'][j]) for j in (1,2,3));assert f1.b<0
c0=box(old['c']).mid();b=t*t/36;D=198/t**2+216/(4-t*t)+216/(16-t*t);Dp=-396/t**3+432*t/(4-t*t)**2+432*t/(16-t*t)**2
alpha=36/t**2-2+(1-b)*D/2;beta=9/t-t/4
ap=-72/t**3-t*D/36+(1-b)*Dp/2;bp=-9/t**2-F(1,4)
# Verify formula consistent with prior box, without assuming interval equality.
C=alpha+beta*f2/f1;C0=box(old['c']);assert max(C.a,C0.a)<=min(C.b,C0.b)
Gp=beta*f3+(bp+alpha-c0)*f2+ap*f1
s=(Gp/f1).mid();Qp=Gp-s*f1;r=(t.b-t.a)/2
assert Qp.mag()<Gp.mag();assert Qp.mag()<F(1,10**64);assert Gp.mag()>10**10
# Point evaluation is not performed: only the transfer error is certified.
result=dict(c0=str(c0),s=str(s),t=t.out(),Gp=Gp.out(),Qp=Qp.out(),root_radius=str(r),old_transfer=str(r*Gp.mag()),new_transfer=str(r*Qp.mag()),reduction_lower=int(Gp.mag()/Qp.mag()),C_overlap=True)
print('s',float(s),'Gp magnitude',float(Gp.mag()),'Qp magnitude',float(Qp.mag()))
print('old/new transfer',float(r*Gp.mag()),float(r*Qp.mag()),'factor',float(Gp.mag()/Qp.mag()))
Path('tangent_result.json').write_text(json.dumps(result,indent=2)+'\n')
assert r*Gp.mag()<F(3275,10**74)  # 3.275e-71
assert r*Qp.mag()<F(4617,10**153) # 4.617e-150
assert Gp.mag()/Qp.mag()>7*10**78
print('strict rational bounds passed')
