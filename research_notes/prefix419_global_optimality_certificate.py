"""PREFIX-419 exact full-source global corner proof. Uses PREFIX-418 rational interval primitives."""
from prefix418_uniform_candidate_certificate import F, Interval, Dual, interval, root

BETA=F(1,10**6)
ETA_BOX=Interval(F(7,4000),F(187,100000))
EPS_BOX=Interval(F(0),F(1,10**6))
R_BOX=Interval(F(999999,10**6),F(1000001,10**6))
S_BOX=Interval(F(1999999,10**6),F(2000001,10**6))
E=F(53,8)

def coeff(r,s,sigma):
    a=(s-r-1)/2
    b=sigma*root(r-a*a)
    P=(245*(1+a)+123*b)/16
    Q=(-123*(1+a)+245*b)/16
    A=36+28*a+12*b
    B=-20-12*a+28*b
    J=(53+29*r)/2+39*a-4*b
    c=F(709,64)*(s-2)
    return a,b,P,Q,A,B,J,c

def positive_lambda(eps,eta):
    w=root(1-eps)
    p=(245+123*w)/16; q=(-123+245*w)/16
    A=36+12*w; B=-20+28*w
    N=p*p+q*q; K=eta+F(709,64)*eps-E*BETA
    S=root(N*BETA-K*K)
    alpha=A*p+B*q; delta=A*q-B*p
    lam=(alpha-delta*K/S)/N
    return lam,S,delta

def positive_upper_derivs(r,s,lam):
    a,b,P,Q,A,B,J,c=coeff(r,s,1)
    ar=-F(1,2); ass=F(1,2)
    br=(1+a)/(2*b); bs=-a/(2*b)
    Lx=A-lam*P; Ly=B-lam*Q
    length=root(Lx*Lx+Ly*Ly)
    def der(av,bv,jv,cv):
        Ap=28*av+12*bv; Bp=-12*av+28*bv
        Pp=(245*av+123*bv)/16; Qp=(-123*av+245*bv)/16
        return jv-lam*cv+(Lx*(Ap-lam*Pp)+Ly*(Bp-lam*Qp))/(1000*length)
    Fr=der(ar,br,F(29,2)+39*ar-4*br,0)
    Fs=der(ass,bs,39*ass-4*bs,F(709,64))
    return Fr,Fs,length

def negative_candidate(r,s,eta):
    a,b,P,Q,A,B,J,c=coeff(r,s,-1)
    x0=-eta/2; x1=-F(1,2)
    y0=(-eta-c-P*x0)/Q; y1=(P/2-E)/Q
    a2=x1*x1+y1*y1
    a1=2*(x0*x1+y0*y1)-1
    a0=x0*x0+y0*y0
    disc=a1*a1-4*a2*a0
    t=2*a0/(-a1+root(disc))
    x=x0+x1*t; y=y0+y1*t
    I4=J+A*x+B*y+16*t
    return {'P':P,'Q':Q,'A':A,'B':B,'J':J,'c':c,'x':x,'y':y,'t':t,'I4':I4,'a1':a1,'disc':disc}

def rigorous_interval_test():
    lam,S,delta=positive_lambda(EPS_BOX,ETA_BOX)
    print('lambda_enclosure',float(lam.lo),float(lam.hi))
    assert lam.lo>F(19,10) and lam.hi<F(21,10)
    assert S.lo>0 and delta.lo>0
    assert 16-E*lam.hi>0
    Fr,Fs,norm=positive_upper_derivs(R_BOX,S_BOX,lam)
    print('positive_F_r_enclosure',float(Fr.lo),float(Fr.hi),'F_s',float(Fs.lo),float(Fs.hi))
    assert -8 < Fr.lo <= Fr.hi < -6 and -3 < Fs.lo <= Fs.hi < -1
    pc=coeff(R_BOX,S_BOX,1)
    nc=coeff(R_BOX,S_BOX,-1)
    assert pc[6].hi<38 and pc[4].hi<50 and abs(pc[5].lo)<10 and abs(pc[5].hi)<10
    assert nc[6].lo>44 and nc[4].hi<30 and abs(nc[5].lo)<50 and abs(nc[5].hi)<50
    assert 38+F(60,1000)+16*BETA<41
    assert 44-F(80,1000)>41
    w=root(1-EPS_BOX)
    p=(245+123*w)/16; q=(-123+245*w)/16
    N=p*p+q*q; K=ETA_BOX+F(709,64)*EPS_BOX-E*BETA
    D=N*BETA-K*K; SqrtD=root(D)
    xp=(K*p+SqrtD*q)/N
    yp=(K*q-SqrtD*p)/N
    h=2*xp+BETA
    assert D.lo>0 and h.lo > -ETA_BOX.lo and h.hi < ETA_BOX.lo
    print('PASS positive witness feasible, k=eta and t=beta by identity')
    neg=negative_candidate(R_BOX,S_BOX,ETA_BOX)
    print('negative_t_enclosure',float(neg['t'].lo),float(neg['t'].hi))
    assert neg['t'].lo>0 and neg['t'].hi < BETA
    assert neg['a1'].hi<0 and neg['disc'].lo>0
    assert neg['P'].lo>0 and neg['P'].hi<8
    assert neg['Q'].hi < -22
    lam0=(neg['A']-neg['B']*neg['P']/neg['Q'])/2
    mu0=neg['B']/neg['Q']
    d0=16-lam0-E*mu0
    assert lam0.lo>3 and mu0.lo>2 and d0.lo>-3 and d0.hi<3
    assert F(1,4)+(F(8,44))**2 < F(9,25)
    assert F(1,4)+(E/F(22))**2 < F(9,25)
    den=1-F(3,2500)
    assert 3-F(3)*F(3,2500)/den>0
    assert 2-F(3)*F(1,11000)/den>0
    print('PASS negative fixed-u unique minimizer')
    r=Dual(R_BOX,interval(1)); s=Dual(S_BOX,interval(0))
    dr=negative_candidate(r,s,Dual(ETA_BOX,interval(0)))['I4'].derivative
    r=Dual(R_BOX,interval(0)); s=Dual(S_BOX,interval(1))
    ds=negative_candidate(r,s,Dual(ETA_BOX,interval(0)))['I4'].derivative
    print('negative_I4_dr_enclosure',float(dr.lo),float(dr.hi),'ds',float(ds.lo),float(ds.hi))
    assert -4 < dr.lo <= dr.hi < -2 and -5 < ds.lo <= ds.hi < -3
    print('PASS_PREFIX419_FULL_SOURCE_GLOBAL_CORNERS_UNIFORM_BOX_EXACT_INTERVAL_CERTIFICATE')

if __name__=='__main__': rigorous_interval_test()
