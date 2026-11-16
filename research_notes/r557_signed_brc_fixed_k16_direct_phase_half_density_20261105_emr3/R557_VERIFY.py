#!/usr/bin/env python3
"""R557: exact signed-BRC k=16 root disks and direct angle-order exclusion.
All theorem-bearing checks use integers/Fraction. Numeric centers were discovered
separately; this verification script does not use floating-point root solving.
"""
from fractions import Fraction as F
from math import comb, lcm
from sympy import Matrix
from hashlib import sha256

K = 16
D = 2*K-1
EPS = F(1,10**20)
CENTERS = [
    ('14.322657442658031247309370262466254926137410794796', '19.721619752562433333068611698186358232122875613367'),
    ('14.322657442658031247309370262466254926137410794796', '-19.721619752562433333068611698186358232122875613367'),
    ('6.7005482979446607996052080631860119046943287851515', '-4.9607876681281699817072194515506132049049280120903'),
    ('6.7005482979446607996052080631860119046943287851515', '4.9607876681281699817072194515506132049049280120903'),
    ('7.0061479589186256012883247803905763183016146820209', '0'),
    ('3.4985205945502327051497846597581067998475614575582', '-2.1859159350852820134814304476584629598761074727516'),
    ('3.4985205945502327051497846597581067998475614575582', '2.1859159350852820134814304476584629598761074727516'),
    ('2.2745926892856874753962779897802938190145631275230', '-1.3066142188396959446871538789088550565934003840268'),
    ('2.2745926892856874753962779897802938190145631275230', '1.3066142188396959446871538789088550565934003840268'),
    ('1.6530665042622579675412029414097992525007501449813', '-0.87835158422275629831467386036724974200027371771239'),
    ('1.6530665042622579675412029414097992525007501449813', '0.87835158422275629831467386036724974200027371771239'),
    ('1.2820726314377742213432046377668625615778716375550', '-0.63914631674561978476705213219062497764667018866225'),
    ('1.2820726314377742213432046377668625615778716375550', '0.63914631674561978476705213219062497764667018866225'),
    ('1.0386907737063567205286187283185399739000856205607', '-0.49189876852112050376324849358513447802125894939234'),
    ('1.0386907737063567205286187283185399739000856205607', '0.49189876852112050376324849358513447802125894939234'),
    ('0.86911441884362946085297510412533337103186193126776', '-0.39293783971291161961155927550272621505533677179477'),
    ('0.86911441884362946085297510412533337103186193126776', '0.39293783971291161961155927550272621505533677179477'),
    ('0.74626597077297050672636317017766555426971601542975', '-0.32132457131874256371223431437436033514791059429212'),
    ('0.74626597077297050672636317017766555426971601542975', '0.32132457131874256371223431437436033514791059429212'),
    ('0.65461651434692131549854289416065528704107356803279', '-0.26634647708200197233162919620487571000356752350445'),
    ('0.65461651434692131549854289416065528704107356803279', '0.26634647708200197233162919620487571000356752350445'),
    ('0.58445053066518794047726956283145536481921625427989', '-0.22189586096014136038448773069296815794550622578380'),
    ('0.58445053066518794047726956283145536481921625427989', '0.22189586096014136038448773069296815794550622578380'),
    ('0.52934900103748038328527660907507901550957017087422', '-0.18408232328405006714829157726359925610657644212300'),
    ('0.52934900103748038328527660907507901550957017087422', '0.18408232328405006714829157726359925610657644212300'),
    ('0.48476216232386101598154569425810194857411680913944', '-0.15010084582695834000711155746171407382702571982794'),
    ('0.48476216232386101598154569425810194857411680913944', '0.15010084582695834000711155746171407382702571982794'),
    ('0.44694342516788332130208751689281686542202565486699', '-0.11746294306841953326051411321733907778117619008110'),
    ('0.44694342516788332130208751689281686542202565486699', '0.11746294306841953326051411321733907778117619008110'),
    ('0.41127506353775211835810977559773519650904068697306', '-0.082809907822551461663770165261624868520889319044244'),
    ('0.41127506353775211835810977559773519650904068697306', '0.082809907822551461663770165261624868520889319044244'),
]

