"""Exact rational certificate for two C89 double-slope transversality points.

All acceptance inequalities are Fraction calculations, including root brackets
and outward-rounded interval operations. mpmath is not used by this certificate.
"""
from fractions import Fraction as Q
import json
from pathlib import Path

SCALE = 10**100

def lower(x):
    x=Q(x); return Q((x*SCALE).numerator//(x*SCALE).denominator,SCALE)
def upper(x):
    return -lower(-Q(x))

class I:
    def __init__(self,a,b=None):
        if isinstance(a,I): self.a,self.b=a.a,a.b; return
        self.a,self.b=lower(a),upper(a if b is None else b)
        assert self.a<=self.b
    def __add__(self,o):
        o=I(o); return I(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return I(-self.b,-self.a)
    def __sub__(self,o):return self+-I(o)
    def __rsub__(self,o):return I(o)+-self
    def __mul__(self,o):
        o=I(o); s=[a*b for a in (self.a,self.b) for b in (o.a,o.b)]; return I(min(s),max(s))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=I(o); assert not o.a<=0<=o.b
        return self*I(1/o.b,1/o.a)
    def __rtruediv__(self,o): return I(o)/self
    def __pow__(self,n):
        assert n>=0
        if n==0:return I(1)
        if n%2==0 and self.a<=0<=self.b:return I(0,max(self.a**n,self.b**n))
        v=[self.a**n,self.b**n];return I(min(v),max(v))
    def json(self): return [str(self.a),str(self.b)]
    def approx(self):return [float(self.a),float(self.b)]

def h(a,d):
    m=Q(7,16)*a**4*d; n=m*a
    return 1/(a-1)+5-4*m/(1+m)-5*n/(1+n)

def root_a(d,side):
    lo,hi=(Q(1,2),Q(9,10)) if side=='left' else (Q(6,5),Q(2))
    assert h(lo,d)>0 and h(hi,d)<0
    for _ in range(180):
        mid=(lo+hi)/2
        if h(mid,d)>0:lo=mid
        else:hi=mid
    return I(lo,hi)

def u15(a,d,side):
    m=Q(7,16)*a**4*d;n=m*a
    aa=1-a if side=='left' else a-1
    dd=1-d if d.b<1 else d-1
    return a**57*d**70*aa**15*dd**15/((1+m)**15*(1+n)**15)

def reduced_slope_target_gradient(a,d,u):
    # At h=0, t=K*s with K=(4/d)^(4/9). The returned row is dt/(K*d(u,h)).
    m=Q(7,16)*a**4*d;n=m*a
    ha=-1/(a-1)**2-16*m/(a*(1+m)**2)-25*n/(a*(1+n)**2)
    hd=-4*m/(d*(1+m)**2)-5*n/(d*(1+n)**2)
    r=Q(14,3)+d/(d-1)-m/(1+m)-n/(1+n)
    ra=-4*m/(a*(1+m)**2)-5*n/(a*(1+n)**2)
    rd=-1/(d-1)**2-m/(d*(1+m)**2)-n/(d*(1+n)**2)
    den=-3-9*r
    s=9*r/den
    sa=9*(-3*ra-15*r*ha)/den**2
    sd=9*(-3*rd-15*r*hd)/den**2-Q(4,9)*s/d
    ua=-u/(5*a);ud=u*r/d
    jac=ua*hd-ud*ha
    return [(sa*hd-sd*ha)/jac,(-sa*ud+sd*ua)/jac],jac

def branch(side,dlo,dhi,u,monotonic):
    dlo,dhi=Q(dlo),Q(dhi)
    al=root_a(dlo,side);ah=root_a(dhi,side)
    vl=u15(al,I(dlo),side);vh=u15(ah,I(dhi),side);tar=u**15
    if monotonic==1:
        assert vl.b<tar<vh.a
    else:
        assert vh.b<tar<vl.a
    # h_A<0 and h_d<0, hence A decreases with d along h=0.
    box=I(ah.a,al.b);dbox=I(dlo,dhi)
    grad,jac=reduced_slope_target_gradient(box,dbox,u)
    assert jac.a*jac.b>0
    return {'side':side,'u':str(u),'d':dbox.json(),'A':box.json(),
            'u15_at_dlo':vl.json(),'u15_at_dhi':vh.json(),
            'jacobian_uh_Ad':jac.json(),'reduced_gradient': [v.json() for v in grad]},grad

def certificate():
    data={}
    specs={
      'two_complete_positive_branches':(Q(1,10),[
        ('left','1.370569828237','1.370569828239',1),
        ('right','1.275633060655','1.275633060657',1)]),
      'left_fold_pair':(Q(1,250),[
        ('left','0.696797114537','0.696797114539',1),
        ('left','0.907335131163','0.907335131165',-1)])}
    for name,(u,spec) in specs.items():
        bs=[];gs=[]
        for side,lo,hi,mon in spec:
            b,g=branch(side,lo,hi,u,mon);bs.append(b);gs.append(g)
        det=gs[0][0]*gs[1][1]-gs[0][1]*gs[1][0]
        assert det.a*det.b>0
        if name=='two_complete_positive_branches':assert Q(9,1000)<det.a<det.b<Q(1,100)
        else:assert -20<det.a<det.b<-19
        data[name]={'h':'0','branches':bs,'reduced_double_slope_determinant':det.json(),
                    'display_determinant':det.approx()}
    return {'arithmetic':'Fraction with outward rational rounding to 100 decimal places',
            'statement':'det d(t_0,t_1)/d(u,h) = K_0 K_1 * displayed reduced determinant, K_i > 0',
            'certificates':data}

if __name__=='__main__':
    out=certificate()
    path=Path(__file__).with_name('double_slope_certificate.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    for k,v in out['certificates'].items():print(k,v['display_determinant'])
