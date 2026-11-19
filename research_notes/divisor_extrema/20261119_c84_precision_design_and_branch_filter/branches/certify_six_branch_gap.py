"""Exact rational isolation of six macro roots and their B2 separation.

The analytic root-count theorem is inherited from C81/C82. This certificate
isolates all its six roots at h=0, G/C=1/250, and bounds -A*h_A on each.
Only Fraction arithmetic is used for the certificates; decimals are display.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def h(a, d):
    m = F(7, 16) * a**4 * d
    return 1/(a-1)+5-4*m/(1+m)-5*m*a/(1+m*a)


def a_bracket(d, side, bits=110, H=F(0)):
    lo, hi = (F(0), F(1)) if side == 0 else (F(1), F(4))
    if side:
        assert h(F(4), d) < H
    for _ in range(bits):
        mid = (lo+hi)/2
        if h(mid, d) > H:
            lo = mid
        else:
            hi = mid
    assert h(lo, d) > H > h(hi, d)
    return lo, hi


def u15_box(a, A, d, D):
    assert (a-1)*(A-1) > 0 and (d-1)*(D-1) >= 0
    e0, e1 = sorted((abs(a-1), abs(A-1)))
    f0, f1 = sorted((abs(d-1), abs(D-1)))
    ml, mh = F(7,16)*a**4*d, F(7,16)*A**4*D
    low = a**57*d**70*(e0*f0/((1+mh)*(1+mh*A)))**15
    high = A**57*D**70*(e1*f1/((1+ml)*(1+ml*a)))**15
    return low, high


TARGET = F(1,250)


def compare_u(d, side, H=F(0), target=TARGET):
    for bits in (110, 160, 240):
        a,A = a_bracket(d, side, bits, H)
        low,high = u15_box(a,A,d,d)
        if high < target**15:
            return -1
        if low > target**15:
            return 1
    raise ArithmeticError('Target sign unresolved at exact rational d')


def bump_interval(a, b):
    """Exact interval for z/(1+z)^2 on [a,b]."""
    f = lambda z:z/(1+z)**2
    return min(f(a),f(b)), F(1,4) if a <= 1 <= b else max(f(a),f(b))


def q_interval(a,A,d,D):
    radial = sorted((a/(a-1)**2,A/(A-1)**2))
    ml,mh = F(7,16)*a**4*d,F(7,16)*A**4*D
    ub = bump_interval(ml,mh)
    vb = bump_interval(a*ml,A*mh)
    return radial[0]+16*ub[0]+25*vb[0], radial[1]+16*ub[1]+25*vb[1]


def outward(x, upper, scale=10**12):
    q,r=divmod(x.numerator*scale,x.denominator)
    return F(q+int(upper and r!=0),scale)


def isolate(side, lo, hi, increasing, label, H=F(0), target=TARGET):
    sign_lo,sign_hi = compare_u(lo,side,H,target),compare_u(hi,side,H,target)
    assert (sign_lo,sign_hi) == ((-1,1) if increasing else (1,-1))
    for _ in range(64):
        mid=(lo+hi)/2
        sign=compare_u(mid,side,H,target)
        if (sign < 0) == increasing:
            lo=mid
        else:
            hi=mid
    assert compare_u(lo,side,H,target)==sign_lo and compare_u(hi,side,H,target)==sign_hi
    a=a_bracket(hi,side,H=H)[0]
    A=a_bracket(lo,side,H=H)[1]
    ql,qh=q_interval(a,A,lo,hi)
    return {'side':['left','right'][side],'segment':label,
            'A_interval':[str(a),str(A)],'d_interval':[str(lo),str(hi)],
            'q_interval':[str(outward(ql,False)),str(outward(qh,True))],
            'display':{'A':[float(a),float(A)],'d':[float(lo),float(hi)],
                       'q':[float(ql),float(qh)]}}



def rectangle_certificate():
    Hlo,Hhi=F(-1,10000),F(1,10000)
    ulo,uhi=F(3999,10**6),F(4001,10**6)
    roots=[]
    segments=[(F(1,100),F(3,4),True,'first negative-lobe root'),
              (F(3,4),F(1),False,'second negative-lobe root'),
              (F(1),F(11,10),True,'positive-lobe root')]
    for side in (0,1):
        for lo,hi,inc,label in segments:
            # u increases with H at fixed d whenever H<1/5.
            corners=[isolate(side,lo,hi,inc,label,Hlo,uhi),
                     isolate(side,lo,hi,inc,label,Hhi,ulo)]
            dlo=min(F(x['d_interval'][0]) for x in corners)
            dhi=max(F(x['d_interval'][1]) for x in corners)
            a=a_bracket(dhi,side,H=Hhi)[0]
            A=a_bracket(dlo,side,H=Hlo)[1]
            a,A=outward(a,False),outward(A,True)
            dlo,dhi=outward(dlo,False),outward(dhi,True)
            qlo,qhi=q_interval(a,A,dlo,dhi)
            qlo,qhi=outward(qlo,False),outward(qhi,True)
            assert a>F(3,4) and dlo>F(1,3) and qhi<17
            assert min(abs(dlo-1),abs(dhi-1))>F(1,50)
            roots.append({'side':['left','right'][side],'segment':label,
                          'A_interval':[str(outward(a,False)),str(outward(A,True))],
                          'd_interval':[str(outward(dlo,False)),str(outward(dhi,True))],
                          'q_interval':[str(qlo),str(qhi)],
                          'q_display':[float(qlo),float(qhi)]})
    qs=sorted((F(r['q_interval'][0]),F(r['q_interval'][1])) for r in roots)
    gap=min(y[0]-x[1] for x,y in zip(qs,qs[1:]))
    assert gap>F(3,40)
    B2gap=F(225,16)*2*ulo*F(3,40)
    assert B2gap>F(1,128)
    jacobian_upper=F(4001,10**6)*(F(68,3)*70+F(27,4)/3)
    assert jacobian_upper<7
    mass_lower=6*F(2,135)*(Hhi-Hlo)*(uhi-ulo)/7
    assert mass_lower==F(1,196875000000)
    return {'source_mass_lower':str(mass_lower),'jacobian_upper_simplified':'7',
            'h_interval':[str(Hlo),str(Hhi)],
            'G_over_C_interval':[str(ulo),str(uhi)],'roots':roots,
            'q_gap_lower':str(gap),'simple_q_gap_lower':'3/40',
            'B2_gap_lower':str(B2gap),'threshold':'1/128',
            'positive_margin':str(B2gap-F(1,128)),
            'scope':'Every target in this exact rectangle has six regular interior roots; these boxes and gaps hold uniformly.'}


def main():
    roots=[]
    for side in (0,1):
        assert compare_u(F(1,100),side)<0
        assert compare_u(F(3,4),side)>0
        assert compare_u(F(1),side)<0
        assert compare_u(F(11,10),side)>0
        roots += [isolate(side,F(1,100),F(3,4),True,'first negative-lobe root'),
                  isolate(side,F(3,4),F(1),False,'second negative-lobe root'),
                  isolate(side,F(1),F(11,10),True,'positive-lobe root')]
    intervals=sorted((F(r['q_interval'][0]),F(r['q_interval'][1])) for r in roots)
    gap=min(y[0]-x[1] for x,y in zip(intervals,intervals[1:]))
    assert gap>F(3,40)
    # C=(1323/320)*4^(8/15)/Gamma(1/4)>1323/640>2.
    assert F(154,45)+F(1,2)<4 and F(1323,640)>2
    B2_gap=F(225,16)*2*TARGET*F(3,40)
    assert B2_gap==F(27,3200)
    threshold=F(4,64**1)*F(1,8)  # 4/(L beta^(3/2)), L=1,beta=64.
    assert threshold==F(1,128)<B2_gap
    rectangle=rectangle_certificate()
    result={'target_rectangle':rectangle,'scope':'Exact rational root boxes and q gaps, analytic six-root theorem required',
            'h':'0','G_over_C':str(TARGET),'roots':roots,
            'minimum_q_gap_lower':str(gap),'minimum_q_gap_lower_display':float(gap),
            'simple_q_gap_lower':'3/40','simple_B2_gap_lower':str(B2_gap),
            'L':'1','beta':'64','far_collision_threshold':str(threshold),
            'margin':str(B2_gap-threshold),'assertions_passed':True}
    path=Path(__file__).with_name('six_branch_gap_certificate.json')
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'roots':len(roots),'point_q_gap_lower':str(gap),
                      'rectangle_q_gap_lower':rectangle['q_gap_lower'],
                      'rectangle_B2_gap_lower':rectangle['B2_gap_lower'],
                      'source_mass_lower':rectangle['source_mass_lower'],
                      'threshold':rectangle['threshold'],'assertions_passed':True},indent=2))


if __name__=='__main__':
    main()