def catalan(k): return comb(2*k,k)//(k+1)
def H(k,t):
    r=2*k+1
    if t<2 or t>r:return 0
    return comb(r+t,2*t)*sum(comb(t-1,2*q)*4**q*catalan(k-q)
                             for q in range(min((t-1)//2,k)+1))
def H_raw(k,t):
    r=2*k+1
    if t<2 or t>r:return 0
    total=0
    for q in range(r-t+1):
        h=r-2*q
        if 0<=h<=2*t: total+=comb(2*t,h)*comb(r-t,q)
        if 0<=h-1<=2*t: total-=comb(2*t,h-1)*comb(r-t,q)
    return comb(r+t,2*t)*total

def characteristic():
    C=catalan(K)
    assert C==35357670
    assert all(H(K,t)==H_raw(K,t) for t in range(2,2*K+2))
    p2=F(H(K,2),C)
    assert p2==52360
    a=[(-1)**(j-1)*F(H(K,j+2),C)/p2 for j in range(1,D+1)]
    co=[F(1)]+[-v for v in a]
    lc=1
    for v in co: lc=lcm(lc,v.denominator)
    ints=[int(v*lc) for v in co]
    assert ints[0]>0 and all(F(v,ints[0])==c for v,c in zip(ints,co))
    return ints,a,p2

def add(x,y):return (x[0]+y[0],x[1]+y[1])
def mul(x,y):return(x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def n2(x):return x[0]*x[0]+x[1]*x[1]
def upper(x):return abs(x[0])+abs(x[1])
def lower(x):return max(abs(x[0]),abs(x[1]))
def taylor(center,coeffs):
    v=[]
    for a in coeffs:
        new=[(F(a),F(0))]+[(F(0),F(0))]*len(v)
        for j,z in enumerate(v):
            new[j]=add(new[j],mul(center,z))
            new[j+1]=add(new[j+1],z)
        v=new
    return v

def root_cert(coeffs):
    cc=[(F(x),F(y)) for x,y in CENTERS]
    assert len(cc)==D==31
    ratios=[]
    for i,c in enumerate(cc):
        b=taylor(c,coeffs)
        lhs=lower(b[1])*EPS
        rhs=upper(b[0])+sum((upper(b[j])*EPS**j for j in range(2,D+1)),F(0))
        assert lhs>rhs, ('rouche',i)
        ratios.append(rhs/lhs)
    assert all(n2((cc[i][0]-cc[j][0],cc[i][1]-cc[j][1]))>4*EPS**2
               for i in range(D) for j in range(i+1,D))
    assert cc[0][0]==cc[1][0] and cc[0][1]==-cc[1][1] and cc[0][1]>0
    assert n2(cc[0])>(F(24)+EPS)**2
    assert all(n2(c)<(F(9)-EPS)**2 for c in cc[2:])
    assert cc[0][0]>EPS and cc[0][1]>cc[0][0]+2*EPS
    assert (cc[0][1]+EPS)**2<3*(cc[0][0]-EPS)**2
    assert max(ratios)<F(1,1000)
    print('R557_K16_ROUCHE_PASS d=31 pairs=465 radius=1e-20 dominant_modulus_gt=24 other_modulus_lt=9 ratio_lt=1/1000',flush=True)
    return cc[0]

# Strict rational intervals for arctan: alternating power-series remainder bound.
def atan_bounds(x,n):
    assert 0<=x<1
    v=F(0)
    for j in range(n): v+=(-1)**j*x**(2*j+1)/F(2*j+1)
    err=x**(2*n+1)/F(2*n+1)
    return v-err,v+err

def signed_atan_bounds(x,n):
    if x>=0:return atan_bounds(x,n)
    l,h=atan_bounds(-x,n)
    return -h,-l

def phase_cert(c):
    # For theta=arg(lambda) in (pi/4,pi/3), lambda=c_x+i c_y+err.
    re,im=c
    ratio_min=(re-EPS)/(im+EPS)
    ratio_max=(re+EPS)/(im-EPS)
    assert F(7,10)<ratio_min<ratio_max<F(4,5)
    # atan(r)=2 atan(1/3) + atan((4r-3)/(4+3r)); tan(2 atan(1/3))=3/4.
    tmin=(4*ratio_min-3)/(4+3*ratio_min)
    tmax=(4*ratio_max-3)/(4+3*ratio_max)
    assert -F(1,20)<tmin<=tmax<F(1,20)
    A1lo,A1hi=atan_bounds(F(1,3),60)
    Tlo,_=signed_atan_bounds(tmin,25)
    _,Thi=signed_atan_bounds(tmax,25)
    # Machin identity pi=16 atan(1/5)-4 atan(1/239)
    A5lo,A5hi=atan_bounds(F(1,5),60)
    A239lo,A239hi=atan_bounds(F(1,239),20)
    pi_lo=16*A5lo-4*A239hi
    pi_hi=16*A5hi-4*A239lo
    assert F(3)<pi_lo<pi_hi<F(22,7)
    th_lo=pi_lo/2-2*A1hi-Thi
    th_hi=pi_hi/2-2*A1lo-Tlo
    lo=th_lo/pi_hi
    hi=th_hi/pi_lo
    assert F(1,4)<lo<hi<F(1,3)
    # If lambda/conj(lambda) is q-torsion, theta/pi=p/q in lowest terms.
    # Degree lambda/conj(lambda) <= d(d-1); hence phi(q) <= d(d-1).
    degree_bound=D*(D-1)
    qbound=2*degree_bound**2
    phi=list(range(qbound+1))
    for p in range(2,qbound+1):
        if phi[p]==p:
            for m in range(p,qbound+1,p):phi[m]-=phi[m]//p
    checked=0
    min_gap=None
    closest=(None,None)
    for q in range(2,qbound+1):
        if phi[q]>degree_bound:continue
        checked+=1
        # No integer p belongs to the certified interval [q*lo,q*hi].
        low_int=(q*lo.numerator+lo.denominator-1)//lo.denominator
        high_int=(q*hi.numerator)//hi.denominator
        assert low_int>high_int,('rational_angle_candidate',q,low_int,high_int)
        # For reporting a coarse min distance in rational units, not a proof need.
    print('R557_K16_PHASE_NONTORSION_PASS candidate_orders=',checked,'q_range=2..',qbound,
          'theta_over_pi_interval_width_lt_1e-18=',hi-lo<F(1,10**18),flush=True)
    return checked,qbound

def recurrence(a):
    t=[F(1)]
    for m in range(1,1025):
        t.append(sum((a[j-1]*t[m-j] for j in range(1,min(m,D)+1)),F(0)))
    result=(sum(x>0 for x in t),sum(x<0 for x in t),sum(x==0 for x in t),
            sum(t[i]*t[i-1]<0 for i in range(1,len(t))))
    print('R557_K16_RECURRENCE_PASS m=0..1024 plus=%d minus=%d zero=%d adjacent_switches=%d'%result,flush=True)
    for m in range(1,17):
        M=Matrix([[H_raw(K,3+i-j) for j in range(m)] for i in range(m)])
        assert M.det(method='berkowitz')==t[m]*(catalan(K)*F(H(K,2),catalan(K)))**m, m
    print('R557_K16_RAW_BERKOWITZ_PASS H_identities=32 matrices=16',flush=True)
    return result

def verify():
    co,a,p2=characteristic()
    print('R557_K16_COEFFICIENT_PASS catalan=35357670 p2=52360 degree=31')
    c=root_cert(co)
    phase_cert(c)
    recurrence(a)
    print('R557_K16_HALF_DENSITY_AUTHOR_CERT_PASS',flush=True)
if __name__=='__main__': verify()
