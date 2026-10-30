#!/usr/bin/env python3
"""PREFIX-373 exact rational Banach boxes for four H3 physical five-Port sources.
Python 3 standard library only; no float decisions, external physics, X6/BRC runtime.
"""
from fractions import Fraction as F
import json

class I:
    def __init__(self,l,h=None):
        if isinstance(l,I): self.l,self.h=l.l,l.h
        else: self.l=F(l);self.h=F(h) if h is not None else self.l
        assert self.l<=self.h
    def __add__(self,b):
        b=I(b);return I(self.l+b.l,self.h+b.h)
    __radd__=__add__
    def __neg__(self):return I(-self.h,-self.l)
    def __sub__(self,b):return self+-I(b)
    def __rsub__(self,b):return I(b)-self
    def __mul__(self,b):
        b=I(b);v=[self.l*b.l,self.l*b.h,self.h*b.l,self.h*b.h]
        return I(min(v),max(v))
    __rmul__=__mul__
    def abs(self):return max(abs(self.l),abs(self.h))

def dot(a,b):return sum((u*v for u,v in zip(a,b)),I(0))

# Exactly B=A[3:,:] A[:3,:]^{-1} for the frozen five-Port matrix.
B=[((F(5,2),F(9,2)),(F(3,2),F(7,2)),(F(0),F(4))),
   ((F(11,4),F(15,8)),(F(11,4),F(15,8)),(F(5,4),F(9,4)))]

def equations(z,x):
    a,b,c,d=z
    k=F(1101,424)-F(995,106)*x
    obs=[F(217,106)-F(381,53)*x,F(1133,848)-F(921,212)*x]
    values=[a*a+b*b-x,c*c+d*d-k]
    J=[[2*a,2*b,I(0),I(0)],[I(0),I(0),2*c,2*d]]
    for row,target in zip(B,obs):
        (ar,ai),(br,bi),(cr,ci)=row
        R=[ar,br,-bi,cr,-ci];H=[ai,bi,br,ci,cr]
        re=I(R[0])+dot([I(y) for y in R[1:]],z)
        im=I(H[0])+dot([I(y) for y in H[1:]],z)
        values.append(re*re+im*im-target)
        J.append([2*(re*R[j]+im*H[j]) for j in range(1,5)])
    return values,J

def inverse4(A):
    rows=[[F(a.l) for a in row]+[F(i==j) for j in range(4)] for i,row in enumerate(A)]
    for i in range(4):
        h=next(j for j in range(i,4) if rows[j][i])
        rows[i],rows[h]=rows[h],rows[i]
        p=rows[i][i];rows[i]=[v/p for v in rows[i]]
        for j in range(4):
            if j!=i:
                t=rows[j][i];rows[j]=[a-t*b for a,b in zip(rows[j],rows[i])]
    return [row[4:] for row in rows]

# Isolate the unique H3 cubic root using signs and positive derivative.
lo=F('0.14221831783254270');hi=F('0.14221831783254271')
coef=(6063581288774033,-1986113892546671,211884780353647,-7404639584785)
def p(x):
    a,b,c,d=coef;return ((a*x+b)*x+c)*x+d
assert p(lo)<0<p(hi)
a,b,c,d=coef
assert (3*a*I(lo,hi)*I(lo,hi)+2*b*I(lo,hi)+c).l>0
xbox=I(lo,hi)

seeds=[
 ('S0',['0.058042063464','0.372625061827','-1.109818309508','0.173284738518'],F('0.04'),F('0.05')),
 ('S1',['-0.376617319750','-0.019434821770','-1.033720330782','0.439484423444'],F('0.19'),F('0.20')),
 ('S2',['-0.350254450435','-0.139786042876','-0.998209376263','0.515075064300'],F('0.26'),F('0.27')),
 ('S3',['-0.350254450435','-0.139786042876','-0.717408911887','0.864319809947'],F('0.82'),F('0.83'))]
r=F(1,100000);out=[]
for label,raw,left,right in seeds:
    z=[F(s) for s in raw]
    f0,J0=equations([I(a) for a in z],I((lo+hi)/2))
    pre=inverse4(J0)
    domain=[I(a-r,a+r) for a in z]
    f,J=equations(domain,xbox)
    fc,_=equations([I(a) for a in z],xbox)
    shift=max(dot([I(v) for v in row],fc).abs() for row in pre)
    K=max(sum(( (I(int(i==j))-dot([I(v) for v in pre[i]],
                    [J[k][j] for k in range(4)])).abs()
              for j in range(4)),F(0)) for i in range(4))
    assert shift<F(1,10**10) and K<F(1,50)
    assert shift+K*r<r
    C=(I(1)+domain[2])*(I(1)+domain[2])+domain[3]*domain[3]
    assert left<C.l and C.h<right
    out.append({'label':label,'seed':raw,'radius':str(r),
       'K_below':'1/50','shift_below':'1/10000000000',
       'C_window':[str(left),str(right)]})
for i in range(4):
    for j in range(i+1,4):
        assert any(abs(F(seeds[i][1][k])-F(seeds[j][1][k]))>2*r for k in range(4))
windows=[(a,b) for _,_,a,b in seeds]
thresholds=[F(3,25),F(23,100),F(109,200)]
for i,t in enumerate(thresholds):
    assert windows[i][1]+F(1,40)<t<windows[i+1][0]-F(1,40)
print(json.dumps({'unit':'PREFIX-373','xH_interval':[str(lo),str(hi)],
 'physical_source_boxes':out,'observer':'C=|1+v|^2',
 'thresholds':[str(t) for t in thresholds],
 'additive_noise_tolerance':'1/40','exact_rational_certified':True,
 'four_source_exhaustion_depends_on':'PREFIX-372 (unreviewed)',
 'native_X6_or_typed_BRC_executed':False,'independent_review':False},indent=2))
print('PASS_PREFIX373_EXACT_FOUR_SOURCE_C_OBSERVER')
