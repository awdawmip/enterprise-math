#!/usr/bin/env python3
"""PREFIX-396: exact rational enclosure certificate for a joint-noise six-source fiber.
No floating point is used for the proof. Run: python verify_prefix396.py
"""
from fractions import Fraction as F
import json, hashlib, sys

class I:
    __slots__=("a","b")
    def __init__(self,a,b=None):
        if isinstance(a,I): self.a=a.a; self.b=a.b;return
        self.a=F(a);self.b=F(a if b is None else b)
        assert self.a<=self.b
    def __add__(x,y):
        y=I(y);return I(x.a+y.a,x.b+y.b)
    __radd__=__add__
    def __neg__(x):return I(-x.b,-x.a)
    def __sub__(x,y):return x+-I(y)
    def __rsub__(x,y):return I(y)+-x
    def __mul__(x,y):
        y=I(y);v=(x.a*y.a,x.a*y.b,x.b*y.a,x.b*y.b)
        return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(x,y):
        y=I(y);assert y.a*y.b>0
        return x*I(F(1,y.b),F(1,y.a))
    def __pow__(x,n):
        assert n==2
        if x.a<=0<=x.b:return I(0,max(x.a*x.a,x.b*x.b))
        return I(min(x.a*x.a,x.b*x.b),max(x.a*x.a,x.b*x.b))
    def sign(self):
        if self.a>0:return '+'
        if self.b<0:return '-'
        return '0?'
    def contains0(self):return self.a<=0<=self.b
    def to_obj(self):return [str(self.a),str(self.b)]

def num(p,q=1):return F(p,q)
BASE=[F(1),F(121,100),F(73,36),F(532313,23400),F(11531293,748800)]
r0=F(11,10);k0=BASE[2];s40=BASE[3];s50=BASE[4]
RAW_BINS=[(F(-2),F(-19,10)),(F(-7,10),F(-3,5)),
          (F(-1,20),F(-1,50)),(F(1,10),F(1,5)),
          (F(19),F(20)),(F(160),F(170))]
ABS_BINS=[(F(1,50),F(1,20)),(F(1,10),F(1,5)),
          (F(3,5),F(7,10)),(F(19,10),F(2)),
          (F(19),F(20)),(F(160),F(170))]

def poly_parts(z,r,k,s4,s5):
    z=I(z);r=I(r);k=I(k);s4=I(s4);s5=I(s5)
    R=1+z**2;U=r*(1-z**2);V=2*r*z
    l4=56*U+24*V+72*R
    m4=-24*U+56*V-40*R
    n4=78*U-8*V+(32*k+29*r**2+53-2*s4)*R
    l5=980*U+492*V+980*R
    m5=-492*U+980*V-492*R
    n5=1418*U+(424*k+709*r**2+709-64*s5)*R
    D=l4*m5-m4*l5
    C=m4*n5-m5*n4
    T=l5*n4-l4*n5
    H=C**2+T**2-k*D**2
    D2=(3776-4032*r**2)*R-256*r*(1-z**2)+47104*r*z
    return H,D,D2

def cu(z,r):
    z=I(z);r=I(r)
    return 1+r**2+2*r*(1-z**2)/(1+z**2)

def iso_cert(xi,eta=F(1,200)):
    assert xi>=0 and xi<=F(1,2)
    assert 2*(1+max(BASE))*xi <= 50*xi
    dr=50*xi;r=I(r0-dr,r0+dr);k=I(k0-dr,k0+dr)
    s4=I(s40-dr,s40+dr);s5=I(s50-dr,s50+dr)
    results=[]
    for j,(lo,hi) in enumerate(RAW_BINS):
        lh=poly_parts(lo,r,k,s4,s5)[0]
        rh=poly_parts(hi,r,k,s4,s5)[0]
        d2=poly_parts(I(lo,hi),r,k,s4,s5)[2]
        assert lh.sign() in ('+','-') and rh.sign() in ('+','-') and lh.sign()!=rh.sign(), ('root sign',j,lh.sign(),rh.sign())
        assert d2.sign() in ('+','-'), ('determinant',j,d2.sign())
        results.append({'bin':j+1,'z':[str(lo),str(hi)],'left_H_sign':lh.sign(),'right_H_sign':rh.sign(),'det_sign':d2.sign(),
                        'min_abs_H_endpoint_lower_bound':str(min(min(abs(lh.a),abs(lh.b)),min(abs(rh.a),abs(rh.b)))) if False else None})
    cb=[]
    for j,(lo,hi) in enumerate(ABS_BINS):
        c_lo=cu(hi,r);c_hi=cu(lo,r)
        cb.append(I(c_lo.a,c_hi.b))
    margins=[]
    for j in range(5):
        gap=cb[j].a-cb[j+1].b
        assert gap>2*eta,('observer',j,gap,eta)
        margins.append(gap)
    return {'xi':str(xi),'eta':str(eta),'normalization_radius':str(dr),
            'all_six_root_signs_and_delta_safe':True,'root_bins':results,
            'all_six_cu_noisy_intervals_separated':True,
            'observer_gaps_lower_bounds':[str(g) for g in margins],
            'smallest_gap_gt_2_eta':min(margins)>2*eta}

if __name__=='__main__':
    trials=['1/1000000','1/10000000','1/100000000','1/1000000000','1/10000000000','1/100000000000','1/1000000000000']
    failures=[];success=[]
    for t in trials:
        try:success.append(iso_cert(F(t)))
        except AssertionError as e:failures.append((t,str(e)[:150]))
    if not success:raise AssertionError(f'no certified positive radius: {failures}')
    best=success[0]
    print('CERTIFIED_RAW_INTENSITY_NOISE_RADIUS',best['xi'])
    print('CERTIFIED_CU_MEASUREMENT_NOISE_RADIUS',best['eta'])
    print('CERTIFIED_ROOT_INTERVAL_SIGNS',[(r['left_H_sign'],r['right_H_sign'],r['det_sign']) for r in best['root_bins']])
    print('CERTIFIED_CU_GAP_LOWER_BOUNDS',best['observer_gaps_lower_bounds'])
    print('FAILED_LARGER_RADII',failures)
    print('PASS_PREFIX396_ALL_SIX_REAL_SOURCES_UNDER_JOINT_RAW_INTENSITY_AND_CU_NOISE')
    out={'status':'PASS_PREFIX396_ALL_SIX_REAL_SOURCES_UNDER_JOINT_RAW_INTENSITY_AND_CU_NOISE','certificate':best,'larger_trials_not_certified':failures,'note':'These are conservative exact interval bounds, not an optimal noise radius.'}
    with open(__file__.replace('.py','_results.json'),'w',encoding='utf8') as f:json.dump(out,f,ensure_ascii=False,indent=2)
